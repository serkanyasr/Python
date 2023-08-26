import cv2
import numpy as np
import matplotlib.pyplot as plt




# RENK İLE NESNE TESPİTİ  (tekrar tekrar et)

from collections import deque  # tesspit edilen objecin merkesizini depolaycak veri

buffer_size= 16  # deque nin boyutu
pts= deque(maxlen=buffer_size)

# mavi renk aralığı HSV formatında

blueLower=(84,98,0)
blueUpper=(179,255,255)

#capture

cap= cv2.VideoCapture(0)
# cap.set(3,960)
# cap.set(4,480)

while True:
    sucsess, ImgOriginal=cap.read()
    if sucsess:
        #blur
        blured= cv2.GaussianBlur(ImgOriginal,(11,11),0)
        # HSV formata çevirme
        hsv=cv2.cvtColor(blured, cv2.COLOR_BGR2HSV)
        cv2.imshow("hsv",hsv)
        # mavi rengi tespit edebilmek için maske oluşturma
        mask=cv2.inRange(hsv,blueLower,blueUpper)
        #maskenin etradında kalan gürültüleri silme
        mask=cv2.erode(mask,None,iterations=2)
        mask=cv2.dilate(mask,None,iterations=2)
        cv2.imshow("ımage",mask),cv2.waitKey(0)


        # konturlerme işlemi


        (contours,_)= cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        center= None

        if len(contours)>0:
            # En büyük koturu al
            c= max(contours,key=cv2.contourArea)

            #dikdörtgene çevir
            rect=cv2.minAreaRect(c)
            ((x,y),(width,height),rotation)=rect
            s= "x:{},y:{},width:{},height:{},rotation:{}".format(np.round(x),np.round(y),np.round(width),np.round(height),np.round(rotation))
            print(s)
            box= cv2.boxPoints(rect)
            box=np.int64(box)

            # Moment
            M=cv2.moments(c)
            center=(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))

            #çizdirme
            cv2.drawContours(ImgOriginal,[box],0,(0,255,255),2)

            # Merkeze bir nokta çizelim
            cv2.circle(ImgOriginal,center,5,(255,0,255),-1)

            # bilgileri ekrana yazdır
            cv2.putText(ImgOriginal,s,(25,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),2)

        cv2.imshow("ımage",ImgOriginal)





    if cv2.waitKey(1) & 0XFF==ord("q"):
        break
