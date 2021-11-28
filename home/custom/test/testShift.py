#!/usr/bin/python

import wiringpi
import time

# One of the following MUST be called before using IO functions:
wiringpi.wiringPiSetup()      # For sequential pin numbering

dataPin = 12
clockPin = 14
latchPin = 10

for x in range(8):
	wiringpi.shiftOut(12,14,10,255);
	wiringpi.shiftOut(12,14,10,255);
	time.sleep(0.2)
	wiringpi.shiftOut(12,14,10,0);
	wiringpi.shiftOut(12,14,10,0);
	time.sleep(0.2)

LEDout = 1;

for x in range(8):
	wiringpi.shiftOut(12,14,10,LEDout);
	LEDout = LEDout << 1;
	time.sleep(0.5);
	print format(LEDout, "08b");

