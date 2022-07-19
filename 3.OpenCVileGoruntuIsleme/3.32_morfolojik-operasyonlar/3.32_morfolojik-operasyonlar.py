# -*- coding: utf-8 -*-

# Erozyon = Ön taraftaki nesnenin sınırlarını aşındırır
# Genişleme = Görüntüdeki beyaz bölmeyi attırır
# Açma = Erozyon + Genişleme (Gürültünün azaltılmasını sağlar)
# Kapatma = Genişleme + Erozyon (Ön plandaki nesnelerin içindeki delikler veya nesne üzerindeki 
#           küçük siyah noktaları kapatmak için kullanışlıdır)
# Morfolojik Gradyan = Görüntünün genişlemesi e erozyonu arasındaki fark

import cv2
import matplotlib.pyplot as plt
import numpy as np

# resmi içe aktar
img = cv2.imread('github.png')
plt.figure(), plt.imshow(img, cmap = 'gray'), plt.axis('off'), plt.title('Orijinal Görsel')

# Erozyon
kernel = np.ones((5,5), dtype = np.uint8)
result = cv2.erode(img, kernel, iterations = 1) # 1 erozoyon yapar
plt.figure(), plt.imshow(result, cmap = 'gray'), plt.axis('off'), plt.title('Erozyon Görsel')

# Genişleme - Dilation
result2 = cv2.dilate(img, kernel, iterations = 1)
plt.figure(), plt.imshow(result2, cmap = 'gray'), plt.axis('off'), plt.title('Genişleme')

# White Noise
whiteNoise = np.random.randint(0, 2, size = img.shape[:2])
whiteNoise = whiteNoise *255

#Açılma 

