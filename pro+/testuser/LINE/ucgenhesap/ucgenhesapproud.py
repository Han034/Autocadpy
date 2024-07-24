from pyautocad import Autocad, APoint
import math

# AutoCAD'e bağlan
acad = Autocad(create_if_not_exists=True)
acad.prompt("AutoCAD'e bağlandım\n")

# Üçgenin köşe noktaları
A = APoint(270, 100)  # A noktası (270, 100)
B = APoint(370, 100)  # B noktası (370, 100)
C = APoint(270, 510)  # C noktası (270, 510)

# Dik kenar üzerindeki nokta
y0 = 200
a = APoint(270, y0)  # a noktası (270, 450)

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

# AutoCAD'e üçgenin kenarlarını çiz
acad.model.AddLine(A, C)
acad.model.AddLine(A, B)
acad.model.AddLine(B, C)

# AutoCAD'e eğimli çizgiyi çiz
acad.model.AddLine(a, b)

# Hesaplama sonuçlarını yazdır
print(f"Kesişim noktası: ({b.x}, {b.y})")
print(f"Çizginin uzunluğu: {line_length:.2f}")

# AutoCAD'de çizim sonuçlarını belirt
acad.prompt(f"Kesişim noktası: ({b.x}, {b.y})\n")
acad.prompt(f"Çizginin uzunluğu: {line_length:.2f}\n")
