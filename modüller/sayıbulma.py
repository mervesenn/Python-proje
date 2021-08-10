import random
import time

print("""***********
sayı tahmin oyunu
1 ile 40 arasında sayıyı tahmin edin

""")

rastgelesayi = random.randint(1,40)
tahminhakki = 7

while True:
    tahmin = int(input("tahmininiz:"))
    if(tahmin < rastgelesayi):
        print("bilgiler sorgulanıyor")
        time.sleep(1)
        print("daha yüksek bir sayı söyleyin")
        tahminhakki -= 1
        
    elif (tahmin > rastgelesayi):
        print("bilgiler sorgulanıyor")
        time.sleep(1)
        print("daha düşük bir sayı söyleyin")
        tahminhakki -= 1
        
    else:
        print("bilgiler sorgulanıyor")
        time.sleep(1)
        print("tebrikler! sayınız:", rastgelesayi)
        break
        
    if(tahminhakki == 0):
        print("tahmin hakkınız bitti")
        print("sayınız:", rastgelesayi)
        break
