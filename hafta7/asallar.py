sayi = 14

total = 0
sayac = 0

asal_sayilar = []
sonuc = []

for i in range(2, sayi):
    sayac = 0
    for j in range(2, i):
        if(i % j == 0):
            sayac += 1
            continue
    if sayac == 0:
        total += i
        asal_sayilar.append(i)

sonuc.append(asal_sayilar)
sonuc.append(total)

print(sonuc)

isim = "denizhan"

for harf in isim:
    if harf == 'e':
        print("harf e dir")

kongre = ["samsun", "amasya", "erzurum", "sivas"]

print(kongre[0].title())

kelime = "MARMARA"
print(kelime.center(15))

print(kelime.replace('A', 'P'))
