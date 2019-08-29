#!/usr/bin/python3
import os
import sys
import time
os.chdir("dht")
import Adafruit_DHT as dt
time.sleep(15)
while True:
	humidity, temperature = dt.read_retry(11,4)
	print("temperature: "+str(temperature))
	time.sleep(5)
	if temperature >= 27:
		os.chdir("..")
		os.system("python3 lcd.py" +str(temperature))
