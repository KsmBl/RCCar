import RPi.GPIO as GPIO
import threading
import time

globalDistance = 0

def distanceScanner(triggerPin, echoPin):
	global globalDistance

	try:
		while True:

			GPIO.output(triggerPin, True)
			time.sleep(0.00001)
			GPIO.output(triggerPin, False)

			startTime = time.time()
			stopTime = time.time()

			while GPIO.input(echoPin) == 0:
				startTime = time.time()

			while GPIO.input(echoPin) == 1:
				stopTime = time.time()

			timeElapsed = stopTime - startTime
			distance = (timeElapsed * 34300) / 2
			globalDistance = round(distance, 2)
			time.sleep(0.016666)
	except KeyboardInterrupt:
		GPIO.cleanup()
		return 1

def startDistanceScanner(triggerPin, echoPin):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(triggerPin, GPIO.OUT)
	GPIO.setup(echoPin, GPIO.IN)

	distanceScannerThread = threading.Thread(target=distanceScanner, args=[triggerPin, echoPin])
	distanceScannerThread.start()

def getDistance():
	global globalDistance
	return globalDistance
