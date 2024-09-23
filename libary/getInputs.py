import time
import json
import os

##config
ANALOG_0_MIN = 68
ANALOG_0_MAX = 1095
ANALOG_1_MIN = 111
ANALOG_1_MAX = 1093
ANALOG_2_MIN = 3
ANALOG_2_MAX = 1093
DIGITAL_0_MIN = 1566
DIGITAL_0_MAX = 1585

inputErrorTicks = 0
MAX_INPUT_ERROR_TICKS = 3

def setInputSettings():
	import sys
	sys.path.insert(0, './libary')
	sys.path.insert(0, './libary/ADS1x15')
	import ADS1x15

	#Analog-Digital-Settings
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

	global inputErrorTicks

	if axisValues == ['']:
		inputErrorTicks += 1
		if inputErrorTicks >= MAX_INPUT_ERROR_TICKS:
			return "ERROR"
		return ['']
	
	inputErrorTicks -= 1
	if inputErrorTicks < 0:
		inputErrorTicks = 0

	axis0 = int(axisValues[0])
	axis1 = int(axisValues[1])
	axis2 = int(axisValues[2])
	axis3 = int(axisValues[3])

	#clean Inputs
	if axis0 <= ANALOG_0_MIN:
		axis0 = ANALOG_0_MIN
	elif axis0 >= ANALOG_0_MAX:
		axis0 = ANALOG_0_MAX
	axis0 = (axis0 - ANALOG_0_MIN) / (ANALOG_0_MAX - ANALOG_0_MIN) * 1000 + 1000

	if axis1 <= ANALOG_1_MIN:
		axis1 = ANALOG_1_MIN
	elif axis1 >= ANALOG_1_MAX:
		axis1 = ANALOG_1_MAX
	axis1 = (axis1 - ANALOG_1_MIN) / (ANALOG_1_MAX - ANALOG_1_MIN) * 1000 + 1000


	if axis2 <= ANALOG_2_MIN:
		axis2 = ANALOG_2_MIN
	elif axis2 >= ANALOG_2_MAX:
		axis2 = ANALOG_2_MAX
	axis2 = (axis2 - ANALOG_2_MIN) / (ANALOG_2_MAX - ANALOG_2_MIN) * 1000 + 1000

	if axis3 <= DIGITAL_0_MIN:
		axis3 = DIGITAL_0_MIN
	elif axis3 >= DIGITAL_0_MAX:
		axis3 = DIGITAL_0_MAX
	axis3 = (axis3 - DIGITAL_0_MIN) / (DIGITAL_0_MAX - DIGITAL_0_MIN) * 1000 + 1000

	axisValues = [int(axis0), int(axis1), int(axis2), int(axis3)]

	return axisValues

