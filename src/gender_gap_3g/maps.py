# Packages
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import datetime as dt
import os
import imageio


def load_Iran_shape_files(*,Iran_shapefiles_paths ,Cities_name_path ):
    Iran_shapefiles = {name:gpd.read_file(path).to_crs("EPSG:2058") for name, path in Iran_shapefiles_paths.items()}
    Iran_shapefiles["Cities"]["FID"] = np.arange(Iran_shapefiles["Cities"].shape[0])
    
    Cities_name = pd.read_excel(Cities_name_path)
    Iran_shapefiles["Cities"] = Iran_shapefiles["Cities"].rename(columns ={'CITY_NAME':'CITY_NAME_old', 'CITY_ENG':'CITY_ENG_old' , 'OSTAN_NAME': 'OSTAN_NAME_old'})
    Iran_shapefiles["Cities"] = Iran_shapefiles["Cities"].merge(Cities_name,on="FID")
    return Iran_shapefiles
