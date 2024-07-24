from pyautocad import Autocad, APoint, aDouble
import win32com.client
import pythoncom
import json
from math import pi

# JSON dosyasını okuma
with open('input_data_form2.json', 'r') as f:
    data = json.load(f)

# JSON verilerini değişkenlere ata, varsayılan değerler 0
H2_LEN = int(data.get("H2_LEN", 0))
H3_LEN = int(data.get("H3_LEN", 0))
H4_LEN = int(data.get("H4_LEN", 0))
H4X_LEN = int(data.get("H4X_LEN", 0))
H5_LEN = int(data.get("H5_LEN", 0))
H5X_LEN = int(data.get("H5X_LEN", 0))
H6_LEN = int(data.get("H6_LEN", 0))
H7_LEN = int(data.get("H7_LEN", 0))
H9_LEN = int(data.get("H9_LEN", 0))
H9X_LEN = int(data.get("H9X_LEN", 0))
H10_LEN = int(data.get("H10_LEN", 0))
H10X_LEN = int(data.get("H10X_LEN", 0))
H15_LEN = int(data.get("H15_LEN", 0))
H16_LEN = int(data.get("H16_LEN", 0))
H17_LEN = int(data.get("H17_LEN", 0))
Q100 = int(data.get("Q100", 0))

# Değişkenleri ekrana yazdır
print(f"H2_LEN: {H2_LEN}")
print(f"H3_LEN: {H3_LEN}")
print(f"H4_LEN: {H4_LEN}")
print(f"H4X_LEN: {H4X_LEN}")
print(f"H5_LEN: {H5_LEN}")
print(f"H5X_LEN: {H5X_LEN}")
print(f"H6_LEN: {H6_LEN}")
print(f"H7_LEN: {H7_LEN}")
print(f"H9_LEN: {H9_LEN}")
print(f"H9X_LEN: {H9X_LEN}")
print(f"H10_LEN: {H10_LEN}")
print(f"H10X_LEN: {H10X_LEN}")
print(f"H15_LEN: {H15_LEN}")
print(f"H16_LEN: {H16_LEN}")
print(f"H17_LEN: {H17_LEN}")
print(f"Q100: {Q100}")

"""
H2_LEN = 100
H3_LEN = 600
H4_LEN = 250
H4X_LEN = 250
H5_LEN = 80
H5X_LEN = 130
H6_LEN = 50
H7_LEN = 10
H9_LEN = 314
H9X_LEN = 309
H10_LEN = 213
H10X_LEN = 211
H15_LEN = 50
H16_LEN=50
H17_LEN=50
Q100 = 20
#==============================================
#H8_LEN = 0
#H8X_LEN = 0
#H11_LEN = 0
#H11X_LEN = 0
#H12_LEN = 0
#H13_LEN = 0
#H13X_LEN = 0
#H14_LEN = 0
#H14X_LEN = 0
"""

#Q100 = 20
move = 2000
H4X_LEN =  H4_LEN 
H2X_LEN = H2_LEN
H15X_LEN = H15_LEN
H1_LEN = H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN
H12X_LEN = H1_LEN-H9_LEN-H9X_LEN

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
                                    0+move, 0,0,
                                    0+move, H4_LEN,0,
                                    -H5_LEN+move, H4_LEN,0,
                                    -H5_LEN+move, H4_LEN + H6_LEN,0,
                                    H9_LEN-H6_LEN+move-4,H4_LEN + H6_LEN + H7_LEN-10,0, #n7
                                    H9_LEN+move,H4_LEN,0,
                                    H1_LEN-H9X_LEN+move,H4_LEN,0,
                                    H1_LEN-H9X_LEN+H6_LEN+move+4,H4_LEN+H6_LEN+H7_LEN-10,0, #n12
                                    H9_LEN+H12X_LEN+H9X_LEN+H5X_LEN+move, H4_LEN+H6_LEN,0,
                                    H9_LEN+H12X_LEN+H9X_LEN+H5X_LEN+move, H4_LEN,0,
                                    H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+move, H4_LEN,0,
                                    H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+move,0,0,
                                    H10_LEN+H15_LEN+H3_LEN+move,0,0,
                                    H10_LEN+H15_LEN+H3_LEN+move,-H16_LEN,0,
                                    H10_LEN+H15_LEN+move,-H16_LEN,0,
                                    H10_LEN+H15_LEN+move,0,0,
                                    H10_LEN+move, 0,0,
                                    0+move, 0,0
                                     ]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "GRAVEL", True)
hatch.AppendOuterLoop(outer)
hatch.PatternScale = 5
hatch.EntityTransparency = 70
#hatch.Layer = "Layer4"

out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                     H10_LEN+H15_LEN+move,0,0,
                                     H10_LEN+H15_LEN+move,-H16_LEN,0,
                                     H10_LEN+H15_LEN+H3_LEN+move,-H16_LEN,0,
                                     H10_LEN+H15_LEN+H3_LEN+move,0,0,
                                     H10_LEN+H15_LEN+move,0,0
                                     ]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.PatternScale = 7
hatch.Color = 4
hatch.EntityTransparency = 70

out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                    H10_LEN+H15_LEN+move,-H16_LEN-H17_LEN,0,
                                    H10_LEN+H15_LEN+move,-H16_LEN,0,
                                    H10_LEN+H15_LEN+H3_LEN+move,-H16_LEN,0,
                                    H10_LEN+H15_LEN+H3_LEN+move,-H16_LEN-H17_LEN,0,
                                    H10_LEN+H15_LEN+move,-H16_LEN-H17_LEN,0
]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "AR-CONC", True)
hatch.AppendOuterLoop(outer)
hatch.PatternScale = 0.18
hatch.EntityTransparency = 70

out_loop = []
arc29 = acadModel.AddCIRCLE(aaPoint(H10_LEN+H15_LEN+70+move,45, 0), Q100)
arc29.lineweight = -1
out_loop.append(arc29)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.Color = 4
hatch.EntityTransparency = 90

out_loop = []
arc30 = acadModel.AddCIRCLE(aaPoint(H1_LEN-H10X_LEN-H15X_LEN-85+move,45, 0), Q100)
arc29.lineweight = -1
out_loop.append(arc30)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.Color = 4
hatch.EntityTransparency = 90

out_loop = []
arc31 = acadModel.AddCIRCLE(aaPoint(H10_LEN+H15_LEN-50+move,180, 0), 10)
arc29.lineweight = -1
out_loop.append(arc31)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.Color = 4
hatch.EntityTransparency = 90


out_loop = []
arc32 = acadModel.AddCIRCLE(aaPoint(H10_LEN+H15_LEN-50+200+move,180, 0), 10)
arc29.lineweight = -1
out_loop.append(arc32)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.Color = 4
hatch.EntityTransparency = 90


out_loop = []
arc33 = acadModel.AddCIRCLE(aaPoint(H10_LEN+H15_LEN-50+400+move,180, 0), 10)
arc29.lineweight = -1
out_loop.append(arc33)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.Color = 4
hatch.EntityTransparency = 90


out_loop = []
arc34 = acadModel.AddCIRCLE(aaPoint(H10_LEN+H15_LEN-50+600+move,180, 0), 10)
arc29.lineweight = -1
out_loop.append(arc34)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.Color = 4
hatch.EntityTransparency = 90


out_loop = []
arc35 = acadModel.AddCIRCLE(aaPoint(H10_LEN+H15_LEN+(H3_LEN/2)+move,-H2_LEN-100, 0), 40)
arc29.lineweight = -1
out_loop.append(arc35)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.Color = 4
hatch.EntityTransparency = 90


out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                     -H5_LEN+move, H4_LEN + H6_LEN,0,
                                     -H5_LEN+move, H4_LEN + H6_LEN + H7_LEN,0,
                                     H9_LEN-H6_LEN+move,H4_LEN + H6_LEN + H7_LEN,0, #n6
                                     +H9_LEN+15+move,H4_LEN+10,0, #n8
                                     H1_LEN-H9X_LEN+move-15,H4_LEN+10,0,#n11
                                     H1_LEN-H9X_LEN+H6_LEN+move,H4_LEN+H6_LEN+H7_LEN,0, #n13
                                     H9_LEN+H12X_LEN+H9X_LEN+H5X_LEN+move, H4_LEN+H6_LEN+H7_LEN,0,
                                     H9_LEN+H12X_LEN+H9X_LEN+H5X_LEN+move, H4_LEN+H6_LEN,0,
                                     H1_LEN-H9X_LEN+H6_LEN+move+4,H4_LEN+H6_LEN+H7_LEN-10,0, #n12
                                     H1_LEN-H9X_LEN+move,H4_LEN,0,
                                     H9_LEN+move,H4_LEN,0,
                                     H9_LEN-H6_LEN+move-4,H4_LEN + H6_LEN + H7_LEN-10,0, #n7
                                     -H5_LEN+move, H4_LEN + H6_LEN,0
                                     ]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.EntityTransparency = 70

out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                     H10_LEN+move, -H2_LEN,0,
                                     H10_LEN+move, 0,0,
                                     H10_LEN+H15_LEN+move,0,0,
                                     H10_LEN+H15_LEN+move,-H16_LEN-H17_LEN,0,
                                     H10_LEN+move, -H2_LEN,0
                                     ]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.EntityTransparency = 70

out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                     H10_LEN+H15_LEN+H3_LEN+H15X_LEN+move,0,0,
                                     H10_LEN+H15_LEN+H3_LEN+H15X_LEN+move,-H16_LEN-H17_LEN,0,
                                     H10_LEN+H15_LEN+H3_LEN+move,-H16_LEN-H17_LEN,0,
                                     H10_LEN+H15_LEN+H3_LEN+move,0,0,
                                     H10_LEN+H15_LEN+H3_LEN+H15X_LEN+move,0,0
                                     ]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.EntityTransparency = 70

#================bağlan============================================
# AutoCAD'e bağlan
acad = Autocad(create_if_not_exists=True)
acad.prompt("AutoCAD'e bağlanıldı\n")
print(acad.doc.Name)

n1 = APoint(0+move, 0)
n2 = APoint(0+move, H4_LEN)
n3 = APoint(-H5_LEN+move, H4_LEN)
n4 = APoint(-H5_LEN+move, H4_LEN + H6_LEN)
n5 = APoint(-H5_LEN+move, H4_LEN + H6_LEN + H7_LEN)
#=============================================
#n6 = APoint(H9_LEN-20+move,H4_LEN+H6_LEN-H7_LEN-10)
n6 = APoint(H9_LEN-H6_LEN+move,H4_LEN + H6_LEN + H7_LEN)
#n7 = APoint(H9_LEN-20+move,H4_LEN+H6_LEN-H7_LEN-20)
n7 = APoint(H9_LEN-H6_LEN+move-4,H4_LEN + H6_LEN + H7_LEN-10)
n8 = APoint(+H9_LEN+15+move,H4_LEN+10)
n9 = APoint(H9_LEN+move,H4_LEN)
n10 = APoint(H1_LEN-H9X_LEN+move,H4_LEN)
#=============================================
n11 = APoint(H1_LEN-H9X_LEN+move-15,H4_LEN+10)
#n12 = APoint(H1_LEN-H9X_LEN+15+move,H4_LEN+H6_LEN-H7_LEN-20)
n12 = APoint(H1_LEN-H9X_LEN+H6_LEN+move+4,H4_LEN+H6_LEN+H7_LEN-10)
#n13 = APoint(H1_LEN-H9X_LEN+10+move,H4_LEN+H6_LEN-H7_LEN-10)
n13 = APoint(H1_LEN-H9X_LEN+H6_LEN+move,H4_LEN+H6_LEN+H7_LEN)
#=============================================
n14 = APoint(H9_LEN+H12X_LEN+H9X_LEN+H5X_LEN+move, H4_LEN+H6_LEN)
n15 = APoint(H9_LEN+H12X_LEN+H9X_LEN+H5X_LEN+move, H4_LEN+H6_LEN+H7_LEN)
n16 = APoint(H9_LEN+H12X_LEN+H9X_LEN+H5X_LEN+move, H4_LEN)
n17 = APoint(H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+move, H4_LEN)
n18 = APoint(H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+move,0)
n19 = APoint(H10_LEN+H15_LEN+H3_LEN+H15_LEN+move,0)
n20 = APoint(H10_LEN+H15_LEN+H3_LEN+H15X_LEN+move,-H16_LEN-H17_LEN)
n21 = APoint(H10_LEN+move, -H2_LEN)
n22 = APoint(H10_LEN+move, 0)
n23 = APoint(H10_LEN+H15_LEN+move,0)
n24 = APoint(H10_LEN+H15_LEN+move,-H16_LEN)
n25 = APoint(H10_LEN+H15_LEN+move,-H16_LEN-H17_LEN)
n26 = APoint(H10_LEN+H15_LEN+H3_LEN+move,-H16_LEN-H17_LEN)
n27 = APoint(H10_LEN+H15_LEN+H3_LEN+move,-H16_LEN)
n28 = APoint(H10_LEN+H15_LEN+H3_LEN+move,0)
#DAİRE NOKTALARI
n29 = APoint(H10_LEN+H15_LEN+70+move,45)
n30= APoint(H1_LEN-H10X_LEN-H15X_LEN-85+move,45)
n31 = APoint(H10_LEN+H15_LEN-50+move,180)
n32 = APoint(H10_LEN+H15_LEN-50+200+move,180)
n33 = APoint(H10_LEN+H15_LEN-50+400+move,180)
n34 = APoint(H10_LEN+H15_LEN-50+600+move,180)
n35 = APoint(H10_LEN+H15_LEN+(H3_LEN/2)+move,-H2_LEN-100)


#=============================================

H4 = acad.model.AddLine(n1,n2)
H4X = acad.model.AddLine(n17,n18)
H5 = acad.model.AddLine(n2,n3)
H5X = acad.model.AddLine(n16,n17)
H6 = acad.model.AddLine(n3,n4)
H6X = acad.model.AddLine(n14,n16)
H7 = acad.model.AddLine(n4,n5)
H7X = acad.model.AddLine(n15,n14)
H8 = acad.model.AddLine(n5,n6)
H8X = acad.model.AddLine(n4,n7)
H9 = acad.model.AddLine(n6,n8)
H9 = acad.model.AddLine(n2,n9)
H9X = acad.model.AddLine(n10,n17)
H10X = acad.model.AddLine(n18,n19)
H11 = acad.model.AddLine(n6,n8)
H11X = acad.model.AddLine(n7,n9)
H12 = acad.model.AddLine(n8,n11)
H12X = acad.model.AddLine(n9,n10)
H13 = acad.model.AddLine(n11,n13)
H13X = acad.model.AddLine(n10,n12)
H14 = acad.model.AddLine(n15,n13)
H14X = acad.model.AddLine(n12,n14)
H2X = acad.model.AddLine(n19,n20)
H15XY = acad.model.AddLine(n20,n26)
H17X = acad.model.AddLine(n26,n27)
H16X = acad.model.AddLine(n27,n28)
H15X = acad.model.AddLine(n28,n19)
H3 = acad.model.AddLine(n25,n26)
H3X = acad.model.AddLine(n24,n27)
H3XX = acad.model.AddLine(n23,n28)
H15Y = acad.model.AddLine(n21,n25)
H17 = acad.model.AddLine(n24,n25)
H16 = acad.model.AddLine(n23,n24)
H2 = acad.model.AddLine(n21,n22)
H15 = acad.model.AddLine(n22,n23)
H10 = acad.model.AddLine(n1,n22)


N29C = acad.model.AddCircle(n29,Q100)
N30C = acad.model.AddCircle(n30,Q100)
N31C = acad.model.AddCircle(n31,10)
N32C = acad.model.AddCircle(n32,10)
N33C = acad.model.AddCircle(n33,10)
N34C = acad.model.AddCircle(n34,10)
N35C = acad.model.AddCircle(n35,40)

# Çizgilerin kalınlığını varsayılan yap
for line in [H4, H4X, H5, H5X, H6, H6X, H7, H7X, H8, H8X, H9, H9X, H10X, H11, H11X, H12, H12X, H13, H13X, H14, H14X, H2X, H15XY, H17X, H16X, H15X, H3, H3X, H3XX, H15Y, H17, H16, H2, H15, H10]:
    line.Lineweight = -1

acad.ActiveDocument.Regen(1)

