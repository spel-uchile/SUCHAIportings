#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'


import multiprocessing


def task_comunications():
    print(taskHandler.name, taskHandler.pid, taskHandler.is_alive(), taskHandler.exitcode)

taskHandler = multiprocessing.Process(group=None,
                                      target=task_comunications,
                                      name="task_comunications",
                                      args=(),
                                      kwargs={})