import random 
import time

# # # # 1


# time.sleep(2)
# sayac = True 
# while sayac:
#     print("Zar atılıyor..")
#     zar = random.randint(1,6)
#     print("1. zar" , zar)    
#     zar = random.randint(1,6)
#     print("2. zar" , zar)    
#     sayac = input("Zarı tekrar atmak ister misiniz : ")
#     if sayac.lower() == "yes":
#         sayac == True
#     if sayac == "no":
#         sayac = False


# # # 2 


# isim = input("Merhaba adın : ")

# sayac  = 5 
# sayi = random.randint(1,20)
# print("Merhaba",isim,"1 ile 20 arasında bir sayı tuttum bilmek için 5 şansın var ")
# tahmin = 0
# hak = 1 
# while sayac!=0:
#     sayac -=1
#     tahmin = int(input("Tahminin : "))
#     if sayi == tahmin:
#         print("Harika",hak,"defada bildin")
#         break
#     if sayi < tahmin:
#         print("aklımdaki sayı daha küçük , kalan deneme hakkkın :",sayac )
#     elif sayi > tahmin :
#         print("aklımdaki sayı daha büyük , kalan deneme hakkın : ",sayac)
#     hak+=1

# if sayac== 0 :
#     print("üzgünüm bilemedin aklımdaki sayı  :",sayi)




sifre = input("sezarın şifresi : ")
yenisifre= ""
for harf in sifre:
    if harf == "x" or harf == "X":
        if harf.islower():
            yenisifre += "a"     
        else:
            yenisifre+="A"
        harf = ""
    if harf == "y" or harf == "Y":
        if harf.islower():
            yenisifre+="b"
        else:
            yenisifre+="B"
        harf = ""
    if harf == "z" or harf == "Z":
        if harf.islower():
            yenisifre+="c"
        else:
            yenisifre+="C"
        harf = ""
    elif harf.isalpha():  
            yenisifre+= chr(int(ord(harf)+3))
    else:
        yenisifre+=harf  

print("yeni mesaj :",yenisifre)
