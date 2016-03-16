/*                                 SUCHAI
 *                      NANOSATELLITE FLIGHT SOFTWARE
 *
 *      Copyright 2013, Carlos Gonzalez Cortes, carlgonz@ug.uchile.cl
 *      Copyright 2013, Tomas Opazo Toro, tomas.opazo.t@gmail.com
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
#include "suchaiDeployment.h"

//FreeRTOS tasks and Queue Handlers
//extern xTaskHandle taskComunicationsHandle;
//extern xTaskHandle taskDispatcherHandle;
//extern xTaskHandle taskConsoleHandle;
//extern xTaskHandle taskFlightPlanHandle;
//extern xTaskHandle taskFlightPlan2Handle;
//extern xTaskHandle taskFlightPlan3Handle;
//extern xTaskHandle taskHouskeepingHandle;
//extern xQueueHandle dispatcherQueue;

//void dep_init_suchai_hw(void)
//{
//    #if (SCH_TDEPLOYMENT_VERBOSE)
//        printf("\n[suchaiDeployment] dep_init_suchai_hw()..\r\n");
//    #endif
//
//    /* External Perippherals/Componentes/subsystems/Hw etc ..*/
//    dep_init_sysbus_hw(NULL);
//}
//
//void dep_init_suchai_repos(void){
//    #if (SCH_TDEPLOYMENT_VERBOSE)
//        printf("\n[suchaiDeployment] dep_init_suchai_repos()..\r\n");
//    #endif
//
//    /* Repositories */
//    dep_init_stateRepo(NULL);   //modify specific reset-dependant STA_StateVar vars
//    dep_init_cmdRepo(NULL);     //loads cmdXXX repos to be used
//    dep_init_dataRepo(NULL);    //prepares GnrlPurposeBuff to be used
//    /* Other structures */
//    dep_init_adHoc_strcts(NULL);
//}
//
///**
// * Initializes status  repository
// *
// * @param param Not used
// * @return 1
// */
//int dep_init_stateRepo(void *param)
//{
//    #if (SCH_TDEPLOYMENT_VERBOSE>=1)
//        printf("\n[dep_init_stateRepo] Initializing state repository..\r\n");
//    #endif
//
//    #if (SCH_TDEPLOYMENT_VERBOSE>=2)
//        printf("    * sta_onReset_BusStateRepo()..\r\n");
//    #endif
//    sta_onReset_BusStateRepo();
//
//    #if (SCH_TDEPLOYMENT_VERBOSE>=2)
//        printf("    * sta_onReset_PayStateRepo()..\r\n");
//    #endif
//    sta_onReset_PayStateRepo();
//
//    return 1;
//}
//
//extern cmdFunction trxFunction[];
//extern cmdFunction ppcFunction[];
//extern cmdFunction conFunction[];
//extern cmdFunction epsFunction[];
//extern cmdFunction drpFunction[];
//extern cmdFunction srpFunction[];
//extern cmdFunction payFunction[];
//extern cmdFunction rtcFunction[];
//extern cmdFunction tcmFunction[];
//extern cmdFunction thkFunction[];
//extern int trx_sysReq[];
//extern int ppc_sysReq[];
//extern int con_sysReq[];
//extern int eps_sysReq[];
//extern int drp_sysReq[];
//extern int srp_sysReq[];
//extern int pay_sysReq[];
//extern int rtc_sysReq[];
//extern int tcm_sysReq[];
//extern int thk_sysReq[];
///**
// * Initializes command repository
// *
// * @param param Not used
// * @return 1
// */
//int dep_init_cmdRepo(void *param)
//{
//    #if (SCH_TDEPLOYMENT_VERBOSE>=1)
//        printf("\n[dep_init_cmdRepo] Initializing command repository..\r\n");
//    #endif
//
////    #if (SCH_TASKDEPLOYMENT_VERBOSE>=2)
////        printf("    * Commands rep.\r\n");
////    #endif
////    repo_onResetCmdRepo();
//
//    #if (SCH_TDEPLOYMENT_VERBOSE>=2)
//        printf("    * Attaching cmdCON..\r\n");
//    #endif
//    CmdRepo_cmdXXX_handler cmdCON_handler;
//    cmdCON_handler.cmdOwn = SCH_CMD_CON;
//    cmdCON_handler.nCmd = CON_NCMD;
//    cmdCON_handler.p_xxxFunction = conFunction;
//    cmdCON_handler.p_xxxSysReq = con_sysReq;
//    cmdCON_handler.xxx_onReset = con_onResetCmdCON;
//    repo_set_cmdXXX_hanlder(cmdCON_handler);
//
//    // ...
//
//    return 1;
//}
//
///**
// * Initializes data repository
// *
// * @param param Not used
// * @return 1
// */
//int dep_init_dataRepo(void *param)
//{
//    #if (SCH_TDEPLOYMENT_VERBOSE>=1)
//        printf("\n[dep_init_Repos] Initializing data repositories..\r\n");
//    #endif
//
//    /* Initializing dataRepository*/
//    #if (SCH_TDEPLOYMENT_VERBOSE>=2)
//        printf("    * onReset data Repository..\r\n");
//    #endif
//    dat_onReset_dataRepo(TRUE);
//
//    /* Initializing the rest of dataRepository structures */
//    #if (SCH_TDEPLOYMENT_VERBOSE>=2)
//        printf("        * onReset Fligh Plan..\r\n");
//    #endif
//    dat_onReset_FlightPlan();
//
////    #if (SCH_TASKDEPLOYMENT_VERBOSE>=2)
////        printf("    * onReset Telecommand Buffer..\r\n");
////    #endif
////    dat_onReset_TeleCmdBuff();
//
//    #if (SCH_TDEPLOYMENT_VERBOSE>=2)
//        printf("        * onReset Payloads..\r\n");
//    #endif
//    dat_onReset_Payload_Buff();
//
//    return 1;
//}
//
///**
// * Initializes all data repositories
// *
// * @param param Not used
// * @return 1
// */
//int dep_init_adHoc_strcts(void *param)
//{
//    #if (SCH_TDEPLOYMENT_VERBOSE>=1)
//        printf("\n[dep_init_GnrlStruct] Initializing other structures...\r\n");
//    #endif
//
//    //Deprecated
////    #if( SCH_EPS_ONBOARD == 1 )
////        /* Initializing EPS struct */
////        #if (SCH_TDEPLOYMENT_VERBOSE>=2)
////            printf("    * init EPS structs\r\n");
////        #endif
////
////        setStateFlagEPS( (unsigned char)sta_get_BusStateVar(sta_eps_state_flag) );
////    #endif
//
//    return 1;
//}
//
///**
// * Ends taskDeployment by deleting it.
// * @param param Not used
// * @return 1 succes
// */
//int dep_suicide(void *param)
//{
//    #if (SCH_TDEPLOYMENT_VERBOSE)
//        printf("[suchaiDeployment] ENDS\r\n");
//        printf("[suchaiDeployment] Deleting task\r\n");
//    #endif
//    vTaskDelete(NULL);
//
//    while(1)
//    {
//        printf("    vTaskDelete(NULL) did NOT work out...\r\n");
//        __delay_ms(3000);
//    }
//
//    return 1;
//}
//
///**
// * Starts all task.
// * @param param Not used
// * @return 1 success, 0 fails
// */
//void dep_init_suchai_tasks(void)
//{
//    /* Crating base tasks */
//    printf("\n[main] Starting base tasks...\r\n");
//    #if(SCH_TASKEXECUTER_INSIDE_TASKDISPATCHER==1)
//        xTaskCreate(taskDispatcher, (signed char *)"DIS", 4.5*configMINIMAL_STACK_SIZE, NULL, 4, &taskDispatcherHandle);
//    #else
//        xTaskCreate(taskExecuter, (signed char *)"EXE", 3*configMINIMAL_STACK_SIZE, NULL, 4, &taskExecuterHandle);
//        xTaskCreate(taskDispatcher, (signed char *)"DIS", 1.5*configMINIMAL_STACK_SIZE, NULL, 3, &taskDispatcherHandle);
//    #endif
//
//    /* Creating other tasks*/
//    #if (SCH_TDEPLOYMENT_VERBOSE>=1)
//        printf("\n[dep_launch_tasks] Starting all tasks...\r\n");
//    #endif
//
//    #if (SCH_TCONSOLE_USE == 1)
//        #if (SCH_TDEPLOYMENT_VERBOSE>=2)
//            printf("    * Creating taskConsole\r\n");
//        #endif
//        xTaskCreate(taskConsole, (signed char *)"CON", 1.5*configMINIMAL_STACK_SIZE, NULL, 2, &taskConsoleHandle);
//        __delay_ms(300);
//    #endif
//}
///**
// * Initializes all peripherals and subsystems.
// * @param param Not used.
// * @return 1 success, 0 fail.
// */
//int dep_init_sysbus_hw(void *param)
//{
//    int resp;
//    //STA_BusStateVar hw_isAlive;
//
//    #if (SCH_TDEPLOYMENT_VERBOSE>=1)
//        printf("\n[dep_init_bus_hw] Initializig external hardware...\r\n");
//    #endif
//
//    #if (SCH_MEMSD_ONBOARD==1)
//    {
//        #if (SCH_TDEPLOYMENT_VERBOSE>=2)
//            printf("    * External MemSD .. ");
//        #endif
//        //resp = dat_sd_init();
//        resp =  SD_init_memSD();
//        //hw_isAlive = sta_MemSD_isAlive;
//        //sta_set_stateVar(hw_isAlive, resp);
//        #if (SCH_TDEPLOYMENT_VERBOSE>=2)
//            if(resp == 0x01){
//                printf("Ok\r\n");
//            }
//            else{
//                printf("Fail\r\n");
//            }
//        #endif
//    }
//    #endif
//
//    #if (SCH_SYSBUS_ONBOARD==1 && SCH_MEMEEPROM_ONBOARD==1 )
//    {
//        #if (SCH_TDEPLOYMENT_VERBOSE>=2)
//            printf("    * External MemEEPROM .. ");
//        #endif
//        resp = mem_init_EEPROM();
//        //hw_isAlive = sta_MemEEPROM_isAlive;
//        //sta_set_stateVar(hw_isAlive, resp);
//        #if (SCH_TDEPLOYMENT_VERBOSE>=2)
//            if(resp == 0x01){
//                printf("Ok\r\n");
//            }
//            else{
//                printf("Fail\r\n");
//            }
//        #endif
//    }
//    #endif
//
//    #if (SCH_RTC_ONBOARD==1)
//    {
//        #if (SCH_TDEPLOYMENT_VERBOSE>=2)
//            printf("    * External RTC .. ");
//        #endif
//        resp = RTC_init();
//        //hw_isAlive = sta_RTC_isAlive;
//        //sta_set_stateVar(hw_isAlive, resp);
//        #if (SCH_TDEPLOYMENT_VERBOSE>=2)
//            if(resp == 0x01){
//                printf("Ok\r\n");
//            }
//            else{
//                printf("Fail\r\n");
//            }
//        #endif
//    }
//    #endif
//
//    #if (SCH_TRX_ONBOARD==1)
//    {
//        #if (SCH_TDEPLOYMENT_VERBOSE>=2)
//            printf("    * External TRX .. ");
//        #endif
//        //Check if suchai is deployed to select correct trx configuration
//        int deployed = sta_get_BusStateVar(sta_dep_ant_deployed);
//        //Initialize trx
//        resp  = trx_initialize(&deployed);
//        //hw_isAlive = sta_TRX_isAlive;
//        //sta_set_stateVar(hw_isAlive, resp);
//        #if (SCH_TDEPLOYMENT_VERBOSE>=2)
//            if(resp == 0x01){
//                printf("Ok\r\n");
//            }
//            else{
//                printf("Fail\r\n");
//            }
//        #endif
//    }
//    #endif
//
//    #if (SCH_EPS_ONBOARD==1)
//    {
//        #if (SCH_TDEPLOYMENT_VERBOSE>=2)
//            printf("    * External EPS .. ");
//        #endif
//        resp  = eps_initialize(NULL);
//        //hw_isAlive = sta_EPS_isAlive;
//        //sta_set_stateVar(hw_isAlive, resp);
//        #if (SCH_TDEPLOYMENT_VERBOSE>=2)
//            if(resp == 0x01){
//                printf("Ok\r\n");
//            }
//            else{
//                printf("Fail\r\n");
//            }
//        #endif
//    }
//    #endif
//
//    #if (SCH_ANTENNA_ONBOARD==1)
//    {
//        #if (SCH_TDEPLOYMENT_VERBOSE>=2)
//            printf("    * External Antenna .. ");
//        #endif
//        resp = sta_get_BusStateVar(sta_AntSwitch_isOpen);
//        //hw_isAlive = sta_Antenna_isDeployed;
//        //sta_set_stateVar(hw_isAlive, resp);
//        #if (SCH_TDEPLOYMENT_VERBOSE>=2)
//            if(resp == 0x01){
//                printf("Ok (Deployed)\r\n");
//            }
//            else{
//                printf("Fail (NOT Deployed)\r\n");
//            }
//            printf("Antenna Deployment is carried out (if pending) by Task Housekeeping\r\n");
//            //check_deploy_antenna();
//        #endif
//
//    }
//    #endif
//
//    return 1;
//}
