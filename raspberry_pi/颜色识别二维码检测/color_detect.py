import cv2
import numpy as np
import imutils

def rec(lower,upper):
    #camera = cv2.VideoCapture(0)
    #(ret,img) = camera.read()
    '''using existing pictures'''
    img = cv2.imread('../img/10_20_1.png')
    
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
    max_max = np.array([])
    sub_max = np.array([])
    i = 0
    for c in cnts:
        if max_max.any():
            if cv2.contourArea(c) > cv2.contourArea(max_max):
                sub_max = max_max
                max_max = c
            elif sub_max.any():
                if cv2.contourArea(c) > cv2.contourArea(sub_max):
                    sub_max = c
            else :
                sub_max = c
        else :
            max_max = c
    x = [0,0]
    y = [0,0]
    radius =[0,0]
    ((x[0],y[0]),radius[0]) = cv2.minEnclosingCircle(max_max)
    ((x[1],y[1]),radius[1]) = cv2.minEnclosingCircle(sub_max)
    print(x[0], y[0])
    print(x[1], y[1])
    #if radius > 20:
    for i in range(2):
        cv2.circle(img,(int(x[i]),int(y[i])),int(radius[i]),(0,5,525),2)
        img_result = img
        cv2.imshow('img_result',img_result)
    cv2.waitKey(0)#等待任意键按下继续
    #camera.release()
    cv2.destroyAllWindows()

def main():
    green_low = [40,90,90]
    green_upper = [77,255,255]

    red_low = [156,140,90]
    red_upper = [180,255,255]

    blue_low_high = [100,160,160]
    blue_upper_high = [124,255,240]
    
    blue_low_low = [100,170,100]
    blue_upper_low = [124,255,140]

    rec(green_low,green_upper)
    
    #rec(blue_low_high,blue_upper_high)
    #rec(blue_low_low,blue_upper_low)
    
    #rec(red_low,red_upper)

if __name__ == "__main__":
    main()
