# -*- coding: utf-8 -*-

''' ortalama bulanıklaştırma: bir görüntünün normalleştirilmiş bir kutu filtresiyle sarılamsı ile
yapılır. çekirdek alanı altındaki tüm pixellerin ortalamasını alır ve bu ortalamayı merkezi öğe 
ile yer değiştirir'''

'''gauss bulanıklaştırma: kutu filtrsi yerine gauss çekirdeği kullanılır. pozitif ve tek olması 
gereken çekirdeğin genişliği ve yüksekliğni belirtir. sigmaX ve sigmaY, X ve Y yönlerindeki 
standart sapmayı belirtmeliyiz'''

'''medyan bulanıklaştırma: çekirdek alanı altındaki tüm pixellerin medyanını alır ve merkezi öğe
bu medyan değerle değiştirilir. tuz ve biber gürültüsüne karşı oldukça etkilidir (ekrandaki
siyah-beyaz noktacıklara tuz ve biber gürültüsü denir)'''

import cv2
import matplotlib.pyplot as plt 
import numpy as np
import warnings
warnings.filterwarnings('ignore')

img = cv2.imread('nyc.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img)
plt.axis('off')
plt.title('orijinal')
plt.show()