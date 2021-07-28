import time
class Hayvanlar():
    def __init__(self,tür="omurgasızlar ve omurgalılar",yaşamalanı="kara,hava ve su",beslenmeçeşiti="etçil,otçul veya hem etçil hem otçul",ayaksayısı="2-4 arasında değişmektedir"):
        self.tür = tür
        self.yaşamalanı = yaşamalanı
        self.beslenmeçeşiti = beslenmeçeşiti
        self.ayaksayısı = ayaksayısı
    def bilgilerigöster(self):
        print("hayvanların genel özellikleri")
        print("1)türü:{}\n2)yaşam alanı:{}\n3)beslenme çeşiti:{}\n4)ayak sayısı:{}\n".format(self.tür,self.yaşamalanı,self.beslenmeçeşiti,self.ayaksayısı))
class Köpekler(Hayvanlar):
    def __init__(self,tür="memeli",yaşamalanı="kara",beslenmeçeşiti="etçil",ayaksayısı="4",tipiközellikleri=["hızlıdırlar","fazla doğum yaparlar","ömürleri kısadır"],cinsleri=["Rotweiler","Dogo","Pitbull","Golden"]):
        super().__init__(tür,yaşamalanı,beslenmeçeşiti,ayaksayısı)
        print("Köpek class'ının init fonksiyonu")
        self.cinsleri = cinsleri
        self.tipiközellikleri = tipiközellikleri
    def bilgilerigöster(self):
        print("Köpeklerin genel özellikleri")
        print("1)türü:{}\n2)yaşam alanı:{}\n3)beslenme çeşiti:{}\n4)ayak sayısı:{}\n5)tipik özellikleri:{}\n6)cinsleri:{}\n".format(self.tür,self.yaşamalanı,self.beslenmeçeşiti,self.ayaksayısı,self.tipiközellikleri,self.cinsleri))
    def cinsekle(self):
        cinslistesi = input("cinleri araya virgül koyarak giriniz:")
        listeler = cinslistesi.split(",")
        for i in listeler:
            self.cinsleri.append(i)
    def özellikekle(self):
        tipik = input("aralarına virgül koyarak özellikleri giriniz:")
        tipiklistesi = tipik.split(",")
        for i in tipiklistesi:
            self.tipiközellikleri.append(i)
    def __str__(self):
        return "özellik sayısı:{}\ncins sayısı:{}\n".format(len(self.tipiközellikleri),len(self.cinsleri))

class Kuşlar(Hayvanlar):
    def __init__(self,tür="memeli",yaşamalanı="hava ve kara",beslenmeçeşiti="etçil",ayaksayısı="2",tipiközellikleri=["uçarlar","hızlıdırlar","uçma mesafeleri 10km çıkabilir"],cinsleri=["Muhabbet Kuşu","Sultan Papağanı","Hint Bülbülü","Amazon Papağanı"]):
        super().__init__(tür,yaşamalanı,beslenmeçeşiti,ayaksayısı)
        print("Kuşların init fonksiyonu")
        self.cinsleri = cinsleri
        self.tipiközellikleri = tipiközellikleri
    def bilgilerigöster(self):
        print("Kuşların genel özellikleri")
        print("1)türü:{}\n2)yaşam alanı:{}\n3)beslenme çeşiti:{}\n4)ayak sayısı:{}\n5)tipik özellikleri:{}\n6)cinsleri:{}\n".format(self.tür,self.yaşamalanı,self.beslenmeçeşiti,self.ayaksayısı,self.tipiközellikleri,self.cinsleri))
    def cinsekle(self):
        cinslistesi = input("cinsleri araya virgül koyarak giriniz:")
        listeler = cinslistesi.split(",")
        for i in listeler:
            self.cinsleri.append(i)
    def özellikekle(self):
        tipik = input("aralarına virgül koyarak özellikleri giriniz:")
        tipiklistesi = tipik.split(",")
        for i in tipiklistesi:
            self.tipiközellikleri.append(i)
    def __str__(self):
        return "özellik sayısı:{}\ncins sayısı:{}\n".format(len(self.tipiközellikleri),len(self.cinsleri))
class Atlar(Hayvanlar):
    def __init__(self,tür="memeli",yaşamalanı="kara",beslenmeçeşiti="otçul",ayaksayısı="4",tipiközellikleri=["hızlıdırlar","nalları vardır","boyları uzundur"],cinsleri=["Dole Pony","Arap Atı","İnhiliz Atı"]):
        super().__init__(tür,yaşamalanı,beslenmeçeşiti,ayaksayısı)
        print("Atlar class'ının init fonksiyonu")
        self.cinsleri = cinsleri
        self.tipiközellikleri = tipiközellikleri
    def bilgilerigöster(self):
        print("Atların genel özellikleri")
        print("1)türü:{}\n2)yaşam alanı:{}\n3)beslenme çeşiti:{}\n4)ayak sayısı:{}\n5)tipik özellikleri:{}\n6)cinsleri:{}\n".format(self.tür,self.yaşamalanı,self.beslenmeçeşiti,self.ayaksayısı,self.tipiközellikleri,self.cinsleri))
    def cinsekle(self):
        cinslistesi = input("cinsleri araya virgül koyarak giriniz:")
        listeler = cinslistesi.split(",")
        for i in listeler:
            self.cinsleri.append(i)
    def özellikekle(self):
        tipik = input("aralarına virgül koyarak özellikleri giriniz:")
        tipiklistesi = tipik.split(",")
        for i in tipiklistesi:
            self.tipiközellikleri.append(i)
    def __str__(self):
        return "özellik sayısı:{}\ncins sayısı:{}\n".format(len(self.tipiközellikleri),len(self.cinsleri))
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
    seçim=input("işleminizi giriniz:")
    if seçim == "1":
        hayvanlar = Hayvanlar()
        hayvanlar.bilgilerigöster()
    elif seçim == "2":
        köpekler = Köpekler()
        köpekler.bilgilerigöster()
        time.sleep(1)
        sel = input("1)cins ekleme\n2)özellik ekleme\n3)özellik ve cins sayıları\n4)çıkış\n")
        if sel == "1":
            köpekler.cinsekle()
        elif sel == "2":
            köpekler.özellikekle()
        elif sel == "3":
            print(köpekler)
        else:
            print("bu menüden çıkış yapılıyor")
            time.sleep(1)
    elif seçim == "3":
        kuşlar = Kuşlar()
        kuşlar.bilgilerigöster()
        time.sleep(1)
        sel = input("1)cins ekleme\n2)özellik ekleme\n3)özellik ve cins sayıları\n4)çıkış\n")
        if sel == "1":
            kuşlar.cinsekle()
        elif sel == "2":
            kuşlar.özellikekle()
        elif sel == "3":
            print(kuşlar)
        else:
            print("bu menüden çıkış yapılıyor")
            time.sleep(1)
    elif seçim == "4":
        atlar = Atlar()
        atlar.bilgilerigöster()
        time.sleep(1)
        sel = input("1)cins ekleme\n2)özellik ekleme\n3)özellik ve cins sayıları\n4)çıkış\n")
        if sel == "1":
            atlar.cinsekle()
        elif sel == "2":
            atlar.özellikekle()
        elif sel == "3":
            print(atlar)
        else:
            print("bu menüden çıkış yapılıyor")
            time.sleep(1)
    else:
        print("işleminiz sonlandırılıyor..")
        time.sleep(1)
        break


