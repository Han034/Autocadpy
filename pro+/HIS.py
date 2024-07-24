from pyautocad import Autocad, APoint, aDouble
import win32com.client
import pythoncom
import json
from math import pi
import math

#============DEĞERLER======================================

# JSON dosyasını okuma
with open('input_data_form1.json', 'r') as f:
    data = json.load(f)

# JSON verilerini değişkenlere ata
A1_LEN = int(data.get("A1_LEN", 0))
A2_LEN = int(data.get("A2_LEN", 0))
A3_LEN = int(data.get("A3_LEN", 0))

B1_LEN = int(data.get("B1_LEN", 0))
B2_LEN = int(data.get("B2_LEN", 0))

C1_LEN = int(data.get("C1_LEN", 0))
C2_LEN = int(data.get("C2_LEN", 0))
C3_LEN = int(data.get("C3_LEN", 0))
C4_LEN = int(data.get("C4_LEN", 0))

D1_LEN = int(data.get("D1_LEN", 0))
D2_LEN = int(data.get("D2_LEN", 0))
D4_LEN = int(data.get("D4_LEN", 0))
D5_LEN = int(data.get("D5_LEN", 0))

H2_LEN = int(data.get("H2_LEN", 0))
H3_LEN = int(data.get("H3_LEN", 0))
H4_LEN = int(data.get("H4_LEN", 0))
H5_LEN = int(data.get("H5_LEN", 0))

G_LEN = int(data.get("G_LEN", 0))

#T_LEN = int(data.get("T_LEN", 0))
TB1_LEN = int(data.get("TB1_LEN", 0))
TB2_LEN = int(data.get("TB2_LEN", 0))

A10_LEN = int(data.get("A10_LEN", 0))
B10_LEN = int(data.get("B10_LEN", 0))
E10_LEN = int(data.get("E10_LEN", 0))

# Değişkenleri ekrana yazdır
print(f"A1_LEN: {A1_LEN}")
print(f"A2_LEN: {A2_LEN}")
print(f"A3_LEN: {A3_LEN}")

print(f"B1_LEN: {B1_LEN}")
print(f"B2_LEN: {B2_LEN}")

print(f"C1_LEN: {C1_LEN}")
print(f"C2_LEN: {C2_LEN}")
print(f"C3_LEN: {C3_LEN}")
print(f"C4_LEN: {C4_LEN}")

print(f"D1_LEN: {D1_LEN}")
print(f"D2_LEN: {D2_LEN}")
print(f"D4_LEN: {D4_LEN}")
print(f"D5_LEN: {D5_LEN}")

print(f"H2_LEN: {H2_LEN}")
print(f"H3_LEN: {H3_LEN}")
print(f"H4_LEN: {H4_LEN}")
print(f"H5_LEN: {H5_LEN}")

print(f"G_LEN: {G_LEN}")

#print(f"T_LEN: {T_LEN}")
print(f"TB1_LEN: {TB1_LEN}")
print(f"TB2_LEN: {TB2_LEN}")

"""
A1_LEN= 100
A2_LEN= 100
A3_LEN= 50

B1_LEN= 470
B2_LEN= 120

C1_LEN = 800
C2_LEN= 50
C3_LEN= 50
C4_LEN= 50

D1_LEN = 125
D2_LEN = 75
D4_LEN= 50
D5_LEN = 100

H2_LEN= 100
H3_LEN= 180
H4_LEN = 180
H5_LEN= 150

G_LEN = 10

TB1_LEN = 250
TB2_LEN = 250

T_LEN= 100 #gereksiz



"""

#============İÇ HESAPLAMA======================================
B10_LEN = 20 #sbt
A10_LEN = 40 #sbt
E10_LEN = (A10_LEN*(B1_LEN-A2_LEN-A1_LEN))/(B10_LEN)
B3_LEN = (B1_LEN)-(A1_LEN+A2_LEN+B2_LEN+A3_LEN)
B2_asagi_cizgi = B2_LEN/8
R_LEN = ((H5_LEN*B3_LEN)/(H3_LEN+H4_LEN+H5_LEN))
S_LEN= (G_LEN*R_LEN)/(H5_LEN)
B1_E10 = B1_LEN-E10_LEN

#==================================================

#==================ÜÇGEN NOKTA HESAPLAMA(k_10)================================
# AutoCAD'e bağlan
acad = Autocad(create_if_not_exists=True)
acad.prompt("AutoCAD'e bağlanıldı\n")
print(acad.doc.Name)

# Üçgenin köşe noktaları
A = APoint(A2_LEN+A3_LEN+B2_LEN,H2_LEN)  # A noktası (270, 100)
B = APoint(B1_LEN-A1_LEN,H2_LEN)  # B noktası (370, 100)
C = APoint(A2_LEN+B2_LEN+A3_LEN,(H2_LEN+H3_LEN+H4_LEN+H5_LEN))  # C noktası (270, 510)

# Dik kenar üzerindeki nokta
y0 = H2_LEN+H3_LEN+H4_LEN-10
a = APoint(A2_LEN+B2_LEN+A3_LEN, y0)  # a noktası (270, 450)

# Hipotenüsün denklemi: y = -4.1x + 1637
hipotenus_slope = (C.y - B.y) / (C.x - B.x)  # Eğim hesaplanması
hipotenus_intercept = C.y - (hipotenus_slope * C.x)  # y-keseni hesaplanması

# Çizgi denklemi: y = y0
line_slope = -0,3
line_intercept = y0

# Kesişim noktası hesaplaması
x_intercept = (line_intercept - hipotenus_intercept) / hipotenus_slope
y_intercept = line_intercept

# Kesişim noktası hipotenüs üzerinde olmalı
b = APoint(x_intercept, y_intercept)  # k_10 noktası

# Çizginin uzunluğunu hesapla
line_length = math.sqrt((b.x - a.x)**2 + (b.y - a.y)**2)
print(line_length)

# Hesaplama sonuçlarını yazdır
print(f"Kesişim noktası: ({b.x}, {b.y})")
print(f"Çizginin uzunluğu: {line_length:.2f}")

#---------------------su2---------------------------------
#su1 = (A2_LEN+A3_LEN,H2_LEN+H3_LEN+H4_LEN-35)
# Dik kenar üzerindeki nokta
y0 = H2_LEN+H3_LEN+H4_LEN-55
a2 = APoint(A2_LEN+B2_LEN+A3_LEN, y0)  # a noktası (270, 450)

# Hipotenüsün denklemi: y = -4.1x + 1637
hipotenus_slope = (C.y - B.y) / (C.x - B.x)  # Eğim hesaplanması
hipotenus_intercept = C.y - (hipotenus_slope * C.x)  # y-keseni hesaplanması

# Çizgi denklemi: y = y0
line_slope = -0,3
line_intercept = y0

# Kesişim noktası hesaplaması
x2_intercept = (line_intercept - hipotenus_intercept) / hipotenus_slope
y2_intercept = line_intercept

# Kesişim noktası hipotenüs üzerinde olmalı
b2 = APoint(x2_intercept, y2_intercept)  # k_10 noktası

# Çizginin uzunluğunu hesapla
line_length = math.sqrt((b2.x - a2.x)**2 + (b2.y - a2.y)**2)
print(line_length)

# Hesaplama sonuçlarını yazdır
print(f"Kesişim noktası: ({b2.x}, {b2.y})")
print(f"Çizginin uzunluğu: {line_length:.2f}")
#----------------------------------------------------------

#---------------------su4---------------------------------
#su3 = APoint(A2_LEN+A3_LEN,H2_LEN+H3_LEN+H4_LEN-55)
# Dik kenar üzerindeki nokta
y0 = H2_LEN+H3_LEN+H4_LEN-80
a4 = APoint(A2_LEN+B2_LEN+A3_LEN, y0)  # a noktası (270, 450)

# Hipotenüsün denklemi: y = -4.1x + 1637
hipotenus_slope = (C.y - B.y) / (C.x - B.x)  # Eğim hesaplanması
hipotenus_intercept = C.y - (hipotenus_slope * C.x)  # y-keseni hesaplanması

# Çizgi denklemi: y = y0
line_slope = -0,3
line_intercept = y0

# Kesişim noktası hesaplaması
x4_intercept = (line_intercept - hipotenus_intercept) / hipotenus_slope
y4_intercept = line_intercept

# Kesişim noktası hipotenüs üzerinde olmalı
b4 = APoint(x4_intercept, y4_intercept)  # k_10 noktası

# Çizginin uzunluğunu hesapla
line_length = math.sqrt((b4.x - a4.x)**2 + (b4.y - a4.y)**2)
print(line_length)

# Hesaplama sonuçlarını yazdır
print(f"Kesişim noktası: ({b4.x}, {b4.y})")
print(f"Çizginin uzunluğu: {line_length:.2f}")
#---------------------------------------------------------

#---------------------su6---------------------------------
#su5 = APoint(A2_LEN,H2_LEN+H3_LEN-60)
# Dik kenar üzerindeki nokta
y0 = H2_LEN+H3_LEN-75
a6 = APoint(A2_LEN+B2_LEN+A3_LEN, y0)  # a noktası (270, 450)

# Hipotenüsün denklemi: y = -4.1x + 1637
hipotenus_slope = (C.y - B.y) / (C.x - B.x)  # Eğim hesaplanması
hipotenus_intercept = C.y - (hipotenus_slope * C.x)  # y-keseni hesaplanması

# Çizgi denklemi: y = y0
line_slope = -0,3
line_intercept = y0

# Kesişim noktası hesaplaması
x6_intercept = (line_intercept - hipotenus_intercept) / hipotenus_slope
y6_intercept = line_intercept

# Kesişim noktası hipotenüs üzerinde olmalı
b6 = APoint(x6_intercept, y6_intercept)  # k_10 noktası

# Çizginin uzunluğunu hesapla
line_length = math.sqrt((b6.x - a6.x)**2 + (b6.y - a6.y)**2)
print(line_length)

# Hesaplama sonuçlarını yazdır
print(f"Kesişim noktası: ({b6.x}, {b6.y})")
print(f"Çizginin uzunluğu: {line_length:.2f}")
#------------------------------------------------------

#---------------------su8---------------------------------
# su7 = APoint(A2_LEN,H2_LEN+H3_LEN-140)
# Dik kenar üzerindeki nokta
y0 = H2_LEN+H3_LEN-155
a8 = APoint(A2_LEN+B2_LEN+A3_LEN, y0)  # a noktası (270, 450)

# Hipotenüsün denklemi: y = -4.1x + 1637
hipotenus_slope = (C.y - B.y) / (C.x - B.x)  # Eğim hesaplanması
hipotenus_intercept = C.y - (hipotenus_slope * C.x)  # y-keseni hesaplanması

# Çizgi denklemi: y = y0
line_slope = -0,3
line_intercept = y0

# Kesişim noktası hesaplaması
x8_intercept = (line_intercept - hipotenus_intercept) / hipotenus_slope
y8_intercept = line_intercept

# Kesişim noktası hipotenüs üzerinde olmalı
b8 = APoint(x8_intercept, y8_intercept)  # k_10 noktası

# Çizginin uzunluğunu hesapla
line_length = math.sqrt((b8.x - a8.x)**2 + (b8.y - a8.y)**2)
print(line_length)

# Hesaplama sonuçlarını yazdır
print(f"Kesişim noktası: ({b8.x}, {b8.y})")
print(f"Çizginin uzunluğu: {line_length:.2f}")
#------------------------------------------------------
#==================================================

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
                                     A2_LEN+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN),0,
                                     A2_LEN+A3_LEN,H2_LEN+H3_LEN+H4_LEN+H5_LEN,0,
                                     A2_LEN+B2_LEN+A3_LEN,(H2_LEN+H3_LEN+H4_LEN+H5_LEN),0,
                                     A2_LEN+B2_LEN+S_LEN+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN),0,
                                     A2_LEN+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN),0
                                     ]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.EntityTransparency = 70

out_loop2 = []
sq2 = acadModel.AddPolyline(aaDouble([
                                     B1_LEN+C1_LEN,C2_LEN+D4_LEN+C3_LEN,0,
                                     B1_LEN+C1_LEN,-C4_LEN,0,
                                     #B1_LEN+C1_LEN,0,0,
                                     B1_LEN+C1_LEN+D1_LEN,-C4_LEN,0,
                                     #B1_LEN+C1_LEN+D1_LEN,0,0,
                                     B1_LEN+C1_LEN+D1_LEN,D5_LEN-C4_LEN,0,
                                     B1_LEN+C1_LEN+D2_LEN,D4_LEN+C2_LEN+C3_LEN,0,
                                     B1_LEN+C1_LEN,C2_LEN+D4_LEN+C3_LEN,0
                                     ]))
sq.lineweight = -1
out_loop2.append(sq2)
outer2 = aavariants(out_loop2)
hatch = acadModel.AddHatch(0, "GRAVEL", True)
hatch.AppendOuterLoop(outer2)
hatch.PatternScale = 10
hatch.EntityTransparency = 70

out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                     B1_LEN+C1_LEN,H2_LEN,0,
                                     B1_LEN+C1_LEN,C2_LEN,0,
                                     B1_LEN,C2_LEN,0,
                                     B1_LEN,H2_LEN,0,
                                     B1_LEN+C1_LEN,H2_LEN,0
                                     ]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "GRAVEL", True)
hatch.AppendOuterLoop(outer)
hatch.PatternScale = 7
hatch.EntityTransparency = 70

out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                     B1_LEN+C1_LEN,H2_LEN,0,
                                     B1_LEN+C1_LEN,C2_LEN,0,
                                     B1_LEN,C2_LEN,0,
                                     B1_LEN,H2_LEN,0,
                                     B1_LEN+C1_LEN,H2_LEN,0
                                     ]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.PatternScale = 7
hatch.Color = 4
hatch.EntityTransparency = 90

out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                    B1_LEN,H2_LEN,0,
                                    B1_LEN,0,0,
                                    0,0,0,
                                    0,H2_LEN,0,
                                    A2_LEN,H2_LEN,0,
                                    A2_LEN,H2_LEN+H3_LEN,0,
                                    A2_LEN+A3_LEN,H2_LEN+H3_LEN,0,
                                    A2_LEN+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN),0,
                                    A2_LEN+A3_LEN,H2_LEN+H3_LEN+H4_LEN-10,0,  
                                            x_intercept, y_intercept,0,                         
                                    #A2_LEN+B2_LEN+A3_LEN+R_LEN,H2_LEN+H3_LEN+H4_LEN-10,0,
                                    B1_LEN-A1_LEN,H2_LEN,0,
                                    B1_LEN,H2_LEN,0
                                     ]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "GRAVEL", True)
hatch.AppendOuterLoop(outer)
hatch.PatternScale = 7
hatch.EntityTransparency = 70

out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                    B1_LEN,0,0,
                                    B1_LEN,C3_LEN,0,
                                    B1_LEN+C1_LEN,C3_LEN,0,
                                    B1_LEN+C1_LEN,0,0,
                                    B1_LEN,0,0
                                     ]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "AR-CONC", True)
hatch.AppendOuterLoop(outer)
hatch.PatternScale = 0.35
hatch.EntityTransparency = 70

out_loop = []
sq = acadModel.AddPolyline(aaDouble([
                                     A2_LEN+A3_LEN,H2_LEN+H3_LEN+H4_LEN,0,
                                     A2_LEN+B2_LEN+A3_LEN+R_LEN+15,H2_LEN+H3_LEN+H4_LEN,0,
                                     A2_LEN+B2_LEN+A3_LEN+R_LEN+15,H2_LEN+H3_LEN+H4_LEN-10,0,
                                     A2_LEN+A3_LEN,H2_LEN+H3_LEN+H4_LEN-10,0,
                                     A2_LEN+A3_LEN,H2_LEN+H3_LEN+H4_LEN,0
                                     ]))
sq.lineweight = -1
out_loop.append(sq)
outer = aavariants(out_loop)
hatch = acadModel.AddHatch(0, "SOLID", True)
hatch.AppendOuterLoop(outer)
hatch.EntityTransparency = 90


#==================================================

# AutoCAD'e bağlan
acad = Autocad(create_if_not_exists=True)
acad.prompt("AutoCAD'e bağlanıldı\n")
print(acad.doc.Name)

#============ŞEKİL ÖTELEME======================================
offset_x = 10
offset_y = 10

#============NOKTALAR===========================================
a = APoint(0,0)
b = APoint(B1_LEN,0)
c = APoint(0,H2_LEN)
d = APoint(A2_LEN,H2_LEN)
e = APoint(A2_LEN,H2_LEN+H3_LEN)
f = APoint(A2_LEN+A3_LEN,H2_LEN+H3_LEN+H4_LEN)
g = APoint(A2_LEN+A3_LEN,H2_LEN+H3_LEN+H4_LEN+H5_LEN)
g_10 = APoint(A2_LEN+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN))
h= APoint(A2_LEN+B2_LEN+A3_LEN,(H2_LEN+H3_LEN+H4_LEN+H5_LEN))
j = APoint(A2_LEN+B2_LEN+S_LEN+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN))
k = APoint(A2_LEN+B2_LEN+A3_LEN+R_LEN,H2_LEN+H3_LEN+H4_LEN)
l = APoint(B1_LEN-A1_LEN,H2_LEN)
m = APoint(B1_LEN,H2_LEN)
n = APoint(B1_LEN,C3_LEN+C2_LEN)
o = APoint(B1_LEN,C3_LEN)
p = APoint(B1_LEN+C1_LEN,C2_LEN+C3_LEN+D4_LEN)
r = APoint(B1_LEN+C1_LEN,C2_LEN)
s = APoint(B1_LEN+C1_LEN,-C4_LEN)
s3 = APoint(B1_LEN+C1_LEN,C3_LEN+C2_LEN)
s2 = APoint(B1_LEN+C1_LEN,C3_LEN)
s1 = APoint(B1_LEN+C1_LEN,0)
t = APoint(B1_LEN+C1_LEN+D1_LEN,-C4_LEN)
za = APoint(A2_LEN+A3_LEN,H2_LEN+H3_LEN)
u = APoint(B1_LEN+C1_LEN+D1_LEN,D5_LEN-C4_LEN)
ü = APoint(B1_LEN+C1_LEN+D2_LEN,D4_LEN+C2_LEN+C3_LEN)
#x1 = APoint(A2_LEN,H2_LEN+A10_LEN)
#x3 = APoint(A2_LEN,H2_LEN+A10_LEN+B10_LEN)
#x2 = APoint(B1_LEN-A1_LEN-E10_LEN,H2_LEN+A10_LEN)
c_sol = APoint(-(TB1_LEN),H2_LEN)
u_sag = APoint(B1_LEN+C1_LEN+D1_LEN+TB1_LEN,D5_LEN-C4_LEN)

k_15 = APoint(A2_LEN+B2_LEN+A3_LEN+R_LEN+15,H2_LEN+H3_LEN+H4_LEN)
f_10 = APoint(A2_LEN+A3_LEN,H2_LEN+H3_LEN+H4_LEN-10)
k_15_10 = APoint(A2_LEN+B2_LEN+A3_LEN+R_LEN+15,H2_LEN+H3_LEN+H4_LEN-10)


su1 = APoint(A2_LEN+A3_LEN,H2_LEN+H3_LEN+H4_LEN-45)
su3 = APoint(A2_LEN+A3_LEN,H2_LEN+H3_LEN+H4_LEN-70)

su5 = APoint(A2_LEN,H2_LEN+H3_LEN-60)
su7 = APoint(A2_LEN,H2_LEN+H3_LEN-140)
"""
#============C_SOL CİZİK============================

c_sol_cizik = APoint(-(TB1_LEN)+1,H2_LEN)
c_sol_cizik_alt = APoint(-(TB1_LEN)+1.5,H2_LEN-0.5)
c_sol_cizik1 = APoint(-(TB1_LEN)+2,H2_LEN)
c_sol_cizik_alt1 = APoint(-(TB1_LEN)+2.5,H2_LEN-0.5)
c_sol_cizik2 = APoint(-(TB1_LEN)+3,H2_LEN)
c_sol_cizik_alt2 = APoint(-(TB1_LEN)+3.5,H2_LEN-0.5)
c_sol_cizik3 = APoint(-(TB1_LEN)+3.5,H2_LEN)
c_sol_cizik_alt3 = APoint(-(TB1_LEN)+4,H2_LEN-0.5)
c_sol_cizik4 = APoint(-(TB1_LEN)+4,H2_LEN)
c_sol_cizik_alt4 = APoint(-(TB1_LEN)+4.5,H2_LEN-0.5)
c_sol_cizik_sag = APoint(-(TB1_LEN)+1,H2_LEN)
c_sol_cizik_alt_sag = APoint(-(TB1_LEN)+0.5,H2_LEN-0.5)
c_sol_cizik_sag2 = APoint(-(TB1_LEN)+2,H2_LEN)
c_sol_cizik_alt_sag2 = APoint(-(TB1_LEN)+1,H2_LEN-0.5)
c_sol_cizik_sag3 = APoint(-(TB1_LEN)+3,H2_LEN)
c_sol_cizik_alt_sag3 = APoint(-(TB1_LEN)+2,H2_LEN-0.5)
c_sol_cizik_sag4 = APoint(-(TB1_LEN)+4,H2_LEN)
c_sol_cizik_alt_sag4 = APoint(-(TB1_LEN)+3,H2_LEN-0.5)
#===================================================

#============U_SAĞ CİZİK============================
u_sag_cizik = APoint(B1_LEN+C1_LEN+D1_LEN+TB1_LEN-1,H2_LEN)
u_sag_cizik_alt = APoint(B1_LEN+C1_LEN+D1_LEN+TB1_LEN-1.5,H2_LEN-0.5)
u_sag_cizik2 = APoint(B1_LEN+C1_LEN+D1_LEN+TB1_LEN-2,H2_LEN)
u_sag_cizik_alt2 = APoint(B1_LEN+C1_LEN+D1_LEN+TB1_LEN-2.5,H2_LEN-0.5)
u_sag_cizik3 = APoint(B1_LEN+C1_LEN+D1_LEN+TB1_LEN-3,H2_LEN)
u_sag_cizik_alt3 = APoint(B1_LEN+C1_LEN+D1_LEN+TB1_LEN-3.5,H2_LEN-0.5)
u_sag_cizik4 = APoint(B1_LEN+C1_LEN+D1_LEN+TB1_LEN-4,H2_LEN)
u_sag_cizik_alt4 = APoint(B1_LEN+C1_LEN+D1_LEN+TB1_LEN-4.5,H2_LEN-0.5)
u_sag_cizik_sol = APoint(B1_LEN+C1_LEN+D1_LEN+TB1_LEN-2,H2_LEN)
u_sag_cizik_alt_sol = APoint(B1_LEN+C1_LEN+D1_LEN+TB1_LEN-0.5,H2_LEN-0.5)
u_sag_cizik_sol2 = APoint(B1_LEN+C1_LEN+D1_LEN+TB1_LEN-3,H2_LEN)
u_sag_cizik_alt_sol2 = APoint(B1_LEN+C1_LEN+D1_LEN+TB1_LEN-2.5,H2_LEN-0.5)
u_sag_cizik_sol3 = APoint(B1_LEN+C1_LEN+D1_LEN+TB1_LEN-4,H2_LEN)
u_sag_cizik_alt_sol3 = APoint(B1_LEN+C1_LEN+D1_LEN+TB1_LEN-3.5,H2_LEN-0.5)
u_sag_cizik_sol4 = APoint(B1_LEN+C1_LEN+D1_LEN+TB1_LEN-5,H2_LEN)
u_sag_cizik_alt_sol4 = APoint(B1_LEN+C1_LEN+D1_LEN+TB1_LEN-4.5,H2_LEN-0.5)
#===================================================
"""

#////////// U_SAĞ CİZİK/////////////////////////////
b2_dik_cizgi = APoint(A2_LEN+B2_asagi_cizgi+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN))
b2_dik_alt = APoint(A2_LEN+B2_asagi_cizgi+A3_LEN,((H2_LEN+H3_LEN+H4_LEN)))
b2_dik_cizgi_kisa = APoint((A2_LEN+(B2_asagi_cizgi/2)+A3_LEN),((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN))
b2_dik_alt_kisa = APoint(A2_LEN+(B2_asagi_cizgi/2)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+(H5_LEN/2))))

b2_dik_cizgi2 = APoint(A2_LEN+(2*B2_asagi_cizgi)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN))
b2_dik_alt2 = APoint(A2_LEN+(2*B2_asagi_cizgi)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN)))
b2_dik_cizgi_kisa2 = APoint((A2_LEN+(1.5*B2_asagi_cizgi)+A3_LEN),((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN))
b2_dik_alt_kisa2 = APoint(A2_LEN+(1.5*B2_asagi_cizgi)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+(H5_LEN/2))))

b2_dik_cizgi3 = APoint(A2_LEN+(3*B2_asagi_cizgi)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN))
b2_dik_alt3 = APoint(A2_LEN+(3*B2_asagi_cizgi)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN)))
b2_dik_cizgi_kisa3 = APoint((A2_LEN+(2.5*B2_asagi_cizgi)+A3_LEN),((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN))
b2_dik_alt_kisa3 = APoint(A2_LEN+(2.5*B2_asagi_cizgi)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+(H5_LEN/2))))

b2_dik_cizgi4 = APoint(A2_LEN+(4*B2_asagi_cizgi)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN))
b2_dik_alt4 = APoint(A2_LEN+(4*B2_asagi_cizgi)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN)))
b2_dik_cizgi_kisa4 = APoint((A2_LEN+(3.5*B2_asagi_cizgi)+A3_LEN),((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN))
b2_dik_alt_kisa4 = APoint(A2_LEN+(3.5*B2_asagi_cizgi)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+(H5_LEN/2))))

b2_dik_cizgi5 = APoint(A2_LEN+(5*B2_asagi_cizgi)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN))
b2_dik_alt5 = APoint(A2_LEN+(5*B2_asagi_cizgi)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN)))
b2_dik_cizgi_kisa5 = APoint((A2_LEN+(4.5*B2_asagi_cizgi)+A3_LEN),((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN))
b2_dik_alt_kisa5 = APoint(A2_LEN+(4.5*B2_asagi_cizgi)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+(H5_LEN/2))))

b2_dik_cizgi6 = APoint(A2_LEN+(6*B2_asagi_cizgi)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN))
b2_dik_alt6 = APoint(A2_LEN+(6*B2_asagi_cizgi)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN)))
b2_dik_cizgi_kisa6 = APoint((A2_LEN+(5.5*B2_asagi_cizgi)+A3_LEN),((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN))
b2_dik_alt_kisa6 = APoint(A2_LEN+(5.5*B2_asagi_cizgi)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+(H5_LEN/2))))

b2_dik_cizgi7 = APoint(A2_LEN+(7*B2_asagi_cizgi)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN))
b2_dik_alt7 = APoint(A2_LEN+(7*B2_asagi_cizgi)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN)))
b2_dik_cizgi_kisa7 = APoint((A2_LEN+(6.5*B2_asagi_cizgi)+A3_LEN),((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN))
b2_dik_alt_kisa7 = APoint(A2_LEN+(6.5*B2_asagi_cizgi)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+(H5_LEN/2))))

b2_dik_cizgi8 = APoint(A2_LEN+(8*B2_asagi_cizgi)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN))
b2_dik_alt8 = APoint(A2_LEN+(8*B2_asagi_cizgi)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN)))
b2_dik_cizgi_kisa8 = APoint((A2_LEN+(7.5*B2_asagi_cizgi)+A3_LEN),((H2_LEN+H3_LEN+H4_LEN+H5_LEN)-G_LEN))
b2_dik_alt_kisa8 = APoint(A2_LEN+(7.5*B2_asagi_cizgi)+A3_LEN,((H2_LEN+H3_LEN+H4_LEN+(H5_LEN/2))))
#//////////////////////////////////////////////////

#============ÇİZGİLER===========================================
B1 = acad.model.AddLine(a,b)
H2 = acad.model.AddLine(a,c)
A2 = acad.model.AddLine(c,d)
H3 = acad.model.AddLine(d,e)
H4 = acad.model.AddLine(za,f)
A3 = acad.model.AddLine(e,za)
H5 = acad.model.AddLine(f,g)
F_K= acad.model.AddLine(f,k)
K_K_15 = acad.model.AddLine(k,k_15)
K15_K1510 = acad.model.AddLine(k_15,k_15_10)
K1510_F10 = acad.model.AddLine(k_15_10,f_10)
YN_j = acad.model.AddLine(g_10,j)
B2 = acad.model.AddLine(g,h)
H2sag = acad.model.AddLine(b,m)
A1 = acad.model.AddLine(m,l)
P = acad.model.AddLine(h,l)
TB1= acad.model.AddLine(c,c_sol)
C2 = acad.model.AddLine(s,r)
C1 = acad.model.AddLine(b,s1)
C1X = acad.model.AddLine(o,s2)
C1XX = acad.model.AddLine(n,s3)
D2 = acad.model.AddLine(p,ü)
C2 = acad.model.AddLine(s2,s3)
D4 = acad.model.AddLine(s3,p)
D1 = acad.model.AddLine(s,t)
D5 = acad.model.AddLine(t,u)
T = acad.model.AddLine(ü,u)
TB2 = acad.model.AddLine(u,u_sag)
d_l = acad.model.AddLine(d,l)
#X3_X2= acad.model.AddLine(x2,x3)

#===============su havzaları====================================
#su1_su2 = acad.model.AddLine(su1,b2)
#su3_su4 = acad.model.AddLine(su3,b4)
#su5_su6 = acad.model.AddLine(su5,b6)
#su7_su8 = acad.model.AddLine(su7,b8)
#============B2 DİK CİZİK============================
B2_DİK_CİZGİ = acad.model.AddLine(b2_dik_cizgi,b2_dik_alt)
B2_DİK_CİZGİ2 = acad.model.AddLine(b2_dik_cizgi2,b2_dik_alt2)
B2_DİK_CİZGİ3 = acad.model.AddLine(b2_dik_cizgi3,b2_dik_alt3)
B2_DİK_CİZGİ4 = acad.model.AddLine(b2_dik_cizgi4,b2_dik_alt4)
B2_DİK_CİZGİ5 = acad.model.AddLine(b2_dik_cizgi5,b2_dik_alt5)
B2_DİK_CİZGİ6 = acad.model.AddLine(b2_dik_cizgi6,b2_dik_alt6)
B2_DİK_CİZGİ7 = acad.model.AddLine(b2_dik_cizgi7,b2_dik_alt7)
B2_DİK_CİZGİ8 = acad.model.AddLine(b2_dik_cizgi8,b2_dik_alt8)

B2_DİK_CİZGİ_KISA = acad.model.AddLine(b2_dik_cizgi_kisa,b2_dik_alt_kisa)
B2_DİK_CİZGİ_KISA2 = acad.model.AddLine(b2_dik_cizgi_kisa2,b2_dik_alt_kisa2)
B2_DİK_CİZGİ_KISA3 = acad.model.AddLine(b2_dik_cizgi_kisa3,b2_dik_alt_kisa3)
B2_DİK_CİZGİ_KISA4 = acad.model.AddLine(b2_dik_cizgi_kisa4,b2_dik_alt_kisa4)
B2_DİK_CİZGİ_KISA5 = acad.model.AddLine(b2_dik_cizgi_kisa5,b2_dik_alt_kisa5)
B2_DİK_CİZGİ_KISA6 = acad.model.AddLine(b2_dik_cizgi_kisa6,b2_dik_alt_kisa6)
B2_DİK_CİZGİ_KISA7 = acad.model.AddLine(b2_dik_cizgi_kisa7,b2_dik_alt_kisa7)
B2_DİK_CİZGİ_KISA8 = acad.model.AddLine(b2_dik_cizgi_kisa8,b2_dik_alt_kisa8)
#===================================================
"""
#============C_SOL CİZİK============================
C_SOL_CIZIK = acad.model.AddLine(c_sol_cizik,c_sol_cizik_alt)
C_SOL_CIZIK1 = acad.model.AddLine(c_sol_cizik1,c_sol_cizik_alt1)
C_SOL_CIZIK2 = acad.model.AddLine(c_sol_cizik2,c_sol_cizik_alt2)
C_SOL_CIZIK3 = acad.model.AddLine(c_sol_cizik3,c_sol_cizik_alt3)
C_SOL_CIZIK4 = acad.model.AddLine(c_sol_cizik4,c_sol_cizik_alt4)
C_SOL_CIZIK_SAG = acad.model.AddLine(c_sol_cizik_sag,c_sol_cizik_alt_sag)
C_SOL_CIZIK_SAG2 = acad.model.AddLine(c_sol_cizik_sag2,c_sol_cizik_alt_sag2)
C_SOL_CIZIK_SAG3 = acad.model.AddLine(c_sol_cizik_sag3,c_sol_cizik_alt_sag3)
C_SOL_CIZIK_SAG4 = acad.model.AddLine(c_sol_cizik_sag4,c_sol_cizik_alt_sag4)
#===================================================
#============U_SOL CİZİK============================
U_SAG_CIZIK = acad.model.AddLine(u_sag_cizik,u_sag_cizik_alt)
U_SAG_CIZIK2 = acad.model.AddLine(u_sag_cizik2,u_sag_cizik_alt2)
U_SAG_CIZIK3 = acad.model.AddLine(u_sag_cizik3,u_sag_cizik_alt3)
U_SAG_CIZIK4 = acad.model.AddLine(u_sag_cizik4,u_sag_cizik_alt4)
U_SAG_CIZIK_SOL = acad.model.AddLine(u_sag_cizik_sol,u_sag_cizik_alt_sol)
U_SAG_CIZIK_SOL2 = acad.model.AddLine(u_sag_cizik_sol2,u_sag_cizik_alt_sol2)
U_SAG_CIZIK_SOL3 = acad.model.AddLine(u_sag_cizik_sol3,u_sag_cizik_alt_sol3)
U_SAG_CIZIK_SOL4 = acad.model.AddLine(u_sag_cizik_sol4,u_sag_cizik_alt_sol4)
#===================================================
"""
# AutoCAD çizimini kaydet (Ctrl+S gibi)
#acad.doc.SendCommand('SAVE\n')

# Kaydetme işlemi tamamlandıktan sonra kullanıcıya bilgi ver
acad.prompt("Çizim kaydedildi.\n")

acad.ActiveDocument.Regen(1)