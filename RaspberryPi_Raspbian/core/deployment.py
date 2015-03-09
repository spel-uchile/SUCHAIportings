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
from repos.cmds import cmdconsole
from repos.cmds import cmdrtc

import logging
logger = logging.getLogger(__name__)


def init_state_repo():
    # logger.debug("")
    state.StateVar.on_reset(False)


def init_command_repo():

    # add cmds to cmdRepo
    cmd_con = cmdconsole.CmdGroupCON()
    command.CmdRepo.add_cmd_group(cmd_con)
    arg = "    * Attaching %s to CmdRepo" % cmd_con.groupName
    logger.debug(arg)

    # debug section
    for i in range(0, command.CmdRepo.get_ncmds(cmd_con.groupName)):
        arg = "get_function_byid(%s, %s) => %s" % (cmd_con.groupName, i, command.CmdRepo.get_function_byid(cmd_con.groupName, i))
        # print(arg)
        logger.debug(arg)
        arg = "get_sysreq_byid(%s, %s) => %s" % (cmd_con.groupName, i, command.CmdRepo.get_sysreq_byid(cmd_con.groupName, i))
        # print(arg)
        logger.debug(arg)

    # cmd_rtc = cmdrtc.CmdRTC()
    # command.CmdRepo.add_cmd_group(cmd_rtc)
    # arg = "    * Attaching %s to CmdRepo" % cmd_rtc.groupName
    # logger.debug(arg)
    #
    # # debug section
    # for i in range(0, command.CmdRepo.get_ncmds(cmd_rtc.groupName)):
    #     arg = "get_function_byid(%s, %s) => %s" % (cmd_rtc.groupName, i, command.CmdRepo.get_function_byid(cmd_rtc.groupName, i))
    #     # print(arg)
    #     logger.debug(arg)
    #     arg = "get_sysreq_byid(%s, %s) => %s" % (cmd_rtc.groupName, i, command.CmdRepo.get_sysreq_byid(cmd_rtc.groupName, i))
    #     # print(arg)
    #     logger.debug(arg)


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

