print("""***************
hesap makinesi programı
işlemler:
1.toplama işlemi
2.çıkarma işlemi
3.çarpma işlemi
4.bölme işlemi
****************
""")

a = int(input("birinci sayı:"))
b = int(input("ikinci sayı:"))
işlem = input("işlemi giriniz:")

if islem == "1":
    print("{} ile {} toplamı {} dir.".format(a, b, a + b))
    
elif islem == "2":
    print("{} ile {} farkı {} dir.".format(a, b, a - b))
    
elif islem == "3":
    print("{} ile {} çarpımı {} dir.".format(a, b, a * b))
    
elif islem == "4":
    print("{} ile {} bölümü {} dir.".format(a, b, a / b))
    
else:
    print("geçersiz işlem.")
