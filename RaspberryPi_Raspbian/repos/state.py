#!/usr/bin/Python
# -*- coding: utf-8 -*-
__author__ = 'toopazo'

from enum import Enum, unique


@unique
class StateVariable(Enum):
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


if __name__ == "__main__":
    print("testing StateVariable enum class ..")
    print("StateVariable.AntSwitch_isOpen => ", StateVariable.AntSwitch_isOpen)
    print("StateVariable.AntSwitch_isOpen.name => ", StateVariable.AntSwitch_isOpen.name)
    print("StateVariable.AntSwitch_isOpen.value => ", StateVariable.AntSwitch_isOpen.value)
    print("StateVariable(5) => ", StateVariable(5))
    print("list(StateVariable) => ", list(StateVariable))
    print("len(StateVariable) => ", len(StateVariable))
    for i in range(0, len(StateVariable)):
        print("StateVariable(%s) => %s" % (i, StateVariable(i)))

    # print(StateVariable(0))
    # print(StateVariable(1))
    # print(StateVariable(73))