from ast import alias
from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from pages.nav import make_side_nav


dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.SKETCHY, dbc_css],
    title="Iowa liquor sales",
    update_title="🍷...",
)
app._favicon = "./android_fav.png"

server = app.server

app.layout = dbc.Container(
    [
        html.H1(
            "🍾 Iowa Liquor Sales 🍾",
            className="bg-primary text-white p-2 mb-2 text-center",
        ),
        dbc.Row(
            [
                dbc.Col(make_side_nav(), xs=4, md=3, xl=2, id="sidebar"),
                dbc.Col(dash.page_container),
            ]
        ),
    ],
   fluid=True,
    className="dbc",
)

if __name__ == "__main__":
    app.run_server(debug=True)
