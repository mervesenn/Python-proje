import sqlite3
import time

class Sarki():
    def __init__(self,sarkiismi,sanatci,album,produksiyonsirketi,dakika,saniye):
        self.sarkiismi = sarkiismi
        self.sanatci = sanatci
        self.album = album
        self.produksiyonsirketi = produksiyonsirketi
        self.dakika = dakika
        self.saniye = saniye
        self.sure = str(self.dakika) + ":" + str(self.saniye)
        
    def __str__(self):
        return "{}/ {}/ {}/ {}/ {}\n".format(self.sarkiismi,self.sanatci,self.album,self.produksiyonsirketi,self.dakika,self.saniye)
    
class Kutuphane():
    def __init__(self):
        self.baglanti = sqlite3.connect("şarkıkütüphanesi.db")
        self.imlec = self.baglanti.cursor()
        self.imlec.execute("Create Table If not exists Sarkilar(İsim TEXT,Sanatci TEXT,Album TEXT,Produksiyonsirketi TEXT,Dakikasüre INT,Saniyesüre INT)")
        self.baglanti.commit()
    def baglantikes(self):
        self.baglanti.close()
    def bilgilerigoster(self):
        self.imlec.execute("Select * From Sarkilar")
        a = self.imlec.fetchall()
        print("(Sıralama: Şarkı ismi/ Sanatçı/ Albüm/ Prodüksiyon şirketi/ Şarkı süresi)\n")
        for i in a:
            print(Sarki(i[0],i[1],i[2],i[3],i[4],i[5]))
            
    def sarkiekle(self):
        print("Lütfen sizden istenilen bilgileri uygun yerlere yazın.)")
        time.sleep(2)
        sarkiismi = input("Şarkı ismi:")
        if (sarkiismi == "q"):
            print("Geri dönülüyor...")
            time.sleep(2)
            return
        
        sanatci = str(input("Sanatçı adı:"))
        if(sarkiismi == "q"):
            print("Geri dönülüyor...")
            time.sleep(2)
            return
        
        album = str(input("Albüm adı:"))
        if (sarkiismi == "q"):
            print("Geri dönülüyor...")
            time.sleep(2)
            return
        
        produksiyonsirketi = str(input("Prodüksiyon şirketi:"))
        if (produksiyonsirketi == "q"):
            print("Geri dönülüyor...")
            time.sleep(2)
            return
        
        try:
            sarkisuresidakika = int(input("Şarkı süresi(dakika):"))
            if (sarkiismi == "q"):
                print("Geri dönülüyor...")
                time.sleep(2)
                return
            
            sarkisuresisaniye = int(input("Şarkı süresi(saniye):"))
            if (sarkiismi == "q"):
                print("Geri dönülüyor...")
                time.sleep(2)
                return
            
        except (ValueError):
            print("Lütfen rakam giriniz.\n")
            return Kutuphane.sarkiekle()
        
        print("Şarkı ekleniyor...")
        time.sleep(2)
        self.imlec.execute("Insert into Sarkilar Values(?,?,?,?,?,?)",(sarkiismi,sanatci,album,produksiyonsirketi,sarkisuresidakika,sarkisuresisaniye))
        self.baglanti.commit()
        print("Şarkı eklendi...")
        
    def sarkisil(self):
        print("Şarkılar:")
        self.imlec.execute("Select İsim From Sarkilar")
        a = self.imlec.fetchall()
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
                self.imlec.execute("Delete From Sarkilar Where İsim = ?",(isim,))
                self.baglanti.commit()
                print("Şarkı silindi.")
                
            elif (i[0] != isim):
                print("Böyle bir isimde şarkı kütüphanede yok.")
                continue
                
    def toplamsure(self):
        self.imlec.execute("Select Dakikasüre, Saniyesüre From Sarkilar")
        a = self.imlec.fetchall()
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
kutuphane = Kutuphane()
print("\tŞarkı kütüphanesi v1.0")
time.sleep(1)
print("\n\t Hoşgeldiniz\n\n(Yardım almak istiyorsanız(h), çıkmak istiyorsanız(q) tuşuna basın.)")
while True:
    print("******************************\n")
    islem = input("----->")
    print("-------------------------\nİşlem yapılıyor,lütfen bekleyiniz...\n---------------------------")
    time.sleep(2)
    if(islem == "q" or islem == "Q"):
        print("Uygulamadan çıkılıyor...")
        time.sleep(2)
        print("\t Hoşçakalın")
        break
        
    elif(islem == "h" or islem == "H"):
        kutuphane.yardim()
        
    elif(islem == "Şarkıları göster" or islem == "ŞARKILARI GÖSTER" or islem == "şarkıları göster"):
        print("Şarkılar:")
        kutuphane.bilgilerigoster()
        
    elif(islem == "Şarkı ekle" or islem == "ŞARKI EKLE" or islem == "şarkı ekle"):
        kutuphane.sarkiekle()
        
    elif(islem == "Şarkı sil" or işlem == "ŞARKI SİL" or islem == "şarkı sil"):
        kutuphane.sarkisil()
        
    elif(islem  == "Toplam süreyi göster" or islem == "TOPLAM SÜREYİ GÖSTER" or islem == "toplam süreyi göster"):
        kutuphane.toplamsure()
         
    else:
        print("Geçersiz işlem")


















