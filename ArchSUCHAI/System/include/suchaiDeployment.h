/**
 * @file  taskDeployment.h
 * @author Tomas Opazo T - tomas.opazo.t@gmail.com
 * @author Carlos Gonzalez C - carlgonz@ug.uchile.cl
 * @date 2012
 * @copyright GNU GPL v3
 *
 * @id 0x1102
 *
 * This task implements a listener that initializes all the flight software.
 */

#ifndef _DEPLOYMENT_H
#define _DEPLOYMENT_H

/* RTOS Includes */
//#include "FreeRTOSConfig.h"
//#include "FreeRTOS.h"
//#include "task.h"
//#include "queue.h"
//#include "list.h"
//
//#include "pic_pc104_config.h"
#include "osw_tasks.h"
#include "osw_queue.h"
#include "osw_gnrlcalls.h"

#include "cmdIncludes.h"
#include "cmdRepository.h"
/* Add ommands definitions*/
#include "cmdCON.h"


//System Tasks
#include "taskDispatcher.h"
#include "taskExecuter.h"
//Application Tasks
#include "taskConsole.h"


void dep_init_suchai_hw(void);
void dep_init_suchai_repos(void);
void dep_InitSystem(void);

int dep_init_sysbus_hw(void *param);
int dep_init_dataRepo(void *param);
int dep_init_cmdRepo(void *param);
int dep_init_stateRepo(void *param);
int dep_init_adHoc_strcts(void *param);

int dep_suicide(void *param);           //deprecated
//int dat_sd_init(void);                //deprecated
//void dep_csp_initialization(void);    //deprecated

#endif //_DEPLOYMENT_H
