/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.c
 * Author: toopazo
 *
 * Created on March 16, 2016, 12:54 PM
 */

#include <stdio.h>
#include <stdlib.h>

//#if(SCH_TARGET_ARCH == 1)
//    /* RTOS INCLUDES */
//    #INCLUDE "FREERTOSCONFIG.H"
//    #INCLUDE "FREERTOS.H"
//    #INCLUDE "TASK.H"
//    #INCLUDE "QUEUE.H"
//    #INCLUDE "SEMPHR.H"
//    #INCLUDE "LIST.H"
//#endif

/* Drivers includes */
//#include "pic_pc104_config.h"

///* Task includes */
//#include "suchaiDeployment.h"

///* Command Includes */
//#include "cmdIncludes.h"

//#if(SCH_TARGET_ARCH == 1)
//    /* Config Words */
//    PPC_DEFAULT_CW1();
//    PPC_DEFAULT_CW2();
//    PPC_DEFAULT_CW3();
//#endif

#include "osw_queue.h"
#include "osw_tasks.h"
#include "osw_gnrlcalls.h"
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

#include "cmdIncludes.h"

OSW_QueueDescriptor dispatcherQueue, i2cRxQueue, executerCmdQueue, executerStatQueue;

//OSSemaphoreHandler statusRepositorySem, consolePrintfSem, rtcPrintSem;
//
OSW_TaskDescriptor taskDeploymentDescriptor, taskDispatcherDescriptor, 
        taskComunicationsDescriptor, taskConsoleDescriptor, taskFlightPlanDescriptor,
        taskFlightPlan2Descriptor, taskFlightPlan3Descriptor, taskHouskeepingDescriptor;

/*
 * 
 */
int main(int argc, char** argv) {
    int stat;
    
    printf("[SUCHAI] Hello world \n");
    OSW_TaskUnitTesting();
    OSW_QueueUnitTesting();

    /* Initializing shared Queues */
    dispatcherQueue = OSW_QueueCreate("dispatcherQueue", 10, sizeof(DispCmd));

    #if(SCH_TASKEXECUTER_INSIDE_TASKDISPATCHER==1)
        //no Queue creation
    #else
        executerCmdQueue = xQueueCreate(1,sizeof(ExeCmd));
        executerStatQueue = xQueueCreate(1,sizeof(int));
    #endif
    //i2cRxQueue = OSQueueCreate("i2cRxQueue", 10, sizeof(char)); //I2C_MTU, sizeof(char));   //TRX_GOMSPACE

//    /* Initializing shared Semaphore */
//    statusRepositorySem = xSemaphoreCreateMutex();
//    consolePrintfSem = xSemaphoreCreateMutex();
//    rtcPrintSem = xSemaphoreCreateMutex();
//
//    /* Configure Peripherals */
//    /* NOTA: EL TIMER 1 Y SU INTERRUPCION ESTAN CONFIGURADOS POR EL S.0. (FreeRTOS) */
////    default_PIC_config();
//
////    /* Initializing LibCSP*/
////    com_csp_initialization(); //Issue #8: Initialize libcsp before trx
//
//    /* System initialization */
////    dep_init_suchai_hw();
////    dep_init_suchai_repos();
//
/////////////////////////////////////////////////
//// Uncomment section only for debug purposes //
/////////////////////////////////////////////////
////    int arg_param = 1;
////    thk_executeBeforeFlight((void *)&arg_param);
////    int tries = 1;
////    thk_deployment_registration(&tries);
/////////////////////////////////////////////////
//// Uncomment section only for debug purposes //
/////////////////////////////////////////////////

    dep_init_cmdRepo(NULL);     //loads cmdXXX repos to be used
        
    /* Crating SUCHAI tasks */
    //sleep(5);
    dep_InitSystem();

    /* Start the scheduler. Should never return */
//    printf("\nStarting FreeRTOS [->]\r\n");
//    vTaskStartScheduler();
    OSW_GnrlcallsSleep(3);

    /*
     * El sistema solo llega hasta aca si el Scheduler falla debido
     * a falta de memoria u otro problema
     */
    printf("[SUCHAI] Scheduler failed \n");
    //ppc_reset(NULL);
    
    stat = OSW_QueueClose(dispatcherQueue, "dispatcherQueue");
    printf("OSQueueClose(dispatcherQueue, \"dispatcherQueue\") = %d \n", stat);

    return (EXIT_SUCCESS);
}

//void vApplicationIdleHook(void)
//{
//    /*
//     * **configUSE_IDLE_HOOK must be set to 1**
//     * Esta funcion se ejecuta cuando el procesador
//     * no esta siendo utilizado por otra tarea
//     */
//
//    ClrWdt();
//    Idle();
//}
//
//void vApplicationStackOverflowHook(xTaskHandle* pxTask, signed char* pcTaskName)
//{
//    printf(">> [%s] Stack overflow! \r\n", pcTaskName);
//    __delay_ms(2000);
//    ppc_reset(NULL);
//}
//
//#define STDIN   0
//#define STDOUT  1
//#define STDERR  2
//#define LF   '\n'
//#define CR   '\r'
//#define STDOUT_NO_CR
//
//void    mon_putc(char ch);
//
//int __attribute__((__weak__, __section__(".libc")))
//write(int handle, void * buffer, unsigned int len)
//{
//    portBASE_TYPE semStatus = xSemaphoreTake(consolePrintfSem, 2000/portTICK_RATE_MS);
//    if(semStatus != pdPASS){return 0;}
//
//    int i = 0;
//    switch (handle)
//    {
//        case STDOUT:
//        case STDERR:
//            while (i < len)
//                mon_putc(((char*)buffer)[i++]);
//            break;
//    }
//    xSemaphoreGive(consolePrintfSem);
//    return (len);  // number of characters written
//}
//
//#define STDOUT_NO_CR_WITH_LF
//void mon_putc(char ch)
//{
//    while(U1STAbits.UTXBF);  /* wait if the buffer is full */
//#ifndef STDOUT_NO_CR_WITH_LF
//    if (LF == ch)
//        putcUART1(CR);
//#endif
//#ifdef STDOUT_NO_CR
//    if (CR == ch)
//        return;
//#endif
//    putcUART1(ch);
//}
//
//BOOL shouldDelayTask( portTickType * const pxPreviousWakeTime, portTickType xTimeIncrement)
//{
//    portTickType xTickCount = xTaskGetTickCount();
//
////    printf("  [shouldDelayTask] xLastWakeTime = %u, xDelay_ticks = %u, "
////            "xTickCount = %u \r\n", *pxPreviousWakeTime,
////            xTimeIncrement, xTickCount);
//
//
//    portTickType xTimeToWake;
//    BOOL xShouldDelay = FALSE;
//
//    /* Generate the tick time at which the task wants to wake. */
//    xTimeToWake = *pxPreviousWakeTime + xTimeIncrement;
//
//    if( xTickCount < *pxPreviousWakeTime )
//    {
//            /* The tick count has overflowed since this function was
//            lasted called.  In this case the only time we should ever
//            actually delay is if the wake time has also	overflowed,
//            and the wake time is greater than the tick time.  When this
//            is the case it is as if neither time had overflowed. */
//            if( ( xTimeToWake < *pxPreviousWakeTime ) && ( xTimeToWake > xTickCount ) )
//            {
//                    xShouldDelay = TRUE;
//                    //printf(" asdasd 1\r\n");
//            }
//    }
//    else
//    {
//            /* The tick time has not overflowed.  In this case we will
//            delay if either the wake time has overflowed, and/or the
//            tick time is less than the wake time. */
//            if( ( xTimeToWake < *pxPreviousWakeTime ) || ( xTimeToWake > xTickCount ) )
//            {
//                    xShouldDelay = TRUE;
//                    //printf(" asdasd 2\r\n");
//            }
//    }
//
////    /* Update the wake time ready for the next call. */
////    *pxPreviousWakeTime = xTimeToWake;
//
//    if( xShouldDelay != FALSE )
//    {
//
//    }
//
//    return xShouldDelay;
//}
