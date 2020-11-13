def toplam(x, y):
    return (x + y)


def carpim(x, y):
    return (x * y)


def enBuyukEleman(dizi):
    temp_sayi = dizi[0]
    for i in dizi:
        if i > temp_sayi:
            temp_sayi = i
    return temp_sayi


def enKucukEleman(dizi):
    temp_sayi = dizi[0]
    for i in dizi:
        if i < temp_sayi:
            temp_sayi = i
    return temp_sayi


def ortalama(dizi):
    toplam = 0
    for i in dizi:
        toplam += i
    return toplam/len(dizi)


def elemanArama(aranan, dizi):
    for i in range(0, len(dizi)):
        if aranan == dizi[i]:
            return i  # aranan dizinin bir parcasi ve indisi i
    return -1  # aranan dizide yok


def essizEleman(aranan, dizi):
    for i in range(0, len(dizi)):
        if aranan == dizi[i]:
            return 1  # aranan dizide var
    return -1  # aranan dizide yok


def siralama(dizi):
    uzunluk = len(dizi)
    for i in range(uzunluk-1):
        for j in range(0, uzunluk-i-1):
            if dizi[j] > dizi[j+1]:
                dizi[j], dizi[j+1] = dizi[j+1], dizi[j]
    return dizi


dizi = [5, 1, 2, 7, 123, 6, 6123]
aranan = 123

print(toplam(5, 7))
print(carpim(5, 7))
print(enBuyukEleman(dizi))
print(enKucukEleman(dizi))
print(ortalama(dizi))
print(elemanArama(123, dizi))  # -1 demek dizide yok demektir
print(essizEleman(125, dizi))  # -1 demek dizide yok demektir
print(siralama(dizi))

a = input("")
