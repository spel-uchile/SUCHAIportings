# -*- coding: utf-8 -*-
__author__ = 'toopazo'


from enum import Enum, unique
from repos import command
from core import gnrl_services
import SUCHAI_config
import datetime
import logging
logger = logging.getLogger(__name__)

@unique
class CmdEnumRTC(Enum):
    rtc_debug = SUCHAI_config.ConfigCmdgroup.SCH_GID_RTC + 0
    rtc_get_time_now = SUCHAI_config.ConfigCmdgroup.SCH_GID_RTC + 1

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


class CmdgroupRTC(command.Cmdgroup):
    cmdgroupName = SUCHAI_config.ConfigCmdgroup.SCH_GNM_RTC
    cmdgroupId = SUCHAI_config.ConfigCmdgroup.SCH_GID_RTC
    cmdEnum = CmdEnumRTC

    def __init__(self):
        command.Cmdgroup.__init__(self)
        self.cmdgroupName = CmdgroupRTC.cmdgroupName
        self.cmdgroupId = CmdgroupRTC.cmdgroupId

    #@staticmethod
    def on_reset(self):
        # Append every command STRICTLY following order

        cmd_i = command.Cmd(cmdid=CmdEnumRTC.rtc_debug.value,
                            name=CmdEnumRTC.rtc_debug.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctRTC.rtc_debug)
        self.cmdgroupCmdBuffer.append(cmd_i)
        # cmd_i_num = int(CmdEnumRTC.rtc_debug.value & int('00001111', 2))
        # gnrl_services.console_print("cmd_i_num %s" % cmd_i_num)
        # self.cmdgroupCmdBuffer.insert(cmd_i_num, cmd_i)

        cmd_i = command.Cmd(cmdid=CmdEnumRTC.rtc_get_time_now.value,
                            name=CmdEnumRTC.rtc_get_time_now.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctRTC.get_time_now)
        self.cmdgroupCmdBuffer.append(cmd_i)
        # cmd_i_num = int(CmdEnumRTC.rtc_get_time_now.value & int('00001111', 2))
        # gnrl_services.console_print("cmd_i_num %s" % cmd_i_num)
        # self.cmdgroupCmdBuffer.insert(cmd_i_num, cmd_i)

        # gnrl_services.console_print("len(CmdEnumRTC) %s, self.get_num_cmds() %s " %
        #                             (len(CmdEnumRTC), self.get_num_cmds()))

        if len(CmdEnumRTC) != self.get_num_cmds():
            arg = "wrong implementation"
            logger.critical(arg)
            raise NotImplemented


class CmdFunctRTC():
    @staticmethod
    def get_time_now(param):
        gnrl_services.console_print(datetime.datetime.now())
        return True

    @staticmethod
    def rtc_debug(param):
        return False
