import pandas as pd
import plotly.graph_objects as go

# Load your reliance_bse_data into a DataFrame
df = pd.read_excel('updated_reliance_data.xlsx')  # Adjust filename if necessary

# Create a Plotly figure
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['dates'], y=df['close'], mode='lines+markers', name='Close Price'))
fig.update_layout(title='Reliance Industries BSE - Closing Price', xaxis_title='Date', yaxis_title='Price (INR)')
fig.show()
