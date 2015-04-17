#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'


import multiprocessing
import SUCHAI_config


class ExeCmd():
    # /**
    #  * Structure that represents a command passed to executer. Contains a pointer of
    #  * type cmdgroupCmdBuffer with the function to execute and one parameter for that
    #  * function
    #  */
    # typedef struct exec_command{
    #     int cmdParam;                  ///< Command parameter
    #     cmdgroupCmdBuffer fnct;           ///< Command function
    # }ExeCmd;
    cmdParam = None
    cmdFunction = None


class DispCmd():
    dispatcherQueue = multiprocessing.Queue(maxsize=1)  # xQueueCreate(25, sizeof(DispCmd))
    if SUCHAI_config.SCH_TASKEXECUTER_INSIDE_TASKDISPATCHER == 1:
        # no Queue creation
        pass
    else:
        executerCmdQueue = multiprocessing.Queue(maxsize=1)    # xQueueCreate(1,sizeof(ExeCmd));
        executerStatQueue = multiprocessing.Queue(maxsize=1)    # xQueueCreate(1,sizeof(int));
    #TODO modified by toopazo to ease porting
    priorityEmulatorSem = multiprocessing.Lock()  # xSemaphoreCreateMutex();

    # /**
    #  * Structure that represent a command passed to dispatcher. Contains only a code
    #  * that represent the function to call, a paremeter and other command's metadata
    #  */
    # typedef struct ctrl_command{
    #     int cmdId;                  ///< Command id, represent the desired command
    #     int cmdParam;                  ///< Command parameter
    #     int idOrig;                 ///< Metadata: Id of sender subsystem
    #     int cmdSysReq;                 ///< Metadata: Level of energy the command requires
    # }DispCmd;
    def __init__(self, cmdid, cmdparam, taskorigid):  # , sysreq):
        self.cmdId = cmdid
        self.cmdParam = cmdparam
        self.taskorigId = taskorigid

    def send_to_dispatcher(self):
        # Only one task can send cmds to dispatcher, the others block until the command is done. If there is enough
        # IDLE time the mutex will be equally/fairly accessed by all Listeners
        # This is equivalent to a OS that guarantees "Fixed priority pre-emptive scheduling"
        # with Listeners given a lower priority relative to the dispatcher task
        DispCmd.priorityEmulatorSem.acquire()
        # gnrl_services.console_print("priorityEmulatorSem was acquired by %s" % disp_cmd.taskorigId)
        DispCmd.dispatcherQueue.put(self)

    @staticmethod
    def receive_from_listeners():
        return DispCmd.dispatcherQueue.get()

    @staticmethod
    def release_priority_emulator_sem():
        DispCmd.priorityEmulatorSem.release()