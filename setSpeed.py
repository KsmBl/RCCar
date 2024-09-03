## return values:
#  0:	all fine
#  1:	input out of possible range (1000 - 2000)

def setSpeed(pwm):
	if pwm < 980:
		return 1
	if pwm > 2020:
		return 1

	speed = (pwm - 1000) / 10 # 1000-2000 -> 0-1000 -> 0-100
	print(f"set Motorspeed to {speed}%")
	return 0
