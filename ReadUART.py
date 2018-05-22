import serial 
import io

ser = serial.Serial( 
port = '/dev/serial0' ,\
baudrate = 115200 ,\
bytesize = serial.EIGHTBITS ,\
timeout = 0)

sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser))

print("connected to: " + ser.port)

temp = ''

while True:
	#s = ser.readline(20) if s != "b''":
	#		print(s)
	for c in ser.read(1):
		temp = temp + str(c)
		print(temp)
		if c == '\n':
			print(temp)
			temp = ''
	
ser.close()


