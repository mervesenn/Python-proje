def asalmi(sayi):
    i = 2
    while i < sayi:
        if (sayi % i == 0):
            return False
        i += 1
    return True
def asalgenerator():
    i = 2
    while True:
        if (asalmi(i)):
            yield i
        i +=1
for sayi in asalgenerator():
    if (sayi > 1000):
        break
    print(sayi)
