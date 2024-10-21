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
	armed = False
	tmpDisarmSpeed = 0

	try:
		print("ready")
		while True:
			Axis = readInputs()

#			#if accelerometer is available
#			PIDresult = PIDloop(PIDs)

			setSteer(Axis[3])

			# arm FLAG
			if not armed and Axis[4] >= 1500 and Axis[2] <= 1010:
				armed = True
				print("armed")
			elif armed and Axis[4] < 1500:
				armed = False
				print("disarmed")

			if armed:
				setSpeed(Axis[2])
				tmpDisarmSpeed = Axis[2]
			else:
				# slow disarming to prevend from damaging the motor
				tmpDisarmSpeed = ((tmpDisarmSpeed - 1000) * 0.7) + 1000

				if tmpDisarmSpeed <= 1050:
					tmpDisarmSpeed = 1000

				setSpeed(tmpDisarmSpeed)

	except KeyboardInterrupt:
		sys.exit()

main()
