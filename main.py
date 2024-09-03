#! /usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

#import ELRS lib

def main():
	while (True):
		setMotorSpeed(1500) #ELRS Axis 1
		setSteer(1600) #ELRS Axis 3
		if GPIO.input(8) == GPIO.HIGH:
			print("Button was pushed!")

def setMotorSpeed(speed):
	pwm = speed - 1000
	print(f"Set Motor PWM to {pwm}") #set PWM

def setSteer(angle):
	print(f"Set Steer angle to {angle}") #set PWM

main()
