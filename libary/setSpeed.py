## return values:
#  0:	all fine
#  1:	input out of possible range (1000 - 2000)

import pigpio

MOTOR = 0
PI = None

# prepare right GPIO pin for a pwm signal that controlls a ESC
def setupSpeedMotor(PIN):
	global MOTOR
	global PI

	MOTOR = PIN

	PI = pigpio.pi()

# set the motorspeed to a value between 1000us and 2000us
def setSpeed(pwm):
	global MOTOR
	global PI

	PI.set_servo_pulsewidth(MOTOR, pwm)
	return 0
