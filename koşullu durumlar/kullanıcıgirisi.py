print("""
******************
kullanıcı girişi
******************
""")

sys_kullanıcı_adı = "merve"
sys_parola = "12345"
girishakkı= 3

while True:
    kullanıcı_adı = input("kullanıcı adı:")
    parola = input("parola:")

    if (kullanıcı_adı != sys_kullanıcı_adı and sys_parola == parola):
        print("kullanıcı adı hatalı!")
        girishakkı -= 1
    elif (kullanıcı_adı == sys_kullanıcı_adı and sys_parola != parola):
        print("parola hatalı!")
        girishakkı -= 1
    elif (kullanıcı_adı != sys_kullanıcı_adı and sys_parola != parola):
        print("kullanıcı adı ve parola hatalı!")
        girishakkı -= 1
    else:
        print("sisteme başarıyla giriş yapıldı.")
        break
    if (girishakkı == 0):
        print("giriş hakkınız bitti")
        break