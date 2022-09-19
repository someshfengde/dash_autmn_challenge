import dash
from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import dash_daq as daq
import plotly.graph_objects as go

dash.register_page(__name__, path="/")

# reading the data
data = pd.read_csv("./data/liquor_iowa_2021.csv")
data["day"] = data["date"].apply(lambda x: pd.to_datetime(x).day_name())
data["week"] = data["date"].apply(lambda x: pd.to_datetime(x).week)

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown("""## 🍷 Retail Revenue by County"""),
                        # select the no of counties to visualize
                        dbc.Row(
                            [
                                dbc.Col(
                                    dcc.Markdown(
                                        """### Select the no of counties to visualize"""
                                    ),
                                    width=8,
                                ),
                                dbc.Col(
                                    daq.NumericInput(
                                        min=10,
                                        max=120,
                                        value=50,
                                        id="no_counties",
                                    ),
                                    width=4,
                                ),
                            ]
                        ),
                        dcc.Graph(id="county_revenue"),
                    ],
                    width=6,
                ),
                dbc.Col(
                    [
                        dcc.Markdown("""## 🍷 Visualizations based on Bottles Sold"""),
                        dbc.Row(
                            [
                                dbc.Col(
                                    dcc.Dropdown(
                                        options=[
                                            "state_bottle_retail",
                                            "state_bottle_cost",
                                            "bottle_volume_ml",
                                            "pack",
                                        ],
                                        value="state_bottle_cost",
                                        id="bottle_select_dropdown",
                                    ),
                                    width=10,
                                ),
                                dbc.Col(
                                    daq.ToggleSwitch(
                                        label="County color",
                                        labelPosition="bottom",
                                        id="county_color_switch",
                                    ),
                                    width=2,
                                ),
                            ]
                        ),
                        dcc.Graph(id="bottles_sold"),
                    ],
                    width=6,
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown("### 🍷 Sales by day/week of the month"),
                        dbc.Row(
                            [
                                dbc.Col(dcc.Markdown("### Day/Week switch"), width=2),
                                dbc.Col(daq.ToggleSwitch(
                                    # label="Day/ Week switch",
                                    id="day_or_week_switch",
                                ),)
                            ]
                        ),
                        dcc.Graph(id="day_week_sales"),
                    ],
                    width=6,
                ),
                dbc.Col(html.Div("Another div")),
            ]
        ),
        dcc.Markdown(
            """
    ## Dataset description
    Dataset provides us information about the **Alcohol sales in Lowa state** .

    This dataset contains spirit purchase info of lowa Class `E` liquor licences by product 
    and date of purchase from Dec 2020 to Nov 2021.
    """
        ),
    ], 
    fluid = True, 
    className = "dbc"
)


@callback(
    [Output("county_revenue", "figure"), Output("bottles_sold", "figure")],
    Input("no_counties", "value"),
    Input("bottle_select_dropdown", "value"),
    Input("county_color_switch", "value"),
)
def show_retail_revenue(no_counties, value, color_switch):
    # top 50 counties by revenue
    # preparing data for county wise sale dollers
    county_data = data.groupby("county")["sale_dollars"].sum().reset_index()
    county_data = county_data.sort_values(by="sale_dollars", ascending=False)
    county_revenue = go.Figure(px.histogram(county_data[:no_counties], "county", "sale_dollars", color = "county"))
    if color_switch:
        bottles_sold = px.scatter(data, "bottles_sold", value, color="county")
    else:
        bottles_sold = px.scatter(data, "bottles_sold", value)
    return county_revenue, bottles_sold


@callback(
    Output("day_week_sales", "figure"),
    Input("day_or_week_switch", "value")
)
def display_counties_sales(day_week_switch):
    if day_week_switch:
        # finding the day 
        total_sales_day = pd.DataFrame(["Day", "sales"])
        total_sales_day = data.groupby("day")["sale_dollars"].sum().reset_index()
        cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        final_data_total_sale = pd.DataFrame({"Day":cats, "sales":total_sales_day["sale_dollars"]})
        fig = px.bar(final_data_total_sale, x="Day", y="sales",color = "Day", title="Total sales by day")
        
    else:
        total_sales_day = pd.DataFrame(["week", "sales"])
        total_sales_day = data.groupby("week")["sale_dollars"].sum().reset_index()
        final_data_total_sale = pd.DataFrame({"week":total_sales_day["week"], "sales":total_sales_day["sale_dollars"]})
        fig = go.Figure(px.bar(final_data_total_sale, x="week", y="sales", color = "sales"))
        # setting y range to 50000 plus 
        fig.update_yaxes(range=[50000,250000])
    return fig
