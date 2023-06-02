import sys
import time
from lib.DFRobot_HX711_I2C import *

IIC_MODE         = 0x01           # default use IIC1
IIC_ADDRESS      = 0x64            # default iic device address
'''
   # The first  parameter is to select iic0 or iic1
   # The second parameter is the iic device address
'''
hx711 = DFRobot_HX711_I2C(IIC_MODE, IIC_ADDRESS)
hx711.begin()

print("the calibration value of the sensor is: ")
# Obtain the calibration value. The accurate calibration value can be obtained after the calibration operation is completed
calibration = hx711.get_calibration()
print(calibration[0])
time.sleep(0.1)