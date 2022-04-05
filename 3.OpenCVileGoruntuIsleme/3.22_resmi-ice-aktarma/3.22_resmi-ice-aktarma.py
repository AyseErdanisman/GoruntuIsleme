# -*- coding: utf-8 -*-

import cv2

# içe aktarma
image = cv2.imread('cats.jpg', 0)
# 0 görünütün siyah beyaz olarak gösterilmesini sağladı (grey screen)

# görselleştrime 
cv2.imshow('Ilk Fotograf', image)
'''image değişkenindeki tutulan sayılar her bir pixelin değerini
ifade eder ve bu rakalmalar 0 - 255 arasıda değişir, size kısmındaki 458 ve 432 
değer de 458*432 den fotoğrafın 197856 pixelden olştuğu anlamına gelir'''

k = cv2.waitKey(0) &0xFF
'kalvyeden komut bekliyor'

if k == 27:
    # 27 esc tuşunun karşılığı
    cv2.destroyAllWindows()
    # tüm pencereleri kapatır
elif k == ord('s'):
    cv2.imwrite('gray_cats.png', image)
    # kalvyede s tuşuna basıldığında fotoğrafı siyah beyaz olarak kaydeder
    # image bizim fotoğrafımız | gray_cats.png kaydedeceği dosya ismi
    cv2.destroyAllWindows()