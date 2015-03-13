# -*- coding: utf-8 -*-
__author__ = 'toopazo'


import multiprocessing
import logging
# from repos import command
from repos.cmds import cmdcon
from repos.cmds import cmdrtc
from core import shared_resources
from core import suchai_types
import time
logger = logging.getLogger(__name__)


def task_housekeeping():
    arg = "name %s, pid %s, is_alive %s, exitcode %s" %\
          (taskHandler.name, taskHandler.pid, taskHandler.is_alive(), taskHandler.exitcode)
    logger.debug(arg)

    for i in range(0, 5):
        # time.sleep(2)

        #send cmd to Dispatcher (blocking call)
        disp_cmd = suchai_types.DispCmd(cmdid=None,   # replaced by groupName and cmdName (cmdId = groupName + cmdName)
                                        param=i,
                                        taskorig=taskHandler.name,   # suchai_types.TaskOrig.THOUSEKEEPING,
                                        sysreq=None,   # filled by Dispatcher
                                        groupname=cmdcon.CmdGroupCON.groupName,
                                        cmdname=cmdcon.CmdGroupCON.cmdEnum.con_help.name)
        shared_resources.dispatcherQueue.put(disp_cmd)  # blocking by default

        #send cmd to Dispatcher (blocking call)
        disp_cmd = suchai_types.DispCmd(cmdid=None,   # replaced by groupName and cmdName (cmdId = groupName + cmdName)
                                        param=i,
                                        taskorig=taskHandler.name,   # suchai_types.TaskOrig.THOUSEKEEPING,
                                        sysreq=None,   # filled by Dispatcher
                                        groupname=cmdrtc.CmdGroupRTC.groupName,
                                        cmdname=cmdrtc.CmdGroupRTC.cmdEnum.rtc_get_time_now.name)
        shared_resources.dispatcherQueue.put(disp_cmd)  # blocking by default

    while True:
        pass

taskHandler = multiprocessing.Process(group=None,
                                      target=task_housekeeping,
                                      name="task_housekeeping",
                                      args=(),
                                      kwargs={})