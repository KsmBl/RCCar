#! /usr/bin/python
import sys
sys.path.insert(0, './libary')
sys.path.insert(0, './libary/ADS1x15')
sys.dont_write_bytecode = True ##TODO: remove before prod

from getInputs import getInputs # local file
from setSpeed import setSpeed # local file
from setSteer import setSteer # local file
from PIDloop import PIDloop # local file
from alert import alert # local file
import ADS1x15
import time

def main():
	PIDs = [1, 1, 1]
	PIDresult = 0

	ADS = ADS1x15.ADS1015(1, 0x48)
	ADS.setGain(ADS.PGA_6_144V)
	f = ADS.toVoltage()

	while True:
		Axis = []
		Axis = getInputs()

		rt = setSpeed(Axis[0])
		if rt:
			print(rt)
			alert(8)

		rt = setSteer(Axis[1], PIDresult)
		if rt:
			print(rt)
			alert(10)

		#if accelerometer is available
		PIDresult = PIDloop(PIDs)


		val_0 = ADS.readADC(0)
		val_1 = ADS.readADC(1)

		print("Analog0: {0:d}\t{1:.3f} V".format(val_0, val_0 * f))
		print("Analog1: {0:d}\t{1:.3f} V".format(val_1, val_1 * f))

		time.sleep(0.2)

main()
