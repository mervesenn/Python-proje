def ekstra(fonksiyon):
    def wrapper(sayılar):
        çiftlertoplamı = 0
        çiftsayılar = 0
        teklertoplamı = 0
        teksayılar = 0
        for sayı in sayılar:
            if (sayı % 2 == 0):
                çiftlertoplamı += sayı
                çiftsayılar += 1
            else:
                teklertoplamı += sayı
                teksayılar += 1
        print("Teklerin ortalaması:",teklertoplamı/teksayılar)
        print("Çiftlerin ortalaması:",çiftlertoplamı/çiftsayılar)
        fonksiyon(sayılar)
    return wrapper
@ekstra

def ortalamabul(sayılar):
    toplam = 0
    for sayı in sayılar:
        toplam += sayı
    print("Genel Ortalama:",toplam/len(sayılar))
ortalamabul([1,2,3,4,34,60,63,32,100,105])