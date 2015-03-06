#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'


from repos import command
from core import gnrluse
import logging
logger = logging.getLogger(__name__)


class CmdCON(command.CmdXXX):

    def __init__(self):
        command.CmdXXX.__init__(self)
        self.name = __name__
        self.cmdOwn = 1

    # #@staticmethod
    # def get_ncmds(self):
    #     return len(self.cmdFunction)

    @staticmethod
    def help(param):
        print("This is the useless %s.%s command" % (CmdCON.__name__, CmdCON.help.__name__))
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
    def error_count_ar(param):
        return False

    #@staticmethod
    def on_reset(self):
        # add every cmd and sysreq to CmdCON.cmdFunction and CmdCON.cmdSysReq

        self.cmdFunction.append(CmdCON.help)
        self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)

        self.cmdFunction.append(CmdCON.promt)
        self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)

        self.cmdFunction.append(CmdCON.error_cmd_toolong)
        self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)

        self.cmdFunction.append(CmdCON.error_count_ar)
        self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)

        self.cmdFunction.append(CmdCON.error_invalid_arg)
        self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)

        self.cmdFunction.append(CmdCON.error_unknown_cmd)
        self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)

        self.cmdFunction.append(CmdCON.debug_msg)
        self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)


