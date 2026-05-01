from data_loader import load_data
from data_cleaner import clean_points
from spatial_preprocessing import reproject_layers

from buffer_analysis import create_service_buffers
from intersection_analysis import compute_intersections
from accessibility_index import compute_zone_accessibility
from visualization import visualize_accessibility


# STEP 1: Load Data
zones, roads, hospitals, parks, schools = load_data()


# STEP 2: Clean Data
schools = clean_points(schools)
hospitals = clean_points(hospitals)
parks = clean_points(parks)


# STEP 3: Reproject Data
zones, roads, schools, hospitals, parks = reproject_layers(
    zones, roads, schools, hospitals, parks
)


# STEP 4: Buffer Analysis
school_buf, hospital_buf, park_buf, road_buf = create_service_buffers(
    schools, hospitals, parks, roads
)


# STEP 5: Intersection Analysis
school_int, hospital_int, park_int = compute_intersections(
    school_buf, hospital_buf, park_buf, road_buf
)


# STEP 6: Accessibility Calculation
zones = compute_zone_accessibility(
    zones, school_int, hospital_int, park_int
)


print("Pipeline executed successfully 🚀")

# STEP 6: Export Processed Data

import os

# Create outputs folder if it doesn't exist
output_folder = "outputs"
os.makedirs(output_folder, exist_ok=True)

# Save zones (with accessibility values if added later)
zones.to_file(os.path.join(output_folder, "zones_processed.geojson"), driver="GeoJSON")

processed_folder = "processed"
os.makedirs(processed_folder, exist_ok=True)

# Save accessibility layers
school_int.to_file(os.path.join(processed_folder, "school_accessibility.geojson"), driver="GeoJSON")
hospital_int.to_file(os.path.join(processed_folder, "hospital_accessibility.geojson"), driver="GeoJSON")
park_int.to_file(os.path.join(processed_folder, "park_accessibility.geojson"), driver="GeoJSON")

print("Processed files saved in folders")