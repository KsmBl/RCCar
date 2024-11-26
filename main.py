#! /usr/bin/python
import sys
sys.path.insert(0, './libary/')

# imports
from getInputs import startInputScanner, readMinMax, readInputs # local file
from hcsr04 import startDistanceScanner, getDistance # local file
from setSpeed import setSpeed, setupSpeedMotor # local file
from setSteer import setSteer, setupSteerPin # local file
from configReader import getConfig # local file
from log import createLogfile, log # local file
from PIDloop import PIDloop # local file
from alert import alert # local file
import time

# drive mode
mode = 1

# car started / stopped
armed = False

# var for slowing the motor down
tmpDisarmSpeed = 0

config = []

# changed when driven too close too walls and Distancecheck is in config.ini for used Mode activated
speedLimit = 0
speedMulti = 1

def main():
	# prepare everything
	setupPi()

	#for running code every fifths time
	fivecount = 0

	global config
	global armed
	global mode

	distance = 0

	try:
		# all prepare work is done
		log("ready")
		print("ready")


		while True:
			# Axis is an Array with all Axis
			Axis = readInputs()

			# read distance to front
			distance = getDistance()

			# run every fifths time
			if fivecount >= 5:
				checkModeSwitcher(Axis)
				fivecount = 1
			else:
				fivecount += 1

			log(f"setSteer {Axis[config['CS']]}")
			setSteer(Axis[config['CS']])

			armDisarm(Axis)
			controllSpeed(Axis, distance)

	except KeyboardInterrupt:
		sys.exit()

def setupPi():
	global config
	config = getConfig()

	# create a logfile in ./log/
	createLogfile(config['OLB'])

	# start thread that reads the inputs from the SBUS pin
	log("startInputScanner...")
	startInputScanner(config['GSB'])

	# start thread that reads the distance to the front
	log("startDistanceScanner...")
	startDistanceScanner(config['GDT'], config['GDE'])

	# read config with calibration values
	log("readMinMax...")
	readMinMax()

	# prepare the right GPIO pin for the servo motor
	log("setupSteerPin...")
	setupSteerPin(config['GS'], config['OMnP'], config['OMxP'])

	# prepare the right GPIO pin for the brushless motor
	log("setupSpeedMotor...")
	setupSpeedMotor(config['GT'])

def checkModeSwitcher(Axis):
	global config
	global mode
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

def armDisarm(Axis):
	global config
	global armed

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

def controllSpeed(Axis, distance):
	global tmpDisarmSpeed
	global config
	global armed
	global mode
	global speedLimit
	global speedMulti

	if armed:
		speed = ((Axis[config['CT']] - 1000) * config[f"M{mode}"]['S']) + 1000

		if config[f"M{mode}"]['D'] == 1:
			# TODO if to close, limit throttle
			if distance <= 30: # cm
				speedMulti = (distance * 3) / 100

			if distance <= 5:
				speedLimit = 3
			elif distance <= 15:
				speedLimit = 2
			elif distance <= 30:
				speedLimit = 1
			else:
				# prevent disabling speedLimit when the sensor is too close to a wall and returns ~804
				if distance >= 30 and speedLimit == 3:
					pass
				else:
					speedLimit = 0
				
			speed = ((speed - 1000) * speedMulti) + 1000

		setSpeed(speed)
		tmpDisarmSpeed = speed

		log(f"setSpeed {tmpDisarmSpeed}")
		print(tmpDisarmSpeed)
		print(speedLimit)
		print(speedMulti)
		print(distance)
		print("--------")
	else:
		# slow disarming to prevend from damaging the motor
		tmpDisarmSpeed = ((tmpDisarmSpeed - 1000) * 0.7) + 1000

		# stoping the motor instant when the motor spins slow enough
		if tmpDisarmSpeed <= 1050:
			tmpDisarmSpeed = 1000

		log(f"setSpeed {tmpDisarmSpeed}")

		setSpeed(tmpDisarmSpeed)

main()
