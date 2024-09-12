import sys
sys.path.insert(0, './libary')
sys.path.insert(0, './libary/ADS1x15')
import ADS1x15

def setInputs():
	ADS = ADS1x15.ADS1015(1, 0x48)
	ADS.setGain(ADS.PGA_6_144V)
	f = ADS.toVoltage()
	return [ADS, f]

def readInputs(ADS):
	axis0 = ADS.readADC(0)
	axis1 = ADS.readADC(1)
	axis2 = ADS.readADC(2)
	axis3 = ADS.readADC(3)
	print(axis0)
	return [axis0, axis1, axis2, axis3]

def getInputs(ADS, t=0, tv=[0, 0, 0, 0]):
	return readInputs(ADS)
