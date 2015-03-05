#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'

from tasks import comunications
from tasks import console
from tasks import dispatcher
from tasks import flightplan
from tasks import housekeeping
import time

from repos import state
from repos import command

import logging
logger = logging.getLogger(__name__)


def init_state_repo():
    # logger.debug("")
    state.StateVar.on_reset(False)


def init_command_repo():
    # add cmds to cmdRepo
    con_handler = command.CmdHandler(name="CmdCON", cmd_own=1, n_cmd=2,
                                     b_function=['function1', 'function2', print],
                                     b_sys_req=[], on_reset_function=None)
    command.CmdRepo.add_commands(con_handler)
    arg = "get_function(con_handler.name, 0) => %s", command.CmdRepo.get_function(con_handler.name, 0)    # debug
    print(arg)
    arg = "get_function(con_handler.name, 1) => %s", command.CmdRepo.get_function(con_handler.name, 1)    # debug
    print(arg)
    arg = "get_function(con_handler.name, 2) => %s", command.CmdRepo.get_function(con_handler.name, 2)    # debug
    print(arg)
    command.CmdRepo.get_function(con_handler.name, 2)("aca ejecuto la funcion que llame con get_function")    # debug
    #pass


def init_data_repo():
    pass


def init_suchai_repos():
    # /* Repositories */
    init_state_repo()       # modify specific reset-dependant STA_StateVar vars
    init_command_repo()     # loads cmdXXX repos to be used
    init_data_repo()        # prepares GnrlPurposeBuff to be used


def launch_tasks():
    handler = dispatcher.taskHandler
    arg = "%s, %s, %s, %s" % (handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    logger.debug(arg)
    handler = comunications.taskHandler
    arg = "%s, %s, %s, %s" % (handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    logger.debug(arg)
    handler = console.taskHandler
    arg = "%s, %s, %s, %s" % (handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    logger.debug(arg)
    handler = flightplan.taskHandler
    arg = "%s, %s, %s, %s" % (handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    logger.debug(arg)
    handler = housekeeping.taskHandler
    arg = "%s, %s, %s, %s" % (handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    logger.debug(arg)
    logger.debug("-------------------------")

    time.sleep(2)

    dispatcher.taskHandler.start()
    comunications.taskHandler.start()
    console.taskHandler.start()
    flightplan.taskHandler.start()
    housekeeping.taskHandler.start()

    time.sleep(2)

    dispatcher.taskHandler.join()
    comunications.taskHandler.join()
    console.taskHandler.join()
    flightplan.taskHandler.join()
    housekeeping.taskHandler.join()

    logger.debug("-------------------------")
    handler = dispatcher.taskHandler
    arg = "%s, %s, %s, %s" % (handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    logger.debug(arg)
    handler = comunications.taskHandler
    arg = "%s, %s, %s, %s" % (handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    logger.debug(arg)
    handler = console.taskHandler
    arg = "%s, %s, %s, %s" % (handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    logger.debug(arg)
    handler = flightplan.taskHandler
    arg = "%s, %s, %s, %s" % (handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    logger.debug(arg)
    handler = housekeeping.taskHandler
    arg = "%s, %s, %s, %s" % (handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    logger.debug(arg)

    logger.info("Suchai Sw: Starting nominal operations ..")

