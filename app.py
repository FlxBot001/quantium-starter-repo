import pandas as pd
import dash
import os
from dash import dcc, html, Input, Output
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
app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Analysis', style={'textAlign': 'center', 'color': '#2C3E50'}),

    dcc.RadioItems(
        id='region-radio',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All', 'value': 'all'}
        ],
        value='all',
        labelStyle={'display': 'inline-block', 'margin-right': '10px'},
        style={'textAlign': 'center', 'margin': '20px 0'}
    ),
    
    dcc.Graph(
        id='sales-line-chart'
    )
], style={'font-family': 'Arial, sans-serif', 'background-color': '#F5F5F5', 'padding': '20px'})

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-radio', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_data = sales_data
    else:
        filtered_data = sales_data[sales_data['region'] == selected_region]
    
    line_chart = px.line(
        filtered_data,
        x='date',
        y='sales',
        title=f'Sales of Pink Morsels in {selected_region.capitalize()} Region' if selected_region != 'all' else 'Sales of Pink Morsels in All Regions',
        labels={'date': 'Date', 'sales': 'Sales'},
        template='plotly_white'
    )
    line_chart.update_layout(title={'x': 0.5, 'xanchor': 'center'}, title_font_size=24)
    return line_chart

# Calling the main file
if __name__ == '__main__':
    app.run_server(debug=True)
