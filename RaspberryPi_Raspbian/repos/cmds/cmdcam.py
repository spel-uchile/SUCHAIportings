# -*- coding: utf-8 -*-
__author__ = 'toopazo'


from repos import command
from core import gnrl_services
import SUCHAI_config
from drivers import camera

from enum import Enum, unique
import datetime
import logging
logger = logging.getLogger(__name__)

@unique
class CmdEnumCAM(Enum):
    cam_debug = SUCHAI_config.ConfigCmdgroup.SCH_GID_CAM + 0
    cam_take_photo = SUCHAI_config.ConfigCmdgroup.SCH_GID_CAM + 1

    @staticmethod
    def get_index(var):
        if hasattr(var, "value"):
            return var.value
        else:
            return -1

    @staticmethod
    def get_string(var):
        if hasattr(var, "cmdName"):
            return var.name
        else:
            return -1


class CmdgroupCAM(command.Cmdgroup):
    cmdgroupName = SUCHAI_config.ConfigCmdgroup.SCH_GNM_CAM
    cmdgroupId = SUCHAI_config.ConfigCmdgroup.SCH_GID_CAM
    cmdEnum = CmdEnumCAM

    def __init__(self):
        command.Cmdgroup.__init__(self)
        self.cmdgroupName = CmdgroupCAM.cmdgroupName
        self.cmdgroupId = CmdgroupCAM.cmdgroupId

    #@staticmethod
    def on_reset(self):
        # Append every command STRICTLY following order

        cmd_i = command.Cmd(cmdid=CmdEnumCAM.cam_debug.value,
                            name=CmdEnumCAM.cam_debug.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctCAM.cam_debug)
        self.cmdgroupCmdBuffer.append(cmd_i)
        # cmd_i_num = int(CmdEnumCAM.cam_debug.value & int('00001111', 2))
        # gnrl_services.console_print("cmd_i_num %s" % cmd_i_num)
        # self.cmdgroupCmdBuffer.insert(cmd_i_num, cmd_i)

        cmd_i = command.Cmd(cmdid=CmdEnumCAM.cam_take_photo.value,
                            name=CmdEnumCAM.cam_take_photo.name,
                            sysreq=SUCHAI_config.Sysreqs.SYSREQ_MIN,
                            funct=CmdFunctCAM.take_photo)
        self.cmdgroupCmdBuffer.append(cmd_i)
        # cmd_i_num = int(CmdEnumCAM.cam_take_photo.value & int('00001111', 2))
        # gnrl_services.console_print("cmd_i_num %s" % cmd_i_num)
        # self.cmdgroupCmdBuffer.insert(cmd_i_num, cmd_i)

        # gnrl_services.console_print("len(CmdEnumCAM) %s, self.get_num_cmds() %s " %
        #                             (len(CmdEnumCAM), self.get_num_cmds()))

        if len(CmdEnumCAM) != self.get_num_cmds():
            arg = "wrong implementation"
            logger.critical(arg)
            raise NotImplemented


class CmdFunctCAM():
    @staticmethod
    def take_photo(param):
        name = str(datetime.datetime.now())
        gnrl_services.console_print("cmdName %s" % name)
        camera.RaspiCamIf.init()
        camera.RaspiCamIf.take_picture(SUCHAI_config.SCH_DATA_FOLDER + name)
        camera.RaspiCamIf.stop()
        gnrl_services.console_print("done")
        return True

    @staticmethod
    def cam_debug(param):
        return False

