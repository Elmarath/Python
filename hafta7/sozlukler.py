def ort_hesapla(isim, ara, final):
    ort = ara*0.4 + final * 0.6
    sonuc = {"ogrenci": isim, "ara_not": ara,
             "final_not": final, "ortalama": ort}

    return sonuc


isim = input("ogrenci adi giriniz:")
vize = int(input("vize notu giriniz"))
final = int(input("final notu giriniz"))
print(ort_hesapla(isim, vize, final))
