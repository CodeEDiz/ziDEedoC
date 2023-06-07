import random


sifre_uzunlugu = int(input("şifre uzunluğunu giriniz"))
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre = ""

for i in range(sifre_uzunlugu):
    sifre = sifre + random.choice(karakterler)

print(sifre)
