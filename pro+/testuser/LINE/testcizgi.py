from pyautocad import Autocad, APoint

# AutoCAD ile bağlantı kur
acad = Autocad(create_if_not_exists=True)
acad.prompt("PyAutoCAD ile AutoCAD'e bağlanıldı.\n")
print(acad.doc.Name)

# n1 ve n20 noktalarını tanımla
n1 = APoint(0, 0)  # n1'in koordinatlarını buraya girin
n20 = APoint(500, 0)  # n20'nin koordinatlarını buraya girin

# Çizgi uzunlukları ve boşluklar
H9 = 10  # H9 uzunluğunu buraya girin
kisa_cizgi_boyu = H9 * 6 / 10
ilk_bosluk = 0.00050
ikinci_bosluk = 0.000050

# Örüntü uzunluğu
oruntu_uzunlugu = kisa_cizgi_boyu + ilk_bosluk + H9 + ikinci_bosluk

# n1 ve n20 noktaları arasındaki mesafeyi hesapla
mesafe = n20.x - n1.x

# Maksimum örüntü sayısını hesapla
oruntu_sayisi = int(mesafe // oruntu_uzunlugu)

# Örüntüleri çiz
for i in range(oruntu_sayisi):
    baslangic_noktasi = APoint(n1.x + i * oruntu_uzunlugu, n1.y)
    
    # Kısa çizgi çiz
    kisa_cizgi_baslangic = baslangic_noktasi
    kisa_cizgi_bitis = APoint(kisa_cizgi_baslangic.x, kisa_cizgi_baslangic.y - kisa_cizgi_boyu)
    acad.model.AddLine(kisa_cizgi_baslangic, kisa_cizgi_bitis)
    
    # Uzun çizgi çiz
    uzun_cizgi_baslangic = APoint(kisa_cizgi_baslangic.x + kisa_cizgi_boyu + ilk_bosluk, n1.y)
    uzun_cizgi_bitis = APoint(uzun_cizgi_baslangic.x, uzun_cizgi_baslangic.y - H9)
    acad.model.AddLine(uzun_cizgi_baslangic, uzun_cizgi_bitis)

print(f"Toplam {oruntu_sayisi} örüntü çizildi.")
