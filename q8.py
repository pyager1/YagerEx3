#8) Return the count of records in the CallsforService feature class.import arcpy
 
arcpy.env.workspace = r"D:\610\Exercise3\Exercise 3.gdb"

lyrfile = "CallsforService"
result = arcpy.GetCount_management(lyrfile)
print('{} has {} records'.format(lyrfile, result[0]))