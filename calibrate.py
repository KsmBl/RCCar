import sys
import time
sys.path.insert(0, './libary')
sys.path.insert(0, './libary/ADS1x15')

from getInputs import setInputSettings, getInputs, startInputScanner # local file
from log import createLogfile, log # local file
import ADS1x15 # local file

def main():
	#Analog-Digital-Converter-Settings
	ADSettings = setInputSettings()
	startInputScanner(ADSettings)
	time.sleep(0.5) #get first inputs

	Axis = []
	Axis = getInputs(ADSettings, False, "raw")

	minAxis = [Axis[0], Axis[1], Axis[2], Axis[3]]
	maxAxis = [Axis[0], Axis[1], Axis[2], Axis[3]]

	try:
		while True:
			Axis = []
			Axis = getInputs(ADSettings, False, "raw")

			time.sleep(0.05)

			i = 0

			while i <= 3:
				if not Axis == [''] and not Axis == "ERROR":
					if int(Axis[i]) < int(minAxis[i]):
						minAxis[i] = int(Axis[i])
					if int(Axis[i]) > int(maxAxis[i]):
						maxAxis[i] = int(Axis[i])

				i += 1

			print(f"value: {Axis}")
			print(f"min:   {minAxis}")
			print(f"max:   {maxAxis}")
			print("+++++++++")
	except KeyboardInterrupt:
		pass

	# read raw inputs
	# write max and min to file

main()
