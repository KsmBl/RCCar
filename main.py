#! /usr/bin/python
import sys
sys.path.insert(0, './libary/')

from getInputs import startInputScanner, readMinMax, readInputs # local file
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

	try:
		while True:
			Axis = readInputs()
			print(Axis)

#			#if accelerometer is available
#			PIDresult = PIDloop(PIDs)

			setSteer(Axis[3])

			# arm FLAG
			if Axis[4] >= 1500:
				setSpeed(Axis[2])
			else:
				setSpeed(1000)

	except KeyboardInterrupt:
		sys.exit()

main()
