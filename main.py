#! /usr/bin/python
import sys
sys.path.insert(0, './libary/')

from getInputs import startInputScanner, readMinMax, readInputs # local file # TODO
from log import createLogfile, log # local file
from setSpeed import setSpeed # local file
from setSteer import setSteer, setupSteerPin # local file
from PIDloop import PIDloop # local file
from alert import alert # local file
import time

BAR_LEN = 30
CHANNEL_COUNT = 6

def main():
	PIDs = [1, 1, 1]
	PIDresult = 0
	startInputScanner()
	readMinMax()
	setupSteerPin(12)

	time.sleep(3)

	print("")
	print("")
	print("")
	print("")
	print("")

	try:
		while True:
			Axis = []
			Axis = readInputs()
			try:
				print("\033[A\033[A\033[A\033[A\033[A\033[A\033[A")
				for i in range(CHANNEL_COUNT):
					ACTIVE_BAR = int((Axis[i] - 1000) * (BAR_LEN / 1000))
					INACTIVE_BAR = BAR_LEN - ACTIVE_BAR
					_ACTIVE_BAR = ACTIVE_BAR * "#"
					_INACTIVE_BAR = INACTIVE_BAR * " "
					print(f"Channel{i + 1}:  {Axis[i]:04} | [{_ACTIVE_BAR}{_INACTIVE_BAR}]")
			except:
				print("ERROR")

#			#if accelerometer is available
#			PIDresult = PIDloop(PIDs)

#			setSteer(Axis[3])

			time.sleep(0.04)
	except KeyboardInterrupt:
		sys.exit()

main()
