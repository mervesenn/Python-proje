import sqlite3
import time

class Şarkı():
    def __init__(self,şarkıismi,sanatçı,albüm,prodüksiyonşirketi,dakika,saniye):
        self.şarkıismi = şarkıismi
        self.sanatçı = sanatçı
        self.albüm = albüm
        self.prodüksiyonşirketi = prodüksiyonşirketi
        self.dakika = dakika
        self.saniye = saniye
        self.süre = str(self.dakika) + ":" + str(self.saniye)
    def __str__(self):
        return "{}/ {}/ {}/ {}/ {}\n".format(self.şarkıismi,self.sanatçı,self.albüm,self.prodüksiyonşirketi,self.dakika,self.saniye)
class Kütüphane():
    def __init__(self):
        self.baglantı = sqlite3.connect("şarkıkütüphanesi.db")
        self.imleç = self.baglantı.cursor()
        self.imleç.execute("Create Table If not exists Şarkılar(İsim TEXT,Sanatçı TEXT,Albüm TEXT,Prodüksiyonşirketi TEXT,Dakikasüre INT,Saniyesüre INT)")
        self.baglantı.commit()
    def baglantıekes(self):
        self.baglantı.close()
    def bilgilerigöster(self):
        self.imleç.execute("Select * From Şarkılar")
        a = self.imleç.fetchall()
        print("(Sıralama: Şarkı ismi/ Sanatçı/ Albüm/ Prodüksiyon şirketi/ Şarkı süresi)\n")
        for i in a:
            print(Şarkı(i[0],i[1],i[2],i[3],i[4],i[5]))
    def şarkıekle(self):
        print("Lütfen sizden istenilen bilgileri uygun yerlere yazın.)")
        time.sleep(2)
        şarkıismi = input("Şarkı ismi:")
        if (şarkıismi == "q"):
            print("Geri dönülüyor...")
            time.sleep(2)
            return
        sanatçı = str(input("Sanatçı adı:"))
        if(şarkıismi == "q"):
            print("Geri dönülüyor...")
            time.sleep(2)
            return
        albüm = str(input("Albüm adı:"))
        if (şarkıismi == "q"):
            print("Geri dönülüyor...")
            time.sleep(2)
            return
        prodüksiyonşirketi = str(input("Prodüksiyon şirketi:"))
        if (prodüksiyonşirketi == "q"):
            print("Geri dönülüyor...")
            time.sleep(2)
            return
        try:
            şarkısüresidakika = int(input("Şarkı süresi(dakika):"))
            if (şarkıismi == "q"):
                print("Geri dönülüyor...")
                time.sleep(2)
                return
            şarkısüresisaniye = int(input("Şarkı süresi(saniye):"))
            if (şarkıismi == "q"):
                print("Geri dönülüyor...")
                time.sleep(2)
                return
        except (ValueError):
            print("Lütfen rakam giriniz.\n")
            return Kütüphane.şarkıekle()
        print("Şarkı ekleniyor...")
        time.sleep(2)
        self.imleç.execute("Insert into Şarkılar Values(?,?,?,?,?,?)",(şarkıismi,sanatçı,albüm,prodüksiyonşirketi,şarkısüresidakika,şarkısüresisaniye))
        self.baglantı.commit()
        print("Şarkı eklendi...")
    def şarkısil(self):
        print("Şarkılar:")
        self.imleç.execute("Select İsim From Şarkılar")
        a = self.imleç.fetchall()
        if (len(a) == 0):
            print("Şarkı listesi boş")
            return
        for i in a:
            print("-" + i[0])
        for i in a:
            isim = input("Silmek istediğiniz şarkının ismini giriniz:")
            if (isim == "q"):
                print("Geri dönülüyor...")
                time.sleep(2)
                return
            elif (i[0] == isim):
                print("Şarkı siliniyor...")
                time.sleep(2)
                self.imleç.execute("Delete From Şarkılar Where İsim = ?",(isim,))
                self.baglantı.commit()
                print("Şarkı silindi.")
            elif (i[0] != isim):
                print("Böyle bir isimde şarkı kütüphanede yok.")
                continue
    def toplamsüre(self):
        self.imleç.execute("Select Dakikasüre, Saniyesüre From Şarkılar")
        a = self.imleç.fetchall()
        geneltoplamdakika = 0
        geneltoplamsaniye = 0
        for i in a:
            geneltoplamdakika += i[0]
            geneltoplamsaniye += i[0]
        while True:
            if(geneltoplamsaniye >= 60):
                x = geneltoplamsaniye // 60
                geneltoplamsaniye %= 60
                geneltoplamdakika += x
                print(geneltoplamdakika,"dakika", geneltoplamsaniye,"saniye")
            else:
                return False
    def yardım(self):
        print("İşlemler:\n\tKütüphanedeki şarkıları görmek için:(Şarkıları göster),\n\tKütüphaneye şarkı eklemek için:(Şarkı ekle),\n\tKütüphaneden şarkı silmek için:(Şarkı sil),\n\tKütüphanedeki toplam şarkı süresini görmek için: (Toplam süreyi göster)yazınız.")
kütüphane = Kütüphane()
print("\tŞarkı kütüphanesi v1.0")
time.sleep(1)
print("\n\t Hoşgeldiniz\n\n(Yardım almak istiyorsanız(h), çıkmak istiyorsanız(q) tuşuna basın.)")
while True:
    print("******************************\n")
    işlem = input("----->")
    print("-------------------------\nİşlem yapılıyor,lütfen bekleyiniz...\n---------------------------")
    time.sleep(2)
    if(işlem == "q" or işlem == "Q"):
        print("Uygulamadan çıkılıyor...")
        time.sleep(2)
        print("\t Hoşçakalın")
        break
    elif(işlem == "h" or işlem == "H"):
        kütüphane.yardım()
    elif(işlem == "Şarkıları göster" or işlem == "ŞARKILARI GÖSTER" or işlem == "şarkıları göster"):
        print("Şarkılar:")
        kütüphane.bilgilerigöster()
    elif(işlem == "Şarkı ekle" or işlem == "ŞARKI EKLE" or işlem == "şarkı ekle"):
        kütüphane.şarkıekle()
    elif(işlem == "Şarkı sil" or işlem == "ŞARKI SİL" or işlem == "şarkı sil"):
        kütüphane.şarkısil()
    elif(işlem  == "Toplam süreyi göster" or işlem == "TOPLAM SÜREYİ GÖSTER" or işlem == "toplam süreyi göster"):
        kütüphane.toplamsüre()
    else:
        print("Geçersiz işlem")


















