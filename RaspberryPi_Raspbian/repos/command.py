#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'

from core import gnrluse
import logging
logger = logging.getLogger(__name__)


class Cmd():
    def __init__(self, name, sysreq, funct):
        self.name = name
        self.sysReq = sysreq
        self.funct = funct

    # def exec(self):
    #     raise NotImplementedError


#base class for CmdCON, CmdPPC, etc
class CmdGroup():

    def __init__(self):
        self.groupName = ""
        self.groupId = 0
        self.cmdBuffer = []        # buffer of Cmd objects

    #@staticmethod
    def on_reset(self):
        raise NotImplementedError

    #@staticmethod
    def get_ncmds(self):
        #raise NotImplementedError
        return len(self.cmdBuffer)


# manages acces to te cmdRepo
class CmdRepo():
    # #define CMD_BUFF_CMDXX_LEN SCH_NUM_CMDXXX
    b_cmd_repo = []

    # void repo_set_cmdXXX_hanlder(CmdRepo_cmdXXX_handler cmdPPC_handler);
    @staticmethod
    def add_cmd_group(cmd_group):
        # if hasattr(cmd_group, "cmdBuffer"):
        #     CmdRepo.b_cmd_repo.append(cmd_group)
        #     print("cmd_group.groupName =>", cmd_group.groupName)  # debug
        try:
            CmdRepo.b_cmd_repo.append(cmd_group)
            # print("cmd_group.groupName =>", cmd_group.groupName)  # debug
            # print(CmdRepo.b_cmd_repo)

            #execute onReset of added cmd_group
            cmd_group.on_reset()
        except AttributeError:
            pass

    @staticmethod
    def get_ncmds(cmd_name):
        for i in range(0, len(CmdRepo.b_cmd_repo)):
            cmd_group = CmdRepo.b_cmd_repo[i]
            if cmd_group.groupName == cmd_name:
                try:
                    nc = cmd_group.get_ncmds()
                    return nc
                except AttributeError:
                    return -1

    #TODO modified by toopazo to ease porting
    @staticmethod
    def get_function_byname(cmd_name, cmd_id_name):
        #from cmd_id get "groupId" and get bFunction from the corresponding CmdHandler
        #and then, from inside this CmdHandler and using the rest of cmd_id get the
        #corresponding "function and return it"
        res = None
        for i in range(0, len(CmdRepo.b_cmd_repo)):
            cmd_group = CmdRepo.b_cmd_repo[i]
            print("cmd_group.groupName => %s" % cmd_group.groupName)
            if cmd_group.groupName == cmd_name:
                for j in range(0, len(cmd_group.cmdBuffer)):
                    cmd_group_j = cmd_group.cmdBuffer[j]
                    print("cmd_group_j.name => %s" % cmd_group_j.name)
                    if cmd_group_j.name == cmd_id_name:
                        res = cmd_group_j
                        return res
        return res

    #TODO modified by toopazo to ease porting
    # cmdBuffer repo_getFunction(int cmdID);
    @staticmethod
    def get_function_byid(cmd_name, cmd_id):
        #from cmd_id get "groupId" and get bFunction from the corresponding CmdHandler
        #and then, from inside this CmdHandler and using the rest of cmd_id get the
        #corresponding "function and return it"
        res = None
        for i in range(0, len(CmdRepo.b_cmd_repo)):
            cmd_group = CmdRepo.b_cmd_repo[i]
            #print("CmdRepo.b_cmd_repo[i].groupName => %s" % CmdRepo.b_cmd_repo[i].groupName)
            if cmd_group.groupName == cmd_name:
                try:
                    res = cmd_group.cmdBuffer[cmd_id]
                    #print(cmd_group.groupName)
                except IndexError:
                    res = CmdRepo.cmdnull
                return res
        return res

    # int repo_getsysReq(int cmdID);
    @staticmethod
    def get_sysreq_byid(cmd_name, cmd_id):
        #from cmd_id get "groupId" and get bFunction from the corresponding CmdHandler
        #and then, from inside this CmdHandler and using the rest of cmd_id get the
        #corresponding "sysReq and return it"
        res = None
        for i in range(0, len(CmdRepo.b_cmd_repo)):
            cmd_group = CmdRepo.b_cmd_repo[i]
            #print("CmdRepo.b_cmd_repo[i].groupName => %s" % CmdRepo.b_cmd_repo[i].groupName)
            if cmd_group.groupName == cmd_name:
                try:
                    res = cmd_group.cmdBuffer[cmd_id].sysReq
                    #print(cmd_group.groupName)
                except IndexError:
                    res = gnrluse.SysReqs.SYSREQ_MAX
                return res
        return res

    #TODO modified by toopazo to ease porting
    @staticmethod
    def get_sysreq_byname(cmd_name, cmd_id_name):
        #from cmd_id get "groupId" and get bFunction from the corresponding CmdHandler
        #and then, from inside this CmdHandler and using the rest of cmd_id get the
        #corresponding "function and return it"
        res = None
        for i in range(0, len(CmdRepo.b_cmd_repo)):
            cmd_group = CmdRepo.b_cmd_repo[i]
            print("cmd_group.groupName => %s" % cmd_group.groupName)
            if cmd_group.groupName == cmd_name:
                for j in range(0, len(cmd_group.cmdBuffer)):
                    cmd_group_j = cmd_group.cmdBuffer[j]
                    cmd_group_sysreq_j = cmd_group.cmdBuffer[j].sysReq
                    print("cmd_group_j.name => %s" % cmd_group_j.name)
                    print("cmd_group_sysreq_j => %s" % cmd_group_sysreq_j)
                    if cmd_group_j.name == cmd_id_name:
                        res = cmd_group_sysreq_j
                        return res
        return res

    # int cmdNULL(void *param);
    @staticmethod
    def cmdnull(param):
        arg = "cmdnull used with param: %s" % param
        logger.debug(arg)
        print(arg)
        return True


# cmdBuffer repo_getCmd(int cmdID);


# int repo_setCmd(int cmdID, cmdBuffer function);
# int repo_onResetCmdRepo(void);
