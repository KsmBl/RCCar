#import RPi.GPIO as GPIO
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import time

# thats the variable for the GPIO pin where the Motor is connected to
servo = None

# setup and prepare the right GPIO pin
def setupSteerPin(PIN, minPulseWidth, maxPulseWidth):
	global servo
	factory = PiGPIOFactory()

	# setup pin with min and max duty cicle
	servo = Servo(PIN, min_pulse_width=minPulseWidth, max_pulse_width=maxPulseWidth, pin_factory=factory)

# turn motor to a position between -1 and 1
def setSteer(pwm):
	global servo

	angle = (pwm - 1500) / 500
	servo.value = angle

	return 0
