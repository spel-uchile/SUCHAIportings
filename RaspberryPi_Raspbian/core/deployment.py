# -*- coding: utf-8 -*-
__author__ = 'toopazo'

from tasks import comunications
from tasks import console
from tasks import dispatcher
from tasks import flightplan
from tasks import housekeeping

from core import gnrl_services

from repos import state
from repos import command
from repos.cmds import cmdcon
from repos.cmds import cmdrtc
from repos.cmds import cmdcam

import logging
logger = logging.getLogger(__name__)


def init_state_repo():
    arg = "    [init_state_repo]"
    logger.debug(arg)
    gnrl_services.console_print(arg)

    state.StateVar.on_reset()


def init_command_repo():
    arg = "    [init_command_repo]"
    logger.debug(arg)
    gnrl_services.console_print(arg)

    # add cmds to cmdRepo
    cmd_group_xxx = cmdcon.CmdGroupCON()
    command.CmdRepo.add_cmd_group(cmd_group_xxx)
    arg = "      Attaching %s to CmdRepo .." % cmd_group_xxx.groupName
    logger.debug(arg)
    gnrl_services.console_print(arg)

    cmd_group_xxx = cmdrtc.CmdGroupRTC()
    command.CmdRepo.add_cmd_group(cmd_group_xxx)
    arg = "      Attaching %s to CmdRepo .." % cmd_group_xxx.groupName
    logger.debug(arg)
    gnrl_services.console_print(arg)

    cmd_group_xxx = cmdcam.CmdGroupCAM()
    command.CmdRepo.add_cmd_group(cmd_group_xxx)
    arg = "      Attaching %s to CmdRepo .." % cmd_group_xxx.groupName
    logger.debug(arg)
    gnrl_services.console_print(arg)

    # debug info
    arg = "      Commands successfully loaded to CmdRepo: "
    logger.debug(arg)
    gnrl_services.console_print(arg)
    for j in range(0, len(command.CmdRepo.cmd_group_buffer)):
        cmd_group_xxx = command.CmdRepo.cmd_group_buffer[j]
        for i in range(0, cmd_group_xxx.get_ncmds()):
            cmd_i = command.CmdRepo.get_command_byid(cmd_group_xxx.groupName, i)
            arg = "        get_command_byid(%s, %s).name: %s" % (cmd_group_xxx.groupName, i, cmd_i.name)
            gnrl_services.console_print(arg)
            logger.debug(arg)


def init_data_repo():
    arg = "    [init_data_repo]"
    logger.debug(arg)
    gnrl_services.console_print(arg)


def init_suchai_repos():
    arg = "  [init_suchai_repo]"
    logger.debug(arg)
    gnrl_services.console_print(arg)
    # /* Repositories */
    init_state_repo()       # modify specific reset-dependant STA_StateVar vars
    init_command_repo()     # loads cmdXXX repos to be used
    init_data_repo()        # prepares GnrlPurposeBuff to be used


def launch_tasks():
    arg = "[launch_tasks]"
    logger.debug(arg)
    gnrl_services.console_print(arg)

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


