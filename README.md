# 🛰️ Chennai Service Accessibility Analyzer

A GIS-based analytical pipeline to evaluate public service accessibility across Chennai using spatial data processing and geospatial analysis.

This project computes accessibility for essential services such as **schools, hospitals, and parks** by integrating buffer analysis, road network proximity, and zonal statistics to derive a **composite accessibility index**.

---

## 📌 Project Objective

To measure and visualize how well different zones in Chennai are served by key public facilities, helping identify underserved areas and support urban planning decisions.

---

## 🧠 Methodology Overview

The workflow follows a modular geospatial pipeline:

```
Data Collection → Data Cleaning → CRS Standardization → Buffer Creation → 
Road Intersection Analysis → Zonal Aggregation → Accessibility Index → Visualization
```

---

## ⚙️ Tech Stack

* Python
* GeoPandas
* Shapely
* PyProj
* Rtree
* Pandas & NumPy
* Matplotlib (for static maps)
* Folium / Leafmap (optional interactive maps)

---

## 📂 Project Structure

```
chennai-service-accessibility-analyzer/
│
├── data/
│   └── raw/                        # Input shapefiles and GeoJSON
│
├── scripts/
│   ├── data_loader.py             # Load spatial datasets
│   ├── data_cleaner.py            # Clean geometries and attributes
│   ├── spatial_preprocessing.py   # CRS harmonization
│   ├── buffer_analysis.py         # Create service buffers
│   ├── intersection_analysis.py   # Overlay with road network
│   ├── accessibility_index.py     # Compute accessibility metrics
│   ├── visualization.py           # Generate maps
│   └── main.py                    # Pipeline execution script
│
└── README.md
```

---

## 🚀 Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Environment

**Windows (PowerShell):**

```bash
venv\Scripts\activate
```

**Windows (CMD alternative):**

```bash
venv\Scripts\activate.bat
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

```bash
python scripts/main.py
```

---

## 📊 Analysis Workflow

### 1. Data Loading

* Imports zone boundaries, roads, and service locations (schools, hospitals, parks)

### 2. Data Cleaning

* Removes invalid geometries
* Standardizes attribute fields

### 3. Spatial Preprocessing

* Converts all datasets to a projected CRS (EPSG:32644)

### 4. Buffer Analysis

* Schools, hospitals, parks → 1000m buffers
* Roads → 50m buffer

### 5. Intersection Analysis

* Computes overlap between service buffers and road network

### 6. Zonal Accessibility Calculation

* Intersects service coverage with administrative zones
* Computes % of accessible area per zone

### 7. Accessibility Index

A composite index is calculated using normalized values:

```
Accessibility Index =
0.40 × Hospital Accessibility +
0.35 × School Accessibility +
0.25 × Park Accessibility
```

---

## 📈 Output

Each zone contains:

* School Accessibility (%)
* Hospital Accessibility (%)
* Park Accessibility (%)
* Final Accessibility Index (0–1 scale)

---

## 🗺️ Visualization

* Choropleth maps showing accessibility levels
* Optional interactive maps using Leafmap/Folium
* Static maps using Matplotlib for portability

---

## 💡 Key Insights

* Identifies spatial inequality in service distribution
* Highlights zones with low accessibility
* Supports data-driven urban planning decisions

---

## 🔮 Future Improvements

* Add public transport accessibility (bus stops, metro)
* Use network-based analysis instead of Euclidean buffers
* Integrate population density for demand-based analysis
* Develop a web GIS dashboard

---

## 👩‍💻 Author

**Kushi Kondoju**
Urban Planning Graduate | Aspiring GIS Analyst

---

## ⭐ Notes

This project is designed as a **portfolio-ready geospatial analysis pipeline** demonstrating:

* Modular Python scripting
* Spatial analysis using GeoPandas
* Real-world urban planning application

---
