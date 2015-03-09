#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'


from repos import command
from core import gnrluse
import SUCHAI_config
import datetime
import logging
logger = logging.getLogger(__name__)


class CmdRTC(command.CmdGroup):

    def __init__(self):
        command.CmdGroup.__init__(self)
        self.groupName = __name__
        self.groupId = SUCHAI_config.SCH_GID_RTC

    # #@staticmethod
    # def get_ncmds(self):
    #     return len(self.cmdBuffer)

    @staticmethod
    def debug(param):
        print("This is the useless %s.%s command" % (CmdRTC.__name__, CmdRTC.debug.__name__))
        return True

    @staticmethod
    def time(param):
        print(datetime.datetime.now())
        return True

    #@staticmethod
    def on_reset(self):
        # add every cmd and sysReq to CmdRTC.cmdBuffer and CmdRTC.cmdSysReq

        self.cmdBuffer.append(CmdRTC.debug)
        self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)

        self.cmdBuffer.append(CmdRTC.time)
        self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)



