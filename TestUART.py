import serial
import time
import io 

ser = serial.Serial(
port = '/dev/serial0', \
baudrate = 115200, \
bytesize = serial.EIGHTBITS, \
timeout = 0)

while True:
	input = raw_input("Input: ")
	ser.write(input)
	time.sleep(0.1)
	
#	for c in ser.read(20):
#		dat += c
#		if c== '\0':
#			print(dat)
#			dat = ''
#			break
ser.close()
