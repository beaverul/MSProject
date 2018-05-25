import time
import serial
import os
import subprocess
from firebase import firebase
from thread import start_new_thread
from multiprocessing import Process
#soare=4, luna=5, t2=temp, t3=daylight

alarm=['0','0','0','0','0','0']
dates=['0','0','0','0','0','0']
ser = serial.Serial(
  port='/dev/serial0',
  baudrate = 9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)

firebase = firebase.FirebaseApplication("https://smartalarmclock-5ad4f.firebaseio.com", None)
result = firebase.get("Temp", None)
result2 = firebase.get('Light', None)
rtc_time=subprocess.check_output("sudo hwclock -r",  shell=True)
date=rtc_time.split(" ")
hour=date[1].split(".")
t0='t0.txt="'+str(date[0])+'"'
t1='t1.txt="'+str(hour[0])+'"'
t2='t2.txt="'+str(result)+' C"'
t3='t3.txt="Day"'
p2='p2.pic=3'
count=0
EndCom = "\xff\xff\xff"



def alarmtd(alarm, dates, h, d):
  for i in range(0,6):
    alarm[i]= firebase.get('Alarmt'+str(i), None)
    dates[i]= firebase.get('Alarmd'+str(i), None)
  for i in range(0, 6):
    if alarm[i]==h[0]+":"+h[1]+'.0' or (alarm[i]==h[0]+":"+h[1]+'.1' and dates[i]==d[1]+'-'+d[2]):
      pid=os.fork()
      if(pid==0):
        os.system("python song.py")
        exit(0)

def clock():
  check=0
  while True:
    rtc_time=subprocess.check_output("sudo hwclock -r",  shell=True)
    date=rtc_time.split(" ")
    hour=date[1].split(".")
    t0='t0.txt="'+str(date[0])+'"'
    t1='t1.txt="'+str(hour[0])+'"'
    h=hour[0].split(":")
    d=date[0].split("-")
    if h[2]=='00' and check==0:
      check=1
      p1=Process(target=alarmtd, args=(alarm, dates, h, d))
      p1.start()
    if int(h[0])>=22 or int(h[0])<=8:
      p2='p2.pic=4'
      t3='t3.txt="NighT"'
    else:
      p2='p2.pic=3'
      t3='t3.txt="Day"'
    ser.write(t0+EndCom)
    ser.write(t1+EndCom)
    ser.write(t3+EndCom)
    ser.write(p2+EndCom)
    if h[2]=='50' and check==1:
      check=0
      p1.join()
def database():
  while True:
    result = firebase.get("Temp", None)
    result2 = firebase.get('Light', None)
    t2='t2.txt="'+str(result)+' C"'
    ser.write(t2+EndCom)



if __name__== '__main__':
    p2=Process(target=clock)
    p2.start()
    p3=Process(target=database)
    p3.start()
    p2.join()
    p3.join()
