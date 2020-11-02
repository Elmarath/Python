
isim = input("isminizi giriniz")
tersisim = (isim[::-1])

print(tersisim)

if isim == tersisim:
    print("isim palindromdur")
else:
    print("isim palindrom değildir")
