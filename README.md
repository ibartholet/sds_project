## **SDS210 Project - Wildfire Mapping in South America** ##

#### **Project Title & Description**
This project creates different layers displaying fires in South America. The different layers aim to answer where fires are located, how intense they burn, and which biomes are affected by the wildfires. 
**maybe change this**

#### **Data Sources** 
Explicit links to where the raw open data was obtained.

#### **Setup Instructions**
To create this project the software *VS Code* was used. However, it can also be executed using *JupiterLab*.

The following libraries are required to run the code:
- requests
- pandas
- geopandas
- time
- matplotlib.pyplot -> ist ein Modul aus einem Package
- folium
- contextily -> evtl. noch rausnehmen
- cmcrameri -> evtl. noch rausnehmen
- cartopy -> evtl. noch rausnehmen, Submodul
- geodatasets -> evtl. noch rausnehmen, Package


**Execution Order of this project**
1. Get access to the data: create a personal map key here XXX (for most recent data) and create an EarthData account here: xxx (for data older than 7 days)
2. Run the Heatmap_SouthAmerica.ipynb notebook first. This shows the distribution and clustering of the fires in South America.
3. Run the .ipynb notebook second. Here, a layer of Northern South America Fires is mapped
4. Run the .ipynb. Now, a choropleth map of biomes is constructed. First, the data will be cleaned, then the choropleth map is programmed. In the end, the previously created maps will be combined to one single map with several layers to toggle on and off.




