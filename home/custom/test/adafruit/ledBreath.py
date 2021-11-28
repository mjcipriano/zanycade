#!/usr/bin/python

from board import SCL, SDA
import busio
import time
# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685

# Create the I2C bus interface.
i2c_bus = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c_bus)

maxValue = 65535
stepSize =512 
delayTime = 0.001

# Set the PWM frequency to 60hz.
pca.frequency = 60

# Set the PWM duty cycle for channel zero to 50%. duty_cycle is 16 bits to match other PWM objects
# but the PCA9685 will only actually give 12 bits of resolution.
for b in range(0,maxValue,stepSize):
    for x in range(16):
        pca.channels[x].duty_cycle = b
    time.sleep(delayTime)

for b in range(maxValue,0,-stepSize):
    for x in range(16):
        pca.channels[x].duty_cycle = b
    time.sleep(delayTime)


