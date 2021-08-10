class Dosya():
    def __init__(self):
        with open("metin.txt","r", encoding = "utf-8") as file:
            dosyaicerigi = file.read()
            print(dosyaicerigi)
            kelimeler = dosyaicerigi.split()
            self.sadekelimeler = list()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")
                self.sadekelimeler.append(i)

    def tumkelimeler(self):
        kelimelerkumesi = set()
        for i in self.sadekelimeler:
            kelimelerkumesi.add(i)
        print("Tüm kelimeler....")
        
        for i in kelimelerkumesi:
            print(i)
            print("**************************")
            
    def kelimefrekansi(self):
        kelimesozluk = dict()
        for i in self.sadekelimeler:
            if (i in kelimesozluk):
                kelimesozluk[i] += 1
                
            else:
                kelimesozluk[i] = 1
        for kelime, sayi in kelimesozluk.items():
            print("{} kelimesi {} defa geçiyor...".format(kelime,sayi))
            print("------------------------------")

dosya = Dosya()
dosya.kelimefrekansi()
