import sys
sys.path.insert(0, './libary')

from getInputs import startInputScanner, readInputs # local file
from log import createLogfile, log # local file
import time
import json

CHANNEL_COUNT = 6
CALIBRATE_TIME = 10 # seconds

def main():
	startInputScanner()

	Axis = []
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
		timeGone = 0
		print("")
		print("")
		print("")
		print("")
		print("")

		while True:
			Axis = readInputs("raw")

			time.sleep(0.1)
			timeGone += 0.1 # time.sleep value

			for i in range(CHANNEL_COUNT):
				minAxis[i] = min(minAxis[i], Axis[i])
				maxAxis[i] = max(maxAxis[i], Axis[i])

			print("\033[5A")
			print(f"value: {Axis[:CHANNEL_COUNT]}")
			print(f"min:   {minAxis[:CHANNEL_COUNT]}")
			print(f"max:   {maxAxis[:CHANNEL_COUNT]}")
			print("+++++++++")

			if timeGone >= CALIBRATE_TIME:
				break
	except KeyboardInterrupt:
		pass

	print(f"min:   {minAxis[:CHANNEL_COUNT]}")
	print(f"max:   {maxAxis[:CHANNEL_COUNT]}")

	combined_data = {
		"min": minAxis,
		"max": maxAxis
	}

	with open("calibrates.txt", 'w') as f:
		json.dump(combined_data, f)

	return 0

main()
