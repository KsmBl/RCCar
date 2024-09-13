#! /usr/bin/python
import sys
sys.path.insert(0, './libary')
sys.path.insert(0, './libary/ADS1x15')
sys.dont_write_bytecode = True ##TODO: remove before prod

from getInputs import setInputSettings, getInputs, startInputScanner # local file
from setSpeed import setSpeed # local file
from setSteer import setSteer # local file
from PIDloop import PIDloop # local file
from alert import alert # local file
import ADS1x15
import time

def main():
	PIDs = [1, 1, 1]
	PIDresult = 0
	inputErrorTicks = 0
	maxInputErrorTicks = 3

	#Analog-Digital-Converter-Settings
	ADSettings = setInputSettings()
	startInputScanner(ADSettings)
	time.sleep(0.5) #get first inputs

	while True:
		Axis = []
		Axis = getInputs(ADSettings)
		if not Axis == ['']:
			inputErrorTicks -= 1
			if inputErrorTicks < 0:
				inputErrorTicks = 0

			print(f"Analog0: {Axis[0]}")
			print(f"Analog1: {Axis[1]}")
			print(f"Analog2: {Axis[2]}")
			print(f"Analog3: {Axis[3]}")
			print("___________________")
		else:
			inputErrorTicks += 1
			if inputErrorTicks >= maxInputErrorTicks:
				#update Motors
				print("too much Errors in Inputs")


#		rt = setSpeed(Axis[0])
#		if rt:
#			print(rt)
#			alert(8)

#		rt = setSteer(Axis[1], PIDresult)
#		if rt:
#			print(rt)
#			alert(10)

		#if accelerometer is available
#		PIDresult = PIDloop(PIDs)


		time.sleep(0.05)

main()
