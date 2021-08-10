def ekstra(fonksiyon):
    def wrapper(sayilar):
        ciftlertoplami = 0
        ciftsayilar = 0
        teklertoplami = 0
        teksayilar = 0
        
        for sayi in sayilar:
            if (sayi % 2 == 0):
                ciftlertoplami += sayi
                ciftsayilar += 1
                
            else:
                teklertoplami += sayi
                teksayilar += 1
                
        print("Teklerin ortalaması:", teklertoplami / teksayilar)
        print("Çiftlerin ortalaması:", ciftlertoplami / ciftsayilar)
        fonksiyon(sayilar)
    return wrapper

@ekstra
def ortalamabul(sayilar):
    toplam = 0
    
    for sayi in sayilar:
        toplam += sayi
        
    print("Genel Ortalama:", toplam / len(sayilar))
    
ortalamabul([1,2,3,4,34,60,63,32,100,105])
