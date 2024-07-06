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
df.columns = ['open', 'high', 'low', 'close', 'adjusted_close', 'volume', 'dividend_amount', 'split_coefficient']

# Convert columns to numeric
df = df.apply(pd.to_numeric)

# Save the DataFrame to an Excel file
df.to_excel('reliance_bse_stock_data.xlsx', index=True)

# Save the DataFrame to a JSON file
df.to_json('reliance_bse_stock_data.json', orient='records', date_format='iso')
