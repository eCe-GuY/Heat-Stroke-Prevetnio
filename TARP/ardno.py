#!/usr/bin/python
import serial
import os
import time
ser = serial.Serial('/dev/ttyACM0',9600)
temp = 22  #enter temperature
ser.write(str(temp))
#time.sleep(2)
while True:
    if ser.read() >= temp:
	print(ser.read)
        ser.write('2')
        flag = True
        a = time.time()
        #b = time.time()
        while (time.time()-a) < 120:
            ser.write("1")
            if ser.read():
		print(ser.read)
                ser.write("0")
                flag = False
                break

        if flag:
            ser.write("0")
            os.system("python test.py")
        else:
            time.sleep(6) #sleep the process for 10 minutes.

