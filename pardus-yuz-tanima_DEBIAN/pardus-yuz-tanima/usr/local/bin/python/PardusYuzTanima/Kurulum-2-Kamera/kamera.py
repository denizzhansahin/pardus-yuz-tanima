import cv2
import os

import time


cap = cv2.VideoCapture(0)
deger = 1

while True:
    ret,frame = cap.read()
    
    cv2.imshow("Kamera",frame)

    
    if cv2.waitKey(5000):
        cv2.imwrite('.kamera_kayit/kayit.png',frame)
        os.system("python3 /usr/local/bin/python/PardusYuzTanima/Kurulum-3-Son/kurulum_son.py")
        break
    
    if cv2.waitKey(50) & 0xFF == ord('B'):
        break

cap.release()
cv2.destroyAllWindows()
