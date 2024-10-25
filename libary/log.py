from datetime import datetime
import time
import os

logfile = ""
logbuffer = []
logcount = 0
logbuffersize = 100

def createLogfile(_logbuffersize):
	global logfile
	global logbuffersize
	logbuffersize = _logbuffersize
	logfile = (f"./log/{datetime.now().strftime('rccar_logfile_%Y-%m-%d_%H-%M-%S')}.log")
	os.mknod(logfile)

def log(message):
	global logfile
	global logcount
	global logbuffer
	global logbuffersize

	logcount += 1

	logbuffer.append(message)

	if logcount >= logbuffersize:
		# write into file
		f = open(logfile, "a")
		for i in logbuffer:
			f.write(f"{time.time()} | {i}\n")

		print("logfile written")
		f.close()
		logbuffer = []
		logcount = 0






