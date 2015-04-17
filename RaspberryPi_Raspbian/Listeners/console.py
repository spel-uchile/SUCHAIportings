# -*- coding: utf-8 -*-
__author__ = 'toopazo'


from repos import command
from core import gnrl_services
from core import dispatcherhandler
import SUCHAI_config

import multiprocessing
import sys
import os
import logging
logger = logging.getLogger(__name__)


def con_cmd_handler():
    """ Search every cmdName inside cmdgroup_j for a match/hit
    if successful returns a DispCmd containing the corresponding command  """

    # line = gnrl_services.console_input("r>>")
    line = gnrl_services.console_input("")
    # gnrluse.console_print(line)
    line = line.split()

    #if no match or another error
    hit_flag = False
    hit_cmd_cmdid = ""
    hit_cmd_cmdparam = ""
    disp_cmd = dispatcherhandler.DispCmd(cmdid=SUCHAI_config.GnrlCmds.CMD_NULL,
                                         cmdparam=0,
                                         taskorigid=SUCHAI_config.ConfigTaskorig.TCONSOLE)

    if len(line) != 2:
        gnrl_services.console_print("Bad syntax: cmdId cmdParam")
        return disp_cmd

    # Without the 0x prefix, you need to specify the base explicitly, otherwise there's no way to tell:
    # int("A12FFE12", 16)
    # With the 0x prefix, Python can distinguish hex and decimal automatically:
    # int("0xA12FFE12")
    try:
        user_cmd_id = int(line[0], 16)    # 0x prefix needed
        user_cmd_param = int(line[1])     # No prefix if Decimal is used
    except ValueError:
        gnrl_services.console_print("ValueError: cmdId cmdParam")
        return disp_cmd

    verbose = False
    gnrl_services.console_print("[listener_console]")
    gnrl_services.console_print("  Searching a match for user input " + str(line) + " ..")
    # gnrl_services.console_print("user_cmd_id = %s" % user_cmd_id)
    # gnrl_services.console_print("user_cmd_param = %s" % user_cmd_param)
    # gnrl_services.console_print("-------------------")
    for j in range(0, command.CmdRepo.get_num_cmdgroups()):
        cmdgroup_j = command.CmdRepo.get_cmdgroup(j)
        if verbose:
            gnrl_services.console_print("    cmdgroup_j.cmdgroupName => %s" % cmdgroup_j.cmdgroupName)
        for i in range(0, cmdgroup_j.get_num_cmds()):
            cmd_i = cmdgroup_j.get_cmd(i)
            cmd_i_cmdid = cmd_i.cmdId
            cmd_i_cmdname = cmd_i.cmdName
            if verbose:
                arg = "      cmdId: 0x%0.4X, cmdName: %s, " % (cmd_i_cmdid, cmd_i_cmdname)
                gnrl_services.console_print(arg)
            if user_cmd_id == cmd_i_cmdid:
                hit_cmd_cmdid = user_cmd_id
                hit_cmd_cmdparam = user_cmd_param
                hit_flag = True
                break
        # reevaluate condition to break again (nested loops)
        if hit_flag:
            break

    #check for a hit
    if hit_flag:
        gnrl_services.console_print("  cmdId \"0x%0.4X\" and cmdParam \"%s\" identified as valid command" %
                                    (hit_cmd_cmdid, hit_cmd_cmdparam))
        disp_cmd = dispatcherhandler.DispCmd(cmdid=hit_cmd_cmdid,
                                             cmdparam=hit_cmd_cmdparam,
                                             taskorigid=SUCHAI_config.ConfigTaskorig.TCONSOLE)
        return disp_cmd
    else:
        gnrl_services.console_print("  \"%s\" was NOT identified as command" % user_cmd_id)
        return disp_cmd


def listener_console(fileno):
    sys.stdin = os.fdopen(fileno)  # open stdin in this process
    verbose = False
    if verbose:
        gnrl_services.console_print("main stdin %s" % sys.stdin)
        gnrl_services.console_print("main stdout %s" % sys.stdout)

    arg = "cmdName %s, pid %s, is_alive %s, exitcode %s" %\
          (listenerHandler.name, listenerHandler.pid, listenerHandler.is_alive(), listenerHandler.exitcode)
    logger.debug(arg)

    while True:
        # time.sleep(0.1)  # give time for short commands ( < 0.1 seg) to execute, before the promt

        # /* Parsing command - return CmdDisp structure*/
        new_disp_cmd = con_cmd_handler()

        # /* cmdId = 0xFFFF means no new command */
        if new_disp_cmd.cmdId != command.CmdRepo.cmdnull.cmdId:
            # /* Print the command code */
            gnrl_services.console_print("  con_cmd_handler spawns command 0x%0.4X %s" %
                                        (new_disp_cmd.cmdId, new_disp_cmd.cmdParam))

            # /* Queue NewCmd - Blocking */
            #send cmd to Dispatcher (blocking call)
            disp_cmd = dispatcherhandler.DispCmd(cmdid=new_disp_cmd.cmdId,
                                                 cmdparam=new_disp_cmd.cmdParam,
                                                 taskorigid=new_disp_cmd.taskorigId)
            disp_cmd.send_to_dispatcher()  # blocking by default
        else:
            gnrl_services.console_print("  con_cmd_handler error. No command was spawn")

fn = sys.stdin.fileno()     # get original file descriptor (should be inside main memory scope)
listenerHandler = multiprocessing.Process(group=None,
                                          target=listener_console,
                                          name="listener_console",
                                          args=(fn,),
                                          kwargs={})