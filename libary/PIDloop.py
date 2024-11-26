import sys
sys.path.insert(0, './libary/')

#from mpu6050 import getGyroData

def PIDloop(PIDs):
	P = PIDs[0]
	I = PIDs[1]
	D = PIDs[2]

#	gd = getGyroData()

#	xAccel = round(gd[0]['x'] / 9.807, 2)
#	yAccel = round(gd[0]['y'] / 9.807, 2)
#	zAccel = round(gd[0]['z'] / 9.807, 2)
#	temp = gd[2]

	#print(zAccel)

	### TODO: calculations

	# if steer == 0
		# if -0.2g <= accelX <= 0.2g
			# steer to -accelX * 10

	return 0
