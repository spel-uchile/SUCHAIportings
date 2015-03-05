#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'


import multiprocessing
import logging
logger = logging.getLogger(__name__)


def task_housekeeping():
    arg = "%s, %s, %s, %s" % (taskHandler.name, taskHandler.pid, taskHandler.is_alive(), taskHandler.exitcode)
    logger.debug(arg)

taskHandler = multiprocessing.Process(group=None,
                                      target=task_housekeeping,
                                      name="task_housekeeping",
                                      args=(),
                                      kwargs={})