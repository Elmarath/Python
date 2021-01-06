import sys


def donustur(dosya, max,  sayac, i):
    if int(dosya[i]) > max:
        dosya[i] = str(max) + "\n"
        sayac += 1
    i += 1
    if i >= len(dosya):
        print("Degistirilmis eleman sayisi:")
        print(sayac)
        return None
    donustur(dosya, max, sayac, i)


print("elemanlar alt alta olacak sekilde:")
try:
    dosya_adi = input("dosya adini giriniz")
except:
    print("yanlis giris yaptiniz programdan cikiliyor")
    sys.exit(0)

try:
    max = int(input("maximum degeri giriniz"))
except:
    print("Yanlis girdiniz programdan cikiliyor")
    sys.exit(0)

f = open(dosya_adi)
dosya = f.readlines()

print("Dosyadaki eleman sayisi:")
print(len(dosya))
donustur(dosya, max, 0, 0)
print("Dosya")
print(dosya)
