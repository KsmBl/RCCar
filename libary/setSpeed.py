## return values:
#  0:	all fine
#  1:	input out of possible range (1000 - 2000)

import pigpio

MOTOR = 0
PI = None

def setupSpeedMotor(PIN):
	global MOTOR
	global PI

	MOTOR = PIN

	PI = pigpio.pi()

def setSpeed(pwm):
	global MOTOR
	global PI

	PI.set_servo_pulsewidth(MOTOR, pwm)
	return 0
