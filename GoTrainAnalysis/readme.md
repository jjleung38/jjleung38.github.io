# 🚍 GTA GO Train Transit Coverage Network Analysis


## 📌 Objectives

- Conducted service area analysis on the GO Train railway system to assess its service coverage across the Greater Toronto Area
- Analyzed percentage transit coverage within each GTA Census Subdivision by driving time
- Support transportation planning, such as future stations, with data-driven results
- Identify transit gaps by highlighting municipalities with little coverage within the service area

## 🧰 Tools

- ArcGIS Pro

## ℹ️ Data

- Ministry of Transportation. "GO Train stations"[csv].Scale Not Given. "Ontario Data Catalogue". April 25, 2024. [https://data.ontario.ca/dataset/go-train-stations](https://data.ontario.ca/dataset/go-train-stations)
- Statistics Canada. "2016 Census Program - Age and Sex Highlight Tables"[shp,csv]. 

## 📊 Workflow

- Import the GO Train Station feature class as facilities in the Service Area Analysis tool
- Service Area Analysis based on GO Train Stations
  - Driving Time in 5, 10, and 20 minutes
- Select CSDs in the CSD shapefile that overlap with the service area layer
- Join Census Data with CSD shapefiles using **Spatial Join**
  - Calculate the total area of each CSD polygon with **field calculator**
- Run **Intersect** to produce a new feature class with the overlapped parts of each CSD
  - Calculate the total area of each polygon with **field calculator**
  - Calculate the sum of polygons that share the same CSDUID
- Join the overlapped feature class to the original CSD shapefile
- Calculate % of each CSD's area covered by the service area

## 🗺️ Output

![]()

## ✍️ Author

Jonathan Leung — University of Waterloo, Geomatics with Co-op

