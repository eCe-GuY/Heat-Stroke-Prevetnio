#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False);
GPIO.setup(16,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(18,GPIO.OUT)  #LED to detecT
GPIO.setup(40,GPIO.OUT)	#LCD connect)
GPIO.output(18,False)
GPIO.output(40,True)
a = time.time()
while time.time()-a < 60:
	flag = False
	if GPIO.input(16) == False:
		flag = True
		break
GPIO.output(18,True)
GPIO.output(40,False)
GPIO.cleanup()
if flag:
	time.sleep(60)
if not flag:
	os.system("python3 msg.py")

