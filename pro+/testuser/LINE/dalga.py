from pyautocad import Autocad, APoint
import math

# AutoCAD'e bağlan
acad = Autocad(create_if_not_exists=True)
acad.prompt("AutoCAD'e bağlandım\n")

# Başlangıç ve bitiş noktaları
start_point = APoint(0, 1000)  # Başlangıç noktası (x, y)
end_point = APoint(0, 0)      # Bitiş noktası (x, y)

# Dalga parametreleri
wave_amplitude = 50  # Dalga genliği
wave_length = 100    # Dalga boyu
number_of_waves = 10 # Dalga sayısı

# Dalga noktalarını hesapla ve çiz
current_x = start_point.x
current_y = start_point.y
wave_points = [APoint(current_x, current_y)]

for i in range(1, number_of_waves + 1):
    current_y -= wave_length / 2
    if i % 2 == 1:  # Sola doğru kıvrım
        current_x -= wave_amplitude
    else:  # Sağa doğru kıvrım
        current_x += wave_amplitude
    wave_points.append(APoint(current_x, current_y))
    
    current_y -= wave_length / 2
    wave_points.append(APoint(current_x, current_y))

# AutoCAD'de dalga çizgilerini çiz
for i in range(len(wave_points) - 1):
    acad.model.AddLine(wave_points[i], wave_points[i + 1])

# Çizim tamamlandıktan sonra kullanıcıya bilgi ver
acad.prompt("Dalga çizgisi çizildi.\n")
