from ast import alias
from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SKETCHY, dbc_css])

app.layout = html.Div(
    [
        html.H1(
            "🍷 Iowa Liquor Sales 🍷",
            className="bg-primary text-white p-2 mb-2 text-center",
        ),
        html.Div(
            [
                # html.Div(
                #     dcc.Link(
                #         f"{page['name']} - {page['path']}", href=page["relative_path"]
                #     )
                # )
                # for page in dash.page_registry.values()
            ]
        ),
        dash.page_container,
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
