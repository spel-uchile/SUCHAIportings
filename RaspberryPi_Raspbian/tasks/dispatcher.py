#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'


import multiprocessing
from repos import command
from core import shared_resources
from repos import state
import datetime
import SUCHAI_config
from core import gnrluse
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
        arg = "received Cmd %s from %s CmdGroup" % (disp_cmd.cmdName, disp_cmd.groupName)
        logger.info(arg)

        #fill SysReq info
        sys_req = command.CmdRepo.get_sysreq_byname(disp_cmd.groupName, disp_cmd.cmdName)
        # disp_cmd.sysReq = sys_req

        #check sysReq
        # arg = "sys_req is %s" % sys_req
        # logger.info(arg)
        current_sys_req = state.StateVar.get_value(state.StateVar.eps_soc)
        executable = check_if_executable(current_sys_req, sys_req)

        #execute
        if executable:
            i_time = datetime.datetime.now()
            arg = "executing command"
            logger.info(arg)
            gnrluse.console_print("w>>")
            cmd_funct = command.CmdRepo.get_function_byname(disp_cmd.groupName, disp_cmd.cmdName)
            exitcode = cmd_funct(disp_cmd.param)
            f_time = datetime.datetime.now()

            #report time, return status, etc
            d_time = f_time - i_time
            arg = "command executed"
            logger.info(arg)
            arg = "d_time %s, exitcode %s, sys_req %s" % (d_time, exitcode, sys_req)
            logger.info(arg)
        else:
            #report time, return status, etc
            arg = "command NOT executed (not executable)"
            logger.info(arg)
            arg = "sys_req %s, current_sys_req %s" % (sys_req, current_sys_req)
            logger.info(arg)


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
