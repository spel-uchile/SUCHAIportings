#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'


import multiprocessing
import logging
logger = logging.getLogger(__name__)


def task_flightplan():
    arg = "%s, %s, %s, %s" % (taskHandler.name, taskHandler.pid, taskHandler.is_alive(), taskHandler.exitcode)
    logger.debug(arg)

taskHandler = multiprocessing.Process(group=None,
                                      target=task_flightplan,
                                      name="task_flightplant",
                                      args=(),
                                      kwargs={})