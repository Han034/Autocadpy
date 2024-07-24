from pyautocad import Autocad, APoint

# AutoCAD ile bağlantı kur
acad = Autocad(create_if_not_exists=True)
acad.prompt("PyAutoCAD ile AutoCAD'e bağlanıldı.\n")
print(acad.doc.Name)

# n27 ve n28 noktalarını tanımla
n27 = APoint(0, 0)  # n27'nin koordinatlarını buraya girin
n28 = APoint(1530, 0)  # n28'in koordinatlarını buraya girin

# Çizgi uzunlukları ve boşluklar
H13 = 20  # Uzun çizginin uzunluğunu buraya girin
kisa_cizgi_boyu = H13 * 6 / 10
oruntu_uzunlugu = 17  # Her bir örüntü için toplam uzunluk

# n27 ve n28 noktaları arasındaki mesafeyi hesapla
mesafe = n28.x - n27.x

# Maksimum örüntü sayısını hesapla
oruntu_sayisi = int(mesafe // oruntu_uzunlugu)

# Kısa çizgiler uzun çizgilerin üstünde olmalı
# Uzun çizgilerin üst kısmına kısa çizgileri hizalamak için offset miktarı
offset_miktari = 5  # İstenilen offset miktarını buraya girin

# Çizgilerin yatay, örüntünün dikey eksende ilerlemesini sağla
for i in range(oruntu_sayisi):
    baslangic_noktasi = APoint(n27.x, n27.y + i * oruntu_uzunlugu)
    
    # Uzun çizgi çiz
    uzun_cizgi_baslangic = APoint(baslangic_noktasi.x, baslangic_noktasi.y)
    uzun_cizgi_bitis = APoint(uzun_cizgi_baslangic.x + H13, uzun_cizgi_baslangic.y)
    acad.model.AddLine(uzun_cizgi_baslangic, uzun_cizgi_bitis)
    
    # Kısa çizgi çiz (sola doğru uzanacak şekilde ve uzun çizginin üstünde)
    kisa_cizgi_baslangic = APoint(uzun_cizgi_bitis.x, uzun_cizgi_bitis.y + offset_miktari)
    kisa_cizgi_bitis = APoint(kisa_cizgi_baslangic.x - kisa_cizgi_boyu, kisa_cizgi_baslangic.y)
    acad.model.AddLine(kisa_cizgi_baslangic, kisa_cizgi_bitis)

print(f"Toplam {oruntu_sayisi} örüntü çizildi.")
