from pyautocad import Autocad, APoint, aDouble
import win32com.client
import pythoncom
import json
from math import pi

# JSON dosyasını okuma
with open('input_data_form2.json', 'r') as f:
    data = json.load(f)

# JSON verilerini değişkenlere ata
H1_LEN = int(data.get("H1_LEN", 0))
H2_LEN = int(data.get("H2_LEN", 0))
H3_LEN = int(data.get("H3_LEN", 0))
H4_LEN = int(data.get("H4_LEN", 0))
H5_LEN = int(data.get("H5_LEN", 0))
H6_LEN = int(data.get("H6_LEN", 0))
H7_LEN = int(data.get("H7_LEN", 0))
H9_LEN = int(data.get("H9_LEN", 0))
H10_LEN = int(data.get("H10_LEN", 0))

# Değişkenleri ekrana yazdır
print(f"H1_LEN: {H1_LEN}")
print(f"H2_LEN: {H2_LEN}")
print(f"H3_LEN: {H3_LEN}")
print(f"H4_LEN: {H4_LEN}")
print(f"H5_LEN: {H5_LEN}")
print(f"H6_LEN: {H6_LEN}")
print(f"H7_LEN: {H7_LEN}")
print(f"H9_LEN: {H9_LEN}")
print(f"H10_LEN: {H10_LEN}")

#H1_LEN = 1085
#H2_LEN = 100
#H3_LEN = 560
#H4_LEN = 250
#H5_LEN = 85
#H6_LEN = 70
#H7_LEN = 10
#H9_LEN = 315
#H10_LEN = 265
move = 2000

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
move+H10_LEN,-H2_LEN,0,
move+H10_LEN,0,0,
move+0,0,0,
move+0,H4_LEN,0,
-H5_LEN+move,H4_LEN,0,
-H5_LEN+move,H4_LEN+H6_LEN-H7_LEN,0,
H9_LEN-20+move,H4_LEN+H6_LEN-H7_LEN-20,0,
H9_LEN+move,H4_LEN,0,
H1_LEN-H9_LEN+move,H4_LEN,0,
H1_LEN-H9_LEN+15+move,H4_LEN+H6_LEN-H7_LEN-20,0,
H1_LEN+H5_LEN+move,H4_LEN+H6_LEN-H7_LEN,0,
H1_LEN+H5_LEN+move,H4_LEN,0,
H1_LEN+move,H4_LEN,0,
H1_LEN+move,0,0,
H1_LEN-H10_LEN+move,0,0,
H1_LEN-H10_LEN+move,-H2_LEN,0,
H10_LEN+move,-H2_LEN,0
                                     ]))

out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "GRAVEL", True)
hatch.AppendOuterLoop(outer)
hatch.PatternScale = 10

out_loop = []
arc23 = acadModel.AddCIRCLE(aaPoint(H1_LEN-H10_LEN-85+move,45, 0), 40)
out_loop.append(arc23)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.Color = 4

out_loop = []
arc24 = acadModel.AddCIRCLE(aaPoint(H10_LEN+70+move,45, 0), 40)
out_loop.append(arc24)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.Color = 4

out_loop = []
arc25 = acadModel.AddCIRCLE(aaPoint(H10_LEN-50+move,180, 0), 8)
out_loop.append(arc25)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.Color = 4

out_loop = []
arc26 = acadModel.AddCIRCLE(aaPoint(H10_LEN-50+200+move,180, 0), 8)
out_loop.append(arc26)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.Color = 4

out_loop = []
arc27 = acadModel.AddCIRCLE(aaPoint(H10_LEN-50+400+move,180, 0), 8)
out_loop.append(arc27)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.Color = 4

out_loop = []
arc28 = acadModel.AddCIRCLE(aaPoint(H10_LEN-50+600+move,180, 0), 8)
out_loop.append(arc28)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.Color = 4

out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                     -H5_LEN+move,H4_LEN+H6_LEN-H7_LEN,0,
                                     -H5_LEN+move,H4_LEN+H6_LEN,0,
                                     H9_LEN-20+move,H4_LEN+H6_LEN-H7_LEN-10,0,
                                     H9_LEN+5+move,H4_LEN+10,0,
                                     H1_LEN-H9_LEN+move,H4_LEN+10,0,
                                     H1_LEN-H9_LEN+10+move,H4_LEN+H6_LEN-H7_LEN-10,0,
                                     H1_LEN+H5_LEN+move,H4_LEN+H6_LEN,0,
                                     H1_LEN+H5_LEN+move,H4_LEN+H6_LEN-H7_LEN,0,
                                     H1_LEN-H9_LEN+15+move,H4_LEN+H6_LEN-H7_LEN-20,0,
                                     H1_LEN-H9_LEN+move,H4_LEN,0,
                                     H9_LEN+move,H4_LEN,0,
                                     H9_LEN-20+move,H4_LEN+H6_LEN-H7_LEN-20,0,
                                     -H5_LEN+move,H4_LEN+H6_LEN-H7_LEN,0
]))

out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.PatternScale = 7
hatch.EntityTransparency = 70

#================bağlan============================================
# AutoCAD'e bağlan
acad = Autocad(create_if_not_exists=True)
acad.prompt("AutoCAD'e bağlanıldı\n")
print(acad.doc.Name)
#================NOKTALAR============================================

n1 = APoint(0+move,0)
n2 = APoint(0+move,H4_LEN)
n3 = APoint(-H5_LEN+move,H4_LEN)
n4 = APoint(-H5_LEN+move,H4_LEN+H6_LEN-H7_LEN)
n5 = APoint(-H5_LEN+move,H4_LEN+H6_LEN)
n6 = APoint(H9_LEN-20+move,H4_LEN+H6_LEN-H7_LEN-10)
n7 = APoint(H9_LEN-20+move,H4_LEN+H6_LEN-H7_LEN-20)
n8 = APoint(+H9_LEN+5+move,H4_LEN+10)
n9 = APoint(H9_LEN+move,H4_LEN)
n10 = APoint(H1_LEN-H9_LEN+move,H4_LEN)
n11 = APoint(H1_LEN-H9_LEN+move,H4_LEN+10)
n12 = APoint(H1_LEN-H9_LEN+15+move,H4_LEN+H6_LEN-H7_LEN-20)
n13 = APoint(H1_LEN-H9_LEN+10+move,H4_LEN+H6_LEN-H7_LEN-10)
n14 = APoint(H1_LEN+H5_LEN+move,H4_LEN+H6_LEN-H7_LEN)
n15 = APoint(H1_LEN+H5_LEN+move,H4_LEN+H6_LEN)
n16 = APoint(H1_LEN+H5_LEN+move,H4_LEN)
n17 = APoint(H1_LEN+move,H4_LEN)
n18 = APoint(H1_LEN+move,0)
n19 = APoint(H1_LEN-H10_LEN+move,0)
n20 = APoint(H1_LEN-H10_LEN+move,-H2_LEN)
n21 = APoint(H10_LEN+move,-H2_LEN)
n22 = APoint(H10_LEN+move,0)
#DAİRE NOKTALARI
n23= APoint(H1_LEN-H10_LEN-85+move,45)
n24 = APoint(H10_LEN+70+move,45)
n25 = APoint(H10_LEN-50+move,180)
n26 = APoint(H10_LEN-50+200+move,180)
n27 = APoint(H10_LEN-50+400+move,180)
n28 = APoint(H10_LEN-50+600+move,180)
#=============================================
"""
X olursa o çizginin birebir kopyası ve farklı yerdeki hali
S olursa o çizginin bir bölümü ve kırpılmış hali(küçültülmüş)
"""
H1 = acad.model.AddLine(n19,n22)
H2 = acad.model.AddLine(n21,n22)
H2X = acad.model.AddLine(n19,n20)
H3 = acad.model.AddLine(n21,n20)
H3X = acad.model.AddLine(n22,n19)
H4 = acad.model.AddLine(n1,n2)
H4X = acad.model.AddLine(n17,n18)
H5 = acad.model.AddLine(n2,n3)
H5X = acad.model.AddLine(n16,n17)
H6 = acad.model.AddLine(n3,n5)
H6X = acad.model.AddLine(n14,n16)
H7 = acad.model.AddLine(n5,n4)
H7X = acad.model.AddLine(n15,n14)
H8 = acad.model.AddLine(n5,n6)
H8X = acad.model.AddLine(n4,n7)
H9 = acad.model.AddLine(n2,n9)
H9X = acad.model.AddLine(n10,n17)
H10 = acad.model.AddLine(n1,n22)
H10X = acad.model.AddLine(n18,n19)
H11 = acad.model.AddLine(n6,n8)
H11X = acad.model.AddLine(n7,n9)
H12 = acad.model.AddLine(n8,n11)
H12X = acad.model.AddLine(n9,n10)
H13 = acad.model.AddLine(n11,n13)
H13X = acad.model.AddLine(n10,n12)
H14 = acad.model.AddLine(n15,n13)
H14X = acad.model.AddLine(n12,n14)

N24D = acad.model.AddCircle(n24,40)
N23D = acad.model.AddCircle(n23,40)
N25D = acad.model.AddCircle(n25,8)
N26D = acad.model.AddCircle(n26,8)
N27D = acad.model.AddCircle(n27,8)
N28D = acad.model.AddCircle(n28,8)

acad.ActiveDocument.Regen(1)


