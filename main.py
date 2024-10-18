#! /usr/bin/python
import sys
sys.path.insert(0, './libary/')

from getInputs import * # local file # TODO
from log import createLogfile, log # local file
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
		# TODO
		#print(f"Channel1:  {Axis[0]}")
		#print(f"Channel2:  {Axis[1]}")
		#print(f"Channel3:  {Axis[2]}")
		#print(f"Channel4:  {Axis[3]}")
		#print(f"Channel5:  {Axis[3]}")
		#print(f"Channel6:  {Axis[3]}")
		#print(f"Channel7:  {Axis[3]}")
		#print(f"Channel8:  {Axis[3]}")
		#print("___________________")

#		#if accelerometer is available
#		PIDresult = PIDloop(PIDs)

		time.sleep(0.02)

main()
