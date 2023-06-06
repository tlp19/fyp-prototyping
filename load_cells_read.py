import sys
import time
from lib.DFRobot_HX711_I2C import *

IIC_MODE         = 0x01            # default use IIC1
IIC_ADDRESS      = 0x64        # default i2c device address
'''
   # The first  parameter is to select iic0 or iic1
   # The second parameter is the iic device address
'''

# Initialize the hx711 object
hx711 = DFRobot_HX711_I2C(IIC_MODE ,IIC_ADDRESS)
hx711.begin()

print("start\r\n")

# Manually set the calibration values
hx711.set_calibration(2395.5)  # 2236, 2127, 2260.1, 2395.5
# Tare the sensor
hx711.peel();

while(1):
  # Get the weight of the object
  data = hx711.read_weight(10)
  weight = - data
  print('weight is %.1f g' % weight)
  time.sleep(2)