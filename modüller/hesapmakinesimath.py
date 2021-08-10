from math import*
def toplama(a,b):
    return a+b
def cıkarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bölme(a,b):
    return a/b
print("""*************
"gelişmiş hesap makinesi programı"
"lütfen bir işlem seçiniz"
1.işlem: toplama işlemi
2.işlem: çıkarma işlemi
3.işlem: çarpma işlemi
4.işlem: bölme işlemi
************""")
while True:
    islem = input("işlem seçiniz:")
    if (islem == "q"):
        print("tebrikler çıkış yaptınız")
        break
    elif (islem == "1"):
        a = int(input("birinci sayı:"))
        b = int(input("ikinci sayı:"))
        print(toplama(a,b))
    elif (islem == "2"):
        a = int(input("birinci sayı:"))
        b = int(input("ikinci sayı:"))
        print(cıkarma(a,b))
    elif (islem == "3"):
        a = int(input("birinci sayı:"))
        b = int(input("ikinci sayı:"))
        print(carpma(a,b))
    elif (islem == "4"):
        a = int(input("birinci sayı:"))
        b = int(input("ikinci sayı:"))
        print(bölme(a,b))
    else:
        print("geçersiz işlem yaptınız lütfen tekrar deneyiniz")
