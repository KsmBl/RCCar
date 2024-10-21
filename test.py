import sys
sys.path.insert(0, './libary/')

# from getInputs import getInputs, readInputs # local file
from setSpeed import setSpeed # local file
from setSteer import setupSteerPin, setSteer # local file
from PIDloop import PIDloop # local file
from alert import alert # local file
from time import sleep


def main():
	error = 0
	mode = ""
	try:
		mode = sys.argv[1]
	except:
		pass
	
	if not mode == "":
		a = input("do you have GPIO pins? [y/n]")
		if a in ["Y", "y", "Yes", "yes", "J", "j", "Ja", "ja"]:
			SERVO_PIN = int(input("on which GPIO Pin is your servo motor connected to?"))
			print(f"Your servo motor is connected to GPIO {SERVO_PIN}")
			error += testSteering(SERVO_PIN)

			MOTOR_PIN = int(input("on which GPIO Pin is your motor connected to? (for acceleration)"))
			print(f"Your motor is connected to GPIO {MOTOR_PIN}")
			input("press enter when you tires dont touch the ground!")
			error += testAccelerate(MOTOR_PIN)

		else:
			print("Motor tests skiped")
			print("alert tests skiped")
	else:
		SERVO_PIN = int(input("on which GPIO Pin is your servo motor connected to?"))
		print(f"Your servo motor is connected to GPIO {SERVO_PIN}")
		error += testSteering(SERVO_PIN)

		MOTOR_PIN = int(input("on which GPIO Pin is your motor connected to? (for acceleration)"))
		print(f"Your motor is connected to GPIO {MOTOR_PIN}")
		input("press enter when you tires dont touch the ground!")
		error += testAccelerate(MOTOR_PIN)
		
	### PID overflow ### # TODO

	### alert ### # TODO

	### getInputs ### # TODO

	### log ### # TODO

	return error

def testSteering(SERVO_PIN):
	setupSteerPin(SERVO_PIN)
	setSteer(1000)
	sleep(1)
	setSteer(1500)
	sleep(1)
	setSteer(2000)
	sleep(1)
	setSteer(1500)

	a = input("has your Servo turned? [y/n]")
	if a in ["Y", "y", "Yes", "yes", "J", "j", "Ja", "ja"]:
		return 0
	else:
		print("check you Pin and the config/duty_cicle")
		return 1

def testAccelerate(MOTOR_PIN): # TODO
	return 0

exit(main())
