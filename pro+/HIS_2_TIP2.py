from pyautocad import Autocad, APoint, aDouble
import win32com.client
import pythoncom
import json
from math import pi

#-------------------------------------------------------------------------

# JSON dosyasını okuma
with open('input_data_form2_TIP2.json', 'r') as f:
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
H18_LEN = int(data.get("H18_LEN", 0))
H19_LEN = int(data.get("H19_LEN", 0))
H19X_LEN = int(data.get("H19X_LEN", 0))
H20_LEN = int(data.get("H20_LEN", 0))
H20X_LEN = int(data.get("H20X_LEN", 0))
Q100 = int(data.get("Q100", 0))
"""
H2_LEN = 100
H3_LEN = 860
H4_LEN = 250
H4X_LEN = 250
H5_LEN = 80
H5X_LEN = 130
H6_LEN = 50
H7_LEN = 10
H9_LEN = 314
H9X_LEN = 309
H10_LEN = 100
H10X_LEN = 75
H15_LEN = 50
H16_LEN=50
H17_LEN=50
H18_LEN = 100
H19_LEN = 100
H20_LEN = 100
H19X_LEN = 100
H20X_LEN = 100
Q100 = 20
"""

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
                                    -H19_LEN-H5_LEN+move, H18_LEN+H20_LEN,0,
                                    -H19_LEN-H5_LEN+move, H18_LEN+H20_LEN+H6_LEN,0,
                                    -H19_LEN+H9_LEN-H6_LEN+move, H18_LEN+H20_LEN+H6_LEN+H7_LEN-10,0,
                                    -H19_LEN+H9_LEN+move, H18_LEN+H20_LEN,0,
                                    H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+H19X_LEN-H9X_LEN+move,H18_LEN+H20X_LEN,0,
                                    H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+H19X_LEN-H9X_LEN+H6_LEN+move,H18_LEN+H20X_LEN+H6_LEN,0,
                                    H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+H19X_LEN+H5X_LEN+move,H18_LEN+H20X_LEN+H6_LEN,0,
                                    H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+H19X_LEN+H5X_LEN+move,H18_LEN+H20X_LEN,0,
                                    H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+H19X_LEN+move,H18_LEN+H20X_LEN,0,
                                    H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+H19X_LEN+move,H18_LEN,0,
                                    H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+move,H18_LEN,0,
                                    H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+move,0,0,
                                    H10_LEN+H15_LEN+H3_LEN+move,0,0,
                                    H10_LEN+H15_LEN+H3_LEN+move,-H16_LEN-H17_LEN,0,
                                    H10_LEN+H15_LEN+move,-H16_LEN-H17_LEN,0,
                                    H10_LEN+H15_LEN+move,0,0,
                                    0+move, 0,0,
                                    0+move, H18_LEN,0,
                                    -H19_LEN+move, H18_LEN,0,
                                    -H19_LEN+move, H18_LEN+H20_LEN,0,
                                    -H19_LEN-H5_LEN+move, H18_LEN+H20_LEN,0
                                     ]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "GRAVEL", True)
hatch.AppendOuterLoop(outer)
hatch.PatternScale = 5
hatch.EntityTransparency = 70

out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                     -H19_LEN-H5_LEN+move, H18_LEN+H20_LEN+H6_LEN,0,
                                    -H19_LEN-H5_LEN+move, H18_LEN+H20_LEN+H6_LEN+H7_LEN,0,
                                    -H19_LEN+H9_LEN-H6_LEN+move, H18_LEN+H20_LEN+H6_LEN+H7_LEN,0,
                                    -H19_LEN+H9_LEN+move, H18_LEN+H20_LEN+10,0,
                                    H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+H19X_LEN-H9X_LEN+move,H18_LEN+H20X_LEN+10,0,
                                    H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+H19X_LEN-H9X_LEN+H6_LEN+move,H18_LEN+H20X_LEN+H6_LEN+10,0,
                                    H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+H19X_LEN+H5X_LEN+move,H18_LEN+H20X_LEN+H6_LEN+H7_LEN,0,
                                    H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+H19X_LEN+H5X_LEN+move,H18_LEN+H20X_LEN+H6_LEN,0,
                                    H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+H19X_LEN-H9X_LEN+H6_LEN+move,H18_LEN+H20X_LEN+H6_LEN,0,
                                    H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+H19X_LEN-H9X_LEN+move,H18_LEN+H20X_LEN,0,
                                    -H19_LEN+H9_LEN+move, H18_LEN+H20_LEN,0,
                                    -H19_LEN+H9_LEN-H6_LEN+move, H18_LEN+H20_LEN+H6_LEN+H7_LEN-10,0,
                                    -H19_LEN-H5_LEN+move, H18_LEN+H20_LEN+H6_LEN,0
                                     ]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.EntityTransparency = 70

out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                     H10_LEN+H15_LEN+move,-H16_LEN,0,
                                     H10_LEN+H15_LEN+move,0,0,
                                    H10_LEN+H15_LEN+H3_LEN+move,0,0,
                                    H10_LEN+H15_LEN+H3_LEN+move,-H16_LEN,0,
                                     H10_LEN+H15_LEN+move,-H16_LEN,0,
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
                        H10_LEN+H15_LEN+H3_LEN+move,-H16_LEN-H17_LEN,0,
                                    H10_LEN+H15_LEN+H3_LEN+move,0,0,
H10_LEN+H15_LEN+H3_LEN+H15_LEN+move,0,0,
H10_LEN+H15_LEN+H3_LEN+H15X_LEN+move,-H16_LEN-H17_LEN,0,
H10_LEN+H15_LEN+H3_LEN+move,-H16_LEN-H17_LEN,0,
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
n2 = APoint(-H19_LEN+move, H18_LEN+H20_LEN)
n3 = APoint(-H19_LEN-H5_LEN+move, H18_LEN+H20_LEN)
n4 = APoint(-H19_LEN-H5_LEN+move, H18_LEN+H20_LEN+H6_LEN)
n5 = APoint(-H19_LEN-H5_LEN+move, H18_LEN+H20_LEN+H6_LEN+H7_LEN)

#n6 = APoint(H9_LEN-H6_LEN,H4_LEN + H6_LEN + H7_LEN)
#n7 = APoint(H9_LEN-20,H4_LEN+H6_LEN-H7_LEN-20)
#n7 = APoint(H9_LEN-H6_LEN-4,H4_LEN + H6_LEN + H7_LEN-10)
n8 = APoint(-H19_LEN+H9_LEN+move, H18_LEN+H20_LEN+10)
n9 = APoint(-H19_LEN+H9_LEN+move, H18_LEN+H20_LEN)
n10 = APoint(H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+H19X_LEN-H9X_LEN+move,H18_LEN+H20X_LEN)
#=============================================
n11 = APoint(H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+H19X_LEN-H9X_LEN+move,H18_LEN+H20X_LEN+10)
#n12 = APoint(H1_LEN-H9X_LEN+15,H4_LEN+H6_LEN-H7_LEN-20)
n12 = APoint(H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+H19X_LEN-H9X_LEN+H6_LEN+move,H18_LEN+H20X_LEN+H6_LEN)
#n13 = APoint(H1_LEN-H9X_LEN+10,H4_LEN+H6_LEN-H7_LEN-10)
n13 = APoint(H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+H19X_LEN-H9X_LEN+H6_LEN+move,H18_LEN+H20X_LEN+H6_LEN+10)
#=============================================
n14 = APoint(H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+H19X_LEN+H5X_LEN+move,H18_LEN+H20X_LEN+H6_LEN)
n15 = APoint(H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+H19X_LEN+H5X_LEN+move,H18_LEN+H20X_LEN+H6_LEN+H7_LEN)
n16 = APoint(H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+H19X_LEN+H5X_LEN+move,H18_LEN+H20X_LEN)
n17 = APoint(H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+H19X_LEN+move,H18_LEN+H20X_LEN)
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
nc29 = APoint(H10_LEN+H15_LEN+430+move,30)
n30 = APoint(0+move, H18_LEN)
n31 = APoint(-H19_LEN+move, H18_LEN)
n33 = APoint(H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+move,H18_LEN)
n32 = APoint(H10_LEN+H15_LEN+H3_LEN+H15X_LEN+H10X_LEN+H19X_LEN+move,H18_LEN)

n6 = APoint(-H19_LEN+H9_LEN-H6_LEN+move, H18_LEN+H20_LEN+H6_LEN+H7_LEN)
n7 = APoint(-H19_LEN+H9_LEN-H6_LEN+move, H18_LEN+H20_LEN+H6_LEN+H7_LEN-10)
n35 =APoint(H10_LEN+H15_LEN+210+move,-H16_LEN-H17_LEN-60)

nc31 = APoint(-H19_LEN+H9_LEN-70+move, H18_LEN+H20_LEN-20)
nc32 = APoint(-H19_LEN+H9_LEN-70+200+move, H18_LEN+H20_LEN-20)
nc33 = APoint(-H19_LEN+H9_LEN-70+400+move, H18_LEN+H20_LEN-20)
nc34 = APoint(-H19_LEN+H9_LEN-70+600+move, H18_LEN+H20_LEN-20)
nc35 = APoint(-H19_LEN+H9_LEN-70+800+move, H18_LEN+H20_LEN-20)
H2 = acad.model.AddLine(n21,n22)
H3 = acad.model.AddLine(n25,n26)
H3X = acad.model.AddLine(n24,n27)
H3XX = acad.model.AddLine(n23,n28)
H10 = acad.model.AddLine(n1,n22)
H15 = acad.model.AddLine(n22,n23)
H16 = acad.model.AddLine(n23,n24)
H17 = acad.model.AddLine(n24,n25)
H15XY = acad.model.AddLine(n20,n26)
H17X = acad.model.AddLine(n26,n27)
H16X = acad.model.AddLine(n27,n28)
H15X = acad.model.AddLine(n28,n19)
H2X = acad.model.AddLine(n19,n20)
H15Y = acad.model.AddLine(n21,n25)
H10X = acad.model.AddLine(n18,n19)
H18 = acad.model.AddLine(n1,n30)
H19 = acad.model.AddLine(n30,n31)
H20 = acad.model.AddLine(n31,n2)
H5 = acad.model.AddLine(n2,n3)
H5X = acad.model.AddLine(n16,n17)
H6 = acad.model.AddLine(n3,n4)
H7 = acad.model.AddLine(n4,n5)
H18X = acad.model.AddLine(n18,n33)
H19X = acad.model.AddLine(n33,n32)
H20X = acad.model.AddLine(n17,n32)
H5X = acad.model.AddLine(n17,n16)
H6X = acad.model.AddLine(n14,n16)
H7X = acad.model.AddLine(n15,n14)
H9 = acad.model.AddLine(n2,n9)
H9X = acad.model.AddLine(n10,n17)
H12X = acad.model.AddLine(n9,n10)
H8 = acad.model.AddLine(n5,n6)
H8X = acad.model.AddLine(n4,n7)
H11 = acad.model.AddLine(n6,n8)
H11X = acad.model.AddLine(n7,n9)
H12 =acad.model.AddLine(n8,n11)
H12X =acad.model.AddLine(n9,n10)
H13 = acad.model.AddLine(n11,n13)
H13X = acad.model.AddLine(n10,n12)
H14= acad.model.AddLine(n13,n15)
H14X= acad.model.AddLine(n12,n14)
n6_n7 = acad.model.AddLine(n6,n7)
n8_n9 = acad.model.AddLine(n8,n9)
n10_n11 = acad.model.AddLine(n10,n11)
n12_n13 = acad.model.AddLine(n12,n13)




N31C = acad.model.AddCircle(nc31,15)
N32C = acad.model.AddCircle(nc32,15)
N33C = acad.model.AddCircle(nc33,15)
N34C = acad.model.AddCircle(nc34,15)
N35C = acad.model.AddCircle(nc35,15)
N29C = acad.model.AddCircle(nc29,30)

