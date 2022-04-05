# -*- coding: utf-8 -*-

import cv2
import time 

#video ismi
video_name = 'MOT17-04-DPM.mp4'

# video ice aktarma(capture)
cap = cv2.VideoCapture(video_name)

print('Genislik: ', cap.get(3))
# get in 3. indexi genislige denk gelir
print('Yukseklik: ', cap.get(4))
# 4 -> yukseklik

# vido boş bile olsa cap değişkenine yüklenir bunu kontol etmek için:
if cap.isOpened() == False:
    print('Hata: Video yuklenemedi')

while True:
    # video okuma
    ret, frame = cap.read()
    # read bize return ve frame olmak üzere iki değer döndürür
    # frame -> video içerisinde bulunan her bir fotoğraf
    # return -> ture/false
    
    if ret == True: 
        # time.sleep(0.01)
        # framelerin hızını yavaşlattık (10ms)
        cv2.imshow('Video', frame)
        # fotoğrafı görselleştirdik
        
        ''' burada okunan sadece 1 fotoğraf, bunun video olabilmesi için döngü ile
        ard ard sürkli okunması gerekir (while)'''
    else: break
    # return değer döndürmeyi bitirdiğinde döngüyü kırdı
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    ''' 1. if de gösterilecek bir şey kalamdığı için, 2. if de kendi isteğimle
    videodan çıkmış oluyorum '''
    
cap.release()
# video captue durdurulur. 
cv2.destroyAllWindows()
    
    
    
    
    
    
    
    
    
    
    