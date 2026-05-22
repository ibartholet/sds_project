## **SDS210 Project - Wildfire Mapping in South America** ##

*Author: Isabelle Bartholet*  
*Date: 22.05.2026*

Using near real-time data from NASA's Fire Information for Resource Management System (FIRMS), this project analyses active fire detections in South America. To do so, fire data from the past five days is fetched via the FIRMS API and visualized through timeanimated, interactive and thematic maps.


#### **Data Sources** 
* **API map key:** The API Map Key can be generated on this page: https://firms.modaps.eosdis.nasa.gov/api/map_key/
* **General API overview:** Link to the general FIRMS API overview page: https://firms.modaps.eosdis.nasa.gov/api/
* **Area API:** Link to the specific FIRMS API for the area: https://firms.modaps.eosdis.nasa.gov/api/area/
* Manual on how to use FIRMS API in Python: https://firms.modaps.eosdis.nasa.gov/content/academy/data_api/firms_api_use.html
* Information on the attribute table: https://www.earthdata.nasa.gov/data/catalog/lancemodis-vj114imgtdl-nrt-2
* **Shapefile for World Ecoregions:** A shapefile including information on ecoregions and biomes can be downloaded here: https://ecoregions.appspot.com/

Last access date for all links: 22.05.2026


#### **Setup Instructions**
To create this project the software *VS Code* was used. However, it can also be executed using *JupiterLab*.

**Reproducing the Environment**
To correctly execute, this project the following spatial software stack is required. In order to create the environment, please follow these steps:
1. Ensure Conda is installed.
2. Run: 'conda env create -f environment.yml'
3. Activate: 'conda activate sds-env'


####**Execution Order of this project**
1. Make sure you are on the project branch. The project was set up on there, in case in future  more than one person would like to work on this project. 
2. Get access to the data: Create a personal map key following the link provided above and insert it into the config.py file.
3. Ensure that the files *access_mapkey.py* and *FetchFireData2.py* are in the same folder as the notebooks, which you want to run.
4. Run the Heatmap_SouthAmerica.ipynb notebook first. This shows a timeanimated heatmap of the fire distribution and clustering in South America.
5. Run the BiomeMap_SouthAmerica.ipynb notebook second. Here, the different biomes including the total fires per biomes are mapped in a choropleth map. 
6. Lastly, execute the ThematicMap_SouthAmerica.ipynb which visualizes fire detections in Trinidad and Tobago. 







