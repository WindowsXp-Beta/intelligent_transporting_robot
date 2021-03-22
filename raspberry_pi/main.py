# coding=utf-8
import sys
sys.path.append("./display")
from display.display import display
import serial
import time
import cv2
import numpy as np
import imutils
import pyzbar.pyzbar as pyzbar

'''global settings'''
green_lower = [35,90,90]
green_upper = [77,255,255]

red_lower = [0,90,90]
red_upper = [10,255,255]

blue_lower = [100,90,90]
blue_upper = [124,255,255]

QR_code = ''

# 1 is red
# 2 is green
# 3 is blue
top_order = []
bottom_order = []

class commuicator:
    def __init__(self):
        self.receive_info = ''
        self.ser = serial.Serial('/dev/ttyAMA0', 9600)
        self.Is_correct = False

    '''发送信息后 每隔0.1秒收取一次stm32发送的信息，如果与发送信息相同，不再发送'''
    def send(self, info):
        if None == info:
            return
        self.ser.write(info.encode())
        while not self.Is_correct:
            count = self.ser.inWaiting()
            if not count == 0:
                rcv = self.ser.read(count)
                self.Is_correct = (rcv == info)
                self.ser.flushInput()
                time.sleep(0.1)

    def receive(self):
        count = self.ser.inWaiting()
        if not count == 0:
            self.receive_info = self.ser.read(count).decode()
            

def rec(lower,upper):#传入颜色的hsv区间
    camera = cv2.VideoCapture(0)
    (ret,img) = camera.read()
    cv2.imshow('image1',img)
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    color_low = np.array([lower[0],lower[1],lower[2]])
    color_upper = np.array([upper[0],upper[1],upper[2]])
    mask = cv2.inRange(img_hsv,color_low,color_upper)
    cv2.imshow('image3',mask)
    mask_mf = cv2.medianBlur(mask,7)#中值滤波
    cv2.imshow('middlefilter',mask_mf)
    cnts = cv2.findContours(mask_mf,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    count = 0
    sum_x = 0
    sum_y = 0
    for c in cnts:
        ((x,y),radius) = cv2.minEnclosingCircle(c)
        if radius > 20:
            x,y = int(x),int(y)
            count = count + 1
            sum_x = sum_x + x
            sum_y = sum_y + y
            cv2.circle(img,(x,y),int(radius),(0,5,525),2)
        img_result = img
        cv2.imshow('img_result',img_result)
    cv2.waitKey(0)#等待任意键按下继续
    camera.release()
    cv2.destroyAllWindows()
    return [sum_x, sum_y]

def QR_detect():
    print("begin QR\n")
    camera = cv2.VideoCapture(0)
    #count = 0
    while True:
        camera.read()
        camera.read()
        camera.read()
        camera.read()#先读取4帧，去除延迟
        (reg,img) = camera.read()
        #cv2.imshow('img_1',img)
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        barcodes = pyzbar.decode(img_gray)
        if not barcodes:
           #debug
           #count += 1
           #if count % 100 == 0:
           #print('signal\n')
           continue
        else:
            print("QR_code detect\n")
            #print(barcodes)
            for barcode in barcodes:#有可能有多个二维码
                (x,y,w,h) = barcode.rect
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                barcodeDate = barcode.data.decode("utf-8")
                QR_code = barcodeDate
                #print(barcode.data)
                #print(barcodeDate)
                barcodeType = barcode.type
                # text = "{}({})".format(barcodeDate,barcodeType)
                # cv2.putText(img,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)
                # print("[INFO] Found {} barcode: {}".format(barcodeType,barcodeDate))
                # cv2.imshow('img_result',img)
            # key_num = cv2.waitKey(0)
            # if key_num == ord('q'):
            #     break
            # cv2.destroyAllWindows()
    camera.release()
    cv2.destroyAllWindows()

def main():
    '''第一阶段：从出发区到二维码板的过程中，持续扫描，检测到二维码后停止扫描'''
    QR_detect()
    #检测到二维码后，将其显示在屏幕上
    show = display(QR_code)
    show.show()
    #并将其发送给stm32
    com = commuicator()
    com.send(QR_code)
    '''第二阶段：收到stm32发过来的到达货架前的信号后，拍照识别，并将识别到的顺序传回stm32'''
    while True:
        com.receive()
        if com.receive_info == 'A':
            break
    
    #开始识别摆放顺序
    [green_up, green_low] = rec(green_lower, green_upper)
    [red_up, red_low] = rec(red_lower, red_upper)
    [blue_up, blue_low] = rec(blue_lower, blue_upper)

    #确定上层顺序
    if green_up > red_up and green_up > blue_up:
        top_order[0] = 2
        if red_up > blue_up:
            top_order[1] = 1
            top_order[2] = 3
        else:
            top_order[1] = 3
            top_order[2] = 1
    elif red_up > blue_up:
        top_order[0] = 1
        if green_up > blue_up:
            top_order[1] = 2
            top_order[2] = 3
        else:
            top_order[1] = 3
            top_order[2] = 2
    else:
        top_order[0] = 3
        if red_up > green_up:
            top_order[1] = 1
            top_order[2] = 2
        else:
            top_order[1] = 2
            top_order[2] = 1

    #确定下层顺序
    if green_low > red_low and green_low > blue_low:
        bottom_order[0] = 2
        if red_low > blue_low:
            bottom_order[1] = 1
            bottom_order[2] = 3
        else:
            bottom_order[1] = 3
            bottom_order[2] = 1
    elif red_low > blue_low:
        bottom_order[0] = 1
        if green_low > blue_low:
            bottom_order[1] = 2
            bottom_order[2] = 3
        else:
            bottom_order[1] = 3
            bottom_order[2] = 2
    else:
        bottom_order[0] = 3
        if red_low > green_low:
            bottom_order[1] = 1
            bottom_order[2] = 2
        else:
            bottom_order[1] = 2
            bottom_order[2] = 1
        
    #将摆放信息传回stm32
    com.send(top_order)
    com.send(bottom_order)
    
    
main()
