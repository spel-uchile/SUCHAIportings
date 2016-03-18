/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   osw_queue.h
 * Author: toopazo
 *
 * Created on March 18, 2016, 3:24 PM
 */

#ifndef OSW_QUEUE_H
#define OSW_QUEUE_H

#ifdef __cplusplus
extern "C" {
#endif
////////////////////////////////////////////////////////////////////////////////

#if(SCH_TARGET_ARCH == 0)
    #include "../Arch/posix/p_queue.h"
#elif(SCH_TARGET_ARCH == 1)
    #include "../Arch/freertos/queue.h"
#endif    

////////////////////////////////////////////////////////////////////////////////
#ifdef __cplusplus
}
#endif

#endif /* OSW_QUEUE_H */

