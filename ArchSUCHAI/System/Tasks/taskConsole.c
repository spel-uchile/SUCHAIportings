///*                                 SUCHAI
// *                      NANOSATELLITE FLIGHT SOFTWARE
// *
// *      Copyright 2013, Carlos Gonzalez Cortes, carlgonz@ug.uchile.cl
// *      Copyright 2013, Tomas Opazo Toro, tomas.opazo.t@gmail.com
// *
// * This program is free software: you can redistribute it and/or modify
// * it under the terms of the GNU General Public License as published by
// * the Free Software Foundation, either version 3 of the License, or
// * (at your option) any later version.
// *
// * This program is distributed in the hope that it will be useful,
// * but WITHOUT ANY WARRANTY; without even the implied warranty of
// * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// * GNU General Public License for more details.
// *
// * You should have received a copy of the GNU General Public License
// * along with this program.  If not, see <http://www.gnu.org/licenses/>.
// */
//
#include "taskConsole.h"

extern OSW_QueueDescriptor dispatcherQueue;

const char console_baner[] =
"______________________________________________________________________________\n\
                     ___ _   _  ___ _  _   _   ___ \n\
                    / __| | | |/ __| || | /_\\ |_ _|\n\
                    \\__ \\ |_| | (__| __ |/ _ \\ | | \n\
                    |___/\\___/ \\___|_||_/_/ \\_\\___|\n\
______________________________________________________________________________\n\n";
//"\n\n====== WELCOME TO THE SUCHAI CONSOLE - PRESS ANY KEY TO START ======\n\r"

static int verbose_level = 1;

void *taskConsole(void *param)
{
    printf("[taskConsole] Started \r\n");

    //char ret[10];

    //const unsigned int Delayms = 250 / portTICK_RATE_MS;
    const unsigned int Delayms = 0.250;
    DispCmd newCmd;
    newCmd.idOrig = SCH_TCONSOLE_IDORIG; /* Consola */
    newCmd.cmdId = CMD_CMDNULL;  /* cmdNULL */
    newCmd.param = 0;

    /*Avoid the acummulation of commands while the SUCHAI is still deploying.. */
//    #if (SCH_THOUSEKEEPING_USE == 1)
//        portTickType xLastWakeTime = xTaskGetTickCount();
//        portTickType check_deployment_time = (10000) / portTICK_RATE_MS;      /* check every 10sec  */
//        while( TRUE ){
//            /* TODO: Infinite loop if EEPROM is not onboard */
//            if( sta_get_BusStateVar(sta_dep_ant_deployed)==1 ){
//                break;
//            }
//            vTaskDelayUntil(&xLastWakeTime, check_deployment_time);
//        }
//    #endif

    /* Initializing console */
//    con_init();

#if (SCH_TCONSOLE_VERBOSE>=1)
    //__delay_ms(500);    //helps printing a cleaner banner (avoid interruption)
    OSW_GnrlcallsSleep(0.5);
    printf((char *)console_baner);
#endif

    while(1)
    {
        if(verbose_level >= 1){
            printf("[taskConsole] main loop \r\n");
        }
        //vTaskDelay(Delayms);     //just delay is enough
        OSW_GnrlcallsSleep(Delayms);
        //vTaskDelayUntil(&xLastWakeTime, Delayms);

        ParsedInput newPI = OSW_ConsoleInputParser();
        newCmd.cmdId = newPI.cmdId;
        newCmd.param = newPI.param;
//        char buffer[100];
//        int a = scanf("%s", buffer);
//        printf("%s \r\n", buffer);
//        newCmd.cmdId = con_id_help;/
//        newCmd.idOrig = 0x1101;
//        newCmd.param = 1;
//        newCmd.sysReq = 2;

        /* cmdId = 0xFFFF means no new command */
        if(newCmd.cmdId != CMD_CMDNULL)
        {
            //printf("\r\n");

            switch(verbose_level){
                case 0:
                    break;
                case 1:
                    printf("[taskConsole] Sending: cmd 0x%X, param %d \r\n",
                            newCmd.cmdId, newCmd.param);
                    //printf("[taskConsole] Sending: 0x%X %d [cmd param] \r\n",
                    //        newCmd.cmdId, newCmd.param);
                    break;
                case 2:
                    printf("[taskConsole] newCmd.cmdId 0x%X \n", newCmd.cmdId);
                    printf("[taskConsole] newCmd.idOrig 0x%X \n", newCmd.idOrig);
                    printf("[taskConsole] newCmd.param %d \n", newCmd.param);
                    printf("[taskConsole] newCmd.sysReq %u \n", newCmd.sysReq);
                    break;
            }

            /* Queue newCmd - Blocking */
            //xQueueSend(dispatcherQueue, &newCmd, portMAX_DELAY);
            OSW_QueueSend(dispatcherQueue, (const char *)&newCmd, sizeof(newCmd));
        }
    }
}
