import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO
import pathlib


theme_changer = ThemeChangerAIO(
    aio_id="theme",
    button_props={"color": "primary", "outline": True},
    radio_props={"value": dbc.themes.SKETCHY},
)

def make_header(text, spacing="mt-4"):
    return html.H2(
        text,
        className="text-white bg-primary p-2 " + spacing,
    )


def make_sidebar_category(category="/", title=""):
    include_home = category == "/theme-explorer"
    return dbc.AccordionItem(
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"]),
                    ],
                    href=page["path"],
                    active="exact",
                    className="py-2",
                )
                for page in dash.page_registry.values()
                if page["path"].startswith(category)
                or (page["path"] == "/" and include_home)
            ],
            vertical=True,
            pills=True,
            # className="bg-light",
        ),
        title=title,
    )


def make_side_nav():
    return html.Div(
        [
            theme_changer,
            html.Hr(),
            dbc.Accordion(
                [
                    make_sidebar_category(
                        category="./", title="asdfasdf Explorer"
                    )
                ],
            ),
            dbc.Accordion(
                [
                    make_sidebar_category(
                        category="/adding-themes", title="Adding Themes"
                    )
                ],
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        dbc.Nav(
                            [
                                dbc.NavLink(
                                    "Dash Bootstrap Cheatsheet",
                                    href="cheatsheet_url",
                                    target="_blank",
                                ),
                                dbc.NavLink(
                                    "Dash Examples Index",
                                    href="examples_index_url",
                                    target="_blank",
                                ),
                                dbc.NavLink(
                                    "Dash Docs", href="dash_docs_url", target="_blank"
                                ),
                                dbc.NavLink(
                                    "Dash Forum", href="dash_forum_url", target="_blank"
                                ),
                                dbc.NavLink(
                                    "Dash Bootstrap Components Docs",
                                    href="dbc_components_url",
                                    target="_blank",
                                ),
                                dbc.NavLink(
                                    [
                                        html.I(className="fa-brands fa-github me-2"),
                                        "Dash Bootstrap Templates",
                                    ],
                                    href="",
                                    target="_blank",
                                ),
                            ],
                            vertical=True,
                        ),
                        title="Other Sites",
                    )
                ],
            ),
        ],
        className="sticky-top vh-100 overflow-scroll",
    )
