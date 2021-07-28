import os
def dosyayazdır(isim,belge):
    dosyalar = []
    with open("{}".format(belge),"r+",encoding = "utf-8") as file:
        for i in file:
            i = i.strip("\n")
            dosyalar.append(i)
        if not (isim in dosyalar):
            file.write(isim+"\n")
dosyalar = os.walk("C:\\")

file1 = open("C://Users/Hp/Desktop/txtdosyaları.txt","a+")
file2 = open("C://Users/Hp/Desktop/pdfdosyaları.txt","a+")
file3 = open("C://Users/Hp/Desktop/mp4dosyaları.txt","a+")

file1.close()
file2.close()
file3.close()

for kyolu,kisimleri,disimleri in dosyalar:
    for i in disimleri:
        if i.endswith(".txt"):
            dosyayazdır(kyolu + i,"C://Users/Hp/Desktop/txtdosyaları.txt")
        elif i.endswith(".mp4"):
            dosyayazdır(kyolu + i,"C://Users/Hp/Desktop/mp4dosyaları.txt")
        elif i.endswith(".pdf"):
            dosyayazdır(kyolu + i,"C://Users/Hp/Desktop/pdfdosyaları.txt")

