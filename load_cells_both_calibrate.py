import sys
import time
from lib.DFRobot_HX711_I2C import *

IIC_MODE         = 0x01           # default use IIC1
IIC_ADDRESS_1    = 0x64           # device 1 address
IIC_ADDRESS_2    = 0x65           # device 2 address

loadcell1 = DFRobot_HX711_I2C(IIC_MODE, IIC_ADDRESS_1)
loadcell2 = DFRobot_HX711_I2C(IIC_MODE, IIC_ADDRESS_2)

# Set the trigger threshold (G) for automatic calibration of the weight sensor module. When only the weight of the object on the scale is greater than this value, the module will start the calibration process
# This value cannot be greater than the calibration weight of the set_cal_weight() setting
loadcell1.set_threshold(20)
loadcell2.set_threshold(20)
# Set the calibration weight when the weight sensor module is automatically calibrated (g)
loadcell1.set_cal_weight(54)
loadcell2.set_cal_weight(54)

loadcell1.enable_cal()
loadcell2.enable_cal()

cond = 0
while (cond < 2): 
  time.sleep(1)
  cond = cond + int(loadcell1.get_cal_flag()) + int(loadcell2.get_cal_flag())

print("")
print("The calibration value of the sensors are: ")
# Obtain the calibration value. The accurate calibration value can be obtained after the calibration operation is completed
calibration1 = loadcell1.get_calibration()
calibration2 = loadcell2.get_calibration()

print("1: ", hex(IIC_ADDRESS_1), "", calibration1[0])
print("2: ", hex(IIC_ADDRESS_2), "", calibration2[0])

print("")
time.sleep(0.1)

#2525 2084
#2023 2557
#2270 2340