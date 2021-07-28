print("""*************
faktöriyel bulma programı
çıkmak için 'q' ya basın

*************""")

while True:
    sayı = input("sayı:")
    if (sayı == "q"):
        print("program sonlandırılıyor")
        break
    else:
        sayı = int(sayı)
        faktoriyel = 1
        for i in range(2,sayı+1):
            print("faktöriyel",faktoriyel,"i:",i)
            faktoriyel *= i
        print("faktöriyel", faktoriyel)
