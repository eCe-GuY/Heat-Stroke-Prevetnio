import serial
import time
import os
os.system('sudo chmod 666 /dev/ttyACM0')
ser = serial.Serial('/dev/ttyACM0',9600)
def alrm():
    a = 'd'+'\n'
    ser.write(a)
    z = time.time()
    flg = False
    while (time.time() - z) < 60:
        print(time.time()-z)
        y = ser.read(1)
        print(y)
        if y == 'y':
            flg = True  #Human pressed the button
            print(flg)
            break
        else:
            continue
    return(not flg)
while True:
    a = input("Continue")
    if a == 1:
      alrm()
