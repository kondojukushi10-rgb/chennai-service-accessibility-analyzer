import geopandas as gpd

def load_data():
    zones = gpd.read_file(r"E:\Geospatial_Technology\Capstones\Capstone2\Capstone2_Project1\chennai-service-accessibility-analyzer\data\raw\GCC_Zones.shp")
    roads = gpd.read_file(r"E:\Geospatial_Technology\Capstones\Capstone2\Capstone2_Project1\chennai-service-accessibility-analyzer\data\raw\roads.shp")
    hospitals = gpd.read_file(r"E:\Geospatial_Technology\Capstones\Capstone2\Capstone2_Project1\chennai-service-accessibility-analyzer\data\raw\hospitals.geojson")
    parks = gpd.read_file(r"E:\Geospatial_Technology\Capstones\Capstone2\Capstone2_Project1\chennai-service-accessibility-analyzer\data\raw\parks.geojson")
    schools = gpd.read_file(r"E:\Geospatial_Technology\Capstones\Capstone2\Capstone2_Project1\chennai-service-accessibility-analyzer\data\raw\schools.geojson")

    print("CRS Information")
    print("Zones: ", zones.crs)
    print("Roads: ", roads.crs)
    print("hospitals: ", hospitals.crs)
    print("Parks: ", parks.crs)
    print("Schools: ", schools.crs)

    print("Zones columns:", zones.columns)
    print("Roads columns:", roads.columns)
    print("Hospitals columns:", hospitals.columns)
    print("Parks columns:", parks.columns)
    print("Schools columns:", schools.columns)

    print("Number of features:")
    print("Zones:", len(zones))
    print("Roads:", len(roads))
    print("Hospitals:", len(hospitals))
    print("Parks:", len(parks))
    print("Schools:", len(schools))

    return zones, roads, hospitals, parks, schools


