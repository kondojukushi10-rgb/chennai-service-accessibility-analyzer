import geopandas as gpd

def create_service_buffers(schools, hospitals, parks, roads):
    
    # Create buffers
    school_buffers = schools.copy()
    school_buffers["geometry"] = schools.buffer(1000)

    hospital_buffers = hospitals.copy()
    hospital_buffers["geometry"] = hospitals.buffer(1000)

    park_buffers = parks.copy()
    park_buffers["geometry"] = parks.buffer(1000)

    road_buffers = roads.copy()
    road_buffers["geometry"] = roads.buffer(50)

    # Dissolve buffers
    dissolved_school = school_buffers.dissolve()
    dissolved_hospital = hospital_buffers.dissolve()
    dissolved_park = park_buffers.dissolve()
    dissolved_roads = road_buffers.dissolve()

    return dissolved_school, dissolved_hospital, dissolved_park, dissolved_roads