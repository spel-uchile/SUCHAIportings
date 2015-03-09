#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'

import multiprocessing
import SUCHAI_config
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