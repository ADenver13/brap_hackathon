import dash
from dash import dcc, html, dash_table
from data_utils import process_data
from charts import (
    create_animated_map,
    create_bar_chart,
    create_table_figure,
    create_indicator,
    create_pie,
    create_map
)
import pandas as pd

selected_year = 2024
selected_month = NotImplemented
selected_neighborhood = 'ALL'

# Load and process data
# filtered_df = process_data('data/reports_2024.csv')

filtered_df = pd.read_csv('data/311_rodent_reports_22-24.csv')

# Create charts
animated_map_figure = create_animated_map(filtered_df)

map_figure = create_map(
    f'All Rodent Sightings ({selected_year}) in Neighborhood: {selected_neighborhood}',
    filtered_df[filtered_df['year'] == selected_year],
    breakdown='source'
)

bar_chart_figure = create_bar_chart(filtered_df)

table_figure = create_table_figure(filtered_df)

# First row charts
indicator_above_ground_figure = create_indicator(3439, 'Number of Rats Detected Above Ground (2024)', 3219)
indicator_below_ground_figure = create_indicator(900, 'Number of Rats Detected Below Ground (2024)', 1100)
pie_source_figure = create_pie(filtered_df[filtered_df['year'] == selected_year], 'Number of Cases by Source', 'source')
cases_closed_count_figure = create_indicator(
        ((filtered_df['case_status'] == 'Closed') & (filtered_df['year'] == selected_year)).sum(),
        'Number of Rodent Cases Closed 2024',
        ((filtered_df['case_status'] == 'Closed') & (filtered_df['year'] == selected_year - 1)).sum()
)

# Dash app setup
app = dash.Dash(__name__)

# Apply a custom CSS class to the divs to use the new styles
app.layout = html.Div([
    html.H1("Rodent Activity Tracker (R.A.T)"),

    html.Div([
        html.Div([
            dcc.Graph(figure=indicator_above_ground_figure, className='dash-graph'),
        ], style={'flex': '1', 'padding': '2px', 'min-width': '300px'}),

        html.Div([
            dcc.Graph(figure=indicator_below_ground_figure, className='dash-graph'),
        ], style={'flex': '1', 'padding': '2px', 'min-width': '300px'}),
        html.Div([
            dcc.Graph(figure=cases_closed_count_figure, className='dash-graph'),
        ], style={'flex': '1', 'padding': '2px', 'min-width': '300px'}),
        html.Div([
            dcc.Graph(figure=pie_source_figure, className='dash-graph'),
        ], style={'flex': '1', 'padding': '2px', 'min-width': '300px'}),

    ], style={'display': 'flex', 'flexWrap': 'wrap', 'width': '100%', 'margin': 'auto'}),

    html.H2('Rodent Activity Mapped'),

    # Layout for map chart - Underground
    html.Div([
        dcc.Graph(figure=animated_map_figure, className='dash-graph'),
    ], style={'padding': '1px'}),

    # Layout for map chart - Above Ground
    html.Div([
        dcc.Graph(figure=map_figure, className='dash-graph'),
    ], style={'padding': '1px'}),

    # Layout for table
    html.Div([
        html.H3('Raw 311 Rodent Records'),
        table_figure,
    ]),

])

if __name__ == '__main__':
    app.run_server(debug=True)
