#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'


import multiprocessing
from repos import command
from core import dispatcherhandler
from core import gnrl_services
from repos import state
import datetime
import SUCHAI_config
import logging
logger = logging.getLogger(__name__)


def listener_dispatcher():
    arg = "cmdName %s, pid %s, is_alive %s, exitcode %s" %\
          (listenerHandler.name, listenerHandler.pid, listenerHandler.is_alive(), listenerHandler.exitcode)
    logger.debug(arg)

    while True:
        msg = dispatcherhandler.DispCmd.receive_from_listeners()  # blocking call
        disp_cmd = dispatcherhandler.DispCmd(cmdid=msg.cmdId,
                                             cmdparam=msg.cmdParam,
                                             taskorigid=msg.taskorigId)

        # recover command from CmdRepo
        dispatched_cmd = command.CmdRepo.get_cmd_by_id(disp_cmd.cmdId)
        dispatched_cmd_cmdid = dispatched_cmd.cmdId
        dispatched_cmd_cmdname = dispatched_cmd.cmdName
        dispatched_cmd_cmdsysreq = dispatched_cmd.cmdSysReq
        # recover metadata from requesting Listener (DispCmd)
        dispatched_cmd_cmdparam = disp_cmd.cmdParam
        dispatched_cmd_taskorig = disp_cmd.taskorigId

        #report received Cmd
        arg = "[listener_dispatcher]"
        logger.info(arg)
        gnrl_services.console_print(arg)
        arg = "  Cmdid: 0x%0.4X, CmdName: %s, Listener: 0x%0.4X" %\
              (dispatched_cmd_cmdid, dispatched_cmd_cmdname, dispatched_cmd_taskorig)
        gnrl_services.console_print(arg)
        logger.info(arg)

        #check cmdSysReq
        system_soc = state.StateVar.get_value(state.StateVar.eps_soc)
        executable = check_if_executable(system_soc, dispatched_cmd_cmdsysreq)
        arg = "  Cmd cmdSysReq: %s, System soc: %s, executable: %s" %\
              (dispatched_cmd_cmdsysreq, system_soc, executable)
        logger.info(arg)
        gnrl_services.console_print(arg)

        #execute
        if executable:
            arg = "  >>"
            logger.info(arg)
            gnrl_services.console_print(arg)

            i_time = datetime.datetime.now()
            exitcode = dispatched_cmd.exect(dispatched_cmd_cmdparam)
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
            arg = "  Cmd cmdSysReq: %s, System soc: %s" % (dispatched_cmd_cmdsysreq, system_soc)
            logger.info(arg)
            gnrl_services.console_print(arg)

        arg = "----------------------"
        logger.info(arg)
        gnrl_services.console_print(arg)
        # gnrl_services.console_print("priorityEmulatorSem will be released (cmd sent by %s is done)"
        #                             % disp_cmd.taskorigId)

        # Necesario para emular prioridades de procesos de Listener (Listeners) y Dispatcher
        dispatcherhandler.DispCmd.priorityEmulatorSem.release()

listenerHandler = multiprocessing.Process(group=None,
                                          target=listener_dispatcher,
                                          name="listener_dispatcher",
                                          args=(),
                                          kwargs={})


def check_if_executable(cu_sys_req, sys_req):
    if SUCHAI_config.SCH_TASKDISPATCHER_CHECK_IF_EXECUTABLE == 0:   # Do NOT check, always autorize
        return True
    if cu_sys_req < sys_req:
        return False
    else:
        return True
