import random
import time

print("""***********
sayı tahmin oyunu
1 ile 40 arasında sayıyı tahmin edin

""")

rastgelesayı = random.randint(1,40)
tahminhakkı = 7
while True:
    tahmin = int(input("tahmininiz:"))
    if(tahmin<rastgelesayı):
        print("bilgiler sorgulanıyor")
        time.sleep(1)
        print("daha yüksek bir sayı söyleyin")
        tahminhakkı -= 1
    elif (tahmin>rastgelesayı):
        print("bilgiler sorgulanıyor")
        time.sleep(1)
        print("daha düşük bir sayı söyleyin")
        tahminhakkı -= 1
    else:
        print("bilgiler sorgulanıyor")
        time.sleep(1)
        print("tebrikler! sayınız:",rastgelesayı)
        break
    if(tahminhakkı==0):
        print("tahmin hakkınız bitti")
        print("sayınız:",rastgelesayı)
        break