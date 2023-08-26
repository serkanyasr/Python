
import cv2
import numpy as np
import matplotlib.pyplot as plt


# HAVZA ALGORİTMASI  ÇOOKK ÇOOK ÖNEMLİ

para= cv2.imread("para.jpeg")   # RESMİ İÇE AKTARMA 
# plt.figure(),plt.imshow(para),plt.axis("off"),plt.show()

# loft past feature bluuring  paraalrın köşeleri belli olamsı için blur işlemi uyguluyotruz

coin_blur= cv2.medianBlur(para,ksize=13)   # para üstündeki detayları gizlemiş olduk sadece ana hatları belli
plt.figure(),plt.imshow(coin_blur),plt.axis("off"),plt.show()

# grayscala

coin_gray= cv2.cvtColor(coin_blur,cv2.COLOR_BGR2GRAY)
plt.figure(),plt.imshow(coin_gray,cmap="gray"),plt.axis("off"),plt.show()

# binary treshold paralar ile zemin arası renk farkını daha çok açarak belirgin olmasını sağlamak

ret, coin_trhresh=cv2.threshold(coin_gray,75,255,cv2.THRESH_BINARY)
plt.figure(),plt.imshow(coin_trhresh,cmap="gray"),plt.axis("off"),plt.show()

# kontur aşaması

contour,hierarchy=cv2.findContours(coin_trhresh.copy(),cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contour)):
    if hierarchy[0][i][3]==-1:
        cv2.drawContours(para,contour,i,(0,255,0),10)
plt.figure(),plt.imshow(para),plt.axis("off"),plt.show()


# açılma işlemi  paralar arası köprüleri yok etmek için kullanmamız gerekrir

kernel=np.ones((3,3),np.uint8)
opening=cv2.morphologyEx(coin_trhresh,cv2.MORPH_OPEN,kernel,iterations=2)
plt.figure(),plt.imshow(opening,cmap="gray"),plt.axis("off"),plt.show()

# nesneler arası distance
dist_transform=cv2.distanceTransform(opening,cv2.DIST_L2,5)
plt.figure(),plt.imshow(dist_transform,cmap="gray"),plt.axis("off"),plt.show()

# nesnelri küçülkme

ret,sure_foreground=cv2.threshold(dist_transform,0.4*np.max(dist_transform),255,0)
plt.figure(),plt.imshow(sure_foreground,cmap="gray"),plt.axis("off"),plt.show()

# arka plan için nesneleri büüyüt

sure_bacjground= cv2.dilate(opening,kernel,iterations=1)

sure_foreground= np.uint8(sure_foreground)
unknown= cv2.subtract(sure_bacjground,sure_foreground)
plt.figure(),plt.imshow(unknown,cmap="gray"),plt.axis("off"),plt.show()
# bağlantı
ret,marker= cv2.connectedComponents(sure_foreground)
marker=marker+1

marker[unknown==255]=0
plt.figure(),plt.imshow(marker,cmap="gray"),plt.axis("off"),plt.show()

# havza

marker= cv2.watershed(coin_blur,marker)
plt.figure(),plt.imshow(marker,cmap="gray"),plt.axis("off"),plt.show()

# kontur aşaması

contour,hierarchy=cv2.findContours(marker.copy(),cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contour)):
    if hierarchy[0][i][3]==-1:
        cv2.drawContours(para,contour,i,(255,0,0),10)
plt.figure(),plt.imshow(para),plt.axis("off"),plt.show()