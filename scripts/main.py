from data_loader import load_data
from data_cleaner import clean_points
from spatial_preprocessing import reproject_layers

# Step 1: Load datasets
zones, roads, hospitals, parks, schools = load_data()

# Step 2: Clean point datasets
schools = clean_points(schools)
hospitals = clean_points(hospitals)
parks = clean_points(parks)

# Step 3: Reproject all layers
zones, roads, schools, hospitals, parks = reproject_layers(
    zones, roads, schools, hospitals, parks
)

print("Pipeline executed successfully")