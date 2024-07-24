from pyautocad import Autocad, APoint, aDouble
import win32com.client
import pythoncom
import json
from math import pi
import math

# JSON dosyasını okuma
with open('input_data_form3.json', 'r') as f:
    data = json.load(f)

# JSON verilerini değişkenlere ata, varsayılan değerler 0
H9_LEN = int(data.get("H9_LEN", 0))
H10_LEN = int(data.get("H10_LEN", 0))
H1_LEN = int(data.get("H1_LEN", 0))
H3_LEN = int(data.get("H3_LEN", 0))
H3X_LEN = int(data.get("H3X_LEN", 0))
H4_LEN = int(data.get("H4_LEN", 0))
H5_LEN = int(data.get("H5_LEN", 0))
H6_LEN = int(data.get("H6_LEN", 0))
H11_LEN = int(data.get("H11_LEN", 0))
H11X_LEN = int(data.get("H11X_LEN", 0))
H12_LEN = int(data.get("H12_LEN", 0))
H7_LEN = int(data.get("H7_LEN", 0))
H8_LEN = int(data.get("H8_LEN", 0))
H2_LEN = int(data.get("H2_LEN", 0))
H13_LEN = int(data.get("H13_LEN", 0))
H40_LEN = int(data.get("H40_LEN", 0)) # fark yatay
H30_LEN = int(data.get("H30_LEN", 0)) # fark dikey

# Değişkenleri ekrana yazdır
print(f"H9_LEN: {H9_LEN}")
print(f"H10_LEN: {H10_LEN}")
print(f"H1_LEN: {H1_LEN}")
print(f"H3_LEN: {H3_LEN}")
print(f"H3X_LEN: {H3X_LEN}")
print(f"H4_LEN: {H4_LEN}")
print(f"H5_LEN: {H5_LEN}")
print(f"H6_LEN: {H6_LEN}")
print(f"H11_LEN: {H11_LEN}")
print(f"H11X_LEN: {H11X_LEN}")
print(f"H12_LEN: {H12_LEN}")
print(f"H7_LEN: {H7_LEN}")
print(f"H8_LEN: {H8_LEN}")
print(f"H2_LEN: {H2_LEN}")
print(f"H13_LEN: {H13_LEN}")
print(f"H40_LEN: {H40_LEN}")
print(f"H30_LEN: {H30_LEN}")

#H9_LEN = 50
#H10_LEN = 75
#H1_LEN = 950
#H3_LEN = 160
#H3X_LEN = 250
#H4_LEN = 100
#H5_LEN = 120
#H6_LEN = 50
#H11_LEN = 210
#H11X_LEN = 300
#H12_LEN = 100
#H7_LEN = 1430
#H8_LEN = 1940
#H2_LEN = 1530
#H13_LEN = 150
#H40_LEN = 50 # fark yatay
#H30_LEN = 100 # fark dikey

length1 = H4_LEN
length2 = H4_LEN/2

length1_x = H13_LEN
length2_x = H13_LEN / 2

move = 4000

#================HATCH==================================
acad = win32com.client.Dispatch("AutoCAD.Application")
acadModel = acad.ActiveDocument.ModelSpace

def aaPoint(x,y,z= 0):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8,(x,y,z))
def aaDouble(xyz):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8,(xyz))
def aavariants(object):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, (object))

out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                     0+move, H9_LEN,0,
                                     0+move, H9_LEN + H10_LEN,0,
                                     H2_LEN+move, H9_LEN + H10_LEN,0,
                                     H2_LEN+move, H9_LEN,0,
                                     0+move, H9_LEN,0
]))

sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.PatternScale = 7
hatch.EntityTransparency = 70



out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                     H40_LEN+move, H9_LEN + H10_LEN,0,
                                     0+move, H9_LEN + H10_LEN,0,
                                     0+move, H9_LEN + H10_LEN + H1_LEN,0,
                                     H40_LEN+move, H9_LEN + H10_LEN + H1_LEN,0,
                                     H40_LEN+move, H9_LEN + H10_LEN,0
]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.PatternScale = 7
hatch.EntityTransparency = 70

out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                     H40_LEN+move, H9_LEN + H10_LEN + H1_LEN-H30_LEN,0,
                                     H40_LEN+move, H9_LEN + H10_LEN + H1_LEN,0,
                                     -H3_LEN+H8_LEN-H3X_LEN-H40_LEN+move, H9_LEN + H10_LEN + H1_LEN,0,
                                     -H3_LEN+H8_LEN-H3X_LEN-H40_LEN+move, H9_LEN + H10_LEN + H1_LEN-H30_LEN,0,
                                     H40_LEN+move, H9_LEN + H10_LEN + H1_LEN-H30_LEN,0
]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.PatternScale = 7
hatch.EntityTransparency = 70

out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                     -H3_LEN+H8_LEN-H3X_LEN-H40_LEN+move, H9_LEN + H10_LEN + H1_LEN,0,
                                     -H3_LEN+H8_LEN-H3X_LEN+move, H9_LEN + H10_LEN + H1_LEN,0,
                                     H2_LEN+move, H9_LEN + H10_LEN,0,
                                     H2_LEN-H40_LEN+move, H9_LEN + H10_LEN,0,
                                     -H3_LEN+H8_LEN-H3X_LEN-H40_LEN+move, H9_LEN + H10_LEN + H1_LEN,0
]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.PatternScale = 7
hatch.EntityTransparency = 70

out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                     -H3_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN,0,
                                     -H3_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN,0,
                                     -H3_LEN+H11_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN,0,
                                     -H3_LEN+H11_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN,0,
                                     -H3_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN,0
]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.PatternScale = 7
hatch.EntityTransparency = 70

out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                     -H3_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN,0,
                                     -H3_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN+H6_LEN,0,
                                     -H3_LEN+H11_LEN+H7_LEN+H11X_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN+H6_LEN,0,
                                     -H3_LEN+H8_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN,0,
                                     -H3_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN,0
]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.PatternScale = 7
hatch.EntityTransparency = 70

out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                     -H3_LEN+H8_LEN-H11X_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN,0,
                                     -H3_LEN+H8_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN,0,
                                     -H3_LEN+H8_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN,0,
                                     -H3_LEN+H8_LEN-H11X_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN,0,
                                     -H3_LEN+H8_LEN-H11X_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN,0
]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.PatternScale = 7
hatch.EntityTransparency = 70

out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                     -H3_LEN+H11_LEN+H13_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN,0,
                                     -H3_LEN+H11_LEN+H13_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN,0,
                                     -H3_LEN+H8_LEN-H11X_LEN-H13_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN,0,
                                     -H3_LEN+H8_LEN-H11X_LEN-H13_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN,0,
                                     -H3_LEN+H11_LEN+H13_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN,0
]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.PatternScale = 7
hatch.EntityTransparency = 70

out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                     -H3_LEN+H11_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN+H6_LEN,0,
                                     -H3_LEN+H11_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN+H6_LEN+H12_LEN,0,
                                     -H3_LEN+H11_LEN+H7_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN+H6_LEN+H12_LEN,0,
                                     -H3_LEN+H11_LEN+H7_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN+H6_LEN,0,
                                     -H3_LEN+H11_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN+H6_LEN,0
]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.PatternScale = 7
hatch.EntityTransparency = 70

out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                     H2_LEN-H40_LEN+move, H9_LEN + H10_LEN,0,
                                     H40_LEN+move, H9_LEN + H10_LEN,0,
                                     H40_LEN+move, H9_LEN + H10_LEN + H1_LEN-H30_LEN,0,
                                     -H3_LEN+H8_LEN-H3X_LEN-H40_LEN+move, H9_LEN + H10_LEN + H1_LEN-H30_LEN,0,
                                     H2_LEN-H40_LEN+move, H9_LEN + H10_LEN,0
]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "AR-CONC", True)
hatch.AppendOuterLoop(outer)
hatch.PatternScale = 0.18
hatch.EntityTransparency = 70

#==================================================================

#============İÇ HESAPLAMA======================================


#==================================================

# AutoCAD'e bağlan
acad = Autocad(create_if_not_exists=True)
acad.prompt("AutoCAD'e bağlanıldı\n")
print(acad.doc.Name)


#============NOKTALAR===========================================
n1 = APoint(0+move, 0)
n2 = APoint(0+move, H9_LEN)
n3 = APoint(0+move, H9_LEN + H10_LEN)
n4 = APoint(0+move, H9_LEN + H10_LEN + H1_LEN)
n5 = APoint(-H3_LEN+move, H9_LEN + H10_LEN + H1_LEN)
n6 = APoint(-H3_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN)
n7 = APoint(-H3_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN)
n8 = APoint(-H3_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN+H6_LEN)
n9 = APoint(-H3_LEN+H11_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN+H6_LEN)
n10 = APoint(-H3_LEN+H11_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN+H6_LEN+H12_LEN)
n11 = APoint(-H3_LEN+H11_LEN+H7_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN+H6_LEN+H12_LEN)
n12 = APoint(-H3_LEN+H11_LEN+H7_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN+H6_LEN)
n13 = APoint(-H3_LEN+H11_LEN+H7_LEN+H11X_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN+H6_LEN)
n14 = APoint(-H3_LEN+H8_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN)
n15 = APoint(-H3_LEN+H8_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN)
n16 = APoint(-H3_LEN+H8_LEN+move, H9_LEN + H10_LEN + H1_LEN)
n17 = APoint(-H3_LEN+H8_LEN-H3X_LEN+move, H9_LEN + H10_LEN + H1_LEN)
n18 = APoint(H2_LEN+move, H9_LEN + H10_LEN)
n19 = APoint(H2_LEN+move, H9_LEN)
n20 = APoint(H2_LEN+move, 0)
n21 = APoint(H2_LEN-H40_LEN+move, H9_LEN + H10_LEN)
n22 = APoint(+H40_LEN+move, H9_LEN + H10_LEN)
n23 = APoint(+H40_LEN+move, H9_LEN + H10_LEN + H1_LEN-H30_LEN)
n24 = APoint(-H3_LEN+H8_LEN-H3X_LEN-H40_LEN+move, H9_LEN + H10_LEN + H1_LEN-H30_LEN)
n25 = APoint(-H3_LEN+H8_LEN-H3X_LEN-H40_LEN+move, H9_LEN + H10_LEN + H1_LEN)
n26 = APoint(+H40_LEN+move, H9_LEN + H10_LEN + H1_LEN)
n27 = APoint(-H3_LEN+H11_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN)
n28 = APoint(-H3_LEN+H11_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN)
n29 = APoint(-H3_LEN+H11_LEN+H13_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN)
n30 = APoint(-H3_LEN+H11_LEN+H13_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN)
n31 = APoint(-H3_LEN+H8_LEN-H11X_LEN-H13_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN)
n32 = APoint(-H3_LEN+H8_LEN-H11X_LEN-H13_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN)
n33 = APoint(-H3_LEN+H8_LEN-H11X_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H5_LEN)
n34 = APoint(-H3_LEN+H8_LEN-H11X_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN)

#==================================================



#============ÇİZGİLER===========================================
H2 = acad.model.AddLine(n1,n20)
H9 = acad.model.AddLine(n1,n2)
H8 = acad.model.AddLine(n7,n14)
H8X = acad.model.AddLine(n6,n15)
H10 = acad.model.AddLine(n2,n3)
H1 = acad.model.AddLine(n3,n4)
H3 = acad.model.AddLine(n4,n5)
H4 = acad.model.AddLine(n5,n6)
H5 = acad.model.AddLine(n6,n7)
H6 = acad.model.AddLine(n7,n8)
H11 = acad.model.AddLine(n8,n9)

H12 = acad.model.AddLine(n9,n10)
H12.Linetype = "ACAD_ISO02W100"
H12X = acad.model.AddLine(n11,n12)
H12X.Linetype = "ACAD_ISO02W100"
H7 = acad.model.AddLine(n10,n11)
H7.Linetype = "ACAD_ISO02W100"
H7X = acad.model.AddLine(n9,n12)
H11X = acad.model.AddLine(n12,n13)
H6X = acad.model.AddLine(n13,n14)
H5X = acad.model.AddLine(n14,n15)
H4X = acad.model.AddLine(n15,n16)
H3X = acad.model.AddLine(n16,n17)
H1X = acad.model.AddLine(n17,n18)
H10X = acad.model.AddLine(n18,n19)
H9X = acad.model.AddLine(n19,n20)
H2X = acad.model.AddLine(n3,n18)
H2X_FARKY = acad.model.AddLine(n21,n22)
H2X_FARKD = acad.model.AddLine(n22,n23)
H2X_FARKY2 = acad.model.AddLine(n23,n24)
H2X_FARKY2.Linetype = "ACAD_ISO02W100"
H2X_FARKD2 = acad.model.AddLine(n24,n21)
n4_n17 = acad.model.AddLine(n4,n17)
H13 = acad.model.AddLine(n28,n29)
H13X = acad.model.AddLine(n27,n30)
H5XY = acad.model.AddLine(n29,n30)
H5XYY = acad.model.AddLine(n28,n27)

H13XY = acad.model.AddLine(n32,n33)
H13XY = acad.model.AddLine(n31,n34)
H5XYYY = acad.model.AddLine(n32,n31)
H5XYYYY = acad.model.AddLine(n33,n34)
H2XX = acad.model.AddLine(n2,n19)
N23_N26 = acad.model.AddLine(n23,n26)
N23_N26.Linetype = "ACAD_ISO02W100"
N24_N25 = acad.model.AddLine(n24,n25)
N24_N25.Linetype = "ACAD_ISO02W100"

# Çizgilerin kalınlığını varsayılan yap
for line in [H2, H9, H8, H8X, H10, H1, H3, H4, H5, H6, H11, H12, H12X, H7, H7X, H11X, H6X, H5X, H4X, H3X, H1X, H10X, H9X, H2X, H2X_FARKY, H2X_FARKD, H2X_FARKY2, H2X_FARKD2, n4_n17, H13, H13X, H5XY, H5XYY, H13XY, H5XYYY, H5XYYYY, H2XX, N23_N26, N24_N25]:
    line.Lineweight = -1

print("Çizgilerin kalınlıkları varsayılana döndürüldü.")

#-------------------N2-N19-------------------------------------------
kisa_cizgi_boyu = H9_LEN * 6 / 10
oruntu_uzunlugu = H2_LEN / 90  # Her bir örüntü için toplam uzunluk

# Kısa çizgi uzunluğu ve uzun çizgi uzunluğunu dikkate alarak boşlukları hesapla
ilk_bosluk = oruntu_uzunlugu - (kisa_cizgi_boyu + H9_LEN) / 2
ikinci_bosluk = ilk_bosluk

# n2 ve n19 noktaları arasındaki mesafeyi hesapla
mesafe = n19.x - n2.x

# Maksimum örüntü sayısını hesapla
oruntu_sayisi = int(mesafe // oruntu_uzunlugu)

# Örüntüleri çiz
for i in range(oruntu_sayisi):
    baslangic_noktasi = APoint(n2.x + i * oruntu_uzunlugu, n2.y)
    
    # Kısa çizgi çiz
    kisa_cizgi_baslangic = baslangic_noktasi
    kisa_cizgi_bitis = APoint(kisa_cizgi_baslangic.x, kisa_cizgi_baslangic.y - kisa_cizgi_boyu)
    kisa_cizgi = acad.model.AddLine(kisa_cizgi_baslangic, kisa_cizgi_bitis)
    
    # Uzun çizgi çiz
    uzun_cizgi_baslangic = APoint(kisa_cizgi_baslangic.x + kisa_cizgi_boyu + ilk_bosluk, n2.y)
    uzun_cizgi_bitis = APoint(uzun_cizgi_baslangic.x, uzun_cizgi_baslangic.y - H9_LEN)
    uzun_cizgi = acad.model.AddLine(uzun_cizgi_baslangic, uzun_cizgi_bitis)

    # Çizgilerin kalınlığını varsayılana döndür
    uzun_cizgi.Lineweight = -1
    kisa_cizgi.Lineweight = -1

print(f"Toplam {oruntu_sayisi} örüntü çizildi.")

#-------------------N6-N15-------------------------------------------
kisa_cizgi_boyu = H4_LEN * 6 / 10
oruntu_uzunlugu = H8_LEN / 80  # Her bir örüntü için toplam uzunluk

# Kısa çizgi uzunluğu ve uzun çizgi uzunluğunu dikkate alarak boşlukları hesapla
ilk_bosluk = oruntu_uzunlugu - (kisa_cizgi_boyu + H4_LEN) / 2
ikinci_bosluk = ilk_bosluk

# n6 ve n15 noktaları arasındaki mesafeyi hesapla
mesafe = n15.x - n6.x

# Maksimum örüntü sayısını hesapla
oruntu_sayisi = int(mesafe // oruntu_uzunlugu)

# Örüntüleri çiz
for i in range(oruntu_sayisi):
    baslangic_noktasi = APoint(n6.x + i * oruntu_uzunlugu, n6.y)
    
    # Kısa çizgi çiz
    kisa_cizgi_baslangic = baslangic_noktasi
    kisa_cizgi_bitis = APoint(kisa_cizgi_baslangic.x, kisa_cizgi_baslangic.y - kisa_cizgi_boyu)
    kisa_cizgi = acad.model.AddLine(kisa_cizgi_baslangic, kisa_cizgi_bitis)
    
    # Uzun çizgi çiz
    uzun_cizgi_baslangic = APoint(kisa_cizgi_baslangic.x + kisa_cizgi_boyu + ilk_bosluk, n6.y)
    uzun_cizgi_bitis = APoint(uzun_cizgi_baslangic.x, uzun_cizgi_baslangic.y - H4_LEN)
    uzun_cizgi = acad.model.AddLine(uzun_cizgi_baslangic, uzun_cizgi_bitis)

    # Çizgilerin kalınlığını varsayılana döndür
    uzun_cizgi.Lineweight = -1
    kisa_cizgi.Lineweight = -1

print(f"Toplam {oruntu_sayisi} örüntü çizildi.")

#-------------------N27-N28-------------------------------------------
kisa_cizgi_boyu = H13_LEN * 6 / 10
oruntu_uzunlugu = 17  # Her bir örüntü için toplam uzunluk

# Kısa çizgi uzunluğu ve uzun çizgi uzunluğunu dikkate alarak boşlukları hesapla
ilk_bosluk = oruntu_uzunlugu - (kisa_cizgi_boyu + H13_LEN) / 2
ikinci_bosluk = ilk_bosluk

# n27 ve n28 noktaları arasındaki mesafeyi hesapla
mesafe = H5_LEN

# Maksimum örüntü sayısını hesapla
oruntu_sayisi = int(mesafe // oruntu_uzunlugu) - 1

# Çizgilerin yatay, örüntünün dikey eksende ilerlemesini sağla
for i in range(oruntu_sayisi):
    baslangic_noktasi = APoint(n27.x, n27.y + i * oruntu_uzunlugu + 20)
    
    # Kısa çizgi çiz
    kisa_cizgi_baslangic = APoint(baslangic_noktasi.x, baslangic_noktasi.y)
    kisa_cizgi_bitis = APoint(kisa_cizgi_baslangic.x + kisa_cizgi_boyu, kisa_cizgi_baslangic.y)
    kisa_cizgi = acad.model.AddLine(kisa_cizgi_baslangic, kisa_cizgi_bitis)
    
    # Uzun çizgi çiz
    uzun_cizgi_baslangic = APoint(baslangic_noktasi.x, baslangic_noktasi.y + kisa_cizgi_boyu + ilk_bosluk)
    uzun_cizgi_bitis = APoint(uzun_cizgi_baslangic.x + H13_LEN, uzun_cizgi_baslangic.y)
    uzun_cizgi = acad.model.AddLine(uzun_cizgi_baslangic, uzun_cizgi_bitis)

    # Çizgilerin kalınlığını varsayılana döndür
    uzun_cizgi.Lineweight = -1
    kisa_cizgi.Lineweight = -1


print(f"Toplam {oruntu_sayisi} örüntü çizildi.")

#-------------------N32-N31-------------------------------------------
# Çizgi uzunlukları ve boşluklar
kisa_cizgi_boyu = H13_LEN * 6 / 10
oruntu_uzunlugu = 17  # Her bir örüntü için toplam uzunluk

# n32 ve n31 noktaları arasındaki mesafeyi hesapla
mesafe = H5_LEN

# Maksimum örüntü sayısını hesapla
oruntu_sayisi = int(mesafe // oruntu_uzunlugu)

# Kısa çizgiler uzun çizgilerin üstünde olmalı
# Uzun çizgilerin üst kısmına kısa çizgileri hizalamak için offset miktarı
offset_miktari = 5  # İstenilen offset miktarını buraya girin

# Çizgilerin yatay, örüntünün dikey eksende ilerlemesini sağla
for i in range(oruntu_sayisi):
    baslangic_noktasi = APoint(n32.x, n31.y + i * oruntu_uzunlugu)
    
    # Uzun çizgi çiz
    uzun_cizgi_baslangic = APoint(baslangic_noktasi.x, baslangic_noktasi.y)
    uzun_cizgi_bitis = APoint(uzun_cizgi_baslangic.x + H13_LEN, uzun_cizgi_baslangic.y)
    uzun_cizgi = acad.model.AddLine(uzun_cizgi_baslangic, uzun_cizgi_bitis)
    
    # Kısa çizgi çiz (sola doğru uzanacak şekilde ve uzun çizginin üstünde)
    kisa_cizgi_baslangic = APoint(uzun_cizgi_bitis.x, uzun_cizgi_bitis.y + offset_miktari)
    kisa_cizgi_bitis = APoint(kisa_cizgi_baslangic.x - kisa_cizgi_boyu, kisa_cizgi_baslangic.y)
    kisa_cizgi = acad.model.AddLine(kisa_cizgi_baslangic, kisa_cizgi_bitis)

    # Çizgilerin kalınlığını varsayılana döndür
    uzun_cizgi.Lineweight = -1
    kisa_cizgi.Lineweight = -1

print(f"Toplam {oruntu_sayisi} örüntü çizildi.")

acad.ActiveDocument.Regen(1)



