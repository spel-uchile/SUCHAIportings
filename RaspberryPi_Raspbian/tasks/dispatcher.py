#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'


import multiprocessing
from repos import command
from core import shared_resources
from core import suchai_types
from core import gnrl_services
from repos import state
import datetime
import SUCHAI_config
import logging
logger = logging.getLogger(__name__)


def task_dispatcher():
    arg = "name %s, pid %s, is_alive %s, exitcode %s" %\
          (taskHandler.name, taskHandler.pid, taskHandler.is_alive(), taskHandler.exitcode)
    logger.debug(arg)

    while True:
        disp_cmd = shared_resources.dispatcherQueue.get()  # blocking call

        #report received Cmd
        arg = "[task_dispatcher]"
        logger.info(arg)
        gnrl_services.console_print(arg)
        arg = "  Cmd: %s, CmdGroup: %s, Listener: %s" % (disp_cmd.cmdName, disp_cmd.groupName, disp_cmd.taskOrig)
        gnrl_services.console_print(arg)
        logger.info(arg)

        #fill SysReq info
        sys_req = command.CmdRepo.get_sysreq_byname(disp_cmd.groupName, disp_cmd.cmdName)
        # disp_cmd.sysReq = sys_req

        #check sysReq
        system_soc = state.StateVar.get_value(state.StateVar.eps_soc)
        executable = check_if_executable(system_soc, sys_req)
        arg = "  Cmd sysReq: %s, System soc: %s, executable: %s" % (sys_req, system_soc, executable)
        logger.info(arg)
        gnrl_services.console_print(arg)

        #execute
        if executable:
            arg = "  >>"
            logger.info(arg)
            gnrl_services.console_print(arg)

            i_time = datetime.datetime.now()
            cmd_funct = command.CmdRepo.get_function_byname(disp_cmd.groupName, disp_cmd.cmdName)
            exitcode = cmd_funct(disp_cmd.param)
            f_time = datetime.datetime.now()

            arg = "  <<"
            logger.info(arg)
            gnrl_services.console_print(arg)

            #report time, return status, etc
            d_time = f_time - i_time
            arg = "  d_time: %s, exitcode: %s" % (d_time, exitcode)
            logger.info(arg)
            gnrl_services.console_print(arg)
        else:
            #report time, soc, etc
            arg = "  command NOT executed (not executable)"
            logger.info(arg)
            gnrl_services.console_print(arg)
            arg = "  Cmd sysReq: %s, System soc: %s" % (sys_req, system_soc)
            logger.info(arg)
            gnrl_services.console_print(arg)

        arg = "----------------------"
        logger.info(arg)
        gnrl_services.console_print(arg)
        # gnrl_services.console_print("priorityEmulatorSem will be released (cmd sent by %s is done)"
        #                             % disp_cmd.taskOrig)
        shared_resources.priorityEmulatorSem.release()

taskHandler = multiprocessing.Process(group=None,
                                      target=task_dispatcher,
                                      name="task_dispatcher",
                                      args=(),
                                      kwargs={})


def check_if_executable(cu_sys_req, sys_req):
    if SUCHAI_config.SCH_TASKDISPATCHER_CHECK_IF_EXECUTABLE == 0:   # Do NOT check, always autorize
        return True
    if cu_sys_req < sys_req:
        return False
    else:
        return True
