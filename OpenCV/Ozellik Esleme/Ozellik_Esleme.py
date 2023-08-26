# ÖZELLİK EŞLEŞTİRME
import cv2
import numpy as np
import matplotlib.pyplot as plt

# ANA GÖRÜNTÜ İÇE AKTARMAK

cikolatalar=cv2.imread("cikolata.jpeg",0)
# plt.figure(),plt.imshow(cikolatar,cmap="gray"),plt.axis("off")
cikolata=cv2.imread("nestle.jpg",0)
# plt.figure(),plt.imshow(cikolata,cmap="gray"),plt.axis("off")

# TANIMLAYICALAR
# orb tanımlayıcısı(köşe kenar gibi nesneye ait özellikler)

orb=cv2.ORB_create()

# anahatar nokta tespiti

kp1,des1=orb.detectAndCompute(cikolata,None)  # resim , None maskelem olmadığını gösterir
kp2,des2=orb.detectAndCompute(cikolatalar,None)

# bruteForce Matcher
bf=cv2.BFMatcher(cv2.NORM_HAMMING)

# noktaları eşleştirme
matches= bf.match(des1,des2)

# mesafeye göre sıralama
matches=sorted(matches,key=lambda x: x.distance)

# eşleşen resimleri görselleştirme

plt.figure()

img_match= cv2.drawMatches(cikolata,kp1,cikolatalar,kp2,matches[:20],None,flags=2)
plt.imshow(img_match),plt.axis("off")
plt.show()

# sift tanımlayıcısı
sift= cv2.xfeatures2d.SIFT_create()

bf=cv2.BFMatcher()
# anahtar nokta tespiti sift
kp1,des1=sift.detectAndCompute(cikolata,None)  # resim , None maskelem olmadığını gösterir
kp2,des2=sift.detectAndCompute(cikolatalar,None)  # resim , None maskelem olmadığını gösterir

matches=bf.knnMatch(des1,des2,k=2)