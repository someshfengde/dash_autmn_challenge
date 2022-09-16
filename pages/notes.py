import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__)

layout = html.Div(
    children=[
        html.H1(children="My notes for generating this dashboard application."),
        html.Iframe(
            src="assets/notes2.pdf",
            style={"display": "block", "width": "100%", "height": "100vh"},
            width="100vw",
            className="p-4",
        ),
    ]
)
