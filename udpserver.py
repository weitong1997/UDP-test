# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 23:13:42 2018

@author: WT
"""
import sys
from socket import *
from time import ctime
HOST = "192.168.6.4"
PORT = 90
BUFFERSIZE = 1024

list1=["00001,0,1,30",
       "00001,0,1,20",
       "00001,0,1,10",
       "00001,0,1,0",
       "00001,50,2,120",
       "00001,45,2,90",
       "00001,60,2,60",
       "00001,65,2,30",
       "00001,10,2,0",
       "00001,0,2,0",
       "00001,20,3,30",
       "00001,60,3,10",
       "00001,0,3,0",
       "00001,30,4,30",
       "00001,60,4,10",
       "00001,0,4,0",
       "00001,10,5,30",
       "00001,50,5,20",
       "00001,60,5,5",
       "00001,0,5,0",
       "00001,30,6,30",
       "00001,50,6,10",
       "00001,0,6,0"]
busindex=0

s = socket(AF_INET,SOCK_DGRAM)
s.bind((HOST,PORT))
print('Waiting for connection....')
while True:
    try:
        data,addr = s.recvfrom(BUFFERSIZE)
        data = data.decode(encoding='utf-8').upper()
        print("RECV From" + str(addr) + ":" + data)
        print(ctime())
        #data = "at %s :%s"%(ctime(),data)
        
        s.sendto(bytes(list1[busindex],"ascii"),addr)
        busindex = busindex + 1
        if busindex > 22:
            busindex = 0
    except KeyboardInterrupt:
        print("Server Stopped!")
        s.close()
        sys.exit(0)
    except Exception as  ex:
        print(ex)

s.close()
