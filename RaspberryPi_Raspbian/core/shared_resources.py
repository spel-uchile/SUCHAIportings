#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'

import logging
logger = logging.getLogger(__name__)

# xQueueHandle dispatcherQueue, i2cRxQueue, executerCmdQueue, executerStatQueue;
# xSemaphoreHandle statusRepositorySem, consolePrintfSem, rtcPrintSem;
dispatcherQueue = None  # must be initialized using queue.Queue(maxsize=x)
i2cRxQueue = None  # must be initialized using queue.Queue(maxsize=x)
executerCmdQueue = None  # must be initialized using queue.Queue(maxsize=x)
executerStatQueue = None  # must be initialized using queue.Queue(maxsize=x)
statusRepositorySem = None  # must be initialized using multiprocessing.Lock()
consolePrintfSem = None  # must be initialized using multiprocessing.Lock()
rtcPrintSem = None  # must be initialized using multiprocessing.Lock()