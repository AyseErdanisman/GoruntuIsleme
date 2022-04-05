# -*- coding: utf-8 -*-

import cv2

# capture 
cap = cv2.VideoCapture(0)
# 0 default kamerayı temsil eder, harici kamera takıyorsanız 0 ya da 1 olarak ifade edilir

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) 
# videonun frame genişliğini aldık
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# yukseklik
print(width, height)


# video kaydet
writer = cv2.VideoWriter('video_kaydi.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width, height))
# dosya adı video_kaydi.mp4 
'''fourcc(*'DIVX') -> windows için kullandık, çerçeveleri sıkıştımak için kullanılan
4 karakterli codec kodu '''
# 20 -> saniyeeki frame sayısı, video akış hızı
# (width, height) -> çerçeve boyutu

while True: 
    '''while döngüsü kırılamdığı sürece frameleri frame değşkenin aktarır,
    frame in gelip gelmediğini de return ile kontrol eder'''
    ret, frame = cap.read()
    
    cv2.imshow('Video', frame)
    # videoyu gösterir
    writer.write(frame)
    # videoyu kaydeder 
    
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
writer.release()
cv2.destroyAllWindows()



