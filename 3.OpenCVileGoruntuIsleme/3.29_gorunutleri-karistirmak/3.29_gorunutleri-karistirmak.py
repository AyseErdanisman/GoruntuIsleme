# -*- coding: utf-8 -*-

import cv2
import matplotlib.pyplot as plt

#karşılaştırma 
img1 = cv2.imread('venus.jpg')
'''opencv de renkli resimleri yüklerken default olarak bgr olarak gelir, 
orijinal renkeler çevirmek için'''
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
#bgr to rgb
img2 = cv2.imread('jupiter.jpg')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

#birleştirme için aynı boyutta olmak zorunda
print('eski boyutlar')
print(img1.shape)
print(img2.shape)
print()

print('yeni boyutlar')
img1 = cv2.resize(img1, (600,600))
print(img1.shape)

img2 = cv2.resize(img2, (600,600))
print(img2.shape)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

#karıştırılmış resim = alpha*img1 + beta*img2
blended = cv2.addWeighted(src1 = img1, alpha = 0.5, src2 = img2, beta = 0.5, gamma = 0)
plt.figure()
plt.imshow(blended)







