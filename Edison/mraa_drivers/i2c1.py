
import mraa
import time


class SensTempSUCHAI():
    ST1_ADDRESS = 0b01001000
    ST2_ADDRESS = 0b01001010
    ST3_ADDRESS = 0b01001100
    ST4_ADDRESS = 0b01001110

    STx_REG_TEMP_READ = 0b00000000
    STx_REG_CONFIG = 0b00000001
    STx_REG_TLOW = 0b00000010
    STx_REG_THIGH = 0b00000011

    @staticmethod
    def is_alive(i2cx, device_address):
        #         76543210
        w_reg = 0b01101000
        SensTempSUCHAI.write_reg(i2cx, device_address, SensTempSUCHAI.STx_REG_CONFIG, w_reg)
        r_reg = SensTempSUCHAI.read_reg(i2cx, device_address, SensTempSUCHAI.STx_REG_CONFIG)
        #         76543210
        r_reg = 0b01111111 & r_reg     #erase and ignore OS/ALERT bit
        if r_reg != w_reg:
            print("is_alive: SensTemp[%d] = FALSE !!\n", device_address)
            return False

        #         76543210
        w_reg = 0b01100000
        SensTempSUCHAI.write_reg(i2cx, device_address, SensTempSUCHAI.STx_REG_CONFIG, w_reg)
        r_reg = SensTempSUCHAI.read_reg(i2cx, device_address, SensTempSUCHAI.STx_REG_CONFIG)
        #         76543210
        r_reg = 0b01111111 & r_reg     #erase and ignore OS/ALERT bit
        if r_reg != w_reg:
            print("is_alive: SensTemp[%d] = FALSE !!\n", device_address)
            return False

        print("is_alive: SensTemp[%d] = TRUE !!\n", device_address)
        return True

    @staticmethod
    def write_reg(i2cx, device_address, register_address, data):
        # DATA = [data]
        # N = 1
        # _address = [device_address, register_address]
        # i2c3_master_fputs(DATA, N, _address, 2)

        i2cx.address(device_address)
        i2cx.writeReg(register_address, data)

    @staticmethod
    def read_reg(i2cx, device_address, register_address):
        # ret = 0
        # address = [device_address, register_address]
        # i2c3_master_fgets(&ret, 1, address, 2)

        i2cx.address(device_address)
        ret = i2cx.readReg(register_address)

        return ret


if __name__ == "__main__":
    print(mraa.getVersion())
    i2c1 = mraa.I2c(1)      # MRAA number 07 <=> i2c1_sda Ediosn
                            # MRAA number 19 <=> i2c1_scl Ediosn
    i2c6 = mraa.I2c(6)

    res = SensTempSUCHAI.is_alive(i2c1, SensTempSUCHAI.ST1_ADDRESS)
    print("SensTempSUCHAI.is_alive(SensTempSUCHAI.ST1_ADDRESS) = %s" % res)

    ind = 0
    while True:
        print("write_reg %s" % ind)
        SensTempSUCHAI.write_reg(i2c1, SensTempSUCHAI.ST1_ADDRESS, SensTempSUCHAI.STx_REG_CONFIG, 0b01100000)
        # SensTempSUCHAI.write_reg(i2c6, SensTempSUCHAI.ST1_ADDRESS, SensTempSUCHAI.STx_REG_CONFIG, 0b01100000)
        # time.sleep(0.3)
        ind += 1