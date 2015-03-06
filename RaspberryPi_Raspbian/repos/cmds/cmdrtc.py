#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'


from repos import command
from core import gnrluse
import datetime
import logging
logger = logging.getLogger(__name__)


class CmdRTC(command.CmdXXX):

    def __init__(self):
        command.CmdXXX.__init__(self)
        self.name = __name__
        self.cmdOwn = 1

    # #@staticmethod
    # def get_ncmds(self):
    #     return len(self.cmdFunction)

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
        # add every cmd and sysreq to CmdRTC.cmdFunction and CmdRTC.cmdSysReq

        self.cmdFunction.append(CmdRTC.debug)
        self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)

        self.cmdFunction.append(CmdRTC.time)
        self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)



