import geopandas as gpd

def compute_intersections(school_buf, hospital_buf, park_buf, road_buf):

    school_intersection = gpd.overlay(school_buf, road_buf, how='intersection')
    hospital_intersection = gpd.overlay(hospital_buf, road_buf, how='intersection')
    park_intersection = gpd.overlay(park_buf, road_buf, how='intersection')

    return school_intersection, hospital_intersection, park_intersection