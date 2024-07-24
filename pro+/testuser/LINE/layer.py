import pyautocad
from pyautocad import Autocad, APoint

acad = pyautocad.Autocad(16)
print(acad.doc.name)

acad.doc.Layers.Add("Layer4")
T=acad.model.AddText("LARGE TEXT", APoint(0, 0), 100)
T.Layer="Layer4"