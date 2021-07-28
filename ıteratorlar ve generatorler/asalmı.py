def asalmı(sayı):
    i = 2
    while i<sayı:
        if (sayı % i == 0):
            return False
        i += 1
    return True
def asalgenerator():
    i = 2
    while True:
        if (asalmı(i)):
            yield i
        i +=1
for sayı in asalgenerator():
    if (sayı >1000):
        break
    print(sayı)