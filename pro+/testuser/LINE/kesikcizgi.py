from pyautocad import Autocad, APoint

# AutoCAD ile bağlantı kur
acad = Autocad(create_if_not_exists=True)
#acad.prompt("PyAutoCAD ile AutoCAD'e bağlanıldı.\n")
print(acad.doc.Name)

# Çizgi noktalarını tanımla
start_point = APoint(0, 0)
end_point = APoint(100, 100)

# Çizgi çiz
line = acad.model.AddLine(start_point, end_point)

# Kesik çizgi stilini ayarla (örneğin, "DASHED" çizgi stili)
line.Linetype = "ACAD_ISO02W100"

# Eğer kesik çizgi stili yüklenmemişse, önce yükleyin
#if not acad.doc.Linetypes.Item("ACAD_ISO02W100").HasExtensionDictionary:
#    acad.doc.Linetypes.Load("ACAD_ISO02W100", "acad.lin")

#print("Kesik çizgi çizildi.")