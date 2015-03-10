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
    arg = "name %s, pid %s, is_alive %s, exitcode %s" %\
          (taskHandler.name, taskHandler.pid, taskHandler.is_alive(), taskHandler.exitcode)
    logger.debug(arg)

    for i in range(0, 5):
        # time.sleep(2)

        #send cmd to Dispatcher (blocking call)
        disp_cmd = gnrluse.DispCmd(cmdid=None,   # replaced by groupName and cmdName (cmdId = groupName + cmdName)
                                   param=i,
                                   taskorig=gnrluse.TaskOrig.THOUSEKEEPING,
                                   sysreq=None,   # filled by Dispatcher
                                   groupname=cmdconsole.CmdGroupCON.groupName,
                                   cmdname=cmdconsole.CmdGroupCON.cmdEnum.help)
        shared_resources.dispatcherQueue.put(disp_cmd)  # blocking by default

        #send cmd to Dispatcher (blocking call)
        disp_cmd = gnrluse.DispCmd(cmdid=None,   # replaced by groupName and cmdName (cmdId = groupName + cmdName)
                                   param=i,
                                   taskorig=gnrluse.TaskOrig.THOUSEKEEPING,
                                   sysreq=None,   # filled by Dispatcher
                                   groupname=cmdrtc.CmdGroupRTC.groupName,
                                   cmdname=cmdrtc.CmdGroupRTC.cmdEnum.get_time_now)
        shared_resources.dispatcherQueue.put(disp_cmd)  # blocking by default

taskHandler = multiprocessing.Process(group=None,
                                      target=task_housekeeping,
                                      name="task_housekeeping",
                                      args=(),
                                      kwargs={})