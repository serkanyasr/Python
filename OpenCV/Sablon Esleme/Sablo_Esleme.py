#ŞABLON EŞLEME YÖNTEMİ
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("cat.webp",0)


sablon= cv2.imread("cat_face.PNG",0)
print(img.shape,sablon.shape)   #(486, 728) (234, 269)
h, w= sablon.shape

method=['cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR','cv2.TM_CCORR_NORMED','cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']  # 6 tane method var

# eval() methodu string olan ifadeyi okur ve fonksiyona dönüştürür == 'cv2.TM_CCORR_NORMED'=> cv2.TM_CCORR_NORMED

for meth in method:
    method=eval(meth)
    res=cv2.matchTemplate(img,sablon,method)
    print(res.shape)
    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        top_left=min_loc
    else:
        top_left=max_loc
    bottom_rigth= (top_left[0]+w,top_left[1]+h)

    cv2.rectangle(img,top_left,bottom_rigth,255,2)

    plt.figure()
    plt.subplot(121),plt.imshow(res,cmap="gray")
    plt.title("eşleşen sonuç"),plt.axis("off")
    plt.subplot(122),plt.imshow(img,cmap="gray")
    plt.title("eşleşen sonuç"),plt.axis("off")
    plt.show()
