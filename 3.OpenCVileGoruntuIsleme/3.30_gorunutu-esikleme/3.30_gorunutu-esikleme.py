# -*- coding: utf-8 -*-

import cv2
import matplotlib.pyplot as plt

#resmi içe aktar
img = cv2.imread("img1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
'''renk tonlarını gray skalada gösterir burada söz konusu olan siyha beyaz 
renkler değil, renk tonlarının 0 - 255 arasında ifade edilmesidir'''

plt.figure()
plt.imshow(img, cmap = "gray")
#cmap = 'gray' görüntüyü siyah beyaza dönüşütürür - cmap(colormap)
plt.axis("off")
plt.show()

#eşikleme
_, thresh_img = cv2.threshold(img, thresh = 60, maxval = 255, type = cv2.THRESH_BINARY)
#döndürdüğü ilk parametre bizim için önemsiz -> _
'''thresh = 60 -> 60 üstündeki değerleri göstermez,
maxval=255 -> max değeri belirtir
THRESH_BINARY -> eşik türlerinde kullanılacak max ve min değerleri arasını siler (60-255 - beyaz)
THRESH_BINARY_INV -> ise tam aksini yapar (siyah)'''

plt.figure()
plt.imshow(thresh_img, cmap = "gray")
plt.axis("off")
plt.show()

#uyaralmalı eşik değeri
# fotoğraftaki bütünülüğü sağlayacak şekilde görünütyü işler, genel hatlar eşiklemedeki gibi kaybolmaz
thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11,8)
# 255 max value
# ADAPTIVE_THRESH_MEAN_C -> kullanılacak uyarlanabilir eşikleme algortiması için yöntem
''' 8 -> ADAPTIVE_THRESH_MEAN_C deki C ye denk geliyor, c ye göre bir ortalama alınır ve threshold 
değerine denk gelir '''
# THRESH_BINARY -> eşikleme türü, yeni resmin pixellerinin hangi değerleri alacağını belirtir
# 11 -> block size 

plt.figure()
plt.imshow(thresh_img2, cmap = "gray")
plt.axis("off")
plt.show()
