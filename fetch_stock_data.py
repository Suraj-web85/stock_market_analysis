import requests
import pandas as pd

# Function to fetch and process stock data
def fetch_and_process_stock_data(symbol, excel_output_file, json_output_file):
    # API endpoint for the stock data
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize=full&apikey=demo"

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

    # Extract date part and move it to the 0th index
    df['dates'] = df.index.date  # Extract date part only
    df = df[['dates'] + df.columns[:-1].tolist()]  # Reorder columns with 'dates' at 0th index

    # Save the DataFrame to Excel
    df.to_excel(excel_output_file, index=False)

    # Save the DataFrame to JSON
    df.to_json(json_output_file, orient='records', date_format='iso')

    print(f"Updated data saved to {excel_output_file} and {json_output_file}")

if __name__ == "__main__":
    symbol = 'RELIANCE.BSE'  # Example symbol for Reliance Industries on BSE
    excel_output_file = './data/updated_reliance_data.xlsx'
    json_output_file = './data/updated_reliance_data.json'

    # Fetch and process stock data
    fetch_and_process_stock_data(symbol, excel_output_file, json_output_file)
