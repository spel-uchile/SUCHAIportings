#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'


import multiprocessing
import logging
# from repos import command
from repos.cmds import cmdconsole
from repos.cmds import cmdrtc
from core import shared_resources
from core import gnrluse
import time
logger = logging.getLogger(__name__)


def task_housekeeping():
    arg = "%s, %s, %s, %s" % (taskHandler.name, taskHandler.pid, taskHandler.is_alive(), taskHandler.exitcode)
    logger.debug(arg)
    for i in range(0, 5):
        time.sleep(2)

        #send cmd to Dispatcher (blocking call)
        disp_cmd = gnrluse.DispCmd(cmdid=None,   # replaced by groupname and cmdname (cmdid = groupname + cmdname)
                                   param=i,
                                   taskorig=gnrluse.TaskOrig.THOUSEKEEPING,
                                   sysreq=None,   # filled by Dispatcher
                                   groupname=cmdconsole.CmdGroupCON.groupName,
                                   cmdname=cmdconsole.CmdGroupCON.cmdEnum.help)
        shared_resources.dispatcherQueue.put(disp_cmd)  # blocking by default

        # command.CmdRepo.get_function_byname(cmdconsole.CmdCON().groupName, cmdconsole.CmdCON.help.__name__)(i)
        # command.CmdRepo.get_function_byid(cmdconsole.CmdCON().groupName, 0)(None)
        # command.CmdRepo.get_function_byid(cmdrtc.CmdRTC().groupName, 1)(None)
        # print("command.CmdRepo.get_sysreq_byid(cmdrtc.CmdRTC().groupName, 1) => %s" %
        #       command.CmdRepo.get_sysreq_byid(cmdrtc.CmdRTC().groupName, 1))
        # command.CmdRepo.get_function_byid(cmdrtc.CmdRTC().groupName, 121)(None)
        # print("command.CmdRepo.get_sysreq_byid(cmdrtc.CmdRTC().groupName, 121) => %s"
        #       % command.CmdRepo.get_sysreq_byid(cmdrtc.CmdRTC().groupName, 121))
        # print("**************************************************************")

taskHandler = multiprocessing.Process(group=None,
                                      target=task_housekeeping,
                                      name="task_housekeeping",
                                      args=(),
                                      kwargs={})