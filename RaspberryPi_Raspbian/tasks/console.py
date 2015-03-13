# -*- coding: utf-8 -*-
__author__ = 'toopazo'


import multiprocessing
import time
from repos import command
from core import suchai_types
from core import gnrl_services
from core import shared_resources
import SUCHAI_config
import sys
import os
import logging
logger = logging.getLogger(__name__)


def con_cmd_handler():
    """ Search every cmdName inside cmd_group_xxx for a match/hit
    if successful returns a DispCmd containing the corresponding command  """

    line = gnrl_services.console_input("r>>")
    # gnrluse.console_print(line)
    line = line.split()

    #if no match or another error
    user_cmd_hit = False
    cmd_group_name_hit = ""
    cmd_name_hit = ""
    disp_cmd = suchai_types.DispCmd(cmdid=None,
                                    param=0,
                                    taskorig=suchai_types.TaskOrig.TCONSOLE,
                                    sysreq=None,
                                    groupname="CmdNULL",
                                    cmdname=command.CmdRepo.cmdnull.name)

    if len(line) != 2:
        gnrl_services.console_print("Bad syntax: cmd param")
        return disp_cmd

    user_cmd_name = line[0]
    user_cmd_param = line[1]

    gnrl_services.console_print("-------------------")
    gnrl_services.console_print(line)
    gnrl_services.console_print("user_cmd_name = %s" % user_cmd_name)
    gnrl_services.console_print("user_cmd_param = %s" % user_cmd_param)
    gnrl_services.console_print("-------------------")
    for j in range(0, len(command.CmdRepo.cmd_group_buffer)):
        cmd_group_xxx = command.CmdRepo.cmd_group_buffer[j]
        gnrl_services.console_print("cmd_group_xxx.groupName => %s" % cmd_group_xxx.groupName)
        cmd_i = None
        for i in range(0, command.CmdRepo.get_ncmds(cmd_group_xxx.groupName)):
            cmd_i = command.CmdRepo.get_command_byid(cmd_group_xxx.groupName, i)
            gnrl_services.console_print("cmd_i.name = %s" % cmd_i.name)
            if user_cmd_name == cmd_i.name:
                gnrl_services.console_print(cmd_i.name)
                cmd_group_name_hit = cmd_group_xxx.groupName
                cmd_name_hit = cmd_i.name
                user_cmd_hit = True
                break
        # reevaluate condition to break again (nested loops)
        if user_cmd_name == cmd_i.name:
            break

    #check for a hit
    if user_cmd_hit:
        gnrl_services.console_print("\"%s\" identified as %s with param \"%s\"" %
                              (user_cmd_name, cmd_name_hit, user_cmd_param))
        disp_cmd = suchai_types.DispCmd(cmdid=None,
                                        param=user_cmd_param,
                                        taskorig=suchai_types.TaskOrig.TCONSOLE,
                                        sysreq=None,
                                        groupname=cmd_group_name_hit,
                                        cmdname=cmd_name_hit)
        return disp_cmd
    else:
        gnrl_services.console_print("\"%s\" was NOT identified as command" % user_cmd_name)
        return disp_cmd


def task_console(fileno):
    sys.stdin = os.fdopen(fileno)  # open stdin in this process
    verbose = False
    if verbose:
        gnrl_services.console_print("main stdin %s" % sys.stdin)
        gnrl_services.console_print("main stdout %s" % sys.stdout)

    arg = "name %s, pid %s, is_alive %s, exitcode %s" %\
          (taskHandler.name, taskHandler.pid, taskHandler.is_alive(), taskHandler.exitcode)
    logger.debug(arg)

    while True:
        time.sleep(0.1)  # give time for short commands ( < 0.1 seg) to execute, before the promt

        # /* Parsing command - return CmdDisp structure*/
        new_disp_cmd = con_cmd_handler()

        # /* cmdId = 0xFFFF means no new command */
        if new_disp_cmd.cmdName != command.CmdRepo.cmdnull.name:
            # /* Print the command code */
            gnrl_services.console_print("[Console] con_cmd_handler spawns command %s" % new_disp_cmd.cmdName)

            # /* Queue NewCmd - Blocking */
            #send cmd to Dispatcher (blocking call)
            disp_cmd = suchai_types.DispCmd(cmdid=None,
                                            param=new_disp_cmd.param,
                                            taskorig=taskHandler.name,      # suchai_types.TaskOrig.THOUSEKEEPING,
                                            sysreq=None,                    # filled by Dispatcher
                                            groupname=new_disp_cmd.groupName,
                                            cmdname=new_disp_cmd.cmdName)
            shared_resources.dispatcherQueue.put(disp_cmd)  # blocking by default
        else:
            gnrl_services.console_print("[Console] con_cmd_handler error. No command was spawn")

fn = sys.stdin.fileno()     # get original file descriptor (should be inside main memory scope)
taskHandler = multiprocessing.Process(group=None,
                                      target=task_console,
                                      name="task_console",
                                      args=(fn,),
                                      kwargs={})