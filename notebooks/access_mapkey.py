## Load Map Key and Access Key URL ##

# most of the code used in this file was copied from NASA FIRM: https://firms.modaps.eosdis.nasa.gov/content/academy/data_api/firms_api_use.html, last access: 22.05.2026

import pandas as pd
import requests
from config import MAP_KEY

def check_map_key(map_key): 
  """
  Checks the status of the provided map key by making a request to the NASA FIRMS API.
  It returns a dictionary, which contains the status information of the map key.
  

  Parameters
  -----------
  map_key : str
    This is the NASA FIRMS API key. This function checks the provided key.
  
    
  Returns
  ----------
  dict or None
    If the request is successful, a dictionary containing the status information of the map key is returned, including:
    - transaction_limit: maximum number of allowed transactions
    - current_transactions: number of transactions used 
    - transaction_interval: time window for the transaction limit
    If the request fails, None is returned and an error message will be printed.

      
  Example
  ----------
  >>> check_map_key("your_personal_map_key")
  
  """
  key_url = f"https://firms.modaps.eosdis.nasa.gov/mapserver/mapkey_status/?map_key={map_key}"
  
  try:
    response = requests.get(key_url)

    if response.status_code == 200:
      data = response.json()
      df = pd.Series(data)
      print(df)
      return data 
  
    else:
      print(f"Error in the query: HTTP {response.status_code}")
      print(response.text)
      return None
  
  except Exception as e: 
  # possible error, wrong MAP_KEY value, check for extra quotes, missing letters
    print (f"There is an issue with the query: {e}\n try in your browser: {key_url}")
    return None
  


