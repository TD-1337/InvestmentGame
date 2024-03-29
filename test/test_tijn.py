import requests

string_pt1 = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="
string_pt2 = "TWTR"
string_pt3 = "&interval=5min&outputsize=full&apikey=1MUPY30U6YSICG6M"

string_concat = string_pt1 + string_pt2 + string_pt3

# Get response from server
response = requests.get(string_concat)

# Check if valid
if response.status_code != 200:
    raise ValueError("Could not retrieve data, code:", response.status_code)

# The service sends JSON data, we parse that into a Python datastructure
raw_data = response.json()

# Retrieve the name of the column with our actual data
colname = list(raw_data.keys())[-1]

print(raw_data)