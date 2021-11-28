#!/usr/bin/python
import sys
import os
import logging
from board import SCL, SDA
import busio
import time
# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685


# Default Values

maxValue = 65535
stepSize =1024 
delayTime = 0.001
numLEDs = 16
waveDelay = 0.05
breathDelay = 0.001

#waveArray = [6,[3,1],[2,0],[4,5],14,[11,9],[10,8],[12,13]]
waveArray = [6,[3,1],[2,0],[4,5],14,[11,9],[10,8],[12,13], [12,13], [10,8], [11,9], 14, [4,5], [2,0], [3,1], 6]


def setLED(ledNum, value=maxValue):
    pca.channels[ledNum].duty_cycle = value

def clearLED(ledNum):
    setLED(ledNum,0)

def clearAllLED():
    for x in range(numLEDs):
        clearLED(x)

def setAllLED(value=maxValue):
    for x in range(numLEDs):
        setLED(x,value)

def breathAll(numTimes):
    for a in range(numTimes):
        for b in range(0,maxValue,stepSize):
            setAllLED(b)
            time.sleep(breathDelay)
        # Now off   
        for b in range(maxValue,0,-stepSize):
            setAllLED(b)
            time.sleep(breathDelay)

def breathOn(ledNum):
    if (isinstance(ledNum, int)) :
        for b in range(0,maxValue,stepSize):
            setLED(ledNum, b)
            time.sleep(breathDelay)
    else :
        for b in range(0,maxValue,stepSize):
            for thisLED in ledNum:
                setLED(thisLED, b)
            time.sleep(breathDelay)

def breathOff(ledNum):
    if (isinstance(ledNum, int)) :
        for b in range(maxValue,0,-stepSize):
            setLED(ledNum, b)
            time.sleep(breathDelay)
    else :
        for b in range(maxValue,0,-stepSize):
            for thisLED in ledNum:
                setLED(thisLED, b)
            time.sleep(breathDelay)



def wave():
    for outLED in waveArray:
        if (isinstance(outLED, int)) :
           clearAllLED()
           #print (outLED)
           setLED(outLED)
           time.sleep(waveDelay)
        else :
            for inLED in outLED :
                if(isinstance(inLED, int)):
                    #print (inLED)
                    setLED(inLED)
            time.sleep(waveDelay)
            clearAllLED()

def waveBreath():
    for outLED in waveArray:
        if (isinstance(outLED, int)) :
           #print (outLED)
           breathOn(outLED)
           time.sleep(waveDelay)
           breathOff(outLED)
        else :
            breathOn(outLED)
            time.sleep(waveDelay)
            breathOff(outLED)




total = len(sys.argv)
cmdargs = str(sys.argv)

logging.basicConfig(filename='/home/pi/custom/setLED.log', format='%(levelname)s:%(message)s',  level=logging.DEBUG)

logging.info ("The total numbers of args passed to the script: %d " % total)
logging.info("Args list: %s " % cmdargs)


# Create the I2C bus interface.
i2c_bus = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c_bus)

# Set the PWM frequency to 60hz.
pca.frequency = 60

clearAllLED()

breathOn(1)
breathOn(2)
breathOn([3,4])
breathOn([5,6])
breathOff([1,2,3,4])

breathAll(2)
clearAllLED()
waveBreath()
waveBreath()
wave()
wave()
clearAllLED()
breathOn(range(0,16))

