## Load Map Key and Access Key URL ##

import pandas as pd
import requests
from config import MAP_KEY

def check_map_key(map_key): 
  """
  Checks the status of the provided map key by making a request to the NASA FIRMS API.
  It returns a dictionary, which is then converted into a pandas Series containing the status information of the map key.
  

  Parameters
  -----------
  map_key : str
    This is the NASA FIRMS API key. This function checks the provided key.
  
    
  Returns
  ----------
  dict or None
    If the request is successful, a dicitonary containing the status information of the map key which includes 
    transaction_limit, current_transactions, and transaction_interval is returned.
    If the reques fails, None is returned and an error message will be printed.

    
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
  


