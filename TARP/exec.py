import serial
import os
import time
import threading
os.system('sudo chmod 666 /dev/ttyACM0')
ser = serial.Serial('/dev/ttyACM0',9600)
flag = True

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#'''function for image capturing'''
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
      try:
        os.system("fswebcam")
        time.sleep(2)
        os.system("fswebcam -r 1280x720 --no-banner test/"+str(im)+".jpg")
      except Exception as e:
        print(e)
        take_image()
      thrd[i] = myThread(str(im)+".jpg",str(t))
      thrd[i].start()
      time.sleep(20)
  os.chdir("..")
#function for image capturing ends here
#-----------------------------------------------------------------------------
#Temperature function
def temp():
    a = 't'+'\n'
    ser.write(a)
    print(ser.read(1))
    a = ser.read(5)
    print(a)
    time.sleep(5)
    if float(a) > 25:
        print("Tmp >")
        return True
#s.system('sudo chmod 666 /dev/ttyACM0')
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def humn():
    flg = False
    take_image()
    for i in thrd.values():
        i.join()

    time.sleep(5)
    b = False
    os.chdir("darknet/logs")
    for i in range(2):
        fil =  open('log'+str(i)+'.txt', 'r') #as searchfile:
        for line in fil:
            if 'person' in line:
                b=True
                break
        fil.close()
        if b:
            print("human detected")
            flg = True
            break
    os.chdir("../..")
    return flg

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def alrm():
    a = 'd'+'\n'
    ser.write(a)
    z = time.time()
    flg = False
    while time.time() - z < 60:
        y = ser.read_until('y',1)
        if y:
            flg = True  #Human pressed the button
            break
    return(not flg) #send false for no further process

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#function to send message
def msg():
    ser.write('s'+'\n')
    ser.read_until('y',1) #read 'y' if message sucessfuly sent
#````````````````````````````````````````````````````````````````````````````
thrd = {0:'',1:''}
while True:
    try:
        if(temp()):
            if(humn()):
                if(alrm()):
                    msg()
                else:
                    break
            else:
                time.sleep(5) #sleep for 5 minutes if human not detected
    except Exception as e:
        print(e)
        break

