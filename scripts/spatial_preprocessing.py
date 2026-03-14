import geopandas as gpd

def reproject_layers(zones, roads, schools, hospitals, parks):

    target_crs = 32644

    zones = zones.to_crs(target_crs)
    roads = roads.to_crs(target_crs)
    schools = schools.to_crs(target_crs)
    hospitals = hospitals.to_crs(target_crs)
    parks = parks.to_crs(target_crs)

    print("CRS after reprojection:")
    print("Zones:", zones.crs)
    print("Schools:", schools.crs)
    print("Hospitals:", hospitals.crs)
    print("Parks:", parks.crs)
    print("Roads:", roads.crs)

    return zones, roads, schools, hospitals, parks

