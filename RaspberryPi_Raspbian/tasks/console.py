#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'


import multiprocessing
import time
from repos import command
from repos.cmds import cmdconsole
from repos.cmds import cmdrtc
from core import gnrluse
from core import shared_resources
import SUCHAI_config
import sys
import os
import logging
logger = logging.getLogger(__name__)


def con_cmd_handler():
    line = gnrluse.console_input("r>>")
    # gnrluse.console_print(line)
    line = line.split()
    gnrluse.console_print(line)

    #if no match or another error
    cmd_user_hit = False
    cmd_group_hit = ""
    cmd_name_hit = ""
    disp_cmd = gnrluse.DispCmd(cmdid=None,
                               param=0,
                               taskorig=gnrluse.TaskOrig.TCONSOLE,
                               sysreq=None,
                               groupname="CmdNULL",
                               cmdname=command.CmdRepo.cmdnull.name)

    if len(line) != 2:
        gnrluse.console_print("Bad syntax: cmd param")
        return disp_cmd

    cmd_user = line[0]
    arg_user = line[1]

    #CmdGroupCON
    cmd_group_undercheck = cmdconsole.CmdGroupCON
    cmd_name_undercheck = cmd_group_undercheck.cmdEnum.help
    if cmd_user == cmd_name_undercheck.name:
        cmd_group_hit = cmd_group_undercheck.groupName
        cmd_name_hit = cmd_name_undercheck
        cmd_user_hit = True

    for i in range(0, command.CmdRepo.get_ncmds(cmd_group_undercheck.groupName)):
        arg = "get_function_byid(%s, %s) => %s" % (cmd_group_undercheck.groupName, i,
                                                   command.CmdRepo.get_function_byid(cmd_group_undercheck.groupName, i))
        gnrluse.console_print(arg)
        cmd_i = command.CmdRepo.get_command_byid(cmd_group_undercheck.groupName, i)
        gnrluse.console_print(cmd_i)
        if cmd_user == cmd_i.name:
            gnrluse.console_print(cmd_name_undercheck)
            cmd_group_hit = cmd_group_undercheck.groupName
            cmd_name_hit = cmd_name_undercheck
            cmd_user_hit = True

    #CmdGroupRTC
    cmd_group_undercheck = cmdrtc.CmdGroupRTC
    cmd_name_undercheck = cmd_group_undercheck.cmdEnum.get_time_now
    if cmd_user == cmd_name_undercheck.name:
        cmd_group_hit = cmd_group_undercheck.groupName
        cmd_name_hit = cmd_name_undercheck
        cmd_user_hit = True

    #no match
    if cmd_user_hit:
        gnrluse.console_print("%s identified as %s with param %s" %
                              (cmd_user, cmd_name_hit, arg_user))
        disp_cmd = gnrluse.DispCmd(cmdid=None,
                                   param=arg_user,
                                   taskorig=gnrluse.TaskOrig.TCONSOLE,
                                   sysreq=None,
                                   groupname=cmd_group_hit,
                                   cmdname=cmd_name_hit)
        return disp_cmd
    else:
        gnrluse.console_print("%s was NOT identified as command" % cmd_user)
        return disp_cmd


def task_console(fileno):
    sys.stdin = os.fdopen(fileno)  # open stdin in this process
    gnrluse.console_print("task_console stdin %s" % sys.stdin)
    gnrluse.console_print("task_console stdout %s" % sys.stdout)

    arg = "name %s, pid %s, is_alive %s, exitcode %s" %\
          (taskHandler.name, taskHandler.pid, taskHandler.is_alive(), taskHandler.exitcode)
    logger.debug(arg)

    while True:
        # //vTaskDelayUntil(&xLastWakeTime, Delayms);
        time.sleep(0.1)

        # /* Parsing command - return CmdDisp structure*/
        new_disp_cmd = con_cmd_handler()

        # /* cmdId = 0xFFFF means no new command */
        if new_disp_cmd.cmdName != command.CmdRepo.cmdnull.name:
            # /* Print the command code */
            gnrluse.console_print("[Console] Se genera comando %s \r\n" % new_disp_cmd.cmdName)

            # /* Queue NewCmd - Blocking */
            #send cmd to Dispatcher (blocking call)
            disp_cmd = gnrluse.DispCmd(cmdid=None,   # replaced by groupName and cmdName (cmdId = groupName + cmdName)
                                       param=new_disp_cmd.param,
                                       taskorig=gnrluse.TaskOrig.THOUSEKEEPING,
                                       sysreq=None,   # filled by Dispatcher
                                       groupname=new_disp_cmd.groupName,
                                       cmdname=new_disp_cmd.cmdName)
            shared_resources.dispatcherQueue.put(disp_cmd)  # blocking by default
        else:
            gnrluse.console_print("[Console] NO Se genera comando %s \r\n" % new_disp_cmd.cmdName)

fn = sys.stdin.fileno()     # get original file descriptor (should be inside main memory scope)
taskHandler = multiprocessing.Process(group=None,
                                      target=task_console,
                                      name="task_console",
                                      args=(fn,),
                                      kwargs={})