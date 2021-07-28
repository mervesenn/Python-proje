def tambolenleribulma(sayı):
    tambolenler=[]
    for i in range(2,sayı):
        if (sayı % i == 0):
            tambolenler.append(i)
    return tambolenler
while True:
    sayı = input("sayı:")
    if (sayı == "q"):
        print("program sonlandırılıyor")
        break
    else:
        sayı = int(sayı)
        print("tam bölenler:",tambolenleribulma(sayı))