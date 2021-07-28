def ekstra(fonksiyon):
    def ekstraözellik():
        print("Mükemmel sayılar...")
        for sayı in range(1,1001):
            toplam = 0
            i = 1
            while (i < sayı):
                if (sayı % i == 0):
                    toplam += i

                i += 1
            if (toplam == sayı):
                print(sayı)
        fonksiyon()
    return ekstraözellik
@ekstra
def asalsayılar():
    print("Asal sayılar...")
    for sayı in range(2,1001):
        i = 2
        say = 0
        while (i < sayı):
            if (sayı % i == 0):
                say += 1
            i += 1
        if (say == 0):
            print(sayı)
asalsayılar()
