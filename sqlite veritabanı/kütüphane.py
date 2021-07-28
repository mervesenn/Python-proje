import sqlite3
import time
class Kitap():
    def __init__(self,isim,yazar,yayınevi,tür,baskı):
        self.isim = isim
        self.yazar = yazar
        self.yayınevi = yayınevi
        self.tür = tür
        self.baskı = baskı
    def __str__(self):
        return "Kitap ismi: {}\nYazar: {}\nYayınevi: {}\nTür: {}\nBaskı: {}\n".format(self.isim,self.yazar,self.yayınevi,self.tür,self.baskı)

class Kütüphane():
    def __init__(self):
        self.baglantıolustur()
    def baglantıolustur(self):
        self.baglantı = sqlite3.connect("kütüphane.db")
        self.cursor = self.baglantı.cursor()
        sorgu ="Create Table If not exists kitaplar(isim TEXT,yazar TEXT,yayınevi TEXT,tür TEXT,baskı INT)"
        self.cursor.execute(sorgu)
        self.baglantı.commit()
    def baglantıyıkes(self):
        self.baglantı.close()
    def kitaplarıgöster(self):
        sorgu = "Select * From kitaplar"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()
        if (len(kitaplar) == 0):
            print("Kütüphanede kitap bulunmuyor..")
        else:
            for i in  kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)
    def kitapsorgula(self,isim):
        sorgu = "Select * From kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar = self.cursor.fetchall()
        if (len(kitaplar) == 0):
            print("böyle bir kitap bulunmuyor...")
        else:
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
            print(kitap)
    def kitapekle(self,kitap):
        sorgu = "Insert into kitaplar Values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayınevi,kitap.tür,kitap.baskı))
        self.baglantı.commit()
    def kitapsil(self,isim):
        sorgu = "Delete From kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.baglantı.commit()
    def baskıyükselt(self,isim):
        sorgu = "Select * From kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar = self.cursor.fetchall()
        if (len(kitaplar) == 0):
            print("böyle bir kitap bulunmuyor...")
        else:
            baskı = kitaplar[0][4]
            baskı += 1
            sorgu2 = "Update kitaplar set baskı = ? where isim = ?"
            self.cursor.execute(sorgu2,(baskı,isim))
            self.baglantı.commit()





















