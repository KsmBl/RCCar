def setInputSettings():
	import sys
	sys.path.insert(0, './libary')
	sys.path.insert(0, './libary/ADS1x15')
	import ADS1x15

	ADS = ADS1x15.ADS1015(1, 0x48)
	ADS.setGain(ADS.PGA_6_144V)
	return ADS

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
		axisValues = readInputs(ADS)

	return axisValues

	'''
	i = 0
	while i <= 3: # 3 = 4 channels (0, 1, 2, 3)
		#set value to 0 when its out of tolerance range
		if axisValues[i] < 980:
			axisValues[i] = 0
		elif axisValues[i] > 2020:
			axisValues[i] = 0

		#set value to 0 when its in the tolerance range
		elif axisValues[i] < 1000:
			axisValues[i] = 1000
		elif axisValues[i] > 2000:
			axisValues[i] = 2000


		i += 1
	'''
