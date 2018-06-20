import smbus
import time

PWR_MGMT_1  = 0x6B
SMPLRT_DIV  = 0x19
CONFIG      = 0x1A
GYRO_CONFIG = 0x1B
INT_ENABLE  = 0x38
ACCEL_X     = 0x3B
ACCEL_Y     = 0x3D
ACCEL_Z     = 0x3F
GYRO_X      = 0x43
GYRO_Y      = 0x45
GYRO_Z      = 0x47

class IMU():
    def __init__(self):
        bus = smbus.SMBus(1)
        Device_Address = 0x68
        bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
        bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
        bus.write_byte_data(Device_Address, CONFIG, 0)
        bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
        bus.write_byte_data(Device_Address, INT_ENABLE, 1)

    def read_raw_data(self, regAddr):
        high = bus.read_byte_data(Device_Address, regAddr)
        low = bus.read_byte_data(Device_Address, regAddr+1)
        value = ((high << 8) | low)
        if(value > 32768):
            value = value - 65536
        return value
    def run(self,acc,gyro):
        acc[0] = read_raw_data(ACCEL_X)/16384.0
        acc[1] = read_raw_data(ACCEL_Y)/16384.0
        acc[2] = read_raw_data(ACCEL_Z)/16384.0
        gyro[0] = read_raw_data(GYRO_X)/131.0
        gyro[1] = read_raw_data(GYRO_Y)/131.0
        gyro[2] = read_raw_data(GYRO_Z)/131.0
