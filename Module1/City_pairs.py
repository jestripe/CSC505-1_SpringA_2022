import json
import sys
import pandas as pd

sys.path.insert(0, 'env/lib/python3.9/site-packages')

from env import urllib3
from env import charset_normalizer
from env import requests

# Read in the API key
api_filename = 'api_key.json'

# Make API key usable
api_keys = {}
with open(api_filename, 'r') as f:
    api_secret = json.loads(f.read())
api_key = api_secret['AVIATION_STACK_SECRET']

# Define the URL and end point to be used
base_url = 'http://api.aviationstack.com/v1/flights'

# Define the parameters for the query
params = dict(access_key = api_key, dep_iata = 'DFW', ar_iata = 'MSP', status = 'active', airline_icao = 'aal')

# Get the data
response = requests.get(base_url, params)

# Convert json to a dataframe
t2 = response.json()['data']
df = pd.json_normalize(t2)

# Export to a csv file
df.to_csv('results.csv')