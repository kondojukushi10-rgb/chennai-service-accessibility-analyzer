import geopandas as gpd

def compute_zone_accessibility(zones, school_int, hospital_int, park_int):

    # Calculate zone area
    zones['zone_area_sqm'] = zones.geometry.area

    def calculate_percentage(zones, intersection, column_name):
        zone_intersection = gpd.overlay(zones, intersection, how='intersection')
        zone_intersection['area'] = zone_intersection.geometry.area

        grouped = zone_intersection.groupby('Zone_No')['area'].sum()
        zones[column_name] = zones['Zone_No'].map(grouped).fillna(0)

        percent_col = column_name.replace("area", "percentage")
        zones[percent_col] = (zones[column_name] / zones['zone_area_sqm']) * 100

        return zones

    # Apply for each service
    zones = calculate_percentage(zones, school_int, "school_access_area")
    zones = calculate_percentage(zones, hospital_int, "hospital_access_area")
    zones = calculate_percentage(zones, park_int, "park_access_area")

    return zones