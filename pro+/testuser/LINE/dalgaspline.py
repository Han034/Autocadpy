from pyautocad import Autocad, APoint

# AutoCAD'e bağlan
acad = Autocad(create_if_not_exists=True)
acad.prompt("AutoCAD'e bağlandım\n")

# Başlangıç ve bitiş noktaları
start_point = APoint(0, 1000)  # Başlangıç noktası (x, y)
end_point = APoint(0, 0)       # Bitiş noktası (x, y)

# Dalga parametreleri
wave_amplitude = 50  # Dalga genliği
wave_length = 300    # Dalga boyu

# Dalga noktalarını hesapla
control_points = [
    start_point,
    APoint(start_point.x - wave_amplitude, start_point.y - wave_length / 3),
    APoint(start_point.x + wave_amplitude, start_point.y - 2 * wave_length / 3),
    end_point
]

# AutoCAD'de dalga çizgilerini çiz
spline = acad.model.AddSpline(control_points)

# Çizim tamamlandıktan sonra kullanıcıya bilgi ver
acad.prompt("Dalga çizgisi çizildi.\n")
