import requests
import pandas as pd

# API endpoint for the stock data
url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=RELIANCE.BSE&outputsize=full&apikey=demo"

# Fetch data from the API
response = requests.get(url)
data = response.json()

# Parse the JSON data to a pandas DataFrame
timeseries = data['Time Series (Daily)']
df = pd.DataFrame(timeseries).T

# Convert index to datetime
df.index = pd.to_datetime(df.index)

# Rename columns for clarity
df.columns = [
    'open', 'high', 'low', 'close', 'adjusted_close',
    'volume', 'dividend_amount', 'split_coefficient'
]

# Convert columns to numeric where necessary
df = df.apply(pd.to_numeric)

# Check the data types of each column
print("Data types of each column:")
print(df.dtypes)
print("Missing values in each column:")
print(df.isnull().sum())
