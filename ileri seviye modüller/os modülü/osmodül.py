import os
from datetime import datetime

#print(os.getcwd())
#print(datetime.fromtimestamp(os.stat("test.txt").st_mtime))

for klasoryolu, klasorisimleri, dosyaisimleri in os.walk("C:/Users/Hp/Desktop"):
    #print("klasör yolu", klasoryolu)
    #print("klasör isimleri", klasorisimleri)
    #print("dosya isimleri", dosyaisimleri)
    #print("--------------------------")
    
    for i in dosyaisimleri:
        if (i.endswith(".txt")):
            print(i)
