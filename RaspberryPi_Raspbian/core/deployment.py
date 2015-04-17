# -*- coding: utf-8 -*-
__author__ = 'toopazo'

from Listeners import comunications
from Listeners import console
from Listeners import dispatcher
from Listeners import flightplan
from Listeners import housekeeping

from core import gnrl_services
import SUCHAI_config

from repos import state
from repos import command
from repos import data
from repos.cmds import cmdcon
from repos.cmds import cmdrtc
if SUCHAI_config.SCH_CAM_ONBOARD == 1:
    from repos.cmds import cmdcam
else:
    pass

import logging
logger = logging.getLogger(__name__)


def init_state_repo():
    # modify specific reset-dependant STA_StateVar vars

    arg = "    [init_state_repo]"
    logger.debug(arg)
    gnrl_services.console_print(arg)

    state.StateVar.on_reset()


def init_command_repo():
    # loads cmdXXX repos to be used

    arg = "    [init_command_repo]"
    logger.debug(arg)
    gnrl_services.console_print(arg)

    # add cmds to cmdRepo
    cmdgroup_j = cmdcon.CmdgroupCON()
    command.CmdRepo.add_cmdgroup(cmdgroup_j)
    arg = "      Attaching %s to CmdRepo .." % cmdgroup_j.cmdgroupName
    logger.debug(arg)
    gnrl_services.console_print(arg)

    cmdgroup_j = cmdrtc.CmdgroupRTC()
    command.CmdRepo.add_cmdgroup(cmdgroup_j)
    arg = "      Attaching %s to CmdRepo .." % cmdgroup_j.cmdgroupName
    logger.debug(arg)
    gnrl_services.console_print(arg)

    if SUCHAI_config.SCH_CAM_ONBOARD == 1:
        cmdgroup_j = cmdcam.CmdgroupCAM()
        command.CmdRepo.add_cmdgroup(cmdgroup_j)
        arg = "      Attaching %s to CmdRepo .." % cmdgroup_j.cmdgroupName
        logger.debug(arg)
        gnrl_services.console_print(arg)
    else:
        pass

    # debug info
    arg = "      Commands successfully loaded to CmdRepo: "
    logger.debug(arg)
    gnrl_services.console_print(arg)
    for j in range(0, command.CmdRepo.get_num_cmdgroups()):
        cmdgroup_j = command.CmdRepo.get_cmdgroup(j)
        for i in range(0, cmdgroup_j.get_num_cmds()):
            cmd_i = cmdgroup_j.get_cmd(i)
            arg = "        %s.get_cmd(%s) => cmdId: 0x%0.4X, cmdName: %s, " %\
                  (cmdgroup_j.cmdgroupName, i, cmd_i.cmdId, cmd_i.cmdName)
            gnrl_services.console_print(arg)
            logger.debug(arg)


def init_data_repo():
    # prepares permanent memory to be used by bus and paylaods

    arg = "    [init_data_repo]"
    logger.debug(arg)
    gnrl_services.console_print(arg)

    data.init()


def init_suchai_repos():
    arg = "  [init_suchai_repo]"
    logger.debug(arg)
    gnrl_services.console_print(arg)
    # /* Repositories */
    init_state_repo()       # modify specific reset-dependant STA_StateVar vars
    init_command_repo()     # loads cmdXXX repos to be used
    init_data_repo()        # prepares permanent memory to be used by bus and paylaods


def launch_listeners():
    arg = "[launch_listeners]"
    logger.debug(arg)
    gnrl_services.console_print(arg)

    handler = dispatcher.listenerHandler
    arg = "%s, %s, %s, %s" % (handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    logger.debug(arg)
    handler = comunications.listenerHandler
    arg = "%s, %s, %s, %s" % (handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    logger.debug(arg)
    handler = console.listenerHandler
    arg = "%s, %s, %s, %s" % (handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    logger.debug(arg)
    handler = flightplan.listenerHandler
    arg = "%s, %s, %s, %s" % (handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    logger.debug(arg)
    handler = housekeeping.listenerHandler
    arg = "%s, %s, %s, %s" % (handler.name, handler.pid, handler.is_alive(), handler.exitcode)
    logger.debug(arg)

    # time.sleep(2)
    logger.info("Starting nominal operations ..")

    dispatcher.listenerHandler.start()
    comunications.listenerHandler.start()
    console.listenerHandler.start()
    flightplan.listenerHandler.start()
    housekeeping.listenerHandler.start()

    # time.sleep(2)   # give time for every process to start
    # logger.debug("-------------------------")

    dispatcher.listenerHandler.join()
    comunications.listenerHandler.join()
    console.listenerHandler.join()
    flightplan.listenerHandler.join()
    housekeeping.listenerHandler.join()

    # the systems should never reach this pont, otherwise an error occured

    # handler = dispatcher.listenerHandler
    # arg = "%s, %s, %s, %s" % (handler.cmdName, handler.pid, handler.is_alive(), handler.exitcode)
    # logger.debug(arg)
    # handler = comunications.listenerHandler
    # arg = "%s, %s, %s, %s" % (handler.cmdName, handler.pid, handler.is_alive(), handler.exitcode)
    # logger.debug(arg)
    # handler = console.listenerHandler
    # arg = "%s, %s, %s, %s" % (handler.cmdName, handler.pid, handler.is_alive(), handler.exitcode)
    # logger.debug(arg)
    # handler = flightplan.listenerHandler
    # arg = "%s, %s, %s, %s" % (handler.cmdName, handler.pid, handler.is_alive(), handler.exitcode)
    # logger.debug(arg)
    # handler = housekeeping.listenerHandler
    # arg = "%s, %s, %s, %s" % (handler.cmdName, handler.pid, handler.is_alive(), handler.exitcode)
    # logger.debug(arg)
    #
    # logger.debug("-------------------------")


