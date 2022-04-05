# -*- coding: utf-8 -*-

import cv2 
import numpy as np

#resmi içe aktar
img = cv2.imread('kart.png')
cv2.imshow('orijinal',  img)

#boyut belirleme 
width = 400
height = 500

#point 1 -> resmin 4 köşesinin pixel değeri 
#point 2 -> dönüştürmek istediğimiz resmin köşe değerleri 

point1 = np.float32([[203,1], [1,472], [540,150], [338,617]])
point2 = np.float32([[0,0], [0, height], [width, 0], [width, height]])

#transfom matrisi
matrix = cv2.getPerspectiveTransform(point1, point2)
'''iki noktayı verdikten sonra birinci noktadan ikinci noktaya geçmek için gerekli 
olan transform matrisi oluşturulur. (3x3)'''
print(matrix)

#dönüştürülmüş resim
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
#(resim, rotasyon matrisi, boyutlar)

cv2.imshow('donusturulmus resim', imgOutput)
