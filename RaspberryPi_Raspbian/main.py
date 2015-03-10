#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'

#if defined(__XC16__)
    #include <xc.h>
#else
    #include <p24FJ256GA110.h>
#endif

# /* RTOS Includes */
# include "FreeRTOSConfig.h" # not necessary in this porting
# include "FreeRTOS.h" # not necessary in this porting
#include "task.h" # reemplazable por thread de Python/linux
# import multiprocessing # Process
#include "queue.h" # reemplazable por queue de Python/linux
# import multiprocessing  # Queue
#include "semphr.h" # reemplazable por mutex de Python/linux
import multiprocessing  # Lock
# include "list.h"  # not necessary in this porting

# /* Drivers includes */
# include "pic_pc104_config.h" # reemplazable por las configs de Hw de
# la Raspberry (perifericos como: SPI, I2C, pines IO, WDT, etc)
from hwconfigs import internalconfigs
from hwconfigs import externalconfigs
# /* Task includes */
# include "suchaiDeployment.h" # reemplazable por: dep_init_suchai_hw(); (hw externo a la Raspberry)
#  dep_init_suchai_repos(); (state, data y cmd repos) dep_init_suchai_tasks(); (lanzar task/threads)
from core import deployment
from core import shared_resources

# /* Command Includes */
# include "cmdIncludes.h" # reemplazable por clases con definicion de los comandos "DispCmd" y "ExeCmd"
# from core import command

# import "SUCHAI_config.h"
import SUCHAI_config

import sys
from core import gnrluse

# /* Config Words */
# PPC_DEFAULT_CW1();  # not necessary in this porting
# PPC_DEFAULT_CW2();  # not necessary in this porting
# PPC_DEFAULT_CW3();  # not necessary in this porting

# xQueueHandle dispatcherQueue, i2cRxQueue, executerCmdQueue, executerStatQueue;
# xSemaphoreHandle statusRepositorySem, consolePrintfSem, rtcPrintSem;

# xTaskHandle taskDeploymentHandle, taskDispatcherHandle;
# xTaskHandle taskComunicationsHandle, taskConsoleHandle, taskFlightPlanHandle,
#             taskFlightPlan2Handle, taskFlightPlan3Handle, taskHouskeepingHandle;
import logging
logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG,
                        #format='%(asctime)s:%(name)s:%(levelname)s:%(message)s',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        #format="%(asctime)-15s:%(message)s",
                        datefmt='%Y/%m/%d %H:%M:%S',
                        filename='suchai.log',
                        filemode='a',
                        #disable_existing_loggers=False
                        )
    # logger.info('\n')
    # logger.debug('Hello World')
    # logger.info('You should note this')
    # logger.warning('be warned')
    # logger.error("an normal error arose")
    # logger.critical("a critical error arose")

    logger.info("\n\n")
    logger.info("[main] Entry point")
    gnrluse.console_print("main stdin %s" % sys.stdin)
    gnrluse.console_print("main stdout %s" % sys.stdout)

    # /* Initializing shared Queues */
    # see shared_resources module

    # /* Initializing shared Semaphore */
    # see shared_resources module

    # /* Configure Peripherals */
    # /* NOTA: EL TIMER 1 Y SU INTERRUPCION ESTAN CONFIGURADOS POR EL S.0. (FreeRTOS) */
    # default_PIC_config();
    internalconfigs.init_hw_configs()

    # # /* Initializing LibCSP*/
    # com_csp_initialization(); //Issue #8: Initialize libcsp before trx
    # not necessary in this porting

    # /* System initialization */
    # dep_init_suchai_hw();
    externalconfigs.init_hw_configs()
    # dep_init_suchai_repos();
    deployment.init_suchai_repos()

    # /* Crating SUCHAI tasks */
    # dep_init_suchai_tasks();
    deployment.launch_tasks()   # blocking call, waits child prcesses to join

    # not necessary in this porting
    # # /* Start the scheduler. Should never return */
    # printf("\nStarting FreeRTOS [->]\r\n");
    # vTaskStartScheduler();

    # not necessary in this porting
    # while True:
    #     # /*
    #     #  * El sistema solo llega hasta aca si el Scheduler falla debido
    #     #  * a falta de memoria u otro problema
    #     #  */
    #     printf("\n>>FreeRTOS [FAIL]\n");
    #     ppc_reset(NULL);

    return 0


if __name__ == "__main__":
    main()

# void vApplicationIdleHook(void)
# {
#     /*
#      * **configUSE_IDLE_HOOK must be set to 1**
#      * Esta funcion se ejecuta cuando el procesador
#      * no esta siendo utilizado por otra tarea
#      */
#
#     ClrWdt();
#     Idle();
# }
#
# void vApplicationStackOverflowHook(xTaskHandle* pxTask, signed char* pcTaskName)
# {
#     printf(">> Stak overflow! - TaskName: %s\n", pcTaskName);
#     ppc_reset(NULL);
# }
#
# #define STDIN   0
# #define STDOUT  1
# #define STDERR  2
# #define LF   '\n'
# #define CR   '\r'
# #define STDOUT_NO_CR
#
# void    mon_putc(char ch);
#
# int __attribute__((__weak__, __section__(".libc")))
# write(int handle, void * buffer, unsigned int len)
# {
#     portBASE_TYPE semStatus = xSemaphoreTake(consolePrintfSem, 2000/portTICK_RATE_MS);
#     if(semStatus != pdPASS){return 0;}
#
#     int i = 0;
#     switch (handle)
#     {
#         case STDOUT:
#         case STDERR:
#             while (i < len)
#                 mon_putc(((char*)buffer)[i++]);
#             break;
#     }
#     xSemaphoreGive(consolePrintfSem);
#     return (len);  // number of characters written
# }
#
# #define STDOUT_NO_CR_WITH_LF
# void mon_putc(char ch)
# {
#     while(U1STAbits.UTXBF);  /* wait if the buffer is full */
# #ifndef STDOUT_NO_CR_WITH_LF
#     if (LF == ch)
#         putcUART1(CR);
# #endif
# #ifdef STDOUT_NO_CR
#     if (CR == ch)
#         return;
# #endif
#     putcUART1(ch);
# }
#
# BOOL shouldDelayTask( portTickType * const pxPreviousWakeTime, portTickType xTimeIncrement)
# {
#     portTickType xTickCount = xTaskGetTickCount();
#
# //    printf("  [shouldDelayTask] xLastWakeTime = %u, xDelay_ticks = %u, "
# //            "xTickCount = %u \r\n", *pxPreviousWakeTime,
# //            xTimeIncrement, xTickCount);
#
#
#     portTickType xTimeToWake;
#     BOOL xShouldDelay = FALSE;
#
#     /* Generate the tick time at which the task wants to wake. */
#     xTimeToWake = *pxPreviousWakeTime + xTimeIncrement;
#
#     if( xTickCount < *pxPreviousWakeTime )
#     {
#             /* The tick count has overflowed since this function was
#             lasted called.  In this case the only time we should ever
#             actually delay is if the wake time has also	overflowed,
#             and the wake time is greater than the tick time.  When this
#             is the case it is as if neither time had overflowed. */
#             if( ( xTimeToWake < *pxPreviousWakeTime ) && ( xTimeToWake > xTickCount ) )
#             {
#                     xShouldDelay = TRUE;
#                     //printf(" asdasd 1\r\n");
#             }
#     }
#     else
#     {
#             /* The tick time has not overflowed.  In this case we will
#             delay if either the wake time has overflowed, and/or the
#             tick time is less than the wake time. */
#             if( ( xTimeToWake < *pxPreviousWakeTime ) || ( xTimeToWake > xTickCount ) )
#             {
#                     xShouldDelay = TRUE;
#                     //printf(" asdasd 2\r\n");
#             }
#     }
#
# //    /* Update the wake time ready for the next call. */
# //    *pxPreviousWakeTime = xTimeToWake;
#
#     if( xShouldDelay != FALSE )
#     {
#
#     }
#
#     return xShouldDelay;
# }