#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'


from enum import Enum, unique
from repos import command
from core import gnrluse
import SUCHAI_config
import logging
logger = logging.getLogger(__name__)

@unique
class CmdEnumCON(Enum):
    help = 0
    promt = 1
    error_cmd_toolong = 2
    debug_msg = 3
    error_unknown_cmd = 4
    error_invalid_arg = 5
    error_count_ar = 6

    @staticmethod
    def get_index(var):
        if hasattr(var, "value"):
            return var.value
        else:
            return -1

    @staticmethod
    def get_string(var):
        if hasattr(var, "name"):
            return var.name
        else:
            return -1


class CmdGroupCON(command.CmdGroup):
    groupName = SUCHAI_config.SCH_GNM_CON
    groupId = SUCHAI_config.SCH_GID_CON
    cmdEnum = CmdEnumCON

    def __init__(self):
        command.CmdGroup.__init__(self)
        self.groupName = CmdGroupCON.groupName
        self.groupId = CmdGroupCON.groupId

    #@staticmethod
    def on_reset(self):
        # create a cmd for every enum and then append it to CmdCON.cmdBuffer
        cmd_i = command.Cmd(name=CmdEnumCON.error_cmd_toolong,
                            sysreq=gnrluse.SysReqs.SYSREQ_MIN,
                            funct=CmdFunctCON.error_cmd_toolong)
        self.cmdBuffer.append(cmd_i)

        cmd_i = command.Cmd(name=CmdEnumCON.debug_msg,
                            sysreq=gnrluse.SysReqs.SYSREQ_MIN,
                            funct=CmdFunctCON.debug_msg)
        self.cmdBuffer.append(cmd_i)

        cmd_i = command.Cmd(name=CmdEnumCON.error_count_ar,
                            sysreq=gnrluse.SysReqs.SYSREQ_MIN,
                            funct=CmdFunctCON.error_count_ar)
        self.cmdBuffer.append(cmd_i)

        cmd_i = command.Cmd(name=CmdEnumCON.error_invalid_arg,
                            sysreq=gnrluse.SysReqs.SYSREQ_MIN,
                            funct=CmdFunctCON.error_invalid_arg)
        self.cmdBuffer.append(cmd_i)

        cmd_i = command.Cmd(name=CmdEnumCON.error_unknown_cmd,
                            sysreq=gnrluse.SysReqs.SYSREQ_MIN,
                            funct=CmdFunctCON.error_unknown_cmd)
        self.cmdBuffer.append(cmd_i)

        cmd_i = command.Cmd(name=CmdEnumCON.help,
                            sysreq=gnrluse.SysReqs.SYSREQ_MIN,
                            funct=CmdFunctCON.help)
        self.cmdBuffer.append(cmd_i)

        cmd_i = command.Cmd(name=CmdEnumCON.promt,
                            sysreq=gnrluse.SysReqs.SYSREQ_MIN,
                            funct=CmdFunctCON.promt)
        self.cmdBuffer.append(cmd_i)

        for i in range(0, len(CmdEnumCON)):
            # arg = "CmdEnumCON(%s) => %s" % (i, CmdEnumCON(i))
            # print(arg)
            # logger.debug(arg)
            arg = "self.cmdBuffer[%s] => %s" % (i, self.cmdBuffer[i])
            print(arg)
            logger.debug(arg)
            arg = "self.cmdBuffer[%s].name => %s" % (i, self.cmdBuffer[i].name)
            print(arg)
            logger.debug(arg)
        print()

        if len(CmdEnumCON) != self.get_ncmds():
            arg = "wrong implementation"
            print(arg)
            logger.critical(arg)
            raise NotImplemented


class CmdFunctCON():
    @staticmethod
    def help(param):
        print("This is the useless %s command" % CmdFunctCON.help.__name__)
        print("Used with param %s" % param)
        return True

    @staticmethod
    def promt(param):
        return False

    @staticmethod
    def error_cmd_toolong(param):
        return False

    @staticmethod
    def debug_msg(param):
        return False

    @staticmethod
    def error_unknown_cmd(param):
        return False

    @staticmethod
    def error_invalid_arg(param):
        return False

    @staticmethod
    def error_count_ar( param):
        return False

# class CmdCON(command.CmdGroup):
#
#     def __init__(self):
#         command.CmdGroup.__init__(self)
#         self.groupName = __name__
#         self.groupId = SUCHAI_config.SCH_GID_CON
#
#     # #@staticmethod
#     # def get_ncmds(self):
#     #     return len(self.cmdBuffer)
#
#     @staticmethod
#     def help(param):
#         print("This is the useless %s.%s command" % (CmdCON.__name__, CmdCON.help.__name__))
#         print("Used with param %s" % param)
#         return True
#
#     @staticmethod
#     def promt(param):
#         return False
#
#     @staticmethod
#     def error_cmd_toolong(param):
#         return False
#
#     @staticmethod
#     def debug_msg(param):
#         return False
#
#     @staticmethod
#     def error_unknown_cmd(param):
#         return False
#
#     @staticmethod
#     def error_invalid_arg(param):
#         return False
#
#     @staticmethod
#     def error_count_ar(param):
#         return False
#
#     #@staticmethod
#     def on_reset(self):
#         # add every cmd and sysReq to CmdCON.cmdBuffer and CmdCON.cmdSysReq
#
#         self.cmdBuffer.append(CmdCON.help)
#         self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)
#
#         self.cmdBuffer.append(CmdCON.promt)
#         self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)
#
#         self.cmdBuffer.append(CmdCON.error_cmd_toolong)
#         self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)
#
#         self.cmdBuffer.append(CmdCON.error_count_ar)
#         self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)
#
#         self.cmdBuffer.append(CmdCON.error_invalid_arg)
#         self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)
#
#         self.cmdBuffer.append(CmdCON.error_unknown_cmd)
#         self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)
#
#         self.cmdBuffer.append(CmdCON.debug_msg)
#         self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)
#
#
