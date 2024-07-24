from pyautocad import Autocad, APoint

# AutoCAD ile bağlantı kur
acad = Autocad(create_if_not_exists=True)

# İki nokta tanımlayın
point1 = APoint(0, 0)  # İlk nokta koordinatları
point2 = APoint(10, 5)  # İkinci nokta koordinatları

# Boyut çizgisi oluşturun
acad.model.AddDimAligned(point1, point2, APoint((point1.x + point2.x) / 2, (point1.y + point2.y) / 2))
