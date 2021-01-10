# eger bir sayinin kendisi dışındaki tüm pozitif bolenleri
# kendisine esit ise sayi mukemmel bir sayidir.

sayi = (int(input("bir sayi giriniz")))

total = 0

for i in range(1, sayi):
    if sayi % i == 0:
        total += sayi

if(total == sayi):
    print("Sayi mükemmel sayidir.")
