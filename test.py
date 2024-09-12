import sys
sys.path.insert(0, './libary')
sys.path.insert(0, './libary/ADS1x15')

from getInputs import getInputs, readInputs # local file
from setSpeed import setSpeed # local file
from setSteer import setSteer # local file
from PIDloop import PIDloop # local file
from alert import alert # local file

def main():
	rtvalue = 0

	### set Steer ###
	rt = setSteer(2500, 0)
	if rt == 0:
		print(f"setSteer(2500, 0) ERROR! [{rt}]. Error code 1 expected")
		rtvalue = 1

	rt = setSteer(1500, 0)
	if not rt == 0:
		print(f"setSteer(1500, 0) ERROR! [{rt}]. No Error code expected")
		rtvalue = 1

	rt = setSteer(500, 0)
	if rt == 0:
		print(f"setSteer(500, 0) ERROR! [{rt}]. Error code 1 expected")
		rtvalue = 1

	# PID overflow #
	rt = setSteer(1999, 50)
	if not rt == 0:
		print(f"setSteer(1999, 50) ERROR! [{rt}]. No Error code expected")
		rtvalue = 1

	rt = setSteer(1000, -50)
	if not rt == 0:
		print(f"setSteer(1000, -50) ERROR! [{rt}]. No Error code expected")
		rtvalue = 1

	### set Speed ###
	rt = setSpeed(2500)
	if rt == 0:
		print(f"setSpeed(2500) ERROR! [{rt}]. Error code 1 expected")
		rtvalue = 1

	rt = setSpeed(1500)
	if not rt == 0:
		print(f"setSpeed(1500) ERROR! [{rt}]. No Error code expected")
		rtvalue = 1

	rt = setSpeed(500)
	if rt == 0:
		print(f"setSpeed(500) ERROR! [{rt}]. Error code 1 expected")
		rtvalue = 1

	### get Inputs ###
	rt = getInputs(None, [1500, 900, 999, 2100])
	#valid Input
	if rt[0] > 2020:
		print(f"one value from getInput() is higher than 2020: {rt[0]}")
		rtvalue = 1
	elif rt[0] < 980:
		print(f"one value from getInput() is lower than 980: {rt[0]}")
		rtvalue = 1

	#too low input
	if not rt[1] == 0:
		print(f"{rt[1]} value received. Errorcode 0 is expected")
		rtvalue = 1

	#low input
	if not rt[2] == 1000:
		print(f"{rt[2]} received. 1000 expected")
		rtvalue = 1

	#too high input
	if not rt[3] == 0:
		print(f"{rt[3]} received. Errorcode 0 is expected")
		rtvalue = 1

	return rtvalue

exit(main())
