#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'

import SUCHAI_config
import logging
logger = logging.getLogger(__name__)

#identify payload and let it generate files in nside its folder
#some gnrl schemes for file names shopuld be offered, like datetime.txt and so on ..


def init():
    # prepares permanent memory to be used by bus and paylaods
    pass    # nothing to prepare, usign linux's regular files


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
        filepath = SUCHAI_config.ConfigPermanentMem.SCH_STATE_FOLDER + name
        line = PersistenMem.__read_file(filepath)
        return line

    @staticmethod
    def write_state_var(name, val):
        filepath = SUCHAI_config.ConfigPermanentMem.SCH_STATE_FOLDER + name
        PersistenMem.__write_file(filepath, val)

    # data / payloads
    @staticmethod
    def read_data(name):
        filepath = SUCHAI_config.ConfigPermanentMem.SCH_DATA_FOLDER + name
        line = PersistenMem.__read_file(filepath)
        return line

    @staticmethod
    def write_pay_var(name, val):
        filepath = SUCHAI_config.ConfigPermanentMem.SCH_DATA_FOLDER + name
        PersistenMem.__write_file(filepath, val)
