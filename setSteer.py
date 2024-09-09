## return values:
#  0:	all fine
#  1:	input out of possible range (1000 - 2000)

def setSteer(pwm, PID = 0):
	if not type(PID) == int:
		PID = 0

	# test if pwm signal is in valid range of ELRS axis
	if pwm < 980 or pwm > 2020:
		return 1

	angle = PID + (pwm - 1500) / 5 # 1000-2000 -> -500-500 -> -100-100

	#set angle to valid range
	if angle < -100:
		angle = -100
	elif angle > 100:
		angle = 100

	print(f"set Steerangle to {angle}%")
	return 0
