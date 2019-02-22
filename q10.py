#10) Perform a spatial join between the census tracts feature class and the general offense feature class.import arcpytarget_features = r"D:\610\Exercise3\Exercise 3.gdb\Tracts"
join_features = r"D:\610\Exercise3\Exercise 3.gdb\General_Offense"
out_feature_class = r"D:\610\Exercise3\Exercise 3.gdb\tracts_Offense"

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class)

print("done")