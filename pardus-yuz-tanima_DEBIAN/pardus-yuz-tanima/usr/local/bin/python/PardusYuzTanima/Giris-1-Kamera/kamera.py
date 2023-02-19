import cv2
import os

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    cv2.imshow("Kamera",frame)
    if cv2.waitKey(50):
        cv2.imwrite('.kamera_giris/giris.png',frame)
        os.system("python3 /usr/local/bin/python/PardusYuzTanima/Giris-2-Karsilastirma/giris_karsilastir.py")
        break
    

cap.release()
cv2.destroyAllWindows()
