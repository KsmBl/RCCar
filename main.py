#! /usr/bin/python
import sys
sys.path.insert(0, './libary/')

from getInputs import startInputScanner, readMinMax, readInputs # local file # TODO
from setSpeed import setSpeed, setupSpeedMotor # local file
from setSteer import setSteer, setupSteerPin # local file
from log import createLogfile, log # local file
from PIDloop import PIDloop # local file
from alert import alert # local file
import time

def main():
	PIDs = [1, 1, 1]
	PIDresult = 0
	startInputScanner()
	readMinMax()
	setupSteerPin(12)
	setupSpeedMotor(18)

	time.sleep(3)

	try:
		while True:
			Axis = readInputs()

#			#if accelerometer is available
#			PIDresult = PIDloop(PIDs)

			setSteer(Axis[3])
			setSpeed(Axis[2])

	except KeyboardInterrupt:
		sys.exit()

main()
