#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'


from enum import Enum, unique
from repos import command
from core import suchai_types
from core import gnrl_services
import SUCHAI_config
import datetime
import logging
logger = logging.getLogger(__name__)

@unique
class CmdEnumRTC(Enum):
    rtc_debug = 0
    rtc_get_time_now = 1

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


class CmdGroupRTC(command.CmdGroup):
    groupName = SUCHAI_config.SCH_GNM_RTC
    groupId = SUCHAI_config.SCH_GID_RTC
    cmdEnum = CmdEnumRTC

    def __init__(self):
        command.CmdGroup.__init__(self)
        self.groupName = CmdGroupRTC.groupName
        self.groupId = CmdGroupRTC.groupId

    #@staticmethod
    def on_reset(self):
        # create a cmd for every enum and then append it to CmdRTC.cmdBuffer
        cmd_i = command.Cmd(name=CmdEnumRTC.rtc_debug.name,
                            sysreq=suchai_types.SysReqs.SYSREQ_MIN,
                            funct=CmdFunctRTC.rtc_debug)
        self.cmdBuffer.append(cmd_i)

        cmd_i = command.Cmd(name=CmdEnumRTC.rtc_get_time_now.name,
                            sysreq=suchai_types.SysReqs.SYSREQ_MIN,
                            funct=CmdFunctRTC.get_time_now)
        self.cmdBuffer.append(cmd_i)

        verbose = False
        if verbose:
            for i in range(0, len(CmdEnumRTC)):
                arg = "self.cmdBuffer[%s] => %s" % (i, self.cmdBuffer[i])
                logger.debug(arg)
                arg = "self.cmdBuffer[%s].name => %s" % (i, self.cmdBuffer[i].name)
                logger.debug(arg)

        if len(CmdEnumRTC) != self.get_ncmds():
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
