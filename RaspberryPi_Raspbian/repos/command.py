# -*- coding: utf-8 -*-
__author__ = 'toopazo'

from core import suchai_types
from core import gnrl_services
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
    cmd_group_buffer = []

    # void repo_set_cmdXXX_hanlder(CmdRepo_cmdXXX_handler cmdPPC_handler);
    @staticmethod
    def add_cmd_group(cmd_group):
        # if hasattr(cmd_group, "cmdBuffer"):
        #     CmdRepo.cmd_group_buffer.append(cmd_group)
        #     print("cmd_group.groupName =>", cmd_group.groupName)  # debug
        try:
            CmdRepo.cmd_group_buffer.append(cmd_group)
            # print("cmd_group.groupName =>", cmd_group.groupName)  # debug
            # print(CmdRepo.cmd_group_buffer)

            #execute onReset of added cmd_group
            cmd_group.on_reset()
        except AttributeError:
            pass

    @staticmethod
    def get_ncmds(cmd_group_name):
        for i in range(0, len(CmdRepo.cmd_group_buffer)):
            cmd_group = CmdRepo.cmd_group_buffer[i]
            if cmd_group.groupName == cmd_group_name:
                try:
                    nc = cmd_group.get_ncmds()
                    return nc
                except AttributeError:
                    return 0

    #TODO modified by toopazo to ease porting
    # cmdBuffer repo_getFunction(int cmdID);
    @staticmethod
    def get_command_byid(cmd_group_name, cmd_id):
        """ Search inside cmd_group_buffer after the cmd_group that matches the cmd_id key,
         then for cmd_id inside cmd_group and return the associated Cmd.funct """
        res = None
        for i in range(0, len(CmdRepo.cmd_group_buffer)):
            cmd_group = CmdRepo.cmd_group_buffer[i]
            #print("CmdRepo.cmd_group_buffer[i].groupName => %s" % CmdRepo.cmd_group_buffer[i].groupName)
            if cmd_group.groupName == cmd_group_name:
                try:
                    res = cmd_group.cmdBuffer[cmd_id]
                    #print(cmd_group.groupName)
                except IndexError:
                    res = CmdRepo.cmdnull
                return res
        return res

    #TODO modified by toopazo to ease porting
    @staticmethod
    def get_command_byname(cmd_group_name, cmd_name):
        """ Search inside cmd_group_buffer after the cmd_group that matches the cmd_group_name key,
         then for cmd_name inside cmd_group and return the associated Cmd.funct """
        res = None
        for i in range(0, len(CmdRepo.cmd_group_buffer)):
            cmd_group = CmdRepo.cmd_group_buffer[i]
            # print("cmd_group.groupName => %s" % cmd_group.groupName)
            if cmd_group.groupName == cmd_group_name:
                for j in range(0, len(cmd_group.cmdBuffer)):
                    cmd_j = cmd_group.cmdBuffer[j]
                    # print("cmd_j.name => %s" % cmd_j.name)
                    if cmd_j.name == cmd_name:
                        res = cmd_j
                        return res
        return res

    #TODO modified by toopazo to ease porting
    @staticmethod
    def get_function_byname(cmd_group_name, cmd_name):
        """ Search inside cmd_group_buffer after the cmd_group that matches the cmd_group_name key,
         then for cmd_id inside cmd_group and return the associated Cmd.funct """
        res = None
        for i in range(0, len(CmdRepo.cmd_group_buffer)):
            cmd_group = CmdRepo.cmd_group_buffer[i]
            # print("cmd_group.groupName => %s" % cmd_group.groupName)
            if cmd_group.groupName == cmd_group_name:
                for j in range(0, len(cmd_group.cmdBuffer)):
                    cmd_j = cmd_group.cmdBuffer[j]
                    # print("cmd_j.name => %s" % cmd_j.name)
                    if cmd_j.name == cmd_name:
                        res = cmd_j.funct
                        return res
        return res

    #TODO modified by toopazo to ease porting
    # cmdBuffer repo_getFunction(int cmdID);
    @staticmethod
    def get_function_byid(cmd_group_name, cmd_id):
        """ Search inside cmd_group_buffer after the cmd_group that matches the cmd_id key,
         then for cmd_id inside cmd_group and return the associated Cmd.funct """
        res = None
        for i in range(0, len(CmdRepo.cmd_group_buffer)):
            cmd_group = CmdRepo.cmd_group_buffer[i]
            #print("CmdRepo.cmd_group_buffer[i].groupName => %s" % CmdRepo.cmd_group_buffer[i].groupName)
            if cmd_group.groupName == cmd_group_name:
                try:
                    res = cmd_group.cmdBuffer[cmd_id].funct
                    #print(cmd_group.groupName)
                except IndexError:
                    res = CmdRepo.cmdnull
                return res
        return res

    # int repo_getsysReq(int cmdID);
    @staticmethod
    def get_sysreq_byid(cmd_group_name, cmd_name):
        """ Search inside cmd_group_buffer after the cmd_group that matches the cmd_name key,
         then for cmd_name inside cmd_group and return the associated Cmd.sysReq """
        res = None
        for i in range(0, len(CmdRepo.cmd_group_buffer)):
            cmd_group = CmdRepo.cmd_group_buffer[i]
            #print("CmdRepo.cmd_group_buffer[i].groupName => %s" % CmdRepo.cmd_group_buffer[i].groupName)
            if cmd_group.groupName == cmd_group_name:
                try:
                    res = cmd_group.cmdBuffer[cmd_name].sysReq
                    #print(cmd_group.groupName)
                except IndexError:
                    res = suchai_types.SysReqs.SYSREQ_MAX
                return res
        return res

    #TODO modified by toopazo to ease porting
    @staticmethod
    def get_sysreq_byname(cmd_group_name, cmd_name):
        """ Search inside cmd_group_buffer after the cmd_group that matches the cmd_group_name key,
         then for cmd_id inside cmd_group and return the associated Cmd.sysReq """
        res = None
        for i in range(0, len(CmdRepo.cmd_group_buffer)):
            cmd_group = CmdRepo.cmd_group_buffer[i]
            # print("cmd_group.groupName => %s" % cmd_group.groupName)
            if cmd_group.groupName == cmd_group_name:
                for j in range(0, len(cmd_group.cmdBuffer)):
                    cmd_j = cmd_group.cmdBuffer[j]
                    cmd_sysreq_j = cmd_j.sysReq
                    # print("cmd_j.name => %s" % cmd_j.name)
                    # print("cmd_sysreq_j => %s" % cmd_sysreq_j)
                    if cmd_j.name == cmd_name:
                        res = cmd_sysreq_j
                        return res
        return res

    # int cmdNULL(void *param);
    @staticmethod
    def cmdnull(param):
        arg = "cmdnull used with param: %s" % param
        logger.error(arg)
        gnrl_services.console_print(arg)
        return True

    cmdnull = Cmd(name="cmdnull",
                  sysreq=suchai_types.SysReqs.SYSREQ_MIN,
                  funct=cmdnull)

# cmdBuffer repo_getCmd(int cmdID);


# int repo_setCmd(int cmdID, cmdBuffer function);
# int repo_onResetCmdRepo(void);
