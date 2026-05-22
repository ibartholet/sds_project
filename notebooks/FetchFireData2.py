## Fetch Fire Data for the Last 5 Days ##


import requests
import pandas as pd
import geopandas as gpd
from io import StringIO
from config import MAP_KEY

map_key = MAP_KEY

def fetch_data(map_key):
  
  """
  Fetches data for the indicated timerange (from today 5 days back), region, and sensor by quering the FIRMS API.
  First, the status of the provided API-URL is checked. Then, a request to this API-URL is made. 
  If the request is successful, a dataframe containing all the fires detected in the chosen region are returned. 
  If the return fails, an error message will be printed.
  Currently, the chosen region is South America.

  Parameters
  -----------
  map_key: str
     This is the NASA FIRMS API key. This key is used to authenticate the request.
  

  Returns
  -----------
  pd.DataFrame or None
    If the request is successful, a Pandas DataFrame containing all the detected fires in the chosen region is returned. 
    If the request fails, an error message will be printed and None returned.
  
  Example
  -----------
  >>> fetch_data("your_personal_map_key")

  """

  # define coordinates for region, here for South America (min_lon, min_lat, max_lon, max_lat)
  region_coords = "-81.5,-55.0,-35.0,12.5" #these coordinates can easily be changed to a different region

  # choose the number of days (max. 7)
  days = 5

  # define satellite sensor
  sensor = "VIIRS_NOAA20_NRT"


  # define API endpoint url
  api_url = f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{map_key}/{sensor}/{region_coords}/{days}"

  response = requests.get(api_url)

  # check the status and extract the data
  if response.status_code == 200:
    print("Request successful\n")

    # read url and create dataframe
    df_fire = pd.read_csv(StringIO(response.text)) # StringIO converts text string into a virtual file object; pd.read_csv() is reading directly from RAM -> allows for 1 API call instead of 2

    ## if code does not work, due to too many fires; sample only x amount of rows by adjusting this line of code
    # if len(df_fire) > 1000:
    # df_fire = df_fire.sample(1000, random_state = 42)

    print(f"\n Data download successful! {len(df_fire)} fires found.")

    # For reproducibility current fires will be saved in a csv-file
    df_fire.to_csv("FIRMS_fire_data_today_minus5days.csv", index = False)

    return df_fire
  
  elif response.status_code == 404:
    print(f"Error 404: Page not found")
    return None
  
  elif response.status_code == 401:
     print(f"Error 401: Invalid API-Key, please check map-key")
     return None
  
  elif response.status_code == 400:
     print(f"Error 400: Wrong parameters, please check input parameters.")
     return None
  
  else:
    print(f"Request failed: Status {response.status_code}")
    print(response.text)
    return None