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
    nav_items = []
    for page in dash.page_registry.values():
        if page["name"] == "Dashboard":
            page_name = f"🏠️ {page['name']}"
        elif page["name"] == "Data about":
            page_name = f"📊 {page['name']}"
        elif page["name"] == "Notes":
            page_name = f"📕 {page['name']}"
        else:
            page_name = page["name"]
        nav_items.append(
            html.Div(
                dbc.NavLink(
                    page_name,
                    href=page["relative_path"],
                    active="exact",
                )
            )
        )

    return dbc.AccordionItem(
        dbc.Nav(
            nav_items,
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
                [make_sidebar_category(category="./", title="Liquor data explorer 🔍️")],
            ),
            html.Br(),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        dbc.Nav(
                            [
                                dbc.NavLink(
                                    "😺 GitHub repo",
                                    href="https://github.com/someshfengde/dash_autmn_challenge",
                                    target="_blank",
                                ),
                                dbc.NavLink(
                                    "📧 Contact",
                                    href="mailto:someshfengde@gmail.com",
                                    target="_blank",
                                ),
                            ],
                            vertical=True,
                            pills=True,
                        ),
                        title="App links",
                    ),
                ]
            ),
            html.Br(),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        dbc.Nav(
                            [
                                dbc.NavLink(
                                    "👨‍🎓 Resume",
                                    href="https://drive.google.com/file/d/106-FOqLpbwAFLnWtSFWW4-EMNHunJ1NN/view?usp=sharing",
                                    target="_blank",
                                ),
                                dbc.NavLink(
                                    "🕸️ LinkedIn",
                                    href="https://www.linkedin.com/in/somesh-9188",
                                    target="_blank",
                                ),
                                dbc.NavLink(
                                    "😺 GitHub",
                                    href="https://github.com/someshfengde",
                                    target="_blank",
                                ),
                                dbc.NavLink(
                                    "🌐 Portfolio",
                                    href="https://somesh.gitbook.io/somesh-fengade/",
                                    target="_blank",
                                ),
                            ],
                            vertical=True,
                        ),
                        title="My Socials",
                    )
                ],
            ),
        ],
        className="sticky-top vh-100 overflow-scroll",
    )
