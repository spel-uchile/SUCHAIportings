# -*- coding: utf-8 -*-
__author__ = 'toopazo'

import SUCHAI_config
import sys


def console_print(arg):
    print(arg)


def console_input(arg):
    # asd = "using %s" % str(sys.version_info)
    # console_print(asd)
    if sys.version_info < (3, 0):
        line = raw_input(arg)
    else:
        line = input(arg)
    return line


class PersistenMem():
    @staticmethod
    def __read_file(filepath):
        fd = open(filepath, "r")
        line = fd.read()
        fd.close()
        return line

    @staticmethod
    def __write_file(filepath, val):
        fd = open(filepath, "w")
        fd.write(str(val))
        fd.close()

    # state vars
    @staticmethod
    def read_state_var(name):
        filepath = SUCHAI_config.SCH_STATE_FOLDER + name
        line = PersistenMem.__read_file(filepath)
        return line

    @staticmethod
    def write_state_var(name, val):
        filepath = SUCHAI_config.SCH_STATE_FOLDER + name
        PersistenMem.__write_file(filepath, val)

    # data / payloads
    @staticmethod
    def read_data(name):
        filepath = SUCHAI_config.SCH_DATA_FOLDER + name
        line = PersistenMem.__read_file(filepath)
        return line

    @staticmethod
    def write_pay_var(name, val):
        filepath = SUCHAI_config.SCH_DATA_FOLDER + name
        PersistenMem.__write_file(filepath, val)
