import random
import time

class Kumanda():
    def __init__(self, tvdurum = "kapalı", tvses = 0, kanallistesi = ["trt"], kanal = "trt"):
        self.tvdurum = tvdurum
        self.tvses = tvses
        self.kanallistesi = kanallistesi
        self.kanal = kanal
        
    def tvac(self):
        if (self.tvdurum == "açık"):
            print("televizyon zaten açık")
        else:
            print("televizyon açılıyor..")
            self.tvdurum = "açık"
            
    def tvkapat(self):
        if (self.tvdurum == "kapalı"):
            print("televizyon zaten kapalı")
        else:
            print("televizyon kapanıyor..")
            self.tvdurum = "kapalı"
            
    def sesayarlari(self):
        while True:
            cevap = input("sesi azalt:'<'\nsesi arttır:'>'\nçıkış:çıkış")
            if (cevap == '<'):
                if(self.tvses != 0):
                    self.tvses -= 1
                    print("ses:", self.tvses)
                    
            elif(cevap == ">"):
                if (self.tvses != 31):
                    self.tvses += 1
                    print("ses:", self.tvses)
                    
            else:
                print("ses güncellendi:", self.tvses)
                break
                
    def kanalekle(self, kanalismi):
        print("kanal ekleniyor..")
        time.sleep(1)
        self.kanallistesi.append(kanalismi)
        print("kanal eklendi..")
        
    def rastgelekanal(self):
        rastgele = random.randint(0, len(self.kanallistesi)-1)
        self.kanal = self.kanallistesi[rastgele]
        print("şu anki kanal:", self.kanal)
        
    def __len__(self):
        return len(self.kanallistesi)
    
    def __str__(self):
        return "tv durumu:{}\ntv ses:{}\nkanal listesi:{}\nşu anki kanal:{}\n".format(self.tvdurum, self.tvses, self.kanallistesi, self.kanal)
    
kumanda = Kumanda()
print("""
televizyon uygulaması
1.tv aç
2.tv kapat
3.ses ayarları
4.kanal ekle
5.kanal sayısını öğrenme
6.rastgele kanal geçme
7.tv bilgileri
çıkmak için 'q'ya basın.
""")

while True:
    islem = input("işlemi seçiniz:")
    if (islem == "q"):
        print("program sonlandırılıyor..")
        break
        
    elif (islem == "1"):
        kumanda.tvac()
        
    elif (islem == "2"):
        kumanda.tvkapat()
        
    elif (islem == "3"):
        kumanda.sesayarlari()
        
    elif (islem == "4"):
        kanalisimleri = input("kanal isimlerini ',' ile ayırarak girin:")
        kanallistesi = kanalisimleri.split(",")
        for eklenecekler in kanallistesi:
            kumanda.kanalekle(eklenecekler)
            
    elif (islem == "5"):
        print("kanal sayısı:", len(kumanda))
        
    elif (islem == "6"):
        kumanda.rastgelekanal()
        
    elif (islem == "7"):
        print(kumanda)
        
    else:
        print("geçersiz işlem!")
