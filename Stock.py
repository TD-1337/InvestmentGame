class Stock:
    def __init__(self, name):
        self.name = name

    def retrieve_stock_price_EOD(self, date):
        import requests
        import pandas as pd

        string_pt1 = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="
        string_pt2 = self.name
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

        return close_per_day[date]

    def retrieve_stock_price_now(self):
        import requests

        string_pt1 = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol="
        string_pt2 = self.name
        string_pt3 = "&apikey=1MUPY30U6YSICG6M"

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

        # Extract the corresponding column only
        quote = raw_data[colname]['05. price']

        return quote
