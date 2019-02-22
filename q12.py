import arcpy
import os
import csv

######## 

featureClass = r"D:\610\Exercise3\Exercise 3.gdb\General_Offense"
fieldNames = ['locationTranslation', 'OffenseCustom']
cursorFields = ";".join(fieldNames )

filterStatement = "OffenseCustom= 'BURGLARY FORCE' and locationTranslation='Residence/Home'"
crimeCount = 0

with open('burglariesInResidenceHome.csv', 'w') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	filewriter.writerow(fieldNames)
	with arcpy.da.SearchCursor(featureClass, fieldNames, filterStatement) as cursor:
		for row in cursor:
			crimeCount += 1
			filewriter.writerow(row)

print (" There are " + str(crimeCount) + " burglaries with force in in residences" )