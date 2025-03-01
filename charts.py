import plotly.express as px
from dash import dash_table

def create_map(filtered_df):
    """Create animated map chart"""
    fig = px.scatter_map(
        filtered_df, lat="latitude", lon="longitude",
        animation_frame="month",
        map_style="open-street-map"
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
    return dash_table.DataTable(filtered_df.to_dict('records'), [{"name": i, "id": i} for i in filtered_df.columns])
