# -*- coding: utf-8 -*-
__author__ = 'toopazo'


def console_print(arg):
    print(arg)


def console_input(arg):
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
        filepath = "runtimefiles/state/%s" % name
        line = PersistenMem.__read_file(filepath)
        return line

    @staticmethod
    def write_state_var(name, val):
        filepath = "runtimefiles/state/%s" % name
        PersistenMem.__write_file(filepath, val)

    # data / payloads
    @staticmethod
    def read_data(name):
        filepath = "runtimefiles/data/%s" % name
        line = PersistenMem.__read_file(filepath)
        return line

    @staticmethod
    def write_pay_var(filepath, val):
        filepath = "runtimefiles/data/%s" % filepath
        PersistenMem.__write_file(filepath, val)
