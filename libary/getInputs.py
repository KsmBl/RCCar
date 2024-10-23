import threading
import time
import json
import sys
import os

# set Pin for SBUS receiver to GPIO pin 4
SBUS_PIN = 4

globalAxis =	[0, 0, 0, 0,
		 0, 0, 0, 0,
		 0, 0, 0, 0,
		 0, 0, 0, 0]

# initialize minValues and maxValues for calculate the calibration
minValues = []
maxValues = []

# global variable that says if the sbus reader gets data (only switches from False to True, never back to False!)
readerReady = False

# read calibrate values that are created by calibrate.py
def readMinMax():
	with open("calibrates.txt", 'r') as f:
		data = json.load(f)

	# get global variables
	global minValues
	global maxValues

	# overwrite global variables
	minValues = data["min"]
	maxValues = data["max"]

	return 0

# start a new thread that reads data from the SBUS_PIN GPIO pin
def startInputScanner(mode = "wait"): # wait = wait for scanner is ready, instant = dont wait for scanner to perform a return
	# get global variables
	global globalAxis
	global readerReady

	# start thread
	inputScannerThread = threading.Thread(target=inputScanner)
	inputScannerThread.start()

	while mode == "wait":
		# wait until inputScannerThread says, it gets inputs
		if readerReady:
			return 0
		time.sleep(0.25)

	return 1

# start sbus_reader libary und returns values from it
def inputScanner():
	from readSbus import SbusReader

	# get global variables
	global globalAxis
	global readerReady

	# start reader
	reader = SbusReader(SBUS_PIN)
	reader.begin_listen()

	# check if its connected
	while(not reader.is_connected()):
		print("reader not ready")
		time.sleep(0.25)

	# input reader gets data
	readerReady = True

	#get first valide Input
	time.sleep(0.1)

	try:
		# set globalAxis to the newest data received by the SBUS reader
		while True:
			globalAxis = reader.translate_latest_packet()

	except:
		reader.end_listen()
		sys.exit()

# return values from controller
def readInputs(mode = "correct"):
	# get global variable
	global globalAxis

	# return raw inputs (for calibrate.py)
	if mode == "raw":
		return globalAxis
	elif mode == "correct":
		# correct the inputs with the values that are writte in calibrates.txt by calibrate.py
		return correctInputs(globalAxis)
	else:
		# mode unknown
		print("mode unknown | getInputs.py/readInputs()")

# correct the inputs to values between 1000 and 2000
def correctInputs(Axis):
	# get global variables
	global minValues
	global maxValues

	#clean Inputs
	for i in range(min(len(minValues), len(maxValues))):
		# set value to the minimum / maximum when its lower / higher that the values that was read by calibrate.py
		Axis[i] = max(Axis[i], minValues[i])
		Axis[i] = min(Axis[i], maxValues[i])

		try:
			# scale the value from minValues[i] - maxValues[i] to 1000-2000 (min: 150; max: 450; inputValue: 300; result: 1500)
			Axis[i] = int((Axis[i] - minValues[i]) / (maxValues[i] - minValues[i]) * 1000 + 1000)
		except:
			pass


	return Axis
