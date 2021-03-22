# -*- coding: utf-8 -*
import serial
import time
# 打开串口
ser = serial.Serial("/dev/ttyAMA0", 115200)
def main():
    '''
    while True:
        s = "\r\n123+321\n\r"
        ser.write(s.encode())
        # 必要的软件延时
        time.sleep(0.1)
    '''
    while True:
        count = ser.inWaiting()#get the input byte in the input buffer
        if (count != 0):
            rec = ser.read(count)
            ser.write(rec)
            print(rec.decode())
        ser.flushInput()
        time.sleep(0.1)
    #'''
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if ser != None:
            ser.close()


