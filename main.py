#! /usr/bin/python
import time

import sys
sys.path.insert(0, './libary')
sys.path.insert(0, './libary/ADS1x15')
sys.dont_write_bytecode = True ##TODO: remove before prod

from getInputs import setInputSettings, getInputs, startInputScanner # local file
from setSpeed import setSpeed # local file
from setSteer import setSteer # local file
from PIDloop import PIDloop # local file
from alert import alert # local file
from log import createLogfile, log # local file
import ADS1x15

def main():
	PIDs = [1, 1, 1]
	PIDresult = 0

	#Analog-Digital-Converter-Settings
	ADSettings = setInputSettings()
	startInputScanner(ADSettings)
	time.sleep(0.5) #get first inputs

	while True:
		Axis = []
		Axis = getInputs(ADSettings)
		if Axis == ['']:
			#dont update anything
			pass
			#print("missing inputs")
		elif Axis == "ERROR":
			#print("too much missing packages from getInputs()")
			return
		else:
			print(f"Analog0:  {Axis[0]}")
			print(f"Analog1:  {Axis[1]}")
			print(f"Analog2:  {Axis[2]}")
			print(f"Digital0: {Axis[3]}")
			print("___________________")

#			rt = setSpeed(Axis[2])
#			if rt:
#				print(rt)

#		#if accelerometer is available
#		PIDresult = PIDloop(PIDs)

		time.sleep(0.05)

main()
