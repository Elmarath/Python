calisanlar = {"ahmet": "muhasebe", " ayşe": "pazarlama", "fatma": "satiş"}
print(calisanlar["ahmet"])
calisanlar["mustafa"] = {"guvenlik"}  # ekleme
print(calisanlar)
calisanlar["fatma"] = "insan kaynaklari"  # degisikler
print(calisanlar)

del calisanlar["ahmet"]  # silme
print(calisanlar)

print(calisanlar.keys())  # sözlükteki anahtarlar
print(calisanlar.values())  # sözlükteki değerler
print(calisanlar.items())  # sözlükteki tüm varlıklar

for i in calisanlar:
    print(calisanlar[i])

# bütün ögeleri silmek istersek
# telefon_defteri.clear()
# calisanlar.clear()

soru = input("Sehrinizin adinin tamami kucuk harflerle giriniz:")

cevap = {
    "istanbul": "gök gürültülü ve sağanak yağlışli",
    "ankara": "açık ve güneşli",
    "izmir": "bulutlu"
}

print(cevap.get(cevap, "Bu şehir için havadurumu bilgisi bulunmaktadır."))
