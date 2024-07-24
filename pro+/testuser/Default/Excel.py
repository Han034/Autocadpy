#VİDEO 16 İZLE
import comtypes.client
from pyautocad import Autocad,APoint

try:
    excelApp = comtypes.client.GetActiveObject("Excel.Application")
except:
    excelApp = comtypes.client.CreateObject("Excel.Application")

rutaArchiveExcel = "Masaüstü/cizim.xlsx"
excelWorkbook = excelApp.Workbooks.open(rutaArchiveExcel)
excelSheet = excelWorkbook.Sheets("Points")

coordXInicio = []
coordYInicio = []
coordXFin = []
coordYFin = []

cellTipo = ""
j=0
while cellTipo != None:
    coordXInicio.append(excelSheet.Cells(2+j,1).Value())
    coordYInicio.append(excelSheet.Cells(2 + j, 2).Value())
    coordXFin.append(excelSheet.Cells(2 + j, 3).Value())
    coordYFin.append(excelSheet.Cells(2 + j, 4).Value())
    j+=1
    cellTipo = excelSheet.Cells(2+j,1).Value()

acad = Autocad()
for i in range(0,len(coordXInicio)):
    acad.model.AddLine(APoint(coordXInicio[i],coordYInicio[i],coordXFin[i],coordYFin[i]))

acad.app.ZoomExtents()










