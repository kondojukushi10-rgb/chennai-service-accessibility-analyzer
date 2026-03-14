
import geopandas as gpd

def clean_points(gdf):

    # remove features with empty geometry
    gdf = gdf.dropna(subset=["geometry"])

    # remove duplicate features
    gdf = gdf.drop_duplicates()

    # keep only important columns  
    if "name" in gdf.columns:
        gdf = gdf[["name", "geometry"]]
    else:
        gdf = gdf[["geometry"]]

    return gdf