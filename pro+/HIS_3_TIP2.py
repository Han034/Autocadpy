from pyautocad import Autocad, APoint, aDouble
import win32com.client
import pythoncom
import json
from math import pi

# JSON dosyasını okuma
with open('input_data_form3_TIP2.json', 'r') as f:
    data = json.load(f)

# JSON verilerini değişkenlere ata
H9_LEN = int(data.get("H9_LEN", 0))
H10_LEN = int(data.get("H10_LEN", 0))
H1_LEN = int(data.get("H1_LEN", 0))
H3_LEN = int(data.get("H3_LEN", 0))
H4_LEN = int(data.get("H4_LEN", 0))
H11_LEN = int(data.get("H11_LEN", 0))
H13_LEN = int(data.get("H13_LEN", 0))
H12_LEN = int(data.get("H12_LEN", 0))
H14_LEN = int(data.get("H14_LEN", 0))
H7_LEN = int(data.get("H7_LEN", 0))
H12X_LEN = int(data.get("H12X_LEN", 0))
H3X_LEN = int(data.get("H3X_LEN", 0))
H2_LEN = int(data.get("H2_LEN", 0))
H8_LEN = int(data.get("H8_LEN", 0))
H3X_LEN = int(data.get("H3X_LEN", 0))


"""
H9_LEN = 50
H10_LEN = 75
H1_LEN = 550
H3_LEN = 350
H4_LEN = 100
H11_LEN = 150
H13_LEN = 50
H12_LEN = 250
H14_LEN = 50
H7_LEN = 860
H12X_LEN = 225
#H11X_LEN = 150
H3X_LEN = 325
H2_LEN = 960
H8_LEN = 1635

#H5_LEN = 120
#H6_LEN = 50
#length1 = H4_LEN
#length2 = H4_LEN/2

#length1_x = H13_LEN
#length2_x = H13_LEN / 2
"""
move = 4000
H40_LEN = 50 # fark yatay
H30_LEN = 50 # fark dikey
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
0+move, H9_LEN + H10_LEN,0,
0+move, H9_LEN + H10_LEN + H1_LEN,0,
0+H40_LEN+move, H9_LEN + H10_LEN + H1_LEN,0,
+H40_LEN+move, H9_LEN + H10_LEN,0,
0+move, H9_LEN + H10_LEN,0,
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
0+H40_LEN+move, H9_LEN + H10_LEN + H1_LEN-H30_LEN,0,
0+H40_LEN+move, H9_LEN + H10_LEN + H1_LEN,0,
-H3_LEN+H8_LEN-H3X_LEN-H40_LEN+move, H9_LEN + H10_LEN + H1_LEN,0,
-H3_LEN+H8_LEN-H3X_LEN-H30_LEN+move, H9_LEN + H10_LEN + H1_LEN-H30_LEN,0,
0+H40_LEN+move, H9_LEN + H10_LEN + H1_LEN-H30_LEN,0
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
0+H40_LEN+move, H9_LEN + H10_LEN + H1_LEN,0,
-H3_LEN+move, H9_LEN + H10_LEN + H1_LEN,0,
-H3_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN,0,
0+H40_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN,0,
0+H40_LEN+move, H9_LEN + H10_LEN + H1_LEN,0
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
-H3_LEN+H11_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN,0,
-H3_LEN+H11_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H13_LEN,0,
-H3_LEN+H11_LEN+H12_LEN+H7_LEN+H12X_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H13_LEN,0,
-H3_LEN+H11_LEN+H12_LEN+H7_LEN+H12X_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN,0,
-H3_LEN+H11_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN,0,
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
0+H40_LEN+100+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN,0,
0+H40_LEN+100+move, H9_LEN + H10_LEN + H1_LEN,0,
-H3_LEN+H8_LEN-H3X_LEN-H40_LEN-100+move, H9_LEN + H10_LEN + H1_LEN,0,
-H3_LEN+H8_LEN-H3X_LEN-H40_LEN-100+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN,0,
0+H40_LEN+100+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN,0
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
-H3_LEN+H8_LEN-H3X_LEN-H40_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN,0,
-H3_LEN+H8_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN,0,
-H3_LEN+H8_LEN+move, H9_LEN + H10_LEN + H1_LEN,0,
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
-H3_LEN+H11_LEN+H12_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H13_LEN,0,
-H3_LEN+H11_LEN+H12_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H13_LEN+H14_LEN,0,
-H3_LEN+H11_LEN+H12_LEN+H7_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H13_LEN+H14_LEN,0,
-H3_LEN+H11_LEN+H12_LEN+H7_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H13_LEN,0,
-H3_LEN+H11_LEN+H12_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H13_LEN,0
]))

sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.PatternScale = 7
hatch.EntityTransparency = 70

#=============================================================



# AutoCAD'e bağlan
acad = Autocad(create_if_not_exists=True)
acad.prompt("AutoCAD'e bağlanıldı\n")
print(acad.doc.Name)

n1 = APoint(0+move, 0)
n2 = APoint(0+move, H9_LEN)
n3 = APoint(0+move, H9_LEN + H10_LEN)
n4 = APoint(0+move, H9_LEN + H10_LEN + H1_LEN)
n5 = APoint(-H3_LEN+move, H9_LEN + H10_LEN + H1_LEN)
n6 = APoint(-H3_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN)
n7 = APoint(-H3_LEN+H11_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN)
n8 = APoint(-H3_LEN+H11_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H13_LEN)
n9 = APoint(-H3_LEN+H11_LEN+H12_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H13_LEN)
n10 = APoint(-H3_LEN+H11_LEN+H12_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H13_LEN+H14_LEN)
n11 = APoint(-H3_LEN+H11_LEN+H12_LEN+H7_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H13_LEN+H14_LEN)
n12 = APoint(-H3_LEN+H11_LEN+H12_LEN+H7_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H13_LEN)
n13 = APoint(-H3_LEN+H11_LEN+H12_LEN+H7_LEN+H12X_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN+H13_LEN)
n14 = APoint(-H3_LEN+H11_LEN+H12_LEN+H7_LEN+H12X_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN)
n15 = APoint(-H3_LEN+H8_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN)
n16 = APoint(-H3_LEN+H8_LEN+move, H9_LEN + H10_LEN + H1_LEN)
n17 = APoint(-H3_LEN+H8_LEN-H3X_LEN+move, H9_LEN + H10_LEN + H1_LEN)

n18 = APoint(H2_LEN+move, H9_LEN + H10_LEN)
n19 = APoint(H2_LEN+move, H9_LEN)
n20 = APoint(H2_LEN+move, 0)

n21 = APoint(H2_LEN-H40_LEN+move, H9_LEN + H10_LEN)
n22 = APoint(+H40_LEN+move, H9_LEN + H10_LEN)

n27 = APoint(0+H40_LEN+move, H9_LEN + H10_LEN + H1_LEN)
n28 = APoint(0+H40_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN)
n29 = APoint(0+H40_LEN+100+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN)
n30 = APoint(0+H40_LEN+100+move, H9_LEN + H10_LEN + H1_LEN)

n26 = APoint(0+H40_LEN+move, H9_LEN + H10_LEN + H1_LEN-H30_LEN)
n25 = APoint(-H3_LEN+H8_LEN-H3X_LEN-H30_LEN+move, H9_LEN + H10_LEN + H1_LEN-H30_LEN)
n34 = APoint(-H3_LEN+H8_LEN-H3X_LEN-H40_LEN+move, H9_LEN + H10_LEN + H1_LEN)
n33 = APoint(-H3_LEN+H8_LEN-H3X_LEN-H40_LEN+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN)
n32 = APoint(-H3_LEN+H8_LEN-H3X_LEN-H40_LEN-100+move, H9_LEN + H10_LEN + H1_LEN+H4_LEN)
n31 = APoint(-H3_LEN+H8_LEN-H3X_LEN-H40_LEN-100+move, H9_LEN + H10_LEN + H1_LEN)




H1 = acad.model.AddLine(n3,n4)
H1X = acad.model.AddLine(n18,n17)
H2 = acad.model.AddLine(n1,n20)
H2X = acad.model.AddLine(n2,n19)
H2X = acad.model.AddLine(n3,n18)
H3 = acad.model.AddLine(n4,n5)
H3X = acad.model.AddLine(n17,n16)
H4 = acad.model.AddLine(n5,n6)
H4X = acad.model.AddLine(n15,n16)
H9 = acad.model.AddLine(n1,n2)
H9X = acad.model.AddLine(n20,n19)
H10 = acad.model.AddLine(n2,n3)
H10X = acad.model.AddLine(n19,n18)
H11 = acad.model.AddLine(n6,n7)
H13 = acad.model.AddLine(n7,n8)
H12 = acad.model.AddLine(n8,n9)
H14 = acad.model.AddLine(n10,n9)
H7 = acad.model.AddLine(n10,n11)
H14X = acad.model.AddLine(n12,n11)
H12X = acad.model.AddLine(n12,n13)
H13X = acad.model.AddLine(n14,n13)
H11X = acad.model.AddLine(n14,n15)
N4_N17 = acad.model.AddLine(n4,n17)
N7_N14 = acad.model.AddLine(n7,n14)
N9_N12 = acad.model.AddLine(n9,n12)
N22_N26 = acad.model.AddLine(n22,n26)
N25_N26 = acad.model.AddLine(n25,n26)
N25_N21 = acad.model.AddLine(n25,n21)
N22_N21 = acad.model.AddLine(n22,n21)
N26_N27 = acad.model.AddLine(n26,n27)
N25_N34 = acad.model.AddLine(n25,n34)
N27_N28 = acad.model.AddLine(n27,n28)
N29_N28 = acad.model.AddLine(n29,n28)
N29_N30 = acad.model.AddLine(n29,n30)
N27_N30 = acad.model.AddLine(n27,n30)
N32_N31 = acad.model.AddLine(n32,n31)
N32_N33 = acad.model.AddLine(n32,n33)
N34_N33 = acad.model.AddLine(n34,n33)
N34_N31 = acad.model.AddLine(n34,n31)




#-------------------N2-N19-------------------------------------------
kisa_cizgi_boyu = H9_LEN * 6 / 10
oruntu_uzunlugu = H2_LEN / 90  # Her bir örüntü için toplam uzunluk

# Kısa çizgi uzunluğu ve uzun çizgi uzunluğunu dikkate alarak boşlukları hesapla
ilk_bosluk = oruntu_uzunlugu - (kisa_cizgi_boyu + H9_LEN) / 2
ikinci_bosluk = ilk_bosluk+200

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








