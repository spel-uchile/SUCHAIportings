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
    # def __init__(self, name, cmd_own, n_cmd, b_function, b_sys_req, on_reset):
    # def __init__(self):
    #     self.name = name
    #     self.cmdOwn = cmd_own
    #     self.nCmd = n_cmd
    #     self.bFunction = b_function     # buffer of functions
    #     self.bSysReq = b_sys_req        # buffer of sysReq
    #     self.onResetFunction = on_reset_function
    pass


#base class for CmdCON, CmdPPC, etc
#@unique
#class CmdXXX(Enum):
class CmdXXX():
    def __init__(self, cmdown, ncmd):  # , cmd_function_repo):
        self.cmdOwn = cmdown
        self.nCmd = ncmd
        self.cmdFunction = []          # buffer of functions
        self.cmdSysReq = []            # buffer of sysReq

    @staticmethod
    def on_reset(verbose):
        raise NotImplementedError


class CmdRepo():
    # #define CMD_BUFF_CMDXX_LEN SCH_NUM_CMDXXX
    b_cmd_repo = []

    # void repo_set_cmdXXX_hanlder(CmdRepo_cmdXXX_handler cmdPPC_handler);
    @staticmethod
    def add_cmdrepo(cmd_handler):
        # if hasattr(cmd_handler, "cmdFunction"):
        #     CmdRepo.b_cmd_repo.append(cmd_handler)
        #     print("cmd_handler.name =>", cmd_handler.name)  # debug
        try:
            CmdRepo.b_cmd_repo.append(cmd_handler)
            # print("cmd_handler.name =>", cmd_handler.name)  # debug
        except AttributeError:
            pass

    @staticmethod
    def get_ncmds(cmd_name):
        for i in range(0, len(CmdRepo.b_cmd_repo)):
            if CmdRepo.b_cmd_repo[i].name == cmd_name:
                try:
                    nc = CmdRepo.b_cmd_repo[i].get_ncmds()
                    return nc
                except AttributeError:
                    return -1

    # cmdFunction repo_getFunction(int cmdID);
    @staticmethod
    def get_function(cmd_name, cmd_id):
        #from cmd_id get "cmdOwn" and get bFunction from the corresponding CmdHandler
        #and then, from inside this CmdHandler and using the rest of cmd_id get the
        #corresponding "function and return it"
        res = None
        for i in range(0, len(CmdRepo.b_cmd_repo)):
            #print("CmdRepo.b_cmd_repo[i].name => %s" % CmdRepo.b_cmd_repo[i].name)
            if CmdRepo.b_cmd_repo[i].name == cmd_name:
                try:
                    res = CmdRepo.b_cmd_repo[i].cmdFunction[cmd_id]
                except IndexError:
                    res = None

        # print("list(CmdRepo.b_cmd_repo)", list(CmdRepo.b_cmd_repo))         # debug
        # print("CmdRepo.b_cmd_repo[0] =>", CmdRepo.b_cmd_repo[0])            # debug
        # print("CmdRepo.b_cmd_repo[0].name =>", CmdRepo.b_cmd_repo[0].name)  # debug

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
