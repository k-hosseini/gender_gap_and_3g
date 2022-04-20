# Packages
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import datetime as dt
import os
import imageio

# test
def temp(x):
    return(x)


# # Paths
# # addresses
# Political_divistions      = r"C:\Users\khoss\Desktop\Files\Economics Data\Shapefiles\01.Political Divisions of Iran\1.Data"
# Iran_shapefiles_paths={}
# Iran_shapefiles_paths['Country']          = Political_divistions+r"\1.Country Boundary\Country Boundary.shp"
# Iran_shapefiles_paths['Provinces']        = Political_divistions+r"\2.Provinces Boundary\Provinces Boundary.shp"
# Iran_shapefiles_paths['Counties']         = Political_divistions+r"\3.Counties Boundary\Counties Boundary.shp"
# Iran_shapefiles_paths['Cities']           = Political_divistions+r"\6.Cities Boundary & Point\City (precise)\Cities.shp"




# Mylinkov = r"C:\Users\khoss\Desktop\Files\Economics Data\3G\mylnikov\22-12-2019"
# cells_path = Mylinkov+r'\Iran_V0.dta'
# coverage_maps_path = Mylinkov+r"\Coverage_maps"

# mylnikov_location_csv = Mylinkov+r"\ArcGIS_files\coverage_csv_by_quarter"
# Cities_name_path = Mylinkov+"\\Name_Maching\\Cities.xlsx"








# # Loading Iran shapefiles
# def load_Iran_shape_files(*,Iran_shapefiles_paths ,Cities_name_path ):
#     Iran_shapefiles = {name:gpd.read_file(path).to_crs("EPSG:2058") for name, path in Iran_shapefiles_paths.items()}
#     Iran_shapefiles["Cities"]["FID"] = np.arange(Iran_shapefiles["Cities"].shape[0])
    
#     Cities_name = pd.read_excel(Cities_name_path)
#     Iran_shapefiles["Cities"] = Iran_shapefiles["Cities"].rename(columns ={'CITY_NAME':'CITY_NAME_old', 'CITY_ENG':'CITY_ENG_old' , 'OSTAN_NAME': 'OSTAN_NAME_old'})
#     Iran_shapefiles["Cities"] = Iran_shapefiles["Cities"].merge(Cities_name,on="FID")
#     return Iran_shapefiles




# # Read Mylinkove and initial preparation 
# def read_mylinkov(cells_path):

#     cells = pd.read_stata(cells_path)
    
#     cells["date_created"]   = cells["created"].apply(lambda x:dt.datetime.fromtimestamp(x))
#     cells["updated_date"]   = cells["updated"].apply(lambda x:dt.datetime.fromtimestamp(x))
#     cells = cells.loc[(cells["radio_type"] =="UMTS") & (cells["date_created"].dt.year >= 2013)] #before 2013, there wer no 3g cell
#     UMTS = cells
#     return UMTS.sort_values(by=['date_created'])




# # Return coverage map using Cities shape file and Mylinkov Dataset
# def coverage_map(*,UMTS_df, Cities , radious=500):
#     UMTS_gdf = gpd.GeoDataFrame(UMTS_df, geometry = gpd.points_from_xy(UMTS_df.lon,UMTS_df.lat) ,  crs='epsg:4326')
#     UMTS_gdf = UMTS_gdf.to_crs("EPSG:2058")
#     # Buffer around cells' location
#     UMTS_buffered_gdf = UMTS_gdf
#     UMTS_buffered_gdf.geometry = UMTS_gdf.geometry.buffer(radious, 6)

#     # Dissolve
#     UMTS_dissolved_gdf = UMTS_buffered_gdf

#     UMTS_dissolved_gdf['common_column'] =1
#     UMTS_dissolved_gdf = UMTS_dissolved_gdf.dissolve(by = ['common_column'])

#     UMTS_Intersected_gdf = gpd.overlay(UMTS_dissolved_gdf,Cities, how = 'intersection')
#     coverage_map = UMTS_Intersected_gdf
#     return coverage_map


# # Return covered area and coverage map at the same time
# def covered_area(*,UMTS_df,Cities,radious=500):
#     coverage_map_gdf = coverage_map(UMTS_df = UMTS_df, Cities = Cities ,radious=radious)
#     covered_area_df =  pd.DataFrame(data ={'covered_area': coverage_map_gdf["geometry"].area/1e6 ,
#             'CITY_ENG'  :coverage_map_gdf["CITY_ENG"],
#             "CITY_NAME" :coverage_map_gdf["CITY_NAME"],
#             'OSTAN_NAME':coverage_map_gdf["OSTAN_NAME"] })
    
#     return (coverage_map_gdf, covered_area_df)


# # Calculate area of citie using Cities shape file
# def city_area(Cities ):
#     return pd.DataFrame(data = {"city_area":Cities["geometry"].area/1e6,
#                                      "CITY_ENG": Cities["CITY_ENG"],
#                                      "CITY_NAME": Cities["CITY_NAME"],
#                                      "OSTAN_NAME": Cities["OSTAN_NAME"]})

# # Returns coverage maps and coverage rates.
# def coverage_rate(* , UMTS_df,Cities,radious=500):
#     city_area_df = city_area(Cities)
#     coverage_map_gdf , covered_area_df = covered_area(UMTS_df=UMTS_df,Cities=Cities,radious=radious)
#     coverage_rate_df = pd.merge(covered_area_df , city_area_df, on=["CITY_ENG", "CITY_NAME" ,"OSTAN_NAME"] , how ="outer")    
#     coverage_rate_df["coverage_rate"] = coverage_rate_df["covered_area"]/ coverage_rate_df["city_area"] 
#     return (coverage_map_gdf , coverage_rate_df)





# # Return coverage map and rate for each quarter in the period that UMTS_df is covering
# def cov_map_rate_period(* , UMTS_df , Cities , radious=500 , frequesncy = 'Q'):
#     # Coverage map for each date
#     dates = pd.period_range(str(UMTS_df['date_created'].min()), str(UMTS_df['date_created'].max()), freq=frequesncy)
#     dates_len = len(dates)
    
    
#     coverage_rates_list=[]
#     coverage_maps_period_dict ={}
    
#     # this must be changed
#     for period in dates:
#         coverage_map_period , coverage_rate_period = coverage_rate(UMTS_df = UMTS_df.loc[UMTS_df['date_created'] < str(period)],Cities = Cities,radious=radious)    
#         # coverage_map_period:
#         coverage_maps_period_dict[str(period)] = coverage_map_period
        
#         # coverage_rate_period
#         coverage_rate_period['date'] = period
#         coverage_rates_list.append(coverage_rate_period)
    
#     coverage_rate_df = pd.concat(coverage_rates_list)
    
    
#     return (coverage_maps_period_dict , coverage_rate_df)



# # Export coverage map png, gif and shp
# def export_maps(* , coverage_maps_period_dict , coverage_maps_path =coverage_maps_path, Country ):  
#     images=[]
#     for period,cov_map in coverage_maps_period_dict.items():
        
#         # export .shp
#         export_shape_file = coverage_maps_period_dict[period][["CITY_NAME","CITY_ENG", "OSTAN_NAME", "geometry"]]
#         try:
#             # Create a new directory because it does not exist 
#             if not os.path.exists(coverage_maps_path+"\\shape_files"):
#                 os.makedirs(coverage_maps_path+"\\shape_files")
#                 print("The new shape_files directory is created!")
#             export_shape_file.to_file(coverage_maps_path+"\\shape_files\\UMTS_"+str(period)+"_500.shp")
#         except:
#             print("coverage map is empty at period:",period)
            
#         # Export .png and .gif
#         fig, ax = plt.subplots(figsize = (20,16))
#         Country.plot(ax=ax,color='grey')
#         cov_map.plot(ax=ax,color='blue')
#         ax.set_axis_off()
#         fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
#         fig.savefig(coverage_maps_path+"\\UMTS_"+str(period)+"_500.png")
#         plt.close(fig)

#         # Animation:
#         images.append(imageio.imread(coverage_maps_path+"\\UMTS_"+str(period)+"_500.png"))
#     imageio.mimsave(coverage_maps_path+"\\UMTS_animation_500.gif", images)


