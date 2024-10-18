import time
import json
import os

##config
ANALOG_0_MIN = 0
ANALOG_0_MAX = 0
DIGITAL_0_MIN = 0
DIGITAL_0_MAX = 0
ANALOG_2_MIN = 0
ANALOG_2_MAX = 0
DIGITAL_1_MIN = 0
DIGITAL_1_MAX = 0

#def _startInputScanner(ADS):
#	# TODO

#should return values between 1000 and 2000
#def readInputs(ADS):
#	# TODO
#	return [axis0, axis1, axis2, axis3]

def getInputs():
#	axis0 = int(axisValues[0])
#	axis1 = int(axisValues[1])
#	axis2 = int(axisValues[2])
#	axis3 = int(axisValues[3])

	#clean Inputs
#	if axis0 <= ANALOG_0_MIN:
#		axis0 = ANALOG_0_MIN
#	elif axis0 >= ANALOG_0_MAX:
#		axis0 = ANALOG_0_MAX
#	axis0 = (axis0 - ANALOG_0_MIN) / (ANALOG_0_MAX - ANALOG_0_MIN) * 1000 + 1000

#	if axis1 <= DIGITAL_0_MIN:
#		axis1 = DIGITAL_0_MIN
#	elif axis1 >= DIGITAL_0_MAX:
#		axis1 = DIGITAL_0_MAX
#	axis1 = (axis1 - DIGITAL_0_MIN) / (DIGITAL_0_MAX - DIGITAL_0_MIN) * 1000 + 1000


#	if axis2 <= ANALOG_2_MIN:
#		axis2 = ANALOG_2_MIN
#	elif axis2 >= ANALOG_2_MAX:
#		axis2 = ANALOG_2_MAX
#	axis2 = (axis2 - ANALOG_2_MIN) / (ANALOG_2_MAX - ANALOG_2_MIN) * 1000 + 1000

#	if axis3 <= DIGITAL_1_MIN:
#		axis3 = DIGITAL_1_MIN
#	elif axis3 >= DIGITAL_0_MAX:
#		axis3 = DIGITAL_0_MAX
#	axis3 = (axis3 - DIGITAL_1_MIN) / (DIGITAL_0_MAX - DIGITAL_1_MIN) * 1000 + 1000
#	axisValues = [int(axis0), int(axis1), int(axis2), int(axis3)]

#	return axisValues
	return 0
