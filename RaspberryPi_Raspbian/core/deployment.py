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
    logger.debug("[init_state_repo]")
    state.StateVar.on_reset(False)


def init_command_repo():
    logger.debug("[init_command_repo]")

    # add cmds to cmdRepo
    cmd_group_xxx = cmdconsole.CmdGroupCON()
    command.CmdRepo.add_cmd_group(cmd_group_xxx)
    arg = "Attaching %s to CmdRepo .." % cmd_group_xxx.groupName
    logger.debug(arg)
    # debug section
    for i in range(0, command.CmdRepo.get_ncmds(cmd_group_xxx.groupName)):
        arg = "get_function_byid(%s, %s) => %s" % (cmd_group_xxx.groupName, i,
                                                   command.CmdRepo.get_function_byid(cmd_group_xxx.groupName, i))
        # print(arg)
        logger.debug(arg)
        arg = "get_sysreq_byid(%s, %s) => %s" % (cmd_group_xxx.groupName, i,
                                                 command.CmdRepo.get_sysreq_byid(cmd_group_xxx.groupName, i))
        # print(arg)
        logger.debug(arg)

    cmd_group_xxx = cmdrtc.CmdGroupRTC()
    command.CmdRepo.add_cmd_group(cmd_group_xxx)
    arg = "Attaching %s to CmdRepo .." % cmd_group_xxx.groupName
    logger.debug(arg)
    # debug section
    for i in range(0, command.CmdRepo.get_ncmds(cmd_group_xxx.groupName)):
        arg = "get_function_byid(%s, %s) => %s" % (cmd_group_xxx.groupName, i,
                                                   command.CmdRepo.get_function_byid(cmd_group_xxx.groupName, i))
        # print(arg)
        logger.debug(arg)
        arg = "get_sysreq_byid(%s, %s) => %s" % (cmd_group_xxx.groupName, i,
                                                 command.CmdRepo.get_sysreq_byid(cmd_group_xxx.groupName, i))
        # print(arg)
        logger.debug(arg)


def init_data_repo():
    logger.debug("[init_data_repo]")


def init_suchai_repos():
    # /* Repositories */
    init_state_repo()       # modify specific reset-dependant STA_StateVar vars
    init_command_repo()     # loads cmdXXX repos to be used
    init_data_repo()        # prepares GnrlPurposeBuff to be used


def launch_tasks():
    logger.debug("[launch_tasks]")

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

    # time.sleep(2)
    logger.info("Starting nominal operations ..")

    dispatcher.taskHandler.start()
    comunications.taskHandler.start()
    console.taskHandler.start()
    flightplan.taskHandler.start()
    housekeeping.taskHandler.start()

    # time.sleep(2)   # give time for every process to start
    # logger.debug("-------------------------")

    dispatcher.taskHandler.join()
    comunications.taskHandler.join()
    console.taskHandler.join()
    flightplan.taskHandler.join()
    housekeeping.taskHandler.join()

    # the systems should never reach this pont, otherwise an error occured

    # handler = dispatcher.taskHandler
    # arg = "%s, %s, %s, %s" % (handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    # logger.debug(arg)
    # handler = comunications.taskHandler
    # arg = "%s, %s, %s, %s" % (handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    # logger.debug(arg)
    # handler = console.taskHandler
    # arg = "%s, %s, %s, %s" % (handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    # logger.debug(arg)
    # handler = flightplan.taskHandler
    # arg = "%s, %s, %s, %s" % (handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    # logger.debug(arg)
    # handler = housekeeping.taskHandler
    # arg = "%s, %s, %s, %s" % (handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    # logger.debug(arg)
    #
    # logger.debug("-------------------------")


