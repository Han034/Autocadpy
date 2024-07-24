from pyautocad import Autocad, APoint
import math

# AutoCAD'e bağlan
acad = Autocad(create_if_not_exists=True)
acad.prompt("AutoCAD'e bağlandım\n")

# Üçgenin köşe noktaları
A = APoint(0, 0)
B = APoint(100, 0)
C = APoint(0, 510)

# Dik kenar üzerindeki nokta
y0 = 200
a = APoint(0, y0)

# Hipotenüsün denklemi: y = -5.1x + 510
hipotenus_slope = -5.1
hipotenus_intercept = 510

# Çizgi denklemi: y = -0.03x + y0
# Açıyı buraya yazacağız
line_slope = 0
line_intercept = y0

# Kesişim noktası hesaplaması
x_intercept = (hipotenus_intercept - line_intercept) / (line_slope - hipotenus_slope)
y_intercept = line_slope * x_intercept + line_intercept

# Kesişim noktası hipotenüs üzerinde olmalı
b = APoint(x_intercept, y_intercept)

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
