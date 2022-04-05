# -*- coding: utf-8 -*-

import cv2

img = cv2.imread('cats.jpg', 0)
print('resim boyutu: ', img.shape)
# resim boyutunu yazdırır

# resized
cv2. imshow('Orijinal', img)
imgResized = cv2.resize(img, (250, 250))
print('resized img shape: ', imgResized.shape)
cv2.imshow('img resized', imgResized)

# kırpma
imgCropoed = img[:350,0:400] -> yukseklik / genislik
# 200 e 300 olan pixelleri aldık
# x ekseni 0-200 pixel
# y ekseni 0-300 pixel seçildi

cv2.imshow('kirpik resim', imgCropoed) 
