#! /usr/bin/python
import sys
sys.path.insert(0, './libary/')

from getInputs import startInputScanner, readMinMax, readInputs # local file
from setSpeed import setSpeed, setupSpeedMotor # local file
from setSteer import setSteer, setupSteerPin # local file
from configReader import getConfig # local file
from log import createLogfile, log # local file
from PIDloop import PIDloop # local file
from alert import alert # local file
import time

config = []

def main():
	global config
	config = getConfig()

	# create a logfile int ./log/
	createLogfile(config['OLB'])

	# start thread that reads the inputs from the SBUS pin
	log("startInputScanner...")
	startInputScanner(config['GSB'])

	# read config with calibration values
	log("readMinMax...")
	readMinMax()

	# prepare the right GPIO pin for the servo motor
	log("setupSteerPin...")
	setupSteerPin(config['GS'], config['OMnP'], config['OMxP'])

	# prepare the right GPIO pin for the brushless motor
	log("setupSpeedMotor...")
	setupSpeedMotor(config['GT'])

	# set armed to false, so the car cant start
	armed = False

	# tmpDisarmSpeed is for slowing the brushless motor down instead of stopping it instantly
	tmpDisarmSpeed = 0

	# counter for stuff that runs only every fifths time
	fivecount = 0

	mode = 1

	try:
		# all prepare work is done
		log("ready")
		print("ready")

		while True:
			# Axis is an Array with all Axis
			Axis = readInputs()

			# run every fifths time
			if fivecount >= 5:
				# check for mode mode
				if config['M1']['Mn'] <= Axis[config['CM']] <= config['M1']['Mx']:
					# switch mode
					if not mode == 1:
						mode = 1
						log(f"switched to mode {mode}")
						print(f"switched to mode {mode}")
				elif config['M2']['Mn'] <= Axis[config['CM']] <= config['M2']['Mx']:
					# switch mode
					if not mode == 2:
						mode = 2
						log(f"switched to mode {mode}")
						print(f"switched to mode {mode}")
				elif config['M3']['Mn'] <= Axis[config['CM']] <= config['M3']['Mx']:
					# switch mode
					if not mode == 3:
						mode = 3
						log(f"switched to mode {mode}")
						print(f"switched to mode {mode}")

				fivecount = 1
			else:
				fivecount += 1

			log(f"setSteer {Axis[config['CS']]}")
			setSteer(Axis[config['CS']])
			PIDloop([0, 0, 0])

			# arm the car when the throttle is down and the arm switch is fliped
			if not armed and config['CAMn'] <= Axis[config['CA']] <= config['CAMx'] and Axis[config['CT']] <= config['OMT']:
				armed = True
				log("armed")
				print("armed")
			# disarm when switch is fliped to the 0 position
			elif armed and Axis[config['CA']] <= config['CAMn']:
				armed = False
				log("disarmed")
				print("disarmed")

			# spin motor only when car is armed
			if armed:
				speed = ((Axis[config['CT']] - 1000) * config[f"M{mode}"]['S']) + 1000
				setSpeed(speed)
				tmpDisarmSpeed = speed

				log(f"setSpeed {tmpDisarmSpeed}")
				print(tmpDisarmSpeed)
			else:
				# slow disarming to prevend from damaging the motor
				tmpDisarmSpeed = ((tmpDisarmSpeed - 1000) * 0.7) + 1000

				# stoping the motor instant when the motor spins slow enough
				if tmpDisarmSpeed <= 1050:
					tmpDisarmSpeed = 1000
				log(f"setSpeed 0")

				setSpeed(tmpDisarmSpeed)

	except KeyboardInterrupt:
		sys.exit()

main()
