import time
class Hayvanlar():
    
    def __init__(self, tur = "omurgasızlar ve omurgalılar", yasamalani = "kara,hava ve su", beslenmecesiti = "etçil,otçul veya hem etçil hem otçul", ayaksayisi = "2-4 arasında değişmektedir"):
        self.tur = tur
        self.yasamalanı = yasamalani
        self.beslenmecesiti = beslenmecesiti
        self.ayaksayisi = ayaksayisi
        
    def bilgilerigoster(self):
        print("hayvanların genel özellikleri")
        print("1)türü:{}\n2)yaşam alanı:{}\n3)beslenme çeşiti:{}\n4)ayak sayısı:{}\n".format(self.tur, self.yasamalani, self.beslenmecesiti, self.ayaksayisi))
        
class Kopekler(Hayvanlar):
    def __init__(self, tur = "memeli", yasamalani = "kara", beslenmecesiti = "etçil", ayaksayisi = "4", tipikozellikleri = ["hızlıdırlar","fazla doğum yaparlar","ömürleri kısadır"], cinsleri = ["Rotweiler","Dogo","Pitbull","Golden"]):
        super().__init__(tur, yasamalani, beslenmecesiti, ayaksayisi)
        print("Köpek class'ının init fonksiyonu")
        self.cinsleri = cinsleri
        self.tipikozellikleri = tipiközellikleri
        
    def bilgilerigoster(self):
        print("Köpeklerin genel özellikleri")
        print("1)türü:{}\n2)yaşam alanı:{}\n3)beslenme çeşiti:{}\n4)ayak sayısı:{}\n5)tipik özellikleri:{}\n6)cinsleri:{}\n".format(self.tur, self.yasamalanı, self.beslenmecesiti, self.ayaksayisi, self.tipikozellikleri, self.cinsleri))
        
    def cinsekle(self):
        cinslistesi = input("cinsleri araya virgül koyarak giriniz:")
        listeler = cinslistesi.split(",")
        for i in listeler:
            self.cinsleri.append(i)
            
    def ozellikekle(self):
        tipik = input("aralarına virgül koyarak özellikleri giriniz:")
        tipiklistesi = tipik.split(",")
        for i in tipiklistesi:
            self.tipikozellikleri.append(i)
            
    def __str__(self):
        return "özellik sayısı:{}\ncins sayısı:{}\n".format(len(self.tipikozellikleri), len(self.cinsleri))

class Kuslar(Hayvanlar):
    def __init__(self, tur = "memeli", yasamalani = "hava ve kara", beslenmecesiti = "etçil", ayaksayisi = "2", tipikozellikleri = ["uçarlar","hızlıdırlar","uçma mesafeleri 10km çıkabilir"], cinsleri = ["Muhabbet Kuşu","Sultan Papağanı","Hint Bülbülü","Amazon Papağanı"]):
        super().__init__(tur, yasamalani, beslenmecesiti, ayaksayisi)
        print("Kuşların init fonksiyonu")
        self.cinsleri = cinsleri
        self.tipikozellikleri = tipikozellikleri
        
    def bilgilerigoster(self):
        print("Kuşların genel özellikleri")
        print("1)türü:{}\n2)yaşam alanı:{}\n3)beslenme çeşiti:{}\n4)ayak sayısı:{}\n5)tipik özellikleri:{}\n6)cinsleri:{}\n".format(self.tur, self.yasamalani, self.beslenmecesiti, self.ayaksayisi, self.tipikozellikleri, self.cinsleri))
        
    def cinsekle(self):
        cinslistesi = input("cinsleri araya virgül koyarak giriniz:")
        listeler = cinslistesi.split(",")
        for i in listeler:
            self.cinsleri.append(i)
            
    def ozellikekle(self):
        tipik = input("aralarına virgül koyarak özellikleri giriniz:")
        tipiklistesi = tipik.split(",")
        for i in tipiklistesi:
            self.tipikozellikleri.append(i)
            
    def __str__(self):
        return "özellik sayısı:{}\ncins sayısı:{}\n".format(len(self.tipikozellikleri), len(self.cinsleri))
    
class Atlar(Hayvanlar):
    def __init__(self, tur = "memeli", yasamalani = "kara", beslenmecesiti = "otçul", ayaksayisi = "4", tipikozellikleri = ["hızlıdırlar","nalları vardır","boyları uzundur"], cinsleri = ["Dole Pony","Arap Atı","İnhiliz Atı"]):
        super().__init__(tur, yasamalani, beslenmecesiti, ayaksayisi)
        print("Atlar class'ının init fonksiyonu")
        self.cinsleri = cinsleri
        self.tipikozellikleri = tipikozellikleri
        
    def bilgilerigoster(self):
        print("Atların genel özellikleri")
        print("1)türü:{}\n2)yaşam alanı:{}\n3)beslenme çeşiti:{}\n4)ayak sayısı:{}\n5)tipik özellikleri:{}\n6)cinsleri:{}\n".format(self.tur, self.yasamalani, self.beslenmecesiti, self.ayaksayisi, self.tipikozellikleri, self.cinsleri))
        
    def cinsekle(self):
        cinslistesi = input("cinsleri araya virgül koyarak giriniz:")
        listeler = cinslistesi.split(",")
        for i in listeler:
            self.cinsleri.append(i)
            
    def ozellikekle(self):
        tipik = input("aralarına virgül koyarak özellikleri giriniz:")
        tipiklistesi = tipik.split(",")
        for i in tipiklistesi:
            self.tipikozellikleri.append(i)
            
    def __str__(self):
        return "özellik sayısı:{}\ncins sayısı:{}\n".format(len(self.tipikozellikleri), len(self.cinsleri))
    
while True:
    print("""
    ****************
    Hayvanlar Aleminin Genel Özellikleri
    ****************
    1)hayvanların genel özellikleri
    2)köpeklerin genel özellikleri
    3)kuşların genel özellikleri
    4)atların genel özellikleri
    5)çıkış
    """)
    
    secim = input("işleminizi giriniz:")
    if secim == "1":
        hayvanlar = Hayvanlar()
        hayvanlar.bilgilerigoster()
        
    elif secim == "2":
        kopekler = Kopekler()
        kopekler.bilgilerigoster()
        time.sleep(1)
        sel = input("1)cins ekleme\n2)özellik ekleme\n3)özellik ve cins sayıları\n4)çıkış\n")
        if sel == "1":
            kopekler.cinsekle()
        elif sel == "2":
            kopekler.ozellikekle()
        elif sel == "3":
            print(kopekler)
        else:
            print("bu menüden çıkış yapılıyor")
            time.sleep(1)
            
    elif secim == "3":
        kuslar = Kuslar()
        kuslar.bilgilerigoster()
        time.sleep(1)
        sel = input("1)cins ekleme\n2)özellik ekleme\n3)özellik ve cins sayıları\n4)çıkış\n")
        if sel == "1":
            kuslar.cinsekle()
        elif sel == "2":
            kuslar.ozellikekle()
        elif sel == "3":
            print(kuslar)
        else:
            print("bu menüden çıkış yapılıyor")
            time.sleep(1)
            
    elif secim == "4":
        atlar = Atlar()
        atlar.bilgilerigoster()
        time.sleep(1)
        sel = input("1)cins ekleme\n2)özellik ekleme\n3)özellik ve cins sayıları\n4)çıkış\n")
        if sel == "1":
            atlar.cinsekle()
        elif sel == "2":
            atlar.ozellikekle()
        elif sel == "3":
            print(atlar)
        else:
            print("bu menüden çıkış yapılıyor")
            time.sleep(1)
            
    else:
        print("işleminiz sonlandırılıyor..")
        time.sleep(1)
        break


