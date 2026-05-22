## **SDS210 Project - Wildfire Mapping in South America** ##

*Author: Isabelle Bartholet*  
*Date: 22.05.2026*

Using near real-time data from NASA's Fire Information for Resource Management System (FIRMS), this project analyses active fire detections in South America. To do so, fire data from the past five days is fetched via the FIRMS API and visualized through timeanimated, interactive and thematic maps.


#### **Data Sources** 
* **API map key:** The API Map Key can be generated at the bottom of this page: https://firms.modaps.eosdis.nasa.gov/api/data_availability/
* **General API overview:** Link to the general FIRMS API overview page: https://firms.modaps.eosdis.nasa.gov/api/
* **Area API:** Link to the specific FIRMS API for the area: https://firms.modaps.eosdis.nasa.gov/api/area/
* Manual on how to use FIRMS API in Python: https://firms.modaps.eosdis.nasa.gov/content/academy/data_api/firms_api_use.html
* Information on the attribute table: https://www.earthdata.nasa.gov/data/catalog/lancemodis-vj114imgtdl-nrt-2


#### **Setup Instructions**
To create this project the software *VS Code* was used. However, it can also be executed using *JupiterLab*.

**Reproducing the Environment**
To correctly execute, this project the following spatial software stack is required. In order to create the environment, please follow these steps:
1. Ensure Conda is installed.
2. Run: 'conda env create -f environment.yml'
3. Activate: 'conda activate sds-env'


####**Execution Order of this project**
1. Get access to the data: Create a personal map key following the link provided above and insert it into the config.py file.
2. Ensure that the files *access_mapkey.py* and *FetchFireData2.py* are in the same folder as the notebooks, which you want to run.
3. Run the Heatmap_SouthAmerica.ipynb notebook first. This shows a timeanimated heatmap of the fire distribution and clustering in South America.
4. Run the BiomeMap_SouthAmerica.ipynb notebook second. Here, the different biomes including the total fires per biomes are mapped in a choropleth map. 
5. Lastly, execute the ThematicMap_SouthAmerica.ipynb which visualizes fire detections in Trinidad and Tobago. 






