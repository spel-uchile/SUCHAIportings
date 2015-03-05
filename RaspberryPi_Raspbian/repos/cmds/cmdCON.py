#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'


from repos import command
import logging
logger = logging.getLogger(__name__)


class CmdCON(command.CmdXXX):
    dict = dict(
        help=CmdConFunction.help,                 # ///< @cmd_first
        promt=CmdConFunction.promt,                # ///< @cmd
        error_cmd_toolong=2,    # ///< @cmd
        debug_msg=3,            # ///< @cmd
        error_unknown_cmd=4,    # ///< @cmd
        error_invalid_arg=5,    # ///< @cmd
        error_count_ar=6        # ///< @cmd
    )


class CmdConFunction():
    @staticmethod
    def help(param):
        return False

    @staticmethod
    def promt(param):
        return False

    @staticmethod
    def error_cmd_toolong(param):
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
    