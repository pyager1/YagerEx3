#9) Create a feature class (you may re-use the geodatabase from Question 5). Add a field to your feature class. Then add a domain to the just created field. Finally, add at least 5 values to your domain. (*Your domain may be of any type)

import arcpy

arcpy.env.workspace = r"D:\610\Exercise3\Question5.gdb"
arcpy.env.overwriteOutput = True





# Set local variables
out_path = r"D:\610\Exercise3\Question5.gdb"
out_name = "Nuts"
geometry_type = "POLYGON"



# Execute CreateFeatureclass
arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type)

print ("done")

fc = "Nuts"
fieldName1 = "Types"


arcpy.AddField_management(fc, fieldName1, "TEXT")

print("done2")

# Name: MakeDomain.py
# Description: Create an attribute domain to constrain pipe material values
 

# Set local parameters
domName = "NutTypes"
inField = fieldName1
inFeatures = fc

# Process: Create the coded value domain
arcpy.CreateDomain_management(out_path, domName, "All kinds of nuts", 
                              "TEXT", "CODED")
    
# Store all the domain values in a dictionary with the domain code as the "key" 
# and the domain description as the "value" (domDict[code])
domDict = {"C":"Cashew", "P": "Pistachio", "A": "Almond", 
           "B": "Brazil Nuts", "W": "Walnuts"}

# Process: Add valid material types to the domain
# use a for loop to cycle through all the domain codes in the dictionary
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(out_path, domName, code, domDict[code])

print("done3") 