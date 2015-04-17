#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'

from core import shared_resources # for access to deployment.statusRepositorySem
from core import gnrl_services
from repos import data
from enum import Enum, unique
import logging
logger = logging.getLogger(__name__)


@unique
class StateVar(Enum):
    # // Bus Hw status (connected trough the PC/104 to the OBC -PIC24-)
    RTC_isAlive = 0
    TRX_isAlive = 1
    EPS_isAlive = 2
    MemEEPROM_isAlive = 3
    MemSD_isAlive = 4
    AntSwitch_isOpen = 5

    # // Payload Hw status (connected trough the PC/104 to the OBC -PIC24-)
    pay_lagmuirProbe_isAlive = 6
    pay_sensTemp_isAlive = 7
    pay_gps_isAlive = 8
    pay_expFis_isAlive = 9
    pay_camera_isAlive = 10
    pay_gyro_isAlive = 11
    pay_tmEstado_isAlive = 12
    pay_battery_isAlive = 13
    pay_debug_isAlive = 14
    pay_lagmuirProbe_isDeployed = 15

    # //FLIGHT PLAN => (C&DH subsystem)
    fpl_index = 16            # // Indice del flight plan que sera editado

    # //PPC => (C&DH subsystem)
    ppc_opMode = 17
    ppc_lastResetSource = 18
    ppc_hoursAlive = 19
    ppc_hoursWithoutReset = 20
    ppc_resetCounter = 21
    ppc_wdt = 22				# // 1=WDT Active =  0=WDT Inactive
    ppc_osc = 23				# // holds Current Oscillator
    ppc_MB_nOE_USB_nINT_stat = 24
    ppc_MB_nOE_MHX_stat = 25
    ppc_MB_nON_MHX_stat = 26
    ppc_MB_nON_SD_stat = 27

    # //DEP => (C&DH subsystem)
    dep_ant_deployed = 28            # // 1=already deployed =  0=not deployed yet
    dep_ant_tries = 29               # // Number of tries to deploy antenna
    dep_year = 30
    dep_month = 31
    dep_week_day = 32
    dep_day_number = 33
    dep_hours = 34
    dep_minutes = 35
    dep_seconds = 36

    # //RTC => (C&DH subsystem)
    rtc_year = 37
    rtc_month = 38
    rtc_week_day = 39
    rtc_day_number = 40
    rtc_hours = 41
    rtc_minutes = 42
    rtc_seconds = 43

    # //EPS => (Energy subsystem)
    eps_bat0_voltage = 44
    eps_bat0_current = 45
    eps_bus5V_current = 46
    eps_bus3V_current = 47
    eps_bus_battery_current = 48
    eps_bat0_temp = 49
    eps_panel_pwr = 50
    eps_status = 51
    eps_soc = 52
    eps_socss = 53
    eps_state_flag = 54
    eps_charging = 55

    # /* Revisar de aqui hacia abajo si aun son necesarios !!! */

    # //TRX => (Communication subsystem)
    trx_opmode = 56           # // Operation mode
    trx_count_tm = 57         # // number of sended TM
    trx_count_tc = 58        # // number of received TC
    trx_day_last_tc = 59      # // day of the last received tc (since 1/1/00)
    trx_beacon_period = 60    # // Beacon period in seconds
    trx_beacon_bat_lvl = 61   # // Batery voltage required to transmit beacon
    trx_rx_baud = 62          # // RX baudrate
    trx_tx_baud = 63          # // TX baudrate

    # //PAYLOAD
    pay_lagmuirProbe_state = 64
    pay_sensTemp_state = 65
    pay_gps_state = 66
    pay_expFis_state = 67
    pay_camera_state = 68
    pay_gyro_state = 69
    pay_tmEstado_state = 70
    pay_battery_state = 71
    pay_debug_state = 72

    # //*************
    # stateVar_last_one = 73    # //Elemento sin sentido =  solo se utiliza para marcar el largo del arreglo

    @staticmethod
    def get_index(state_var):
        if hasattr(state_var, "value"):
            return state_var.value
        else:
            return -1

    @staticmethod
    def get_string(state_var):
        if hasattr(state_var, "cmdName"):
            return state_var.name
        else:
            return -1

    # int sta_get_stateVar(STA_StateVar indxVar);
    @staticmethod
    def get_value(state_var):
        shared_resources.statusRepositorySem.acquire()

        if state_var == StateVar.RTC_isAlive:
            value = 1
        elif state_var == StateVar.AntSwitch_isOpen:
            value = 2
        elif state_var == StateVar.eps_soc:
            value = 2
        elif state_var == StateVar.ppc_resetCounter:
            value = data.PersistenMem.read_state_var(StateVar.ppc_resetCounter.name)
        else:
            value = -1
            arg = "get_value(%s) does NOT exists" % state_var
            logger.error(arg)

        shared_resources.statusRepositorySem.release()
        return value

    # void sta_onReset_stateRepo(void);
    @staticmethod
    def on_reset():
        gnrl_services.console_print("      [on_reset]")
        gnrl_services.console_print("        Updating state vars ..")

        #--------------------
        # ppc_resetCounter
        # read
        val = data.PersistenMem.read_state_var(StateVar.ppc_resetCounter.name)
        # write new val
        val = int(val)
        val += 1
        data.PersistenMem.write_state_var(StateVar.ppc_resetCounter.name, val)
        #check
        val = data.PersistenMem.read_state_var(StateVar.ppc_resetCounter.name)
        if val == 1:
            gnrl_services.console_print("          First time on, ppc_resetCounter = %s" % val)
        else:
            gnrl_services.console_print("          ppc_resetCounter = %s" % val)
        #--------------------
        # state_var_x
        #--------------------
        # state_var_y
        #--------------------

        verbose = False
        if verbose:
            for j in range(0, len(StateVar)):
                arg = "          %s(%s) => %s" % (StateVar.__name__, j, StateVar(j))
                gnrl_services.console_print(arg)
                logger.debug(arg)


if __name__ == "__main__":
    pass
    # # print("testing StateVar enum class ..")
    # # print("StateVar.AntSwitch_isOpen => ", StateVar.AntSwitch_isOpen)
    # # print("StateVar.AntSwitch_isOpen.cmdgroupName => ", StateVar.AntSwitch_isOpen.cmdgroupName)
    # # print("StateVar.AntSwitch_isOpen.value => ", StateVar.AntSwitch_isOpen.value)
    # # print("StateVar(5) => ", StateVar(5))
    #
    # for i in range(0, len(StateVar)):
    #     print("StateVar(%s) => %s" % (i, StateVar(i)))
    # print()
    #
    # print("list(StateVar) => ", list(StateVar))
    # print("len(StateVar) => ", len(StateVar))
    # print("hasattr(StateVar, pay_debug_state) =>", hasattr(StateVar, "pay_debug_state"))
    # print("getattr(StateVar, pay_debug_state) =>", getattr(StateVar, "pay_debug_state"))
    # print("dir(StateVar) =>", dir(StateVar.AntSwitch_isOpen))
    # print("dir(StateVar.get_value) =>", dir(StateVar.get_value))
    # print()
    #
    # print("StateVar.get_string(StateVar.AntSwitch_isOpen) =>", StateVar.get_string(StateVar.AntSwitch_isOpen))
    # print("StateVar.get_index(StateVar.AntSwitch_isOpen) =>", StateVar.get_index(StateVar.AntSwitch_isOpen))
    # print("StateVar.get_value(StateVar.AntSwitch_isOpen) =>", StateVar.get_value(StateVar.AntSwitch_isOpen))
    # print()
    #
    # # print(StateVar(0))
    # # print(StateVar(1))
    # # print(StateVar(73))