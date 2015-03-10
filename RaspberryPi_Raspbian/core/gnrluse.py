#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'

# /**
#  * @file  cmdIncludes.h
#  * @author Tomas Opazo T - tomas.opazo.t@gmail.com
#  * @author Carlos Gonzalez C - carlgonz@ug.uchile.cl
#  * @date 2012/
#  * @copyright GNU GPL v3
#  *
#  * This header have general definitions about commands prototipes and related
#  * data structures.
#  */

#ifndef CMD_INCLUDES_H
#define CMD_INCLUDES_H

#include "SUCHAI_config.h"

# /**
#  *  Defines the prototype that every command must conform
#  */
# typedef int (*cmdBuffer)( void * );
#
#
# typedef void (*onResetFunction)( void );


class ExeCmd():
    # /**
    #  * Structure that represents a command passed to executer. Contains a pointer of
    #  * type cmdBuffer with the function to execute and one parameter for that
    #  * function
    #  */
    # typedef struct exec_command{
    #     int param;                  ///< Command parameter
    #     cmdBuffer fnct;           ///< Command function
    # }ExeCmd;
    param = None
    cmdFunction = None


class DispCmd():
    # /**
    #  * Structure that represent a command passed to dispatcher. Contains only a code
    #  * that represent the function to call, a paremeter and other command's metadata
    #  */
    # typedef struct ctrl_command{
    #     int cmdId;                  ///< Command id, represent the desired command
    #     int param;                  ///< Command parameter
    #     int idOrig;                 ///< Metadata: Id of sender subsystem
    #     int sysReq;                 ///< Metadata: Level of energy the command requires
    # }DispCmd;
    def __init__(self, cmdid, param, taskorig, sysreq, groupname, cmdname):
        self.cmdId = cmdid
        self.param = param
        self.taskOrig = taskorig
        self.sysReq = sysreq
        #TODO modified by toopazo to ease porting
        self.groupName = groupname        # cmd groupName (CmdCON, CmdRTC, etc)
        self.cmdName = cmdname      # cmd name (CmdCON.help.__name, CmdRTC.debug.__name__, etc)


# from core import const
# const.val = 1   # can only be set once
# const.val = 2   # the second time produces an error

class GnrlCmds():
    #define CMD_CMDNULL     (0xFFFF)    ///< Dummy command id. Represent a null command
    CMD_NULL = 0xFFFF
    #define CMD_STOP        (0xFFFE)    ///< Reserved id. Represent a stop or separation code
    CMD_STOP = 0xFFFE


class TaskOrig():
    #define CMD_IDORIG_TCONSOLE         (0x1101)
    TCONSOLE = 0x1101
    #define CMD_IDORIG_THOUSEKEEPING    (0x1102)
    THOUSEKEEPING = 0x1102
    #define CMD_IDORIG_TCOMUNICATIONS   (0x1103)
    TCOMUNICATIONS = 0x1103
    #define CMD_IDORIG_TFLIGHTPLAN      (0x1104)
    TFLIGHTPLAN = 0x1104
    #define CMD_IDORIG_TFLIGHTPLAN2     (0x1105)
    TFLIGHTPLAN2 = 0x1105
    #define CMD_IDORIG_TFLIGHTPLAN3     (0x1106)
    TFLIGHTPLAN3 = 0x1106
    #define CMD_IDORIG_TDEPLOYMENT      (0x1107)
    TDEPLOYMENT = 0x1107


#define CMD_SYSREQ_MIN      (1)     ///< Min energy level possible
#define CMD_SYSREQ_MAX      (9)     ///< Max energy level possible
class SysReqs():
    SYSREQ_MIN = 1
    SYSREQ_MAX = 10


def console_print(arg):
    print(arg)


def console_input(arg):
    line = input(arg)
    return line

#endif /* CMD_INCLUDES_H */
