#import RPi.GPIO as GPIO
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import time

servo = None

def setupSteerPin(PIN):
	global servo
	factory = PiGPIOFactory()
	servo = Servo(PIN, min_pulse_width=0.0005, max_pulse_width=0.0025, pin_factory=factory)

def setSteer(pwm):
	global servo

	angle = (pwm - 1500) / 500
	servo.value = angle

	return 0
