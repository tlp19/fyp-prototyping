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

# Set the trigger threshold (G) for automatic calibration of the weight sensor module. When only the weight of the object on the scale is greater than this value, the module will start the calibration process
# This value cannot be greater than the calibration weight of the set_cal_weight() setting
hx711.set_threshold(10)
# Set the calibration weight when the weight sensor module is automatically calibrated (g)
hx711.set_cal_weight(53)

hx711.enable_cal()
while hx711.get_cal_flag() != True: 
  time.sleep(1)

print("the calibration value of the sensor is: ")
# Obtain the calibration value. The accurate calibration value can be obtained after the calibration operation is completed
calibration = hx711.get_calibration()
print(calibration[0])
time.sleep(0.1)