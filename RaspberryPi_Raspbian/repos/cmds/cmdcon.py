# -*- coding: utf-8 -*-
__author__ = 'toopazo'


from enum import Enum, unique
from repos import command
from core import suchai_types
from core import gnrl_services
import SUCHAI_config
import logging
logger = logging.getLogger(__name__)

@unique
class CmdEnumCON(Enum):
    con_help = 0
    con_promt = 1
    con_error_cmd_toolong = 2
    con_debug_msg = 3
    con_error_unknown_cmd = 4
    con_error_invalid_arg = 5
    con_error_count_ar = 6

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
        cmd_i = command.Cmd(name=CmdEnumCON.con_error_cmd_toolong.name,
                            sysreq=suchai_types.SysReqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_error_cmd_toolong)
        self.cmdBuffer.append(cmd_i)

        cmd_i = command.Cmd(name=CmdEnumCON.con_debug_msg.name,
                            sysreq=suchai_types.SysReqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_debug_msg)
        self.cmdBuffer.append(cmd_i)

        cmd_i = command.Cmd(name=CmdEnumCON.con_error_count_ar.name,
                            sysreq=suchai_types.SysReqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_error_count_ar)
        self.cmdBuffer.append(cmd_i)

        cmd_i = command.Cmd(name=CmdEnumCON.con_error_invalid_arg.name,
                            sysreq=suchai_types.SysReqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_error_invalid_arg)
        self.cmdBuffer.append(cmd_i)

        cmd_i = command.Cmd(name=CmdEnumCON.con_error_unknown_cmd.name,
                            sysreq=suchai_types.SysReqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_error_unknown_cmd)
        self.cmdBuffer.append(cmd_i)

        cmd_i = command.Cmd(name=CmdEnumCON.con_help.name,
                            sysreq=suchai_types.SysReqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_help)
        self.cmdBuffer.append(cmd_i)

        cmd_i = command.Cmd(name=CmdEnumCON.con_promt.name,
                            sysreq=suchai_types.SysReqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_promt)
        self.cmdBuffer.append(cmd_i)

        verbose = False
        if verbose:
            for i in range(0, len(CmdEnumCON)):
                arg = "self.cmdBuffer[%s] => %s" % (i, self.cmdBuffer[i])
                # print(arg)
                logger.debug(arg)
                arg = "self.cmdBuffer[%s].name => %s" % (i, self.cmdBuffer[i].name)
                # print(arg)
                logger.debug(arg)
            # print()

        if len(CmdEnumCON) != self.get_ncmds():
            arg = "wrong implementation"
            # print(arg)
            logger.critical(arg)
            raise NotImplemented


class CmdFunctCON():
    @staticmethod
    def con_help(param):
        gnrl_services.console_print("This is the useless %s command" % CmdFunctCON.con_help.__name__)
        gnrl_services.console_print("Used with param %s" % param)
        return True

    @staticmethod
    def con_promt(param):
        return False

    @staticmethod
    def con_error_cmd_toolong(param):
        return False

    @staticmethod
    def con_debug_msg(param):
        return False

    @staticmethod
    def con_error_unknown_cmd(param):
        return False

    @staticmethod
    def con_error_invalid_arg(param):
        return False

    @staticmethod
    def con_error_count_ar( param):
        return False
