import time
import random

class Bilgisayar():
    def __init__(self,bilgisayardurum="kapalı",bilgisayarses=13,ekranparlaklık=5):
        self.bilgisayardurum=bilgisayardurum
        self.bilgisayarses=bilgisayarses
        self.ekranparlaklık=ekranparlaklık
    def bilgisayaraç(self):
        if (self.bilgisayardurum=="açık"):
            print("bilgisayar zaten açık")
        else:
            print("bilgisayar açılıyor..")
            self.bilgisayardurum="açık"
    def bilgisayarkapat(self):
        if (self.bilgisayardurum=="kapalı"):
            print("bilgisayar zaten kapalı")
        else:
            print("bilgisayar kapanıyor..")
            self.bilgisayardurum="kapalı"
    def sesayarı(self):
        while True:
            cevap = input("ses azaltmak için f7'e basın:'f7'\nsesi artırmak için f8'e basın:'f8'\nçıkış:çıkış")
            if (cevap=='f7'):
                if(self.bilgisayarses!=0):
                    self.bilgisayarses-=1
                    print("ses:",self.bilgisayarses)
            elif(cevap=='f8'):
                if(self.bilgisayarses!=100):
                    self.bilgisayarses+=1
                    print("ses:",self.bilgisayarses)
            else:
                print("ses güncellendi:",self.bilgisayarses)
                break
    def parlaklık(self):
        while True:
            cevap = input("parlaklığı arttır:'>'\nparlaklığı azalt:'<'\nçıkış:çıkış")
            if (cevap=='>'):
                if(self.ekranparlaklık!=10):
                    self.ekranparlaklık+=1
                    print("ekranparlaklığı:",self.ekranparlaklık)
            elif(cevap=='<'):
                if(self.ekranparlaklık!=0):
                    self.ekranparlaklık-=1
                    print("ekranparlaklığı:",self.ekranparlaklık)
            else:
                print("ekran parlaklığı güncellendi:",self.ekranparlaklık)
                break
    def __str__(self):
        return "bilgisayar durumu:{}\nbilgisayar ses:{}\nbilgisayar ekran parlaklığı:{}\n".format(self.bilgisayardurum,self.bilgisayarses,self.ekranparlaklık)
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
    işlem=input("işlemi seçiniz:")
    if (işlem=="q"):
        print("program sonlandırılıyor..")
        break
    elif (işlem=="1"):
        bilgisayar.bilgisayaraç()
    elif (işlem=="2"):
        bilgisayar.bilgisayarkapat()
    elif (işlem=="3"):
        bilgisayar.sesayarı()
    elif (işlem=="4"):
        bilgisayar.parlaklık()
    elif (işlem=="5"):
        print(bilgisayar)
    else:
        print("geçersiz işlem!")