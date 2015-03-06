#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'

from core import gnrluse
import logging
logger = logging.getLogger(__name__)


# class CmdHandler():
#     def __init__(self, cmdxxx):     # , name, cmdown, onreset_funct):  # , cmd_function_repo):
#         self.cmdxxx = cmdxxx
#         self.name = cmdxxx.name
#         self.cmdOwn = cmdxxx.cmdOwn
#
#         # self.nCmd = 0
#         self.cmdFunction = []          # buffer of functions
#         self.cmdSysReq = []            # buffer of sysReq
#
#     def get_ncmds(self):
#         return len(self.cmdFunction)
#
#     def on_reset(self):
#         self.cmdxxx.on_reset()    # after this call cmdFunction and cmdSysReq are ready/loaded
#         self.cmdFunction = self.cmdxxx.cmdFunction
#         self.cmdSysReq = self.cmdxxx.cmdSysReq


#base class for CmdCON, CmdPPC, etc
class CmdXXX():

    def __init__(self):
        self.name = __name__
        self.cmdOwn = 0
        self.cmdFunction = []        # buffer of functions
        self.cmdSysReq = []          # buffer of functions

    #@staticmethod
    def on_reset(self):
        raise NotImplementedError

    #@staticmethod
    def get_ncmds(self):
        #raise NotImplementedError
        return len(self.cmdFunction)


# manages acces to te cmdRepo
class CmdRepo():
    # #define CMD_BUFF_CMDXX_LEN SCH_NUM_CMDXXX
    b_cmd_repo = []

    # void repo_set_cmdXXX_hanlder(CmdRepo_cmdXXX_handler cmdPPC_handler);
    @staticmethod
    def add_cmd_xxx(cmd_xxx):
        # if hasattr(cmd_xxx, "cmdFunction"):
        #     CmdRepo.b_cmd_repo.append(cmd_xxx)
        #     print("cmd_xxx.name =>", cmd_xxx.name)  # debug
        try:
            CmdRepo.b_cmd_repo.append(cmd_xxx)
            # print("cmd_xxx.name =>", cmd_xxx.name)  # debug
            print(CmdRepo.b_cmd_repo)

            #execute onReset of added cmd_xxx
            cmd_xxx.on_reset()
        except AttributeError:
            pass

    @staticmethod
    def get_ncmds(cmd_name):
        for i in range(0, len(CmdRepo.b_cmd_repo)):
            cmd_xxx = CmdRepo.b_cmd_repo[i]
            if cmd_xxx.name == cmd_name:
                try:
                    nc = cmd_xxx.get_ncmds()
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
            cmd_xxx = CmdRepo.b_cmd_repo[i]
            #print("CmdRepo.b_cmd_repo[i].name => %s" % CmdRepo.b_cmd_repo[i].name)
            if cmd_xxx.name == cmd_name:
                try:
                    res = cmd_xxx.cmdFunction[cmd_id]
                    #print(cmd_xxx.name)
                except IndexError:
                    res = CmdRepo.cmdnull

        # print("list(CmdRepo.b_cmd_repo)", list(CmdRepo.b_cmd_repo))         # debug
        # print("CmdRepo.b_cmd_repo[0] =>", CmdRepo.b_cmd_repo[0])            # debug
        # print("CmdRepo.b_cmd_repo[0].name =>", CmdRepo.b_cmd_repo[0].name)  # debug

        return res

    # int repo_getsysReq(int cmdID);
    @staticmethod
    def get_sysreq(cmd_name, cmd_id):
        #from cmd_id get "cmdOwn" and get bFunction from the corresponding CmdHandler
        #and then, from inside this CmdHandler and using the rest of cmd_id get the
        #corresponding "sysreq and return it"
        res = None
        for i in range(0, len(CmdRepo.b_cmd_repo)):
            cmd_xxx = CmdRepo.b_cmd_repo[i]
            #print("CmdRepo.b_cmd_repo[i].name => %s" % CmdRepo.b_cmd_repo[i].name)
            if cmd_xxx.name == cmd_name:
                try:
                    res = cmd_xxx.cmdSysReq[cmd_id]
                    #print(cmd_xxx.name)
                except IndexError:
                    res = gnrluse.SysReqs.SYSREQ_MAX

        # print("list(CmdRepo.b_cmd_repo)", list(CmdRepo.b_cmd_repo))         # debug
        # print("CmdRepo.b_cmd_repo[0] =>", CmdRepo.b_cmd_repo[0])            # debug
        # print("CmdRepo.b_cmd_repo[0].name =>", CmdRepo.b_cmd_repo[0].name)  # debug

        return res

    # int cmdNULL(void *param);
    @staticmethod
    def cmdnull(param):
        arg = "cmdnull used with param: %s" % param
        logger.debug(arg)
        print(arg)
        return True

#
#
# cmdFunction repo_getCmd(int cmdID);

#
# int repo_setCmd(int cmdID, cmdFunction function);
# int repo_onResetCmdRepo(void);
