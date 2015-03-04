#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'


import multiprocessing


def task_dispatcher():
    print(taskHandler.name, taskHandler.pid, taskHandler.is_alive(), taskHandler.exitcode)

taskHandler = multiprocessing.Process(group=None,
                                      target=task_dispatcher,
                                      name="task_dispatcher",
                                      args=(),
                                      kwargs={})