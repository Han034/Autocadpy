import win32com.client
import pythoncom

# AutoCAD uygulamasını başlat
acad = win32com.client.Dispatch("AutoCAD.Application")
acadModel = acad.ActiveDocument.ModelSpace

# Yardımcı fonksiyonlar
def aaPoint(x, y, z=0):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (x, y, z))

def aaDouble(xyz):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (xyz))

def aavariants(object):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, (object))

# Kare için köşe noktalarını belirleyin
p1 = aaPoint(0, 0)
p2 = aaPoint(0, 10)
p3 = aaPoint(10, 10)
p4 = aaPoint(10, 0)

# Kareyi oluşturun
acadModel.AddLine(p1, p2)
acadModel.AddLine(p2, p3)
acadModel.AddLine(p3, p4)
acadModel.AddLine(p4, p1)

# Solid çizim
pts = [p1, p2, p3, p4, p1]
acadModel.AddSolid(pts)

# Hatch oluşturun (burada solid ile aynı noktaları kullanacağız)
hatch = acadModel.AddHatch(1, True)
hatch.AppendOuterLoop(aavariants([acadModel.AddPolyline(pts)]))
hatch.Evaluate()
