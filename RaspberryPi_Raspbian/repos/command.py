# -*- coding: utf-8 -*-
__author__ = 'toopazo'

import SUCHAI_config
from core import gnrl_services
import logging
logger = logging.getLogger(__name__)


class Cmd():
    def __init__(self, name, cmdid, sysreq, funct):
    # def __init__(self, cmdName, sysreq, cmdFunct):
        self.cmdName = name
        self.cmdId = cmdid
        self.cmdSysReq = sysreq
        self.cmdFunct = funct

    def exect(self, cmd_param):
        res = self.cmdFunct(cmd_param)
        return res


#base class for CmdCON, CmdPPC, etc
class Cmdgroup():

    def __init__(self):
        self.cmdgroupName = ""
        self.cmdgroupId = 0
        self.cmdgroupCmdBuffer = []        # buffer of Cmd objects

    #@staticmethod
    def on_reset(self):
        raise NotImplementedError

    #@staticmethod
    def get_num_cmds(self):
        #raise NotImplementedError
        return len(self.cmdgroupCmdBuffer)

    def get_cmd(self, i):
        return self.cmdgroupCmdBuffer[i]


# manages acces to te cmdRepo
class CmdRepo():
    # #define CMD_BUFF_CMDXX_LEN SCH_NUM_CMDXXX
    cmdrepoCmdgroupBuffer = []

    # void repo_set_cmdXXX_hanlder(CmdRepo_cmdXXX_handler cmdPPC_handler);
    @staticmethod
    def add_cmdgroup(cmd_group):
        # if hasattr(cmd_group, "cmdgroupCmdBuffer"):
        #     CmdRepo.cmdrepoCmdgroupBuffer.append(cmd_group)
        #     print("cmd_group.cmdgroupName =>", cmd_group.cmdgroupName)  # debug
        try:
            CmdRepo.cmdrepoCmdgroupBuffer.append(cmd_group)
            # print("cmd_group.cmdgroupName =>", cmd_group.cmdgroupName)  # debug
            # print(CmdRepo.cmdrepoCmdgroupBuffer)

            #execute onReset of added cmd_group
            cmd_group.on_reset()
        except AttributeError:
            pass

    @staticmethod
    def get_num_cmdgroups():
        return len(CmdRepo.cmdrepoCmdgroupBuffer)

    @staticmethod
    def get_cmdgroup(i):
        return CmdRepo.cmdrepoCmdgroupBuffer[i]

    @staticmethod
    def get_cmd_name_by_id(cmd_id):
        cmd_x = CmdRepo.get_cmd_by_id(cmd_id)
        return cmd_x.cmdName

    @staticmethod
    def get_cmd_sysreq_by_id(cmd_id):
        cmd_x = CmdRepo.get_cmd_by_id(cmd_id)
        return cmd_x.cmdSysReq

    # @staticmethod
    # def get_cmd_funct_by_id(cmd_id):
    #     cmd_x = CmdRepo.get_cmd_by_id(cmd_id)
    #     return cmd_x.cmdFunct

    @staticmethod
    def get_cmd_by_id(cmd_id):
        """ Search inside cmdrepoCmdgroupBuffer after the cmd_group that matches the cmd_id key,
         then for cmd_id inside cmd_group and return the associated Cmd.cmdFunct """
        # cmd_id = "A00F"
        # cmd_id = "1003"
        cmd_id = int(cmd_id)
        cmdgroup_id = int(cmd_id >> 8)*0x100    # get cmdgroupId part from the cmdId
        cmd_num = int(cmd_id & int('00001111', 2))
        # print("cmdgroup_id 0x%x = %s" % (cmdgroup_id, cmdgroup_id))
        # print("cmd_num 0x%x = %s" % (cmd_num, cmd_num))
        res = None
        for i in range(0, len(CmdRepo.cmdrepoCmdgroupBuffer)):
            cmdgroup_i = CmdRepo.get_cmdgroup(i)
            #print("CmdRepo.cmdrepoCmdgroupBuffer[i].cmdgroupName => %s" % CmdRepo.cmdrepoCmdgroupBuffer[i].cmdgroupName)
            if cmdgroup_i.cmdgroupId == cmdgroup_id:
                # # se necesita revisar uno por uno ya que el buffer podria
                # # estar desordenado y el Enum 0 no ser el cmdgroupCmdBuffer[0]
                # for j in range(0, len(cmdgroup_i.cmdgroupCmdBuffer)):
                #     cmd_j = cmdgroup_i.cmdgroupCmdBuffer[j]
                #     print(cmd_j.cmdName)
                #     if cmd_j.value == cmd_num:
                #         res = cmdgroup_i.cmdgroupCmdBuffer[cmd_num]
                #         return res
                # #if there is no match for cmd_j in cmdgroupCmdBuffer return cmdnull
                # res = CmdRepo.cmdnull
                # return res

                # si cmdgroupCmdBuffer coincide con Enum de cmdgroup_i
                # entocnes es valido simplemente ir por el i-esimo
                try:
                    res = cmdgroup_i.get_cmd(cmd_num)
                    # print(res.cmdName)
                except IndexError:
                    res = CmdRepo.cmdnull
                return res
        return res

    # int cmdNULL(void *cmdParam);
    @staticmethod
    def cmdnull(param):
        arg = "cmdnull used with cmdParam: %s" % param
        logger.error(arg)
        gnrl_services.console_print(arg)
        return True

    cmdnull = Cmd(cmdid=SUCHAI_config.GnrlCmds.CMD_NULL,
                  name="cmdnull",
                  sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                  funct=cmdnull)

# cmdgroupCmdBuffer repo_getCmd(int cmdID);


# int repo_setCmd(int cmdID, cmdgroupCmdBuffer function);
# int repo_onResetCmdRepo(void);
