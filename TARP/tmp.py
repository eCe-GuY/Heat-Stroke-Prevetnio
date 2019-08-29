#!/usr/bin/python
import os
import sys
import time
import Adafruit_DHT

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print("Temperature: " +str(temperature)) 
