import serial
import time

def transport(s):
    ser = serial.Serial('/dev/ttyAMA0', 9600)
    ser.write(s.encode())
    time.sleep(0.1)

try: 
    transport('test')
expect KeyboardInterrupt:
    if ser != None:
        ser.close()
