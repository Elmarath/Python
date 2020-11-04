ogrenciler = {}

run = True

while run:
    anahtar = input("sözlüge yeni kayıt eklemek istiyor musunuz? [e/h]")
    if anahtar == "e":
        isim = input("eklemek istediginiz isim")
        numara = input("ogrencinin numarası")
        ogrenciler[isim] = {numara}  # ekleme
    elif anahtar == "h":
        print("hayır dendi, programdan çıkılıyor..")
        run = False
    else:
        print("gecersiz karakter")

print("ogrenci listesi: ")
print(ogrenciler)

a = input("")
