import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/")
from pages.nav import make_side_nav


dataset_description = html.Div(
    [
        dcc.Markdown(
            """
    ## Dataset description
    Dataset provides us information about the **Alcohol sales in Lowa state** .

    This dataset contains spirit purchase info of lowa Class `E` liquor licences by product 
    and date of purchase from Dec 2020 to Nov 2021.
    """
        ),
    ]
)
layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(make_side_nav(), xs=4, md=3, xl=2, id="sidebar"),
                dbc.Col(dataset_description, id="page-content"),
            ]
        ),
    ],
    fluid = True
)

# layout = html.Div(children=[

#
#     make_side_nav()

# ])
