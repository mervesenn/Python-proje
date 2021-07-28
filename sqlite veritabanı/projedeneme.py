from kütüphane import *
print("""*********************
Kütüphane Programına Hoşgeldiniz
İşlemler:
1.Kitapları göster
2.Kitap sorgulama
3.Kitap ekle
4.Kitap sil
5.Baskı yükselt
çıkmak için 'q'ya basın.
***********************
""")

kütüphane = Kütüphane()

while True:
    işlem = input("Yapacağınız işlem:")
    if (işlem == "q"):
        print("program sonlandırılıyor...")
        print("yine bekleriz.")
        break
    elif (işlem == "1"):
        kütüphane.kitaplarıgöster()
    elif (işlem == "2"):
        isim = input("Hangi kitabı istiyorsunuz?")
        print("Kitap sorgulanıyor..")
        time.sleep(2)
        kütüphane.kitapsorgula(isim)
    elif (işlem == "3"):
        isim = input("İsim:")
        yazar = input("Yazar:")
        yayınevi = input("Yayınevi:")
        tür = input("Türü:")
        baskı = int(input("Baskı:"))
        yenikitap = Kitap(isim,yazar,yayınevi,tür,baskı)
        print("Kitap ekleniyor...")
        time.sleep(2)
        kütüphane.kitapekle(yenikitap)
        print("Kitap eklendi...")
    elif (işlem == "4"):
        isim = input("Hangi kitabı silmek istiyorsunuz?")
        cevap = input("Emin misiniz? (E/H)")
        if (cevap == "E"):
            print("Kitap siliniyor...")
            time.sleep(2)
            kütüphane.kitapsil(isim)
            print("Kitap silindi...")
    elif (işlem == "5"):
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz?")
        print("Baskı yükseltiliyor...")
        time.sleep(2)
        kütüphane.baskıyükselt(isim)
        print("Baskı yükseltildi...")
    else:
        print("geçersiz işlem")