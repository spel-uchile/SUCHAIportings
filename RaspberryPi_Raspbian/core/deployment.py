#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'

from tasks import comunications
from tasks import console
from tasks import dispatcher
from tasks import flightplan
from tasks import housekeeping
import time


def init_state_repo():
    pass


def init_command_repo():
    pass


def init_data_repo():
    pass


def init_suchai_repos():
    # /* Repositories */
    init_state_repo()       # modify specific reset-dependant STA_StateVar vars
    init_command_repo()     # loads cmdXXX repos to be used
    init_data_repo()        # prepares GnrlPurposeBuff to be used


def launch_tasks():
    handler = dispatcher.taskHandler
    print(handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    handler = comunications.taskHandler
    print(handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    handler = console.taskHandler
    print(handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    handler = flightplan.taskHandler
    print(handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    handler = housekeeping.taskHandler
    print(handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    print("-------------------------")

    time.sleep(2)

    dispatcher.taskHandler.start()
    comunications.taskHandler.start()
    console.taskHandler.start()
    flightplan.taskHandler.start()
    housekeeping.taskHandler.start()

    time.sleep(2)

    dispatcher.taskHandler.join()
    comunications.taskHandler.join()
    console.taskHandler.join()
    flightplan.taskHandler.join()
    housekeeping.taskHandler.join()

    print("-------------------------")
    handler = dispatcher.taskHandler
    print(handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    handler = comunications.taskHandler
    print(handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    handler = console.taskHandler
    print(handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    handler = flightplan.taskHandler
    print(handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    handler = housekeeping.taskHandler
    print(handler.name, handler.pid, handler.is_alive(), handler.exitcode)

    print("\nStarting Suchai Sw ..\n")


# xQueueHandle dispatcherQueue, i2cRxQueue, executerCmdQueue, executerStatQueue;
# xSemaphoreHandle statusRepositorySem, consolePrintfSem, rtcPrintSem;
dispatcherQueue = None  # must be initialized using queue.Queue(maxsize=x)
i2cRxQueue = None  # must be initialized using queue.Queue(maxsize=x)
executerCmdQueue = None  # must be initialized using queue.Queue(maxsize=x)
executerStatQueue = None  # must be initialized using queue.Queue(maxsize=x)
statusRepositorySem = None  # must be initialized using multiprocessing.Lock()
consolePrintfSem = None  # must be initialized using multiprocessing.Lock()
rtcPrintSem = None  # must be initialized using multiprocessing.Lock()
