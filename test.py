import sys
sys.path.insert(0, './libary/')

# from getInputs import getInputs, readInputs # local file
from setSteer import setupSteerPin, setSteer # local file
from configReader import getConfig # local file
from setSpeed import setSpeed # local file
from PIDloop import PIDloop # local file
from alert import alert # local file
from time import sleep
import pigpio


def main():
	config = getConfig()

	error = 0
	mode = ""
	try:
		mode = sys.argv[1]
	except:
		pass
	
#	if not mode == "":
#		a = input("do you have GPIO pins? [y/n]")
#		if a in ["Y", "y", "Yes", "yes", "J", "j", "Ja", "ja"]:
#			error += testSteering()
#			error += testAccelerate()

#		else:
#			print("Motor tests skiped")
#			print("alert tests skiped")
#	else:
#		error += testSteering()
#		error += testAccelerate()
		
	### PID overflow ### # TODO

	### alert ### # TODO

	### getInputs ### # TODO

	### log ### # TODO

	return error

def testSteering():
	SERVO_PIN = int(input("on which GPIO Pin is your servo motor connected to?"))
	print(f"Your servo motor is connected to GPIO {SERVO_PIN}")

	setupSteerPin(SERVO_PIN, config['OMnP'], config['OMxP'])
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
		print("check your Pin and the duty_cicle in the config file")
		return 1

def testAccelerate():
	MOTOR_PIN = int(input("on which GPIO Pin is your motor connected to? (for acceleration)"))
	print(f"Your motor is connected to GPIO {MOTOR_PIN}")
	input("press enter when your tires dont touch the ground!")
	
	pi = pigpio.pi()

	for i in range(50):
		pi.set_servo_pulsewidth(MOTOR_PIN, i*20 + 1000)
		print(i*20 + 1000)
		sleep(0.05)
		i += 1

	for i in range(50):
		pi.set_servo_pulsewidth(MOTOR_PIN, 2000 - i*20)
		print(2000 - i*20)
		sleep(0.05)
		i += 1

	pi.set_servo_pulsewidth(MOTOR_PIN, 1000)

	a = input("has your Motor turned? [y/n]")
	if a in ["Y", "y", "Yes", "yes", "J", "j", "Ja", "ja"]:
		return 0
	else:
		print("check your Pin and the config")
		return 1

exit(main())
