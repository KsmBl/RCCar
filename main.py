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
	# start thread that reads the inputs from the SBUS pin
	startInputScanner()

	# read config with calibration values
	readMinMax()

	# prepare the right GPIO pin for the servo motor
	setupSteerPin(12)

	# prepare the right GPIO pin for the brushless motor
	setupSpeedMotor(18)

	# set armed to false, so the car cant start
	armed = False

	# tmpDisarmSpeed is for slowing the brushless motor down instead of stopping it instantly
	tmpDisarmSpeed = 0

	try:
		# all prepare work is done
		print("ready")

		while True:
			# Axis is an Array with all Axis
			Axis = readInputs()

			# the 4. channel is the right stick and the horizontal axis
			setSteer(Axis[3])

			# arm the car when the throttle is down and the arm switch is fliped
			if not armed and Axis[4] >= 1500 and Axis[2] <= 1010:
				armed = True
				print("armed")
			# disarm when switch is fliped to the 0 position
			elif armed and Axis[4] < 1500:
				armed = False
				print("disarmed")

			# spin motor only when car is armed
			if armed:
				# the 3. channel is in my case the left vertical stick
				setSpeed(Axis[2])

				tmpDisarmSpeed = Axis[2]
			else:
				# slow disarming to prevend from damaging the motor
				tmpDisarmSpeed = ((tmpDisarmSpeed - 1000) * 0.7) + 1000

				# stoping the motor instant when the motor spins slow enough
				if tmpDisarmSpeed <= 1050:
					tmpDisarmSpeed = 1000

				setSpeed(tmpDisarmSpeed)

	except KeyboardInterrupt:
		sys.exit()

main()
