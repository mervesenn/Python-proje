"""
Asal sayılar: 1'e ve kendisinden başka sayıya bölünmeyen sayılardır.

"""
def asalmı(sayı):
    if(sayı == 1):
        return False
    elif (sayı == 2):
        return True
    else:
        for i in range(2,sayı):
            if(sayı % i == 0):
                return False
        return True
while True:
    sayı = input("sayı:")
    if(sayı == "q"):
        break
    else:
        sayı = int(sayı)
        if(asalmı(sayı)):
            print(sayı,"asal bir sayıdır")
        else:
            print(sayı,"asal bir sayı değildir")