#Using the CallsforService feature class that you’ve been given, add a field called ‘Crime_Explanation’ with the data type Text/String. Then, if the value of field ‘CFSType’ is Burglary Call, write ‘This is a burglary’ into the field that you just added

import arcpy

arcpy.env.workspace = r"D:\610\Exercise3\Exercise 3.gdb"

fc = "CallsforService"
fieldName1 = "Crime_Explanation"


arcpy.AddField_management(fc, fieldName1, "TEXT")






class_field = ['CFSType','Crime_Explanation']


# Create update cursor for feature class 
with arcpy.da.UpdateCursor(fc, class_field) as cursor:
      for row in cursor:
        if row[0] == 'Burglary Call':
           row[1] = 'This is a Burglary'
 
           cursor.updateRow(row)
            
print ("done")