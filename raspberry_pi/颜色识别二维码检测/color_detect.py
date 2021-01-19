import cv2
import numpy as np
import imutils

def rec(lower,upper):
    camera = cv2.VideoCapture(1)
    (ret,img) = camera.read()
    cv2.imshow('image1',img)
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    color_low = np.array([lower[0],lower[1],lower[2]])
    color_upper = np.array([upper[0],upper[1],upper[2]])
    mask = cv2.inRange(img_hsv,color_low,color_upper)
    cv2.imshow('image3',mask)
    mask_mf = cv2.medianBlur(mask,7)
    cv2.imshow('middlefilter',mask_mf)
    cnts = cv2.findContours(mask_mf,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        ((x,y),radius) = cv2.minEnclosingCircle(c)
        if radius > 20:
            x,y = int(x),int(y)
            cv2.circle(img,(x,y),int(radius),(0,5,525),2)
        img_result = img
        cv2.imshow('img_result',img_result)
    cv2.waitKey(0)#等待任意键按下继续
    camera.release()
    cv2.destroyAllWindows()

def main():
    green_low = [38,90,90]
    green_upper = [75,255,255]

    red_low = [160,90,90]
    red_upper = [179,255,255]

    blue_low = [75,90,90]
    blue_upper = [130,255,255]

    rec(green_low,green_upper)
    
    rec(blue_low,blue_upper)

    rec(red_low,red_upper)

main()
