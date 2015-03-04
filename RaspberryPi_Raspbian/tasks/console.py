#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'


import multiprocessing


def task_console():
    print(taskHandler.name, taskHandler.pid, taskHandler.is_alive(), taskHandler.exitcode)

taskHandler = multiprocessing.Process(group=None,
                                      target=task_console,
                                      name="task_console",
                                      args=(),
                                      kwargs={})