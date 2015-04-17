# -*- coding: utf-8 -*-
__author__ = 'toopazo'


from enum import Enum, unique
from repos import command
from core import gnrl_services
import SUCHAI_config
import logging
logger = logging.getLogger(__name__)

@unique
class CmdEnumCON(Enum):
    con_help = SUCHAI_config.ConfigCmdgroup.SCH_GID_CON + 0
    con_promt = SUCHAI_config.ConfigCmdgroup.SCH_GID_CON + 1
    con_error_cmd_toolong = SUCHAI_config.ConfigCmdgroup.SCH_GID_CON + 2
    con_debug_msg = SUCHAI_config.ConfigCmdgroup.SCH_GID_CON + 3
    con_error_unknown_cmd = SUCHAI_config.ConfigCmdgroup.SCH_GID_CON + 4
    con_error_invalid_arg = SUCHAI_config.ConfigCmdgroup.SCH_GID_CON + 5
    con_error_count_ar = SUCHAI_config.ConfigCmdgroup.SCH_GID_CON + 6

    con_debug7 = SUCHAI_config.ConfigCmdgroup.SCH_GID_CON + 7
    con_debug8 = SUCHAI_config.ConfigCmdgroup.SCH_GID_CON + 8
    con_debug9 = SUCHAI_config.ConfigCmdgroup.SCH_GID_CON + 9
    con_debug10 = SUCHAI_config.ConfigCmdgroup.SCH_GID_CON + 10
    con_debug11 = SUCHAI_config.ConfigCmdgroup.SCH_GID_CON + 11
    con_debug12 = SUCHAI_config.ConfigCmdgroup.SCH_GID_CON + 12
    con_debug13 = SUCHAI_config.ConfigCmdgroup.SCH_GID_CON + 13
    con_debug14 = SUCHAI_config.ConfigCmdgroup.SCH_GID_CON + 14
    con_debug15 = SUCHAI_config.ConfigCmdgroup.SCH_GID_CON + 15
    con_debug16 = SUCHAI_config.ConfigCmdgroup.SCH_GID_CON + 16
    con_debug17 = SUCHAI_config.ConfigCmdgroup.SCH_GID_CON + 17


    @staticmethod
    def get_index(var):
        if hasattr(var, "value"):
            return var.value
        else:
            return -1

    @staticmethod
    def get_string(var):
        if hasattr(var, "cmdName"):
            return var.name
        else:
            return -1


class CmdgroupCON(command.Cmdgroup):
    cmdgroupName = SUCHAI_config.ConfigCmdgroup.SCH_GNM_CON
    cmdgroupId = SUCHAI_config.ConfigCmdgroup.SCH_GID_CON
    cmdEnum = CmdEnumCON

    def __init__(self):
        command.Cmdgroup.__init__(self)
        self.cmdgroupName = CmdgroupCON.cmdgroupName
        self.cmdgroupId = CmdgroupCON.cmdgroupId

    #@staticmethod
    def on_reset(self):
        # Append every command STRICTLY following order

        cmd_i = command.Cmd(cmdid=CmdEnumCON.con_help.value,
                            name=CmdEnumCON.con_help.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_help)
        self.cmdgroupCmdBuffer.append(cmd_i)
        # cmd_i_num = int(CmdEnumCON.con_help.value & int('00001111', 2))
        # gnrl_services.console_print("cmd_i_num %s" % cmd_i_num)
        # self.cmdgroupCmdBuffer.insert(cmd_i_num, cmd_i)

        cmd_i = command.Cmd(cmdid=CmdEnumCON.con_promt.value,
                            name=CmdEnumCON.con_promt.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_promt)
        self.cmdgroupCmdBuffer.append(cmd_i)
        # cmd_i_num = int(CmdEnumCON.con_promt.value & int('00001111', 2))
        # gnrl_services.console_print("cmd_i_num %s" % cmd_i_num)
        # self.cmdgroupCmdBuffer.insert(cmd_i_num, cmd_i)

        cmd_i = command.Cmd(cmdid=CmdEnumCON.con_error_cmd_toolong.value,
                            name=CmdEnumCON.con_error_cmd_toolong.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_error_cmd_toolong)
        self.cmdgroupCmdBuffer.append(cmd_i)
        # cmd_i_num = int(CmdEnumCON.con_error_cmd_toolong.value & int('00001111', 2))
        # gnrl_services.console_print("cmd_i_num %s" % cmd_i_num)
        # self.cmdgroupCmdBuffer.insert(cmd_i_num, cmd_i)

        cmd_i = command.Cmd(cmdid=CmdEnumCON.con_debug_msg.value,
                            name=CmdEnumCON.con_debug_msg.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_debug_msg)
        self.cmdgroupCmdBuffer.append(cmd_i)
        # cmd_i_num = int(CmdEnumCON.con_debug_msg.value & int('00001111', 2))
        # gnrl_services.console_print("cmd_i_num %s" % cmd_i_num)
        # self.cmdgroupCmdBuffer.insert(cmd_i_num, cmd_i)

        cmd_i = command.Cmd(cmdid=CmdEnumCON.con_error_unknown_cmd.value,
                            name=CmdEnumCON.con_error_unknown_cmd.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_error_unknown_cmd)
        self.cmdgroupCmdBuffer.append(cmd_i)
        # cmd_i_num = int(CmdEnumCON.con_error_unknown_cmd.value & int('00001111', 2))
        # gnrl_services.console_print("cmd_i_num %s" % cmd_i_num)
        # self.cmdgroupCmdBuffer.insert(cmd_i_num, cmd_i)

        cmd_i = command.Cmd(cmdid=CmdEnumCON.con_error_invalid_arg.value,
                            name=CmdEnumCON.con_error_invalid_arg.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_error_invalid_arg)
        self.cmdgroupCmdBuffer.append(cmd_i)
        # cmd_i_num = int(CmdEnumCON.con_error_invalid_arg.value & int('00001111', 2))
        # gnrl_services.console_print("cmd_i_num %s" % cmd_i_num)
        # self.cmdgroupCmdBuffer.insert(cmd_i_num, cmd_i)

        cmd_i = command.Cmd(cmdid=CmdEnumCON.con_error_count_ar.value,
                            name=CmdEnumCON.con_error_count_ar.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_error_count_ar)
        self.cmdgroupCmdBuffer.append(cmd_i)
        # cmd_i_num = int(CmdEnumCON.con_error_count_ar.value & int('00001111', 2))
        # gnrl_services.console_print("cmd_i_num %s" % cmd_i_num)
        # self.cmdgroupCmdBuffer.insert(cmd_i_num, cmd_i)

        #testing

        cmd_i = command.Cmd(cmdid=CmdEnumCON.con_debug7.value,
                            name=CmdEnumCON.con_debug7.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_debug_msg)
        self.cmdgroupCmdBuffer.append(cmd_i)
        cmd_i = command.Cmd(cmdid=CmdEnumCON.con_debug8.value,
                            name=CmdEnumCON.con_debug8.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_debug_msg)
        self.cmdgroupCmdBuffer.append(cmd_i)
        cmd_i = command.Cmd(cmdid=CmdEnumCON.con_debug9.value,
                            name=CmdEnumCON.con_debug9.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_debug_msg)
        self.cmdgroupCmdBuffer.append(cmd_i)
        cmd_i = command.Cmd(cmdid=CmdEnumCON.con_debug10.value,
                            name=CmdEnumCON.con_debug10.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_debug_msg)
        self.cmdgroupCmdBuffer.append(cmd_i)
        cmd_i = command.Cmd(cmdid=CmdEnumCON.con_debug11.value,
                            name=CmdEnumCON.con_debug11.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_debug_msg)
        self.cmdgroupCmdBuffer.append(cmd_i)
        cmd_i = command.Cmd(cmdid=CmdEnumCON.con_debug12.value,
                            name=CmdEnumCON.con_debug12.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_debug_msg)
        self.cmdgroupCmdBuffer.append(cmd_i)
        cmd_i = command.Cmd(cmdid=CmdEnumCON.con_debug13.value,
                            name=CmdEnumCON.con_debug13.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_debug_msg)
        self.cmdgroupCmdBuffer.append(cmd_i)
        cmd_i = command.Cmd(cmdid=CmdEnumCON.con_debug14.value,
                            name=CmdEnumCON.con_debug14.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_debug_msg)
        self.cmdgroupCmdBuffer.append(cmd_i)
        cmd_i = command.Cmd(cmdid=CmdEnumCON.con_debug15.value,
                            name=CmdEnumCON.con_debug15.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_debug_msg)
        self.cmdgroupCmdBuffer.append(cmd_i)
        cmd_i = command.Cmd(cmdid=CmdEnumCON.con_debug16.value,
                            name=CmdEnumCON.con_debug16.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_debug_msg)
        self.cmdgroupCmdBuffer.append(cmd_i)
        cmd_i = command.Cmd(cmdid=CmdEnumCON.con_debug17.value,
                            name=CmdEnumCON.con_debug17.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctCON.con_debug_msg)
        self.cmdgroupCmdBuffer.append(cmd_i)

        # gnrl_services.console_print("len(CmdEnumCON) %s, self.get_num_cmds() %s " %
        #                             (len(CmdEnumCON), self.get_num_cmds()))

        if len(CmdEnumCON) != self.get_num_cmds():
            arg = "wrong implementation"
            # print(arg)
            logger.critical(arg)
            raise NotImplemented


class CmdFunctCON():
    @staticmethod
    def con_help(param):
        gnrl_services.console_print("This is the useless %s command" % CmdFunctCON.con_help.__name__)
        gnrl_services.console_print("Used with cmdParam %s" % param)
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
