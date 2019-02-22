#Write Python code that selects a subset of the records from a given feature class and writes those features to a different feature class. You may choose which feature class that your code uses.
import arcpy

arcpy.env.workspace = r"D:\610\Exercise3\Exercise 3.gdb"

# Set local variables
inFeatures = "CallsforService"
outLocation = r"D:\610\Exercise3\Exercise 3.gdb"
outFeatureClass = "ShopliftingCalls"
delimitedField = arcpy.AddFieldDelimiters(arcpy.env.workspace, "CFSType")
expression = delimitedField + " = 'Shoplifting Call'"
 
# Execute FeatureClassToFeatureClass
arcpy.FeatureClassToFeatureClass_conversion(inFeatures, outLocation, 
                                            outFeatureClass, expression)

print ("done")