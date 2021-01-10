import random

max = 10
min = 5

a = random.randint(min, max)
print(a)

list = ["erzurum", "bursa", "izmir", "istanbul"]

print(random.choice(list))

calisan1 = "ahmet", "mehmet", "yilmaz", 1988

print(type(calisan1))

sozluk = {"key1": "veri1", "key2": "veri2"}

print(sozluk["key1"])

# sozluk tanımlanirken {} kullanılır

calisanlar = {"ahmet": "muhasebe", "Ayşe": "pazarlama", "fatma": "Satis"}
print(calisanlar["ahmet"])
calisanlar["mustafa"] = "güvenlik"  # ekleme
print(calisanlar)
calisanlar["fatma"] = "insan kaynaklari"  # degisiklik
print(calisanlar)
del calisanlar["ahmet"]  # silme
print(calisanlar.keys())  # sozlukteki anahtarlar
print(calisanlar.values())  # sozlukteki degerler
print(calisanlar.items())

calisanlar.clear()  # tum ogeleri silme
print(calisanlar)

calisanlar.get("fatma")


HavaDurumu = {"ankara": "karli", "izmir": "gunesli", "istanbul": "yagmurlu"}
sehir = input("hava durumunu ogrenmek istediginiz sehrin adini giriniz")
print(HavaDurumu[sehir])

print("merhaba benim adim %s" % "Denizhan")
