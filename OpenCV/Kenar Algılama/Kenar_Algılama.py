import cv2
import numpy as np
import matplotlib.pyplot as plt




# KENAR ALGILAMA
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
img = cv2.imread("resim.jpg", 0)
plt.figure(),plt.imshow(img,cmap="gray"),plt.axis("off")  # görselleştirme işlemi için kullandık

kenarlar = cv2.Canny(img,threshold1=0,threshold2=255)  # canny ile kenarları tanımladık
plt.figure(),plt.imshow(kenarlar,cmap="gray"),plt.axis("off")  # görselleştirme işlemi için kullandık

median_deger= int(np.median(img))   #197   daha az kenar tespiti yapmak için median derğerini buldul
ortalama_deger= int(np.mean(img))   #158

low_threshold= int(max(0, (1 - 0.33)*median_deger))  #kenarları belirlerken  min tress i belirlemek için literarür %67 de alabilir sin  daha net ve az kenar tespiti için #131
max_threshold= int(min(255, (1 + 0.33)*median_deger))  #kenarları belirlerken  min tress i belirlemek için literarür %67 de alabilir sin   daha net ve az kenar tespiti için  #255

kenarlar = cv2.Canny(img,threshold1=low_threshold,threshold2=max_threshold)  # bulfuğumuz tress leri uyguladık
plt.figure(),plt.imshow(kenarlar,cmap="gray"),plt.axis("off")  # görselleştirme işlemi için kullandık




# daha net kenar kontrolü için resme blur işlemi (bulanaklaştırma) yapılır

blur_img= cv2.blur(img,ksize=(2,2))
plt.figure(),plt.imshow(blur_img,cmap="gray"),plt.axis("off")  # görselleştirme işlemi için kullandık

median_deger= int(np.median(blur_img))   #197   daha az kenar tespiti yapmak için median derğerini buldul
ortalama_deger= int(np.mean(blur_img))   #158


low_threshold_blur= int(max(0, (1 - 0.33)*median_deger))  #kenarları belirlerken  min tress i belirlemek için literarür %67 de alabilir sin  daha net ve az kenar tespiti için #131
max_threshold_blur= int(min(255, (1 + 0.33)*median_deger))  #kenarları belirlerken  min tress i belirlemek için literarür %67 de alabilir sin   daha net ve az kenar tespiti için  #255
kenarlar_blur_img = cv2.Canny(blur_img,threshold1=low_threshold_blur,threshold2=max_threshold_blur)  # bulfuğumuz tress leri uyguladık
plt.figure(),plt.imshow(kenarlar_blur_img,cmap="gray"),plt.axis("off")  # görselleştirme işlemi için kullandık

plt.show()
