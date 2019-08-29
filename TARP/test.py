#!usr/bin/python

import threading 
import os
import time
#import RPi.GPIO as GPIO

class myThread(threading.Thread):
	def __init__(self,arg,nam):
		threading.Thread.__init__(self)
		self.arg = arg
		self.nam = nam 
	def run(self):
		detect(self.arg,self.nam)

def detect(args,fnam):
	os.system("./darknet yolo test cfg/yolov1-tiny.cfg tiny-yolov1.weights test/"+str(args)+" > logs/"+ str(fnam))

def take_image():
	os.chdir("darknet")
	for i in range(2):
		im = "img" + str(i)
		t = "log" + str(i) + ".txt"
		print(os.getcwd())
		os.system("fswebcam")
		time.sleep(2)
		os.system("fswebcam -r 1280x720 --no-banner test/"+str(im)+".jpg")
		thrd[i] = myThread(str(im)+".jpg",str(t))
		thrd[i].start()
		time.sleep(20)
	os.chdir("..")


thrd = {0:'',1:''}
take_image()
for i in thrd.values():
	i.join()

time.sleep(5)
b = False
os.chdir("darknet/logs")
for i in range(2):
    fil =  open('log'+str(i)+'.txt', 'r') #as searchfile:
    for line in fil:
        if 'person' or 'dog' or 'cat' in line:
            b=True
            break
    fil.close()
    if b:
	print("human detected")
        break
os.chdir("../..")
if b:
    os.system("python3 pin.py")    #uncomment this line.


