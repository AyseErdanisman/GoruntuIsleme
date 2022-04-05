# -*- coding: utf-8 -*-

import cv2
import numpy as np

#resim oluştur 
img = np.zeros((512, 512, 3), np.uint8)
# 512 512 3 boyutlarına sahip siyah bir resim oluşur, uint8 -> integer
# zeros u ones yapsaydık beyaz bir görünütü elde ederdik
print(img.shape)
cv2.imshow('siyah', img)

# çizgi
cv2.line(img, (0,0), (512,512), (0,255,0), 3) 
# (resim, başlagıç noktası, bitiş noktası, renk(yeşil),  çizgi kalınlığı)
'''opencv rgb olarak değil bgr olarak kabul eder.
(0,0,255) normalde blue yu temsil ederken opencv de red i temsil eder'''
cv2.imshow('cizgi', img )

#dikdörtgen
cv2.rectangle(img, (30,30), (256,256), (255,0,0), cv2.FILLED)
#(resim, başlangıç noktası, bitiş noktası, renk)
# cv2.FILLED -> içini doldurur 
cv2.imshow('dikdortgen', img)

# çember 
cv2.circle(img, (300,300), 45, (0,0,255), cv2.FILLED)
# (resim, merkez, yarıçap, renk)
cv2.imshow('cember', img)

#metin
cv2.putText(img, 'resim', (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
#(resim, başlangıç noktası, font, kalınlık, renk)
cv2.imshow('yazi', img)