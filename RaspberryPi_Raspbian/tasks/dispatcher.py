#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'


import multiprocessing
from repos import command
from core import shared_resources
from core import gnrluse
import logging
logger = logging.getLogger(__name__)


def task_dispatcher():
    arg = "%s, %s, %s, %s" % (taskHandler.name, taskHandler.pid, taskHandler.is_alive(), taskHandler.exitcode)
    logger.debug(arg)

    while True:
        disp_cmd = shared_resources.dispatcherQueue.get()  # blocking by default
        cmd = command.CmdRepo.get_function_byname(disp_cmd.groupname, disp_cmd.cmdname)
        cmd.funct(disp_cmd.param)
        print("**************************************************************")

taskHandler = multiprocessing.Process(group=None,
                                      target=task_dispatcher,
                                      name="task_dispatcher",
                                      args=(),
                                      kwargs={})