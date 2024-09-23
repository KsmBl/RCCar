## return values:
#  0:	all fine
#  1:	input out of possible range (1000 - 2000)

def setSpeed(pwm):
	from gpiozero import PWMOutputDevice
	import time

	if pwm < 980:
		return 1
	if pwm > 2020:
		return 1

	speed = (pwm - 1000) / 1000 # 1000-2000 -> 0-1000 -> 0-1

	PIN = 18

	# Initialize PWM device with 50Hz frequency
	motor = PWMOutputDevice(PIN, frequency=50)

	motor.value = speed
	print(speed)

	return 0
