
import cv2
import numpy as np
import matplotlib.pyplot as plt


# KÖŞE ALGILAMA

img= cv2.imread("resim.png",0)
img= np.float32(img)
img=cv2.resize(img,(294,316)) # yeninden boyulandırkdık
# plt.figure(), plt.imshow(img,cmap="gray"),plt.axis("off")

dst= cv2.cornerHarris(img,blockSize=2,ksize=3,k=0.04) # img , kaç köşeye bakacak, kutucuk boyutu, k ise harris detecktmri için kullannılr
plt.figure(), plt.imshow(dst,cmap="gray"),plt.axis("off")
dst= cv2.dilate(dst,None)     # burda köşeleri daha net bulmak için yaptık
img[ dst > 0.2*dst.max()]=1   # max x0.2 den küçükse 1 e eşitleme yaptık ve daha net görebilmek için
plt.figure(), plt.imshow(dst,cmap="gray"),plt.axis("off")

plt.show()