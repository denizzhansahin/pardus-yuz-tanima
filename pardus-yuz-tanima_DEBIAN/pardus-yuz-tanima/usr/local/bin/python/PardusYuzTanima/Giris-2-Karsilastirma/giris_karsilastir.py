from deepface import DeepFace

import sqlite3
import time
import os


veri_tabani = sqlite3.connect('.pardus_yuz_tanima.sqlite')
imlec = veri_tabani.cursor()
    

import os
print(os.system("pwd"))

a = ".kamera_kayit/kayit.png"
b = ".kamera_giris/giris.png"

deniz = DeepFace.verify(a, b
     , model_name = "ArcFace"
     , detector_backend = "retinaface")

print(deniz["verified"])

if deniz["verified"] == True:
     
     zaman = time.asctime()
     dosya_adi = " "
     veri = (zaman,"True",dosya_adi)
     sql = """INSERT INTO giris_kaydi VALUES(?,?,?) """
     imlec.execute(sql,veri)
     veri_tabani.commit()
     veri_tabani.close()

     os.system("python3 /usr/local/bin/python/PardusYuzTanima/Giris-3-Sonuc/giris_basarili.py")

else:
     
     zaman = time.asctime()
     dosya_adi = ".kamera_giris/hatali_giris/"+str(zaman)+".png"
     veri = (zaman,"False",dosya_adi)
     
     sql = """INSERT INTO giris_kaydi VALUES(?,?,?) """
     imlec.execute(sql,veri)
     veri_tabani.commit()
     veri_tabani.close()
     
     os.rename(".kamera_giris/giris.png", ".kamera_giris/hatali_giris/giris.png")
     os.rename(".kamera_giris/hatali_giris/giris.png",dosya_adi)


     os.system("python3 /usr/local/bin/python/PardusYuzTanima/Giris-3-Sonuc/giris_basarisiz.py")
