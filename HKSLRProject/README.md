# 🚍 Projected Sea Level Rise on Hong Kong Land Use

This project models flood extent in Hong Kong under 3 greenhouse gas emission scenarios as defined by the Intergovernmental Panel on Climate Change (IPCC)

## 📌 Objectives

- Highlight urban areas and land use types that are vulnerable to sea level rise
- Inform urban planners on future spatial risks brought by climate change
- Encourage policymakers to adopt mitigative and adaptive measures
- Raise public awareness on the importance of the threats posed by sea level rise and climate change in general

## 🧰 Tools

- ArcGIS Pro
- Pycharm IDE

## ℹ️ Data

- Lands Department(HK). "Digital Terrain Model"[asc].Scale Not Given. "DATA.GOV.HK". August 1,2020. https://data.gov.hk/en-data/dataset/hk-landsd-openmap-5m-grid-dtm/resource/620c4f4f-eac4-472f-9074-dffa2ad596fd
- Planning Department(HK). "2021 Raster Grids on Land Utilization"[API].Scale Not Given. "DATA.GOV.HK".September 30,2022. https://data.gov.hk/en-data/dataset/hk-pland-pland1-land-utilization-in-hong-kong-raster-grid/resource/6fe96592-0ca5-4a7a-8bc2-b658f76b2880

## 📊 Workflow

- Georeferenced Digital Terrain Model (DTM) to assign coordinates
- Convert DTM into a contour map
- Convert the contour map into a digital elevation model
- Generate the flood extent raster layers using the mean sea level regarding the 3 GHG emissions scenarios
- Overlay flood extent raster layers on Land Utilization Raster Grids to visualize land types that are affected by future coastal flooding

👉👉👉[Method](methods.md)👈👈👈

## 🗺️ Output

![Output](FloodLayout.jpg)

## ✍️ Author

Jonathan Leung — University of Waterloo, Geomatics with Co-op
