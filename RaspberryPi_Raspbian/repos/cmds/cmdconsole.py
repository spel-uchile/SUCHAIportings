#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'


from repos import command
from core import gnrluse
import logging
logger = logging.getLogger(__name__)


#class CmdCON(command.CmdHandler):
class CmdCON(command.CmdXXX):
    def __init__(self, cmdown, ncmd):  # , cmd_function_repo):
        self.name = CmdCON.__name__
        # self.cmdOwn = cmdown
        # self.nCmd = ncmd
        # self.cmdFunction = []          # buffer of functions
        # self.cmdSysReq = []            # buffer of sysReq
        command.CmdXXX.__init__(self, cmdown, ncmd)

        self.on_reset()

    def get_ncmds(self):
        return len(self.cmdFunction)

    def on_reset(self):
        cmd_function_repo = CmdCONFunctions()
        # add every cmd and sysreq to cmdFunction and cmdSysReq
        # for every cmd

        self.cmdFunction.append(cmd_function_repo.help)
        self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)

        self.cmdFunction.append(cmd_function_repo.promt)
        self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)

        self.cmdFunction.append(cmd_function_repo.error_cmd_toolong)
        self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)

        self.cmdFunction.append(cmd_function_repo.error_count_ar)
        self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)

        self.cmdFunction.append(cmd_function_repo.error_invalid_arg)
        self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)

        self.cmdFunction.append(cmd_function_repo.error_unknown_cmd)
        self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)

        self.cmdFunction.append(cmd_function_repo.debug_msg)
        self.cmdSysReq.append(gnrluse.SysReqs.SYSREQ_MIN)


class CmdCONFunctions():
    @staticmethod
    def help(param):
        print("This is the useless %s.%s command" % (CmdCONFunctions.__name__, CmdCONFunctions.help.__name__))
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


