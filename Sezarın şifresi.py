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
