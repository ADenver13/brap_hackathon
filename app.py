import dash
from dash import dcc, html, dash_table, Input, Output
from charts import (
    create_animated_map,
    create_bar_chart,
    create_table_figure,
    create_indicator,
    create_pie,
    create_map
)
import pandas as pd

app = dash.Dash(__name__)

# Load processed
filtered_df = pd.read_csv('data/311_rodent_reports_22-24.csv')

# Initialize selected year and neighborhood
selected_year = 2024
selected_neighborhood = 'ALL'

available_years = ['All', 2022, 2023, 2024]

table_figure = create_table_figure(filtered_df)


# Create charts
def create_initial_charts(filtered_df, selected_year, selected_neighborhood):
    # Filter data based on initial selected values
    filtered_data = filtered_df[
        (filtered_df['year'] == selected_year) & 
        (filtered_df['neighborhood'].isin([selected_neighborhood, 'ALL']))
    ]

    animated_map_figure = create_animated_map(filtered_data)
    map_figure = create_map(
        f'All Rodent Sightings ({selected_year}) in Neighborhood: {selected_neighborhood}',
        filtered_data,
        breakdown='source'
    )
    bar_chart_figure = create_bar_chart(filtered_data)

    indicator_above_ground_figure = create_indicator(3439, 'Number of Rats Detected<br>Above Ground (2024)', 3219)
    indicator_below_ground_figure = create_indicator(900, 'Number of Rats Detected<br>Below Ground (2024)', 1100)
    pie_source_figure = create_pie(filtered_data, 'Number of Cases by Source', 'source')
    cases_closed_count_figure = create_indicator(
        ((filtered_data['case_status'] == 'Closed') & (filtered_data['year'] == selected_year)).sum(),
        'Number of Rodent<br>Cases Closed 2024',
        ((filtered_data['case_status'] == 'Closed') & (filtered_data['year'] == selected_year - 1)).sum()
    )

    return animated_map_figure, map_figure, bar_chart_figure, table_figure, indicator_above_ground_figure, indicator_below_ground_figure, pie_source_figure, cases_closed_count_figure

app.layout = html.Div([
    html.Div([
        html.H1("🐀 Rodent Activity Tracker (R.A.T)", style={'color': 'white', 'margin': '0'}),
        html.H3("Monitoring urban rodent activity using open-source reporting", style={'color': 'white'}),
    ], style={
        'backgroundColor': '#2C3E50', 'textAlign': 'center',
        'borderBottom': '4px solid #1ABC9C'
    }),

    # DROPDOWNS
    html.Div([
        html.Div([
            html.Label("Select Year:"),
            dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': str(year), 'value': year} for year in available_years],
                value=selected_year,
                style={'width': '100%'}
            ),
        ], style={'flex': '2', 'minWidth': '200px', 'marginRight': '10px'}),

        html.Div([
            html.Label("Select Neighborhood:"),
            dcc.Dropdown(
                id='neighborhood-dropdown',
                options=[{'label': neighborhood, 'value': neighborhood} for neighborhood in ['ALL'] + filtered_df['neighborhood'].dropna().unique().tolist()],
                value=selected_neighborhood,
                style={'width': '100%'}
            ),
        ], style={'flex': '2', 'minWidth': '200px'})

    ], style={'display': 'flex', 'width': '100%', 'gap': '10px', 'marginTop': '30px'}),

    # ROW 1 - GENERAL INFO
    html.Div([
        html.Div([dcc.Graph(id='indicator-above-ground', className='dash-graph')], style={'flex': '1', 'padding': '2px', 'min-width': '300px'}),
        html.Div([dcc.Graph(id='indicator-below-ground', className='dash-graph')], style={'flex': '1', 'padding': '2px', 'min-width': '300px'}),
        html.Div([dcc.Graph(id='cases-closed-count', className='dash-graph')], style={'flex': '1', 'padding': '2px', 'min-width': '300px'}),
        html.Div([dcc.Graph(id='pie-source', className='dash-graph')], style={'flex': '2', 'padding': '2px', 'min-width': '300px'}),
    ], style={'display': 'flex', 'flexWrap': 'wrap', 'width': '100%', 'margin': 'auto'}),

    # MAPPING
    html.H2('Rodent Activity Mapped'),

    # Layout for map chart - Underground
    html.Div([dcc.Graph(id='animated-map', className='dash-graph')], style={'padding': '1px'}),

    # Layout for map chart - Above Ground
    html.Div([dcc.Graph(id='map-figure', className='dash-graph')], style={'padding': '1px'}),

    # RAW RECORDS
    html.Div([
        html.H3('Raw 311 Rodent Records'),
        table_figure,
    ], style={'padding': '1px'})
])

# Create callback for dynamic charts update based on dropdown changes
@app.callback(
    [
        Output('animated-map', 'figure'),
        Output('map-figure', 'figure'),
        Output('indicator-above-ground', 'figure'),
        Output('indicator-below-ground', 'figure'),
        Output('cases-closed-count', 'figure'),
        Output('pie-source', 'figure')
    ],
    [
        Input('year-dropdown', 'value'),
        Input('neighborhood-dropdown', 'value')
    ]
)
def update_charts(selected_year, selected_neighborhood):
    # If 'All' is selected, include all years in the filtering
    if selected_year == 'All':
        filtered_data = filtered_df[
            (filtered_df['neighborhood'].isin([selected_neighborhood] if selected_neighborhood != 'ALL' else filtered_df['neighborhood'].unique()))
        ]
    else:
        filtered_data = filtered_df[
            (filtered_df['neighborhood'].isin([selected_neighborhood] if selected_neighborhood != 'ALL' else filtered_df['neighborhood'].unique()))
        ]
    
    # Create updated charts
    animated_map_figure = create_animated_map(filtered_data)
    map_figure = create_map(
        f'All Rodent Sightings ({selected_year}) in Neighborhood: {selected_neighborhood}',
        filtered_data[filtered_data['year'] == selected_year],
        breakdown='source'
    )
    bar_chart_figure = create_bar_chart(filtered_data[filtered_data['year'] == selected_year])
    table_figure = create_table_figure(filtered_data[filtered_data['year'] == selected_year])

    # Handling for indicators with year-over-year comparison
    # Little ugly, could be done better
    if selected_year != 'All':
        # We compare selected_year to previous year for indicators
        indicator_above_ground_figure = create_indicator(
            filtered_data[filtered_data['year'] == selected_year].shape[0],
            f'Number of Rats Detected<br>Above Ground ({selected_year})',
            filtered_data[filtered_data['year'] == (selected_year - 1)].shape[0]
        )
        indicator_below_ground_figure = create_indicator(
            -2,
            f'Number of Rats Detected<br>Below Ground ({selected_year})',
            0,
        )
        cases_closed_count_figure = create_indicator(
            ((filtered_data['case_status'] == 'Closed') & (filtered_data['year'] == selected_year)).sum(),
            f'Number of Rodent<br>Cases Closed {selected_year}',
            ((filtered_data['case_status'] == 'Closed') & (filtered_data['year'] == selected_year - 1)).sum()
        )
    else:
        # If 'ALL' year is selected, use the latest year for year-over-year comparison
        latest_year = available_years[-1]
        previous_year = latest_year - 1

        indicator_above_ground_figure = create_indicator(
            filtered_data[filtered_data['year'] == latest_year].shape[0],
            f'Number of Rats Detected<br>Above Ground ({latest_year})',
            filtered_data[filtered_data['year'] == previous_year].shape[0]
        )
        indicator_below_ground_figure = create_indicator(
            -2,
            f'Number of Rats Detected<br>Below Ground ({latest_year})',
            0,
        )
        cases_closed_count_figure = create_indicator(
            ((filtered_data['case_status'] == 'Closed') & (filtered_data['year'] == latest_year)).sum(),
            f'Number of Rodent<br>Cases Closed {latest_year}',
            ((filtered_data['case_status'] == 'Closed') & (filtered_data['year'] == previous_year)).sum()
        )

    pie_source_figure = create_pie(filtered_data, 'Number of Cases by Source', 'source')

    return (
        animated_map_figure, map_figure, indicator_above_ground_figure, 
        indicator_below_ground_figure, cases_closed_count_figure, pie_source_figure
    )

if __name__ == '__main__':
    app.run_server(debug=True)
