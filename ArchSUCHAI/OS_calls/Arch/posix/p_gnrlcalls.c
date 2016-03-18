
#include "p_gnrlcalls.h"

static unsigned char verbose_level = 2;

void OSW_GnrlcallsSleep(double secs){    
    if(verbose_level >= 3){
        printf("OSW_GnrlcallsSleep: %f [sec] \r\n", secs);
    }
    sleep(secs);
}

void OSW_GnrlcallsWDT(void){
    //ClrWdt()
}