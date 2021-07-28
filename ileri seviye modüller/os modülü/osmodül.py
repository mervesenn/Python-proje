import os
from datetime import datetime
#print(os.getcwd())
#print(datetime.fromtimestamp(os.stat("test.txt").st_mtime))

for klasöryolu,klasörisimleri,dosyaisimleri in os.walk("C:/Users/Hp/Desktop"):
    #print("klasör yolu",klasöryolu)
    #print("klasör isimleri", klasörisimleri)
    #print("dosya isimleri", dosyaisimleri)
    #print("--------------------------")
    for i in dosyaisimleri:
        if (i.endswith(".txt")):
            print(i)