import win32com.client
import pythoncom
from math import pi

acad = win32com.client.Dispatch("AutoCAD.Application")
acadModel = acad.ActiveDocument.ModelSpace

def aaPoint(x,y,z= 0):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8,(x,y,z))
def aaDouble(xyz):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8,(xyz))
def variants(object):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, (object))

out_loop = []
#sq = acadModel.AddPolyline(aaDouble([0,0,0,100,0,0,100,100,0,0,100,0,0,0,0]))
arc = acadModel.AddCIRCLE(aaPoint(0, 50, 0), 50)
#arc2 = acadModel.AddArc(aaPoint(0, 50, 0), 50, 270*pi/180, 90*pi/180)


#out_loop.append(sq)
out_loop.append(arc)
#out_loop.append(arc2)

outer = variants(out_loop)

hatch = acadModel.AddHatch(0, "ANSI31", True)

hatch.AppendOuterLoop(outer)