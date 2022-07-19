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
#uyarıları kaldırır 

#bluring (detayı azaltır, gürültüyü engeller)
img = cv2.imread('nyc.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure() # figür oluşturuldu 
plt.imshow(img) # figür içine görsel eklendi
plt.axis('off')   # eksenler kapatıldı
plt.title('orijinal')
plt.show()

# ortalama bulanıklaştırma yöntemi
dst2 = cv2.blur(img, ksize = (3,3)) # ksize (kutucuk boyutu)
plt.figure(), plt.imshow(dst2), plt.axis('off'), plt.title('Ortalama Bluring')
# opencv dökümantasyonlarında çıktılar dst olarak girdiler src(source) olarak adlandırılır

#Gaussian Blur
gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX = 7) #sigmaY'yi yazmazsan sigmaX'e otomatik olarak eşit olur
plt.figure(), plt.imshow(gb), plt.axis('off'), plt.title('Gaussian Blur')

# Medyan Blur
mb = cv2.medianBlur(img, ksize = 3)
plt.figure(), plt.imshow(mb), plt.axis('off'), plt.title('Medyan Blur')

# Noise
def gaussianNoise(image):
    row, col, ch = image.shape
    #row (satır), col(colon-sütun), ch(chanel(rgm mi(3) greyscale(1) mi olduğunu gösterir))
    mean = 0 # ortalama 
    var = 0.05 # varyansı standart sapmayı elde etmek için kullanıyoruz
    sigma = var**0.5 #standart sapma varyansın kare köküdür
    
    gauss = np.random.normal(mean, sigma, (row,col,ch))
    # gauss un diğer adı normal değılım
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss
    
    return noisy   

# İçe Aktarma
# Normalizasyon
img = cv2.imread('nyc.jpg')
img = cv2. cvtColor(img, cv2.COLOR_BGR2RGB)/255 
plt.figure(), plt.imshow(img), plt.axis('off'), plt.title('orijinal'), plt.show()
  
''' oluşturulan görüntü 0 ortalamalı bir görüntü olduğu için fotoğraf değerlerini 0-1 
arasına indirgedik, eğer 0-255 arasındayken ekleseydik gürültü küçük olduğu için herhangi 
bir şey gözükmeyecekti'''

# gaussian blur ile noise u azaltır
gaussianNoisyImage = gaussianNoise(img)
plt.figure(), plt.imshow(gaussianNoisyImage), plt.axis('off'), plt.title('Gaussian Noisy'), plt.show()

gb2 = cv2.GaussianBlur(gaussianNoisyImage, ksize = (3,3), sigmaX = 7)
plt.figure(), plt.imshow(gb2), plt.axis('off'), plt.title('with Gaussian Blur'), plt.show()

# tuz karabiler gürültüsünü(siyah beyaz noktaların rastgele dağılması) medyan bulur ile kaldırma
def saltPapperNoise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5 # siyah beyaz oranı (%50 - %50)
    amount = 0.004
    noisy = np.copy(image) # orijinal görüntüyü bozmamak için kopyasını noisy e oluşturdu
    
    # salt
    num_salt = np.ceil(amount * image.size * s_vs_p) # beyaz nokta sayısını belirtir
    # ceil ondalıklı sayıyı yuvarlar (1.2 - 1.0)
    coords = [np.random.randint(0, i-1, int(num_salt)) for i in image.shape] # beyaz noktaların kordinatlarını rastgele belirler
    #rastgele int degerler döndürür
    noisy[coords] = 1 # beyaz(1) noktaları ekledi
    
    #pepper 
    num_pepper = np.ceil(amount * image.size* s_vs_p)
    coords = [np.random.randint(0, i-1, int(num_pepper)) for i in image.shape]
    noisy[coords] = 0
    
    return noisy

spImage = saltPapperNoise(img)
plt.figure(), plt.imshow(spImage), plt.axis('off'), plt.title('Salt-Paper'), plt.show()

mb2 = cv2.medianBlur(spImage.astype(np.float32), ksize = 3)
# format uyuşmadığı için astype ile float 32ye çevirdik (öncesinde float 64)
plt.figure(), plt.imshow(mb2), plt.axis('off'), plt.title('Salt-Paper with median blur'), plt.show()
    
     

    
    
    