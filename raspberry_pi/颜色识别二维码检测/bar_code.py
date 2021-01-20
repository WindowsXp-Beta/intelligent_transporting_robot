import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

def QR_detect():
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
            print(barcodes)
            for barcode in barcodes:
                (x,y,w,h) = barcode.rect
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                barcodeDate = barcode.data.decode("utf-8")
                #print(barcode.data)
                #print(barcodeDate)
                barcodeType = barcode.type
                text = "{}({})".format(barcodeDate,barcodeType)
                cv2.putText(img,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)
                print("[INFO] Found {} barcode: {}".format(barcodeType,barcodeDate))
                cv2.imshow('img_result',img)
            key_num = cv2.waitKey(0)
            if key_num == ord('q'):
                break
            cv2.destroyAllWindows()
    camera.release()
    cv2.destroyAllWindows()
   
def main():
    QR_detect()
main()