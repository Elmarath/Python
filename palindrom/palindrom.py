def df_str(girdi):
    girdi = girdi.replace(" ", "")
    girdi = girdi.lower()
    return girdi

# kelime al


girdi = input("bir string giriniz")

# sadece karakterleri birak
girdi = df_str(girdi)

# eger polindrom ise yazdir

reverse_girdi = girdi[::-1]
if girdi == reverse_girdi:
    print("kelime palindromdur")

for i in range(3, len(girdi)):
    pass

# olusturuluabilcek butun palindromları yaz
