#!/usr/bin/env python3
# Package pyserial needed for this - https://pypi.org/project/pyserial/ - pip install pyserial
import serial,datetime,os

#ser = serial.Serial('COM1',9600)		# Windows
ser = serial.Serial('/dev/ttyUSB0',9600)	# Mac/Linux

f   = open("serialdump.txt", "a+")

while True:
    s    = ser.readline()
    now  = str(datetime.datetime.now())

    line = str(now)
    line += ","
    #line = s.decode('utf-8').replace('\r\n','')
    data  = s.decode(encoding='ascii',errors='ignore')
    line += data

    print(line.replace('\r\n',''))			# Prints output to screen
    f.write(line)	# Appends output to file
    f.flush()
