import arcpy
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *
from sys import argv

#Global Variables
Slope = arcpy.GetParameterAsText(0)
Hillract_road_prj = arcpy.GetParameterAsText(1)
hilltract_fault = arcpy.GetParameterAsText(2)
NN_prcpt_prj = arcpy.GetParameterAsText(3)
Risk_Zones_n = arcpy.GetParameterAsText(4)



#For inline variable substitution, parameters passed as a String are evaluated using locals(), globals() and isinstance(). To override, substitute values directly.
def Model4(Slope, Hillract_road_prj, hilltract_fault, NN_prcpt_prj, Risk_Zones_n):  # Model4

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = True

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("3D")
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("ImageAnalyst")
    
    #Local Variables
    Eu_D_Road = "C:\\Users\\SilverSlim\\Desktop\\Python_project\\output\\Eu_D_Road"
    Euclidean_Distance = Eu_D_Road
    Output_direction_raster = ""
    Out_back_direction_raster = ""
    
    EuD_Rd_rclss = "C:\\Users\\SilverSlim\\Desktop\\Python_project\\output\\EuD_Rd_rclss"
    Reclassify_3_ = EuD_Rd_rclss
    
    slope_rclss = "C:\\Users\\SilverSlim\\Desktop\\Python_project\\output\\slope_rclss"
    Reclassify_2_ = slope_rclss
    
    Prep_Rclss = "C:\\Users\\SilverSlim\\Desktop\\Python_project\\output\\Prep_Rclss"
    Reclassify = Prep_Rclss
    
    Eu_D_Flt = "C:\\Users\\SilverSlim\\Desktop\\Python_project\\output\\eu_d_flt"
    Euclidean_Distance_2_ = Eu_D_Flt
    Output_direction_raster_2_ = ""
    Out_back_direction_raster_2_ = ""
    
    EuD_Flt_rclss = "C:\\Users\\SilverSlim\\Desktop\\Python_project\\output\\EuD_Flt_rclss"
    Reclassify_4_ = EuD_Flt_rclss
    
    W_sum_landS = "C:\\Users\\SilverSlim\\Downloads\\sum\\Wighetd_sum\\W_sum_landS1"
    Weighted_Sum = "C:\\Users\\SilverSlim\\Downloads\\sum\\Weightd_Sum1"
    
    
    


    # Process: Euclidean Distance (Euclidean Distance) (sa)
    
    with arcpy.EnvManager(extent="390344.333343628 2420781.42722389 461306.538535633 2626066.45147343 PROJCS[\"WGS_1984_UTM_Zone_46N\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"False_Easting\",500000.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",93.0],PARAMETER[\"Scale_Factor\",0.9996],PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0]]", outputCoordinateSystem="PROJCS[\"WGS_1984_UTM_Zone_46N\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"False_Easting\",500000.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",93.0],PARAMETER[\"Scale_Factor\",0.9996],PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0]]"):
        Eu_D_Road = arcpy.sa.EucDistance(Hillract_road_prj, None, "30", Output_direction_raster, "PLANAR", "", Out_back_direction_raster)
        Eu_D_Road.save(Euclidean_Distance)


    # Process: Reclassify (3) (Reclassify) (sa)
    
    EuD_Rd_rclss = arcpy.sa.Reclassify(Eu_D_Road, "VALUE", "0 600 4;600.010000 1200 3;1200.010000 1800 2;1800.010000 57154 1", "DATA")
    EuD_Rd_rclss.save(Reclassify_3_)


    # Process: Reclassify (2) (Reclassify) (sa)
    
    slope_rclss = arcpy.sa.Reclassify(Slope, "VALUE", "0 3.685185 1;3.685185 9.476191 2;9.476191 15 3;15.001000 23.427249 4;23.427249 67.123016 5", "DATA")
    slope_rclss.save(Reclassify_2_)


    # Process: Reclassify (Reclassify) (sa)
    
    Prep_Rclss = arcpy.sa.Reclassify(NN_prcpt_prj, "VALUE", "9.033007 10.159039 1;10.159039 10.901681 2;10.901681 11.827499 3;11.827499 13.085588 4;13.085588 14.847765 5", "DATA")
    Prep_Rclss.save(Reclassify)


    # Process: Euclidean Distance (2) (Euclidean Distance) (sa)
    
    with arcpy.EnvManager(extent="390344.333343628 2420781.42722389 461306.538535633 2626066.45147343 PROJCS[\"WGS_1984_UTM_Zone_46N\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"False_Easting\",500000.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",93.0],PARAMETER[\"Scale_Factor\",0.9996],PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0]]", outputCoordinateSystem="PROJCS[\"WGS_1984_UTM_Zone_46N\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"False_Easting\",500000.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",93.0],PARAMETER[\"Scale_Factor\",0.9996],PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0]]"):
        Eu_D_Flt = arcpy.sa.EucDistance(hilltract_fault, None, "30", Output_direction_raster_2_, "PLANAR", "", Out_back_direction_raster_2_)
        Eu_D_Flt.save(Euclidean_Distance_2_)


    # Process: Reclassify (4) (Reclassify) (sa)
    
    with arcpy.EnvManager(extent="390344.333343628 2420781.42722389 461306.538535633 2626066.45147343 PROJCS[\"WGS_1984_UTM_Zone_46N\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"False_Easting\",500000.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",93.0],PARAMETER[\"Scale_Factor\",0.9996],PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0]]", outputCoordinateSystem="PROJCS[\"WGS_1984_UTM_Zone_46N\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"False_Easting\",500000.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",93.0],PARAMETER[\"Scale_Factor\",0.9996],PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0]]"):
        EuD_Flt_rclss = arcpy.sa.Reclassify(Eu_D_Flt, "VALUE", "0 5084.519485 5;5084.519485 11076.988879 4;11076.988879 18522.178125 3;18522.178125 27964.857169 2;27964.857169 46305.445312 1", "DATA")
        EuD_Flt_rclss.save(Reclassify_4_)


    # Process: Weighted Sum (Weighted Sum) (sa)
    
    with arcpy.EnvManager(extent="390344.333343628 2420781.42722389 461306.538535633 2626066.45147343 PROJCS[\"WGS_1984_UTM_Zone_46N\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"False_Easting\",500000.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",93.0],PARAMETER[\"Scale_Factor\",0.9996],PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0]]", outputCoordinateSystem="PROJCS[\"WGS_1984_UTM_Zone_46N\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"False_Easting\",500000.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",93.0],PARAMETER[\"Scale_Factor\",0.9996],PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0]]"):
        W_sum_landS = arcpy.sa.WeightedSum(WSTable([[EuD_Rd_rclss, 'VALUE', 10], [slope_rclss, 'VALUE', 40], [Prep_Rclss, 'VALUE', 40], [EuD_Flt_rclss, 'VALUE', 10]]))
        W_sum_landS.save(Weighted_Sum)


    # Process: Rescale by Function (Rescale by Function) (sa)
    Rescale_by_Function = Risk_Zones_n
    with arcpy.EnvManager(compression="NONE", extent="390344.333343628 2420781.42722389 461306.538535633 2626066.45147343 PROJCS[\"WGS_1984_UTM_Zone_46N\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"False_Easting\",500000.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",93.0],PARAMETER[\"Scale_Factor\",0.9996],PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0]]", outputCoordinateSystem="PROJCS[\"WGS_1984_UTM_Zone_46N\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"False_Easting\",500000.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",93.0],PARAMETER[\"Scale_Factor\",0.9996],PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0]]", 
                          pyramid="NONE"):
        Risk_Zones_n = arcpy.sa.RescaleByFunction(W_sum_landS, [["MSSMALL", 110, "", 490, "", 1, 1, ""]], 10, 1)
        Risk_Zones_n.save(Rescale_by_Function)


if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace="C:\\Users\\SilverSlim\\Documents\\ArcGIS\\Projects\\landslide_python\\landslide_python.gdb", workspace="C:\\Users\\SilverSlim\\Documents\\ArcGIS\\Projects\\landslide_python\\landslide_python.gdb"):
        Model4(*argv[1:])
