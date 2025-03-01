import dash
from dash import dcc, html, dash_table
from data_utils import process_data
from charts import create_map, create_bar_chart, create_table_figure

# Load and process data
filtered_df = process_data('data/reports_2024.csv')

# Create charts
map_figure = create_map(filtered_df)
bar_chart_figure = create_bar_chart(filtered_df)

table_figure = create_table_figure(filtered_df)

# Dash app setup
app = dash.Dash(__name__)

# Apply a custom CSS class to the divs to use the new styles
app.layout = html.Div([
    html.H1("Rodent Activity Dashboard"),
    
    # Layout for map chart - Underground
    html.Div([
        html.H3("Rodent Underground Map"),
        dcc.Graph(figure=map_figure, className='dash-graph'),
    ], style={'padding': '1px'}),

    # Layout for map chart - Above Ground
    html.Div([
        html.H3("Rodent Above Ground Map"),
        dcc.Graph(figure=map_figure, className='dash-graph'),
    ], style={'padding': '1px'}),

    # Layout for bar chart
    html.Div([
        html.H3("Rodent Activity Analysis (Bar Chart)"),
        dcc.Graph(figure=bar_chart_figure, className='dash-graph'),
    ], style={'padding': '1px'}),

    # Layout for table
    html.Div([
        html.H3("Rodent Activity Table"),
        table_figure,
    ], style={'padding': '1px'})
])

if __name__ == '__main__':
    app.run_server(debug=True)
