def ekstra(fonksiyon):
    def ekstraozellik():
        print("Mükemmel sayılar...")
        
        for sayi in range(1,1001):
            toplam = 0
            i = 1
            
            while (i < sayi):
                if (sayi % i == 0):
                    toplam += i

                i += 1
            if (toplam == sayi):
                print(sayi)
                
        fonksiyon()
    return ekstraozellik

@ekstra
def asalsayilar():
    print("Asal sayılar...")
    
    for sayi in range(2,1001):
        i = 2
        say = 0
        
        while (i < sayi):
            if (sayi % i == 0):
                say += 1
                
            i += 1
        if (say == 0):
            print(sayi)
            
asalsayilar()
