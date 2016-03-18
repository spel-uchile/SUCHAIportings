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

#ifndef P_CONSOLE_H
#define P_CONSOLE_H

#ifdef __cplusplus
extern "C" {
#endif
////////////////////////////////////////////////////////////////////////////////   
#include <unistd.h>    
#include <stdlib.h>
#include <stdio.h>
    
typedef struct{
    char *cmdname;
    unsigned int cmdid;
    int param;
}ParsedInput;

/**
 * Read from the console, and returns a parsed list
 * according to a pre-defined Language (formal grammar and parser)
 * 
 * 
 * 
 * E.g. A simple language could be InputLanguage, where:
 * 
 * InputLanguage = "exe_cmd" "0x"cmd param | "special_cmd"
 * cmd = {any number from the Alphabet (0-9)}
 * param = {any letter from the Alphabet (ASCII)}
 * 
 * Then:
 * >> 'exe_cmd 0x0001 3' produces ['exe_cmd','1', '3'] because it is a
 * realization of "exe_cmd" "0x"cmd param
 * 
 * >> 'con_help' produces ['con_help'] because it is a
 * realization of "special_cmd"
 * 
 * >> 'thk_EBF 1' produces [''] because it is NOT a valid 
 * word from InputLanguage
 * 
 * >> 'exe_cmd asd 1' produces [''] because it is NOT a valid 
 * word from InputLanguage
 * 
 * >> 'exe_cmd 0x3001 1 2 3' produces [''] because it is NOT a valid 
 * word from InputLanguage
 * 
 * @return 
 */    
ParsedInput OSW_ConsoleInputParser(void);
    
////////////////////////////////////////////////////////////////////////////////
#ifdef __cplusplus
}
#endif

#endif /* P_CONSOLE_H */
 
