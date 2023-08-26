# NESNE TAKİBİ 
# ORTALAMA KAYMA ALGORİTMASI
import cv2
import numpy as np
import matplotlib.pyplot as plt


cap= cv2.VideoCapture(0)

ret, frame = cap.read()

if ret== False:
    print("uyarı")

# yüz algılamak için detection işlemi yapıyoruz xlm dosyasını kullanarak
face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 

face_rect=face_cascade.detectMultiScale(frame)  # yüzü algıaldık ve rect olarak değerler döner x,y,w,h [[228  69 233 233]] dönen değer tuple

print(face_rect)

(face_x,face_y,w,h)=tuple(face_rect[0])
track_window=(face_x,face_y,w,h)=(face_x,face_y,w,h) # ortalama kayma girdisi algoritması


# region of interest

roi= frame[face_y:face_y + h ,face_x:face_x + w ]  # tespit edilen yüzün kordinatları ile ana frameden alma 

hsv_roi=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

roi_his=cv2.calcHist([hsv_roi],[0],None,[180],[0,180])  # takip için histogram gerekli

cv2.normalize(roi_his,roi_his,0,255,cv2.NORM_MINMAX)  # yukarıda oluşan roi_his 0-255 arası normalize ettik


# takip için gerekli durdurma kritirleri
# öğe sayısı count dur hesaplanacak max öğe sayısı
# count doğruluk epsilon değişklik yenilemeli algoritmalar da 

term_crit=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,5,1) # 5 yenileme 1 epsilon demek

while True:
    ret,frame= cap.read()
    if ret:
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        dst=cv2.calcBackProject([hsv],[0],roi_his,[0,180],1) # hesaplanan historamı görüntüde bulmak için kullanılır yüz ifadesinin his ana frame de arıyoruz bu sayede eşleme gerçekleştiriloyr ve takip sağlanıyor
        ret,track_window = cv2.meanShift(dst,track_window,term_crit)
        x,y,w,h=track_window
        img2= cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),5)
        cv2.imshow("i",img2)
        if cv2.waitKey(1) & 0XFF==ord("q"):
            break 