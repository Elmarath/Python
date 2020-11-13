ac_parantez = 0
kapa_parantez = 0
formul = input("parantez hatasini kontrol etmek istediginiz formulu giriniz.")

for i in formul:
    if (i == '('):
        ac_parantez += 1
    elif (i == ')'):
        kapa_parantez += 1

if ac_parantez == kapa_parantez:
    print("formulunuzde parantez hatasi yoktur.")
elif ac_parantez > kapa_parantez:
    print("formulunuzde %d adet fazladan '(' var." %
          (ac_parantez - kapa_parantez))
elif kapa_parantez > ac_parantez:
    print("formulunuzde %d adet fazladan ')' var." %
          (kapa_parantez - ac_parantez))

a = input("")
