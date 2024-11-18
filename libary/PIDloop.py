import sys
sys.path.insert(0, './libary/')

from mpu6050 import getGyroData

def PIDloop(PIDs):
	P = PIDs[0]
	I = PIDs[1]
	D = PIDs[2]

	rt = getGyroData()

	xAccel = round(rt[0]['x'] / 9.807, 2)
	yAccel = round(rt[0]['y'] / 9.807, 2)
	zAccel = round(rt[0]['z'] / 9.807, 2)
	temp = rt[2]

	print(zAccel)
	

	### TODO: calculations

	return 0
