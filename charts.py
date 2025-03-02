import plotly.express as px
import plotly.graph_objects as go
from dash import dash_table

def create_animated_map(filtered_df):
    """Create animated map chart"""
    fig = px.scatter_map(
        filtered_df, lat="latitude", lon="longitude",
        animation_frame="month",
        map_style="open-street-map",
        title='All Rodent Sightings Animated (Jan-Feb) (All Years)'
    )

    fig.update_layout(
        # width=1000,
        height=800
    )
    return fig

def create_bar_chart(filtered_df):
    """Create bar chart for analysis"""
    fig = px.bar(
        filtered_df,
        x='month',
        y='on_time',
        title="Bar Chart Example"
    )
    return fig

def create_table_figure(filtered_df):
    return dash_table.DataTable(
        filtered_df.to_dict('records'),
        [{"name": i, "id": i} for i in filtered_df.columns],
        page_size=10,
        style_table={
            'maxWidth': '100%',
            'overflowX': 'auto',
        },
    )

def create_indicator(number, title, delta):
    fig = go.Figure()
    indicator = go.Indicator(
        mode="number+delta",
        value=number,  # The number to display
        title=title,  # Title of the indicator
        domain={'x': [0, 1], 'y': [0, 1]},  # Set the domain size (controls space for the chart)
        delta = {'reference': delta},
    )
    fig.add_trace(indicator)
    return fig

def create_pie(df, title, breakdown):
    fig = px.pie(
        df,
        names=breakdown,
        title=title
    )
    return fig

def create_map(title, df, breakdown=None):
    """Create animated map chart"""
    fig = px.scatter_map(
        df, lat="latitude", lon="longitude",
        map_style="open-street-map",
        title=title,
        color=breakdown,
    )

    fig.update_layout(
        # width=1000,
        height=800
    )
    return fig
