print("""
******************
kullanıcı girişi
******************
""")

sys_kullanici_adi = "merve"
sys_parola = "12345"

kullanici_adi = input("kullanıcı adı:")
parola = input("parola:")

if (kullanici_adi == sys_kullanici_adi and sys_parola != parola):
    print("parola hatalı!")
    
elif (kullanici_adi != sys_kullanici_adi and sys_parola == parola):
    print("kullanıcı adı hatalı!")
    
elif (kullanici_adi != sys_kullanici_adi and sys_parola != parola):
    print("kullanıcı adı ve parola hatalı!")
    
else:
    print("sisteme başarıyla giriş yapıldı.")
