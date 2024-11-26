import configparser

def getConfig():
	config = configparser.ConfigParser()
	config.read("config.ini")

	return {
		"GSB" : int(config['GPIOs']['Sbuspin']), # GPIO-SBus
		"GS" : int(config['GPIOs']['Steerpin']), # GPIO-Steer
		"GT" : int(config['GPIOs']['ESCpin']), # GPIO-Throttle
		"GDT" : int(config['GPIOs']['DistanceTrigger']), # GPIO-DistanceTrigger
		"GDE" : int(config['GPIOs']['DistanceEcho']), # GPIO-DistanceEcho

		"PID" : [int(config['PID']['P']), int(config['PID']['I']), int(config['PID']['I'])], # PID
		
		"CT" : int(config['Switches / Channel / Axis']['Throttle']), # Channel-Throttle
		"CS" : int(config['Switches / Channel / Axis']['Steer']), # Channel-Steer
		"CA" : int(config['Switches / Channel / Axis']['Arm']), # Channel-Arm
		"CAMn" : int(config['Switches / Channel / Axis']['Armmin']), # Channel-Arm-minimum
		"CAMx" : int(config['Switches / Channel / Axis']['Armmax']), # Channel-Arm-maximum
		"CM" : int(config['Switches / Channel / Axis']['Mode']), # Channel-Mode

		"M1" : {
			"Mn" : int(config['Mode1']['Min']), # Mode1-min switch position
			"Mx" : int(config['Mode1']['Max']), # Mode1-max switch position
			"S" : float(config['Mode1']['Speed']), # Mode1-speed
			"D" : int(config['Mode1']['Distancecheck']) # Mode1-distancecheck from walls
		},

		"M2" : {
			"Mn" : int(config['Mode2']['Min']), # Mode2-min switch position
			"Mx" : int(config['Mode2']['Max']), # Mode2-max switch position
			"S" : float(config['Mode2']['Speed']), # Mode2-speed
			"D" : int(config['Mode2']['Distancecheck']) # Mode2-distancecheck from walls
		},

		"M3" : {
			"Mn" : int(config['Mode3']['Min']), # Mode3-min switch position
			"Mx" : int(config['Mode3']['Max']), # Mode3-max switch position
			"S" : float(config['Mode3']['Speed']), # Mode3-speed
			"D" : int(config['Mode3']['Distancecheck']) # Mode3-distancecheck from walls
		},
	

		"OMT" : int(config['Other']['Maxthrottlearm']), # Other-Max-Throttle for arming
		"OMnP" : float(config['Other']['Minpulsewidth']), # Other-Min-PWM Servo
		"OMxP" : float(config['Other']['Maxpulsewidth']), # Other-Max-PWM Servo
		"OLB" : float(config['Other']['Logbuffersize']) # Other-Log-Buffer
	}
