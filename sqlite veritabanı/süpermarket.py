import sqlite3
import time

class Ürün():
    def __init__(self,urun,adet,marka,fiyat):
        self.urun = urun
        self.adet = adet
        self.marka = marka
        self.fiyat = fiyat
    def __str__(self):
        return "Ürün: {}\nAdet: {}\nMarka: {}\nFiyat: {} Tl\n".format(self.urun,self.adet,self.marka,self.fiyat)
class Market():
    def __init__(self):
        self.baglantıolustur()
    def baglantıolustur(self):
        self.baglantı = sqlite3.connect("supermarket.db")
        self.cursor = self.baglantı.cursor()
        komut = "Create Table If not exists supermarket(Ürün TEXT,Adet INT,Marka TEXT,Fiyat FLOAT)"
        self.baglantı.execute(komut)
        self.baglantı.commit()
    def baglantıkes(self):
        self.baglantı.close()
    def ürünlerigöster(self):
        komut = "Select * From supermarket"
        self.cursor.execute(komut)
        ürünler = self.cursor.fetchall()
        if len(ürünler) == 0:
            print("Süpermarkette ürün bulunmuyor.")
        else:
            for i in ürünler:
                urun = Ürün(i[0],i[1],i[2],i[3])
                print(urun)
    def ürünekle(self):
        komut = "Insert into supermarket Values(?,?,?,?)"
        self.cursor.execute(komut,(Ürün.urun,Ürün.adet,Ürün.marka,Ürün.fiyat))
        self.baglantı.commit()
    def ürünsil(self):
        komut = "Delete From supermarket Where Ürün = ?"
        self.cursor.execute(komut,(Ürün,))
        self.baglantı.commit()
    def adetazalt(self,urun,miktar):
        komut = "Select Adet From supermarket Where Ürün = ?"
        self.cursor.execute(komut,(Ürün,))
        ürünadeti = self.cursor.fetchall()
        for i in ürünadeti:
            for j in i:
                if j <= 0:
                    print("Stokta bu üründen kalmadı.")
                else:
                    yeniadet = j - miktar
                    komut2 = "Update supermarket set Adet = ? Where Ürüm = ?"
                    self.cursor.execute(komut2,(yeniadet,Ürün,))
                    self.baglantı.commit()
    def adetekle(self,urun,miktar):
        komut = "Select Adet From supermarket Where Ürün = ?"
        self.cursor.execute(komut,(Ürün,))
        ürünadeti = self.cursor.fetchall()
        for i in ürünadeti:
            for j in i:
                yeniadet = j + miktar
                komut2 = "Update supermarket set Adet = ? Where Ürün = ?"
                self.cursor.execute(komut2,(yeniadet,Ürün,))
                self.baglantı.commit()
supermarket = Market()

print("""
-----------------------
Süpermarket Uygulaması
-----------------------
1.Ürünleri gör
2.Ürün ekle
3.Ürün sil
4.Satış yap
5.Stok ekle
q-Çıkış
-----------------------
""")
while True:
    x = input("İşlem giriniz:")
    if x == "q":
        print("Çıkış yapılıyor...")
        time.sleep(1)
        print("Hoşçakalın")
        supermarket.baglantıyıkes()
        break
    elif x == "1":
        supermarket.ürünlerigöster()
    elif x == "2":
        urun = input("Ürünün adını girin:")
        adet = int(input("Ürünün adetini girin:"))
        marka = input("Ürünün markasını girin:")
        fiyat = float(input("Ürünün fiyatını girin:"))
        yeniürün = Ürün(urun,adet,marka,fiyat)
        print("Ürün ekleniyor...")
        time.sleep(1)
        supermarket.ürünekle(yeniürün)
        print("Ürün eklendi")
    elif x == "3":
        urun = input("Silmek istediğiniz ürünü girin:")
        rly = input("Emin misiniz? (E/H): ")
        if rly == "E":
            print("Ürün siliniyor...")
            time.sleep(1)
            supermarket.ürünsil(urun)
            print("Ürün silindi")
    elif x == "4":
        urun = input("Hangi ürünü sattınız?:")
        adet = int(input("Kaç adet sattınız?:"))
        print("Satış bilgileri giriliyor....")
        time.sleep(1)
        supermarket.adetazalt(urun,adet)
        print("Bilgiler başarıyla güncellendi")
    elif x == "5":
        urun = input("Hangi ürüne stok ekleyeceksiniz?:")
        adet = int(input("Kaç adet ekleyeceksiniz?:"))
        print("Stok bilgileri giriliyor...")
        time.sleep(1)
        supermarket.adetekle(urun,adet)
        print("Bilgiler başarıyla güncellendi")
    else:
        print("Hatalı işlem")




























































