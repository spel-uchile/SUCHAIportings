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
