#! /usr/bin/python

from getInputs import getInputs # local file
from setSpeed import setSpeed # local file
from setSteer import setSteer # local file
from PIDloop import PIDloop # local file
from alert import alert # local file
import time

def main():
	PIDs = [1, 1, 1]
	PIDresult = 0
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

		time.sleep(0.2)

main()
