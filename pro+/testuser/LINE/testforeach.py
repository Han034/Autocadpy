from pyautocad import Autocad, APoint
import math

# AutoCAD ile bağlantı kur
acad = Autocad(create_if_not_exists=True)

# Başlangıç ve bitiş noktalarını tanımla (örneğin)
n1 = APoint(0, 0)
n20 = APoint(200, 0)

# Çizgi uzunluklarını tanımla
length1 = 40
length2 = 10

# İki nokta arasındaki mesafeyi hesapla
distance = n20.x - n1.x

# En az 4 çizgi olacak şekilde gerekli tekrar sayısını hesapla
total_length = length1 + length2
min_repeats = 4
required_repeats = max(min_repeats, math.ceil(distance / (total_length * 2)))

# Çizim döngüsü
current_x = n1.x
for i in range(required_repeats):
    # İlk çizgiyi çiz (alttan üste)
    start_point = APoint(current_x, n1.y)
    end_point = APoint(current_x, n1.y + length1)
    acad.model.AddLine(start_point, end_point)
    
    current_x += total_length / 2  # Bu adımda yarı mesafe kaydır
    
    # İkinci çizgiyi çiz (üstten alta, sarkıt gibi)
    start_point = APoint(current_x, n1.y + length1)
    end_point = APoint(current_x, n1.y + length1 - length2)
    acad.model.AddLine(start_point, end_point)
    
    current_x += total_length / 2  # Bu adımda kalan yarı mesafe kaydır

print("Çizim tamamlandı.")
