from pyautocad import Autocad, APoint

# AutoCAD ile bağlantı kur
acad = Autocad(create_if_not_exists=True)
acad.prompt("PyAutoCAD ile AutoCAD'e bağlanıldı.\n")
print(acad.doc.Name)

# Dairenin merkez noktasını ve yarıçapını tanımla
n31 = APoint(0, 0)  # n31'in koordinatlarını buraya girin
radius = 10

# Daireyi çiz
N31C = acad.model.AddCircle(n31, radius)

# Çizgi kalınlığını ayarla (örneğin, 0.5 mm)
N31C.Lineweight = 30  # 20, Lineweight değerinin 0.5 mm olduğunu gösterir

print("Dairenin çizgi kalınlığı artırıldı.")
