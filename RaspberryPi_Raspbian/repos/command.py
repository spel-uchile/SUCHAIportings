#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'

from enum import Enum, unique
import logging
logger = logging.getLogger(__name__)


class CmdHandler():
    # typedef struct{
    #     unsigned char cmdOwn;
    #     unsigned int nCmd;
    #     cmdFunction *p_xxxFunction;
    #     int *p_xxxSysReq;
    #     onResetFunction xxx_onReset;
    #
    # }CmdRepo_cmdXXX_handler;
    def __init__(self, name, cmd_own, n_cmd, b_function, b_sys_req, on_reset_function):
        self.name = name
        self.cmdOwn = cmd_own
        self.nCmd = n_cmd
        self.bFunction = b_function     # buffer of functions
        self.bSysReq = b_sys_req        # buffer of sysReq
        self.onResetFunction = on_reset_function


#base class for CmdCON, CmdPPC, etc
#@unique
#class CmdXXX(Enum):
class CmdXXX():
    @staticmethod
    def get_index(state_var):
        if hasattr(state_var, "value"):
            return state_var.value
        else:
            return -1

    @staticmethod
    def get_string(state_var):
        if hasattr(state_var, "name"):
            return state_var.name
        else:
            return -1

    @staticmethod
    def on_reset(verbose):
        raise NotImplementedError


class CmdRepo():
    # #define CMD_BUFF_CMDXX_LEN SCH_NUM_CMDXXX
    b_cmdHandler = []

    # void repo_set_cmdXXX_hanlder(CmdRepo_cmdXXX_handler cmdPPC_handler);
    @staticmethod
    def add_commands(cmd_handler):
        if hasattr(cmd_handler, "bFunction"):
            CmdRepo.b_cmdHandler.append(cmd_handler)
            print("cmd_handler.name =>", cmd_handler.name)  # debug

    # cmdFunction repo_getFunction(int cmdID);
    @staticmethod
    def get_function(cmd_name, cmd_id):
        #from cmd_id get "cmdOwn" and get bFunction from the corresponding CmdHandler
        #and then, from inside this CmdHandler and using the rest of cmd_id get the
        #corresponding "function and return it"
        res = None
        for i in range(0, len(CmdRepo.b_cmdHandler)):
            if CmdRepo.b_cmdHandler[i].name == cmd_name:
                try:
                    res = CmdRepo.b_cmdHandler[i].bFunction[cmd_id]
                except IndexError:
                    res = None

        # print("list(CmdRepo.b_cmdHandler)", list(CmdRepo.b_cmdHandler))         # debug
        # print("CmdRepo.b_cmdHandler[0] =>", CmdRepo.b_cmdHandler[0])            # debug
        # print("CmdRepo.b_cmdHandler[0].name =>", CmdRepo.b_cmdHandler[0].name)  # debug

        return res

    # int repo_getsysReq(int cmdID);
    @staticmethod
    def get_sysreq(cmd_id):
        #from cmd_id get "cmdOwn" and get bFunction from the corresponding CmdHandler
        #and then, from inside this CmdHandler and using the rest of cmd_id get the
        #corresponding "sysreq and return it"
        return 0

    # int cmdNULL(void *param);
    @staticmethod
    def cmdnull(param):
        logger.debug("cmdnull used with param %s", param)
        return True

#
#
# cmdFunction repo_getCmd(int cmdID);

#
# int repo_setCmd(int cmdID, cmdFunction function);
# int repo_onResetCmdRepo(void);
