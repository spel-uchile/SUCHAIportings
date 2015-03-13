# -*- coding: utf-8 -*-
__author__ = 'toopazo'


from enum import Enum, unique
from repos import command
from core import suchai_types
from core import gnrl_services
import datetime
import SUCHAI_config
from drivers import camera
import logging
logger = logging.getLogger(__name__)

@unique
class CmdEnumCAM(Enum):
    cam_debug = 0
    cam_take_photo = 1

    @staticmethod
    def get_index(var):
        if hasattr(var, "value"):
            return var.value
        else:
            return -1

    @staticmethod
    def get_string(var):
        if hasattr(var, "name"):
            return var.name
        else:
            return -1


class CmdGroupCAM(command.CmdGroup):
    groupName = SUCHAI_config.SCH_GNM_CAM
    groupId = SUCHAI_config.SCH_GID_CAM
    cmdEnum = CmdEnumCAM

    def __init__(self):
        command.CmdGroup.__init__(self)
        self.groupName = CmdGroupCAM.groupName
        self.groupId = CmdGroupCAM.groupId

    #@staticmethod
    def on_reset(self):
        # create a cmd for every enum and then append it to CmdCAM.cmdBuffer
        cmd_i = command.Cmd(name=CmdEnumCAM.cam_debug.name,
                            sysreq=suchai_types.SysReqs.SYSREQ_MIN,
                            funct=CmdFunctCAM.cam_debug)
        self.cmdBuffer.append(cmd_i)

        cmd_i = command.Cmd(name=CmdEnumCAM.cam_take_photo.name,
                            sysreq=suchai_types.SysReqs.SYSREQ_MIN,
                            funct=CmdFunctCAM.take_photo)
        self.cmdBuffer.append(cmd_i)

        verbose = False
        if verbose:
            for i in range(0, len(CmdEnumCAM)):
                arg = "self.cmdBuffer[%s] => %s" % (i, self.cmdBuffer[i])
                logger.debug(arg)
                arg = "self.cmdBuffer[%s].name => %s" % (i, self.cmdBuffer[i].name)
                logger.debug(arg)

        if len(CmdEnumCAM) != self.get_ncmds():
            arg = "wrong implementation"
            logger.critical(arg)
            raise NotImplemented


class CmdFunctCAM():
    @staticmethod
    def take_photo(param):
        name = str(datetime.datetime.now())
        gnrl_services.console_print("name %s" % name)
        camera.RaspiCamIf.init()
        camera.RaspiCamIf.take_picture(SUCHAI_config.SCH_DATA_FOLDER + name)
        camera.RaspiCamIf.stop()
        gnrl_services.console_print("done")
        return True

    @staticmethod
    def cam_debug(param):
        return False

