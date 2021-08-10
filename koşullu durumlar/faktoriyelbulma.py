print("""*************
faktöriyel bulma programı
çıkmak için 'q' ya basın

*************""")

while True:
    sayi = input("sayı:")
    if (sayi == "q"):
        print("program sonlandırılıyor")
        break
        
    else:
        sayi = int(sayi)
        faktoriyel = 1
        for i in range(2, sayi + 1):
            print("faktöriyel", faktoriyel,"i:", i)
            faktoriyel *= i
            
        print("faktöriyel", faktoriyel)
