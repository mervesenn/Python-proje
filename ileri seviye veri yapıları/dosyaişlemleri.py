class Dosya():
    def __init__(self):
        with open("metin.txt","r",encoding="utf-8") as file:
            dosyaiçeriği = file.read()
            print(dosyaiçeriği)
            kelimeler = dosyaiçeriği.split()
            self.sadekelimeler = list()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")
                self.sadekelimeler.append(i)

    def tümkelimeler(self):
        kelimelerkümesi = set()
        for i in self.sadekelimeler:
            kelimelerkümesi.add(i)
        print("Tüm kelimeler....")
        for i in kelimelerkümesi:
            print(i)
            print("**************************")
    def kelimefrekansı(self):
        kelimesözlük = dict()
        for i in self.sadekelimeler:
            if (i in kelimesözlük):
                kelimesözlük[i] += 1
            else:
                kelimesözlük[i] = 1
        for kelime,sayı in kelimesözlük.items():
            print("{} kelimesi {} defa geçiyor...".format(kelime,sayı))
            print("------------------------------")

dosya = Dosya()
dosya.kelimefrekansı()