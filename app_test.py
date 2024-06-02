import pandas as pd
import dash
import os
from dash import dcc, html
import plotly.express as px

# Load data
data_dir = 'data'
file_path = os.path.join(data_dir, 'formatted_sales_data.csv')  # Ensure the correct filename
sales_data = pd.read_csv(file_path)  # Read Data

# Convert date column to datetime
sales_data['date'] = pd.to_datetime(sales_data['date'])

# Sort the data by date
sales_data = sales_data.sort_values(by='date')

# Create the app
app = dash.Dash(__name__)

# Define Layout
line_chart = px.line(sales_data, x='date', y='sales', title='Sales of Pink Morsels over Time', labels={'date': 'Date', 'sales': 'Sales'})  # Use px.line to create the line chart

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Analysis'),
    
    dcc.Graph(
        id='sales-line-chart',
        figure=line_chart
    )
])
    
# Calling the main file
if __name__ == '__main__':
    app.run_server(debug=True)
