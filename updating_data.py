import pandas as pd

# Load the Excel file
file_path = './reliance_bse_stock_data.xlsx'
df = pd.read_excel(file_path)
# Convert first column to datetime and rename it to 'dates'
df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
df = df.rename(columns={df.columns[0]: 'dates'})
df['dates'] = df['dates'].dt.date
# Save the modified DataFrame to a new Excel file
output_file = './updated_reliance_data.xlsx'
df.to_excel(output_file, index=False)
