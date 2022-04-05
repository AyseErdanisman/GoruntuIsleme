# -*- coding: utf-8 -*-

import cv2
import numpy as np

#fotoğrafı içe aktar
img = cv2.imread('cats.jpg')
cv2.imshow('orijinal', img)

#horizontal - yatay
hr = np.hstack((img,img))
cv2.imshow('horizontal', hr)

#vertical - dikey
vr = np.vstack((img, img)) #tuple
cv2.imshow('dikey', vr)