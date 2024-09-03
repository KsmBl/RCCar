#! /usr/bin/python

#import ELRS lib
#import PWM lib

def main():
	while (True):
		setMotorSpeed(1500) #ELRS Axis 1
		setSteer(1600) #ELRS Axis 3

def setMotorSpeed(speed):
	print(f"Set Motor Speed to {speed}") #set PWM

def setSteer(angle):
	print(f"Set Steer angle to {angle}") #set PWM

main()
