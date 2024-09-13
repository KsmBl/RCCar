import time
import json
import os

def setInputSettings():
	import sys
	sys.path.insert(0, './libary')
	sys.path.insert(0, './libary/ADS1x15')
	import ADS1x15

	ADS = ADS1x15.ADS1015(1, 0x48)
	ADS.setGain(ADS.PGA_6_144V)
	return ADS

def startInputScanner(ADS):
	pid = os.fork()
	if pid == 0:
		_startInputScanner(ADS)
	else:
		return

def _startInputScanner(ADS):
	ticklengthAverage = 8
	timer = 0 #0 ticks
	Axis = {}
	while True:
		newAxis = readInputs(ADS)
		Axis[timer] = newAxis
		if timer - ticklengthAverage in Axis:
			del Axis[timer - ticklengthAverage]

		timer += 1

		#calculate average of last 20 ticks
		averageAxis0 = 0
		averageAxis1 = 0
		averageAxis2 = 0
		averageAxis3 = 0

		for i in Axis:
			averageAxis0 += Axis[i][0]
			averageAxis1 += Axis[i][1]
			averageAxis2 += Axis[i][2]
			averageAxis3 += Axis[i][3]

		averageAxis0 = averageAxis0 / ticklengthAverage
		averageAxis1 = averageAxis1 / ticklengthAverage
		averageAxis2 = averageAxis2 / ticklengthAverage
		averageAxis3 = averageAxis3 / ticklengthAverage

		allAverageAxis = [int(averageAxis0), int(averageAxis1), int(averageAxis2), int(averageAxis3)]

		with open('Axis.txt', 'w') as fp:
			json.dump(allAverageAxis, fp)

#should return values between 1000 and 2000
def readInputs(ADS):
	import sys
	sys.path.insert(0, './libary')
	sys.path.insert(0, './libary/ADS1x15')
	import ADS1x15

	axis0 = ADS.readADC(0)
	axis1 = ADS.readADC(1)
	axis2 = ADS.readADC(2)
	axis3 = ADS.readADC(3)
	return [axis0, axis1, axis2, axis3]

def getInputs(ADS, axisValues = False):
	if not axisValues:
		with open('Axis.txt', 'r') as fp:
			content = fp.read()
		
		cleaned_content = content.strip('[]')
		axisValues = [(item) for item in cleaned_content.split(',')]

		return axisValues
	else:
		return axisValues

