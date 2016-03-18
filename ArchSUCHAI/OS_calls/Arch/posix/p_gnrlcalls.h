/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   p_gnrlcalls.h
 * Author: toopazo
 *
 * Created on March 18, 2016, 3:59 PM
 */

#ifndef P_GNRLCALLS_H
#define P_GNRLCALLS_H

#ifdef __cplusplus
extern "C" {
#endif
////////////////////////////////////////////////////////////////////////////////

#include <unistd.h>    
#include <stdlib.h>
#include <stdio.h>
    
/**
 * Wrapper of sleep()
 * @param secs
 * @return 
 */    
void OSW_GnrlcallsSleep(double secs);

/**
 * Wrapper of nothing (yet)
 */
void OSW_GnrlcallsWDT(void);
    
////////////////////////////////////////////////////////////////////////////////
#ifdef __cplusplus
}
#endif

#endif /* P_GNRLCALLS_H */

