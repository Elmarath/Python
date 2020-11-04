sifreleme = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
             "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

kelimeSifreli = ""

yazmak_cozmek = input("yazmak mı istiyorsun çözmek mi [y/c]")

anahtar = int(input("sifreleme icin anahtari giriniz: "))

if yazmak_cozmek == "y":

    GirilenKelime = input("kelimeyi giriniz: ")
    for i in range(0, len(GirilenKelime)):
        for index in range(0, len(sifreleme)):
            if sifreleme[index] == GirilenKelime[i]:
                break
        if index + anahtar > len(sifreleme) - 1:
            index -= len(sifreleme)
            kelimeSifreli += sifreleme[index + anahtar]
            index += len(sifreleme)
        else:
            kelimeSifreli += sifreleme[index + anahtar]

elif yazmak_cozmek == "c":

    GirilenKelime = input("kelimeyi giriniz: ")
    for i in range(0, len(GirilenKelime)):
        for index in range(0, len(sifreleme)):
            if sifreleme[index] == GirilenKelime[i]:
                break
        if index - anahtar < 0:
            index += len(sifreleme)
            kelimeSifreli += sifreleme[index - anahtar]
        else:
            kelimeSifreli += sifreleme[index - anahtar]


print(kelimeSifreli)

a = input("")
