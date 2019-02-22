

######### CREATE GEODATABASE #########
import arcpy
arcpy.env.overwriteOutput = True


# Set local variables
out_folder_path = r"D:\610\Exercise3" 
out_name = "Question13.gdb"

# Execute CreateFileGDB
arcpy.CreateFileGDB_management(out_folder_path, out_name)



######### IMPORT SHAPEFILES TO GEODATABASE #########

arcpy.env.workspace = r"D:\610\Exercise3\question13\Question 13"


# Set local variables
in_features = ['tl_2018_us_county.shp', 'tl_2018_04_tract.shp']
out_location = r"D:\610\Exercise3\Question13.gdb"

# Execute FeatureClassToGeodatabase
arcpy.FeatureClassToGeodatabase_conversion(in_features, out_location)



######### CREATE NEW LAYER FOR MARICOPA COUNTY #########

# Import system modules
import arcpy
from arcpy import env

# Set workspace
env.workspace = r"D:\610\Exercise3\Question13.gdb"

# Create layer for Maricopa County
inFeatures = "tl_2018_us_county"
outLocation = r"D:\610\Exercise3\Question13.gdb"
outFeatureClass = "MaricopaCounty"
delimitedField = arcpy.AddFieldDelimiters(arcpy.env.workspace, "NAME")
expression = delimitedField + " = 'Maricopa'"
 
# Execute FeatureClassToFeatureClass
arcpy.FeatureClassToFeatureClass_conversion(inFeatures, outLocation, 
                                            outFeatureClass, expression)

print ("Maricopa county created")




######### CLIP TRACTS TO MARICOPA COUNTY #########

env.workspace = r"D:\610\Exercise3\Question13.gdb"

# Set local variables
in_features = "tl_2018_04_tract"
clip_features = "MaricopaCounty"
out_feature_class = r"D:\610\Exercise3\Question13.gdb\tractsMaricopa"
xy_tolerance = ""

# Execute Clip
arcpy.Clip_analysis(in_features, clip_features, out_feature_class, xy_tolerance)

print("all Done")