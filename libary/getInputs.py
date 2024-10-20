import threading
import time
import json
import sys
import os

SBUS_PIN = 4

globalAxis =	[0, 0, 0, 0,
		 0, 0, 0, 0,
		 0, 0, 0, 0,
		 0, 0, 0, 0]

minValues = []
maxValues = []
readerReady = False

def readMinMax():
	with open("calibrates.txt", 'r') as f:
		data = json.load(f)

	global minValues
	global maxValues

	minValues = data["min"]
	maxValues = data["max"]

	return 0

def startInputScanner(mode = "wait"): # wait = wait for scanner is ready, instant = dont wait for scanner to perform a return
	global globalAxis
	global readerReady
	inputScannerThread = threading.Thread(target=inputScanner)
	inputScannerThread.start()

	while mode == "wait":
		if readerReady:
			return 0
		time.sleep(0.25)

	return 1

def stopInputScanner():
	global inputScannerThread

def inputScanner():
	from readSbus import SbusReader
	global globalAxis
	global readerReady

	reader = SbusReader(SBUS_PIN)
	reader.begin_listen()

	while(not reader.is_connected()):
		print("reader not ready")
		time.sleep(0.25)

	readerReady = True

	#get first valide Input
	time.sleep(0.1)

	try:
		while True:
			globalAxis = reader.translate_latest_packet()

	except:
		reader.end_listen()
		sys.exit()

#should return values between 1000 and 2000
def readInputs(mode = "correct"):
	global globalAxis
	
	if mode == "raw":
		return globalAxis
	elif mode == "correct":
		return correctInputs(globalAxis)
	else:
		print("mode unknown | getInputs.py/readInputs()")

def correctInputs(Axis):
	global minValues
	global maxValues

	#clean Inputs
	for i in range(min(len(minValues), len(maxValues))):
		Axis[i] = max(Axis[i], minValues[i])
		Axis[i] = min(Axis[i], maxValues[i])
		try:
			Axis[i] = int((Axis[i] - minValues[i]) / (maxValues[i] - minValues[i]) * 1000 + 1000)
		except:
			pass


	return Axis
