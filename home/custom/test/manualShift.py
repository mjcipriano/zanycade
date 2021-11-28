#!/usr/bin/python

import pigpio
import time

# One of the following MUST be called before using IO functions:

dataPin = 10
clockPin = 11
latchPin = 8

pi = pigpio.pi()

timeDelay = 0.1

time.sleep(timeDelay)

pi.set_mode(dataPin, pigpio.OUTPUT)
pi.set_mode(clockPin, pigpio.OUTPUT)
pi.set_mode(latchPin, pigpio.OUTPUT)

pi.write(latchPin, 0)
time.sleep(timeDelay)


pi.write(dataPin, 1)
pi.write(clockPin, 1)
pi.write(latchPin, 1)
exit

for x in range(8):
	pi.write(dataPin, 1)
	pi.write(clockPin, 1)
	time.sleep(timeDelay)
	pi.write(clockPin,0)
	time.sleep(timeDelay)

pi.write(latchPin, 1)
time.sleep(timeDelay)
pi.write(latchPin, 0)
time.sleep(timeDelay)
