from subprocess import call
import dash
from dash import html, dcc, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc 
import pandas as pd

dash.register_page(__name__)

data = pd.read_csv("data/liquor_iowa_2021.csv")

table = dash_table.DataTable(
        columns=[
            {"name": i, "id": i, "deletable": True} for i in data.columns
        ],
        data=data.to_dict("records"),
        editable=True,
        cell_selectable=True,
        filter_action="native",
        sort_action="native",
        page_size=20,  # we have less data in this example, so setting to 20
        style_table={"overflowY": "auto"},
    )

layout = dbc.Container(
    children=[
        dcc.Markdown("""
        # Interactive table for exploration in real-time.
        This data table contains only 50000 entry database. 
        """),
        table,
        html.H2("Click following buttons for downloading dataset"),
        dcc.Markdown("this dashboard is developed with `50k` Records dataset"),
        html.Div([
            dbc.Button("50k Records", color="primary", id = "smallest_dataset", target = "_blank"), 
            dbc.Button("1.2M Records", color="primary", id = "medium_dataset", target = "_blank"),
            dbc.Button("12M Records", color="primary", id = "largest_dataset", target = "_blank")
        ]),
        dcc.Download(id = "send_file")

    ]
)

@callback(
    Output("send_file", "data"),
    Input("smallest_dataset", "n_clicks"),
    prevent_initial_call=True,
)
def download_smallest_dataset(n_clicks):
    return dcc.send_file("./data/liquor_iowa_2021.csv")

@callback(
    Output("medium_dataset", "href"),
    Input("medium_dataset", "n_clicks"),
    prevent_initial_call=True,
)
def medium_return(n_clicks):
    return "https://www.kaggle.com/datasets/residentmario/iowa-liquor-sales?sort=published"

@callback(
    Output("largest_dataset", "href"),
    Input("largest_dataset", "n_clicks"),
    prevent_initial_call=True,
)
def large_return(n_clicks):
    return "https://www.kaggle.com/datasets/residentmario/iowa-liquor-sales?sort=published"
