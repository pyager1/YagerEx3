import arcpy

#variables
currentworkspace = r'D:\610\Exercise3\Question5.gdb'
geometryType = 'POLYGON'
spatialRef = arcpy.SpatialReference(26949)

#Feature classes to create
featureList = ["CapitalCities", "Landmarks", "HistoricPlaces", "StateNames", "Nationalities",
"Rivers"]

#set default workspace and allow overwrite
arcpy.env.workspace = currentworkspace
arcpy.env.overwriteOutput = True

#this is a function to create a new feature class

def creatFeatureClass(inFeatureClassName):
    arcpy.CreateFeatureclass_management(currentworkspace
                                        ,inFeatureClassName
                                        ,geometryType
                                        ,''
                                        ,'DISABLED'
                                        ,'DISABLED'
                                        ,spatialRef)
    print('created feature class called ' + inFeatureClassName)
#End of function

#lets run the function or call the feature 

for fc in featureList:
    creatFeatureClass(fc)


