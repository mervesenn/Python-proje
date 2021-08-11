import time
import random

class Bilgisayar():
    def __init__(self, bilgisayardurum = "kapalı", bilgisayarses=13, ekranparlaklik=5):
        self.bilgisayardurum = bilgisayardurum
        self.bilgisayarses = bilgisayarses
        self.ekranparlaklik = ekranparlaklik
        
    def bilgisayarac(self):
        if (self.bilgisayardurum == "açık"):
            print("bilgisayar zaten açık")
            
        else:
            print("bilgisayar açılıyor..")
            self.bilgisayardurum = "açık"
            
    def bilgisayarkapat(self):
        if (self.bilgisayardurum == "kapalı"):
            print("bilgisayar zaten kapalı")
            
        else:
            print("bilgisayar kapanıyor..")
            self.bilgisayardurum = "kapalı"
            
    def sesayari(self):
        while True:
            cevap = input("ses azaltmak için f7'e basın:'f7'\nsesi artırmak için f8'e basın:'f8'\nçıkış:çıkış")
            if (cevap =='f7'):
                if(self.bilgisayarses!= 0):
                    self.bilgisayarses -= 1
                    print("ses:", self.bilgisayarses)
                    
            elif(cevap == 'f8'):
                if(self.bilgisayarses != 100):
                    self.bilgisayarses += 1
                    print("ses:", self.bilgisayarses)
                          
            else:
                print("ses güncellendi:", self.bilgisayarses)
                break
                          
    def parlaklik(self):
        while True:
            cevap = input("parlaklığı arttır:'>'\nparlaklığı azalt:'<'\nçıkış:çıkış")
            if (cevap == '>'):
                if(self.ekranparlaklik != 10):
                    self.ekranparlaklik += 1
                    print("ekranparlaklığı:", self.ekranparlaklik)
            elif(cevap == '<'):
                if(self.ekranparlaklik != 0):
                    self.ekranparlaklik -= 1
                    print("ekranparlaklığı:",self.ekranparlaklik)
            else:
                print("ekran parlaklığı güncellendi:", self.ekranparlaklik)
                break
                          
    def __str__(self):
        return "bilgisayar durumu:{}\nbilgisayar ses:{}\nbilgisayar ekran parlaklığı:{}\n".format(self.bilgisayardurum, self.bilgisayarses, self.ekranparlaklik)
                          
bilgisayar = Bilgisayar()
print("""
bilgisayar
1.bilgisayar aç
2.bilgisayar kapat
3.ses ayarları
4.ekran parlaklığı
5.bilgisayar bilgileri
çıkmak için 'q'ya basın.
""")

while True:
    islem = input("işlemi seçiniz:")
    if (islem == "q"):
        print("program sonlandırılıyor..")
        break
                          
    elif (islem == "1"):
        bilgisayar.bilgisayarac()
                          
    elif (islem == "2"):
        bilgisayar.bilgisayarkapat()
                          
    elif (islem == "3"):
        bilgisayar.sesayari()
                          
    elif (islem == "4"):
        bilgisayar.parlaklik()
                          
    elif (islem == "5"):
        print(bilgisayar)
                          
    else:
        print("geçersiz işlem!")
