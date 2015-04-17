# -*- coding: utf-8 -*-
__author__ = 'toopazo'


# from repos import command
from repos.cmds.cmdcon import CmdEnumCON
from repos.cmds.cmdrtc import CmdEnumRTC
import SUCHAI_config
from core import dispatcherhandler

import multiprocessing
import time
import logging
logger = logging.getLogger(__name__)


def listener_housekeeping():
    arg = "cmdName %s, pid %s, is_alive %s, exitcode %s" %\
          (listenerHandler.name, listenerHandler.pid, listenerHandler.is_alive(), listenerHandler.exitcode)
    logger.debug(arg)

    for i in range(0, 5):
        time.sleep(0.2)

        disp_cmd = dispatcherhandler.DispCmd(cmdid=CmdEnumCON.con_help.value,
                                             cmdparam=i,
                                             taskorigid=SUCHAI_config.ConfigTaskorig.THOUSEKEEPING)
        disp_cmd.send_to_dispatcher()  # blocking by default

        disp_cmd = dispatcherhandler.DispCmd(cmdid=CmdEnumRTC.rtc_get_time_now.value,
                                             cmdparam=i,
                                             taskorigid=SUCHAI_config.ConfigTaskorig.THOUSEKEEPING)
        disp_cmd.send_to_dispatcher()  # blocking by default

    while True:
        pass

listenerHandler = multiprocessing.Process(group=None,
                                          target=listener_housekeeping,
                                          name="listener_housekeeping",
                                          args=(),
                                          kwargs={})