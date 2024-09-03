from getInputs import getInputs # local file
from setSpeed import setSpeed # local file
from setSteer import setSteer # local file
from PIDloop import PIDloop # local file
from alert import alert # local file

### set Steer ###
rt = setSteer(2500, 0)
if rt == 0:
	print(f"setSteer(2500, 0) ERROR! [{rt}]. Error code 1 expected")

rt = setSteer(1500, 0)
if not rt == 0:
	print(f"setSteer(1500, 0) ERROR! [{rt}]. No Error code expected")

rt = setSteer(500, 0)
if rt == 0:
	print(f"setSteer(500, 0) ERROR! [{rt}]. Error code 1 expected")

# PID overflow #
rt = setSteer(1999, 50)
if not rt == 0:
	print(f"setSteer(1999, 50) ERROR! [{rt}]. No Error code expected")

rt = setSteer(1000, -50)
if not rt == 0:
	print(f"setSteer(1000, -50) ERROR! [{rt}]. No Error code expected")

### set Speed ###
rt = setSpeed(2500)
if rt == 0:
	print(f"setSpeed(2500) ERROR! [{rt}]. Error code 1 expected")

rt = setSpeed(1500)
if not rt == 0:
	print(f"setSpeed(1500) ERROR! [{rt}]. No Error code expected")

rt = setSpeed(500)
if rt == 0:
	print(f"setSpeed(500) ERROR! [{rt}]. Error code 1 expected")

### get Inputs ###
rt = getInputs()

for i in rt:
	if i > 2010:
		print(f"one value from getInput() is higher than 2010: {i}")
	elif i < 980:
		print(f"one value from getInput() is lower than 980: {i}")
