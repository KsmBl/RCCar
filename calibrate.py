import sys
sys.path.insert(0, './libary')

from getInputs import startInputScanner, readInputs # local file
from log import createLogfile, log # local file
from configReader import getConfig # local file
import time
import json

# enable 6 channel for the car
CHANNEL_COUNT = 6

# run calibrated script for 10 seconds
CALIBRATE_TIME = 10 # seconds

def main():
	config = getConfig()
	# start a new thread that reads the inputs
	startInputScanner(config['GSB'])

	Axis = []
	# read the raw inputs without calibration
	Axis = readInputs("raw")

	minAxis =	[0, 0, 0, 0,
			 0, 0, 0, 0,
			 0, 0, 0, 0,
			 0, 0, 0, 0]

	maxAxis =	[0, 0, 0, 0,
			 0, 0, 0, 0,
			 0, 0, 0, 0,
			 0, 0, 0, 0]

	minAxis = Axis

	try:
		# counter for the calibration
		timeGone = 0
		print("")
		print("")
		print("")
		print("")
		print("")

		while True:
			# read the raw inputs without calibration
			Axis = readInputs("raw")

			time.sleep(0.1)
			timeGone += 0.1 # time.sleep value

			# set minAxis and maxAxis to the highes and lowest reached values
			for i in range(CHANNEL_COUNT):
				minAxis[i] = min(minAxis[i], Axis[i])
				maxAxis[i] = max(maxAxis[i], Axis[i])

			print("\033[5A")
			print(f"value: {Axis[:CHANNEL_COUNT]}")
			print(f"min:   {minAxis[:CHANNEL_COUNT]}")
			print(f"max:   {maxAxis[:CHANNEL_COUNT]}")
			print("+++++++++")

			# stop script when time is gone
			if timeGone >= CALIBRATE_TIME:
				break
	except KeyboardInterrupt:
		pass

	print(f"min:   {minAxis[:CHANNEL_COUNT]}")
	print(f"max:   {maxAxis[:CHANNEL_COUNT]}")

	# write calibration values in a file
	combined_data = {
		"min": minAxis,
		"max": maxAxis
	}
	with open("calibrates.txt", 'w') as f:
		json.dump(combined_data, f)

	print("CTRL + C to exit script")

	return 0

main()
