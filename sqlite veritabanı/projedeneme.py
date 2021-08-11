from kutuphane import *
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

kutuphane = Kutuphane()

while True:
    islem = input("Yapacağınız işlem:")
    if (islem == "q"):
        print("program sonlandırılıyor...")
        print("yine bekleriz.")
        break
        
    elif (islem == "1"):
        kutuphane.kitaplarigoster()
        
    elif (islem == "2"):
        isim = input("Hangi kitabı istiyorsunuz?")
        print("Kitap sorgulanıyor..")
        time.sleep(2)
        kutuphane.kitapsorgula(isim)
        
    elif (islem == "3"):
        isim = input("İsim:")
        yazar = input("Yazar:")
        yayinevi = input("Yayınevi:")
        tur = input("Türü:")
        baski = int(input("Baskı:"))
        yenikitap = Kitap(isim,yazar,yayinevi,tur,baski)
        print("Kitap ekleniyor...")
        time.sleep(2)
        kutuphane.kitapekle(yenikitap)
        print("Kitap eklendi...")
        
    elif (islem == "4"):
        isim = input("Hangi kitabı silmek istiyorsunuz?")
        cevap = input("Emin misiniz? (E/H)")
        if (cevap == "E"):
            print("Kitap siliniyor...")
            time.sleep(2)
            kutuphane.kitapsil(isim)
            print("Kitap silindi...")
            
    elif (islem == "5"):
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz?")
        print("Baskı yükseltiliyor...")
        time.sleep(2)
        kutuphane.baskiyükselt(isim)
        print("Baskı yükseltildi...")
        
    else:
        print("geçersiz işlem")
