import arcpy

#Setting workspace
arcpy.env.workspace = r"C:\Users\User\Documents\JonathanLeung_Winter2025\HK_DTM_5m_Full"
arcpy.env.overwriteOutput = True

#Contour Tool
HK_DTM = "Whole_HK_DTM_5m.asc"
outContour = r"C:\Users\User\Documents\JonathanLeung_Winter2025\HK_DTM_5m_Full\HK Processing\HK Processing.gdb\Contour_Whole_HKDTM"
arcpy.sa.Contour(HK_DTM,outContour,contour_interval=30,base_contour=0, z_factor=1,contour_type='CONTOUR')