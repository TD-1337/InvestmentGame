import requests
import pandas as pd

# Get response from server
response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&outputsize=full&apikey=demo")

# Check if valid
if response.status_code != 200:
    raise ValueError("Could not retrieve data, code:", response.status_code)

# The service sends JSON data, we parse that into a Python datastructure
raw_data = response.json()

# Retrieve the name of the column with our actual data
colname = list(raw_data.keys())[-1]

# Extract the corresponding column only
data = raw_data[colname]

# Change to dataframe
df = pd.DataFrame(data).T.apply(pd.to_numeric)

# Parse the index to create a datetimeindex
df.index = pd.DatetimeIndex(df.index)

# Fix the column names
df.rename(columns=lambda s: s[3:], inplace=True)

# Get closing price per day
close_per_day = df.close.resample('B').last()

print(close_per_day)