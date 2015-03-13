#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'


from core import gnrl_services
import logging
logger = logging.getLogger(__name__)


def init_hw_configs():
    arg = "  [init_hw_configs]"
    gnrl_services.console_print(arg)
    logger.debug(arg)
