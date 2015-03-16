#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'

import multiprocessing
import SUCHAI_config
from core import gnrl_services
import logging
logger = logging.getLogger(__name__)

dispatcherQueue = multiprocessing.Queue(maxsize=1)  # xQueueCreate(25, sizeof(DispCmd))
if SUCHAI_config.SCH_TASKEXECUTER_INSIDE_TASKDISPATCHER == 1:
    # no Queue creation
    pass
else:
    executerCmdQueue = multiprocessing.Queue(maxsize=1)    # xQueueCreate(1,sizeof(ExeCmd));
    executerStatQueue = multiprocessing.Queue(maxsize=1)    # xQueueCreate(1,sizeof(int));
#endif
# i2cRxQueue se usa para pasar datos desde TRX Gomspace CSP a taskComunications. Para este porting no se usara
# deployment.i2cRxQueue = queue.Queue(maxsize=I2C_MTU)   # xQueueCreate(I2C_MTU, sizeof(char));   //TRX_GOMSPACE

statusRepositorySem = multiprocessing.Lock()  # xSemaphoreCreateMutex();
consolePrintfSem = multiprocessing.Lock()  # xSemaphoreCreateMutex();
rtcPrintSem = multiprocessing.Lock()  # xSemaphoreCreateMutex();
#TODO modified by toopazo to ease porting
priorityEmulatorSem = multiprocessing.Lock()  # xSemaphoreCreateMutex();


def send_to_dispatcher(disp_cmd):
    # Only one task can send cmds to dispatcher, the others block until the command is done. If there is enough
    # IDLE time the mutex will be equally/fairly accessed by all tasks
    # This is equivalent to a OS that guarantees "Fixed priority pre-emptive scheduling"
    # with tasks given a lower priority relative to the dispatcher task
    priorityEmulatorSem.acquire()
    # gnrl_services.console_print("priorityEmulatorSem was acquired by %s" % disp_cmd.taskOrig)
    dispatcherQueue.put(disp_cmd)

# # xQueueHandle dispatcherQueue, i2cRxQueue, executerCmdQueue, executerStatQueue;
# # xSemaphoreHandle statusRepositorySem, consolePrintfSem, rtcPrintSem;
# dispatcherQueue = None  # must be initialized using queue.Queue(maxsize=x)
# i2cRxQueue = None  # must be initialized using queue.Queue(maxsize=x)
# executerCmdQueue = None  # must be initialized using queue.Queue(maxsize=x)
# executerStatQueue = None  # must be initialized using queue.Queue(maxsize=x)
# statusRepositorySem = None  # must be initialized using multiprocessing.Lock()
# consolePrintfSem = None  # must be initialized using multiprocessing.Lock()
# rtcPrintSem = None  # must be initialized using multiprocessing.Lock()
#
#
# def init_queues():
#     global dispatcherQueue, executerCmdQueue, executerStatQueue
#
#     dispatcherQueue = multiprocessing.Queue(maxsize=1)  # xQueueCreate(25, sizeof(DispCmd))
#     if SUCHAI_config.SCH_TASKEXECUTER_INSIDE_TASKDISPATCHER == 1:
#         # no Queue creation
#         pass
#     else:
#         executerCmdQueue = multiprocessing.Queue(maxsize=1)    # xQueueCreate(1,sizeof(ExeCmd));
#         executerStatQueue = multiprocessing.Queue(maxsize=1)    # xQueueCreate(1,sizeof(int));
#     #endif
#     # i2cRxQueue se usa para pasar datos desde TRX Gomspace CSP a taskComunications. Para este porting no se usara
#     # deployment.i2cRxQueue = queue.Queue(maxsize=I2C_MTU)   # xQueueCreate(I2C_MTU, sizeof(char));   //TRX_GOMSPACE
#
#
# def semaphores():
#     global statusRepositorySem, consolePrintfSem, rtcPrintSem
#
#     statusRepositorySem = multiprocessing.Lock()  # xSemaphoreCreateMutex();
#     consolePrintfSem = multiprocessing.Lock()  # xSemaphoreCreateMutex();
#     rtcPrintSem = multiprocessing.Lock()  # xSemaphoreCreateMutex();