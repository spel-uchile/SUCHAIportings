# -*- coding: utf-8 -*-
__author__ = 'toopazo'


import multiprocessing
import logging
logger = logging.getLogger(__name__)


def listener_flightplan():
    arg = "cmdName %s, pid %s, is_alive %s, exitcode %s" %\
          (listenerHandler.name, listenerHandler.pid, listenerHandler.is_alive(), listenerHandler.exitcode)
    logger.debug(arg)

    while True:
        pass

listenerHandler = multiprocessing.Process(group=None,
                                          target=listener_flightplan,
                                          name="task_flightplant",
                                          args=(),
                                          kwargs={})