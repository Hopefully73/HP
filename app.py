import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import dash_bootstrap_components as dbc

import numpy as np
import math
import time
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from components import (
    header, production_speed, items_and_loot, daily_challenge, 
    monster_and_hero_stats, break_and_status_effects
)

from index import app, server

tab1_panels = dbc.Container([production_speed.layout])
tab2_panels = dbc.Container([items_and_loot.layout])
tab3_panels = dbc.Container([daily_challenge.layout])
tab4_panels = dbc.Container([monster_and_hero_stats.layout])
tab5_panels = dbc.Container([break_and_status_effects.layout])

tabs_div = html.Div(
    [
        dcc.Tabs(
            id="tabs-with-classes",
            value="tab-1",
            parent_className="custom-tabs",
            className="custom-tabs-container",
            children=[
                dcc.Tab(
                    label="Production Speed",
                    value="tab-1",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Item Prices & Loot RP",
                    value="tab-2",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Daily Challenge",
                    value="tab-3",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Hero & Monster Stats",
                    value="tab-4",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Break & Status Effects",
                    value="tab-5",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                )
            ],
        ),
        html.Div(id="tabs-content-classes"),
    ],
)

app.layout = html.Div(
    [
        header.layout,
        dbc.Row(
            [
                dbc.Col(width={"size": 1}),
                dbc.Col(tabs_div),
            ],
            className="header_row",
        )
    ]
)


@app.callback(
    Output("tabs-content-classes", "children"),
    Input("tabs-with-classes", "value"),
)
def render_content(tab):
    if tab == "tab-5":
        return dbc.Row(
            [
                dbc.Col(
                    html.Div([tab5_panels]),
                    style={"padding-right": "5em"},
                    className="output-container",
                ),
            ]
        )
    elif tab == "tab-4":
        return dbc.Row(
            [
                dbc.Col(
                    html.Div([tab4_panels]),
                    style={"padding-right": "5em"},
                    className="output-container",
                ),
            ]
        )
    elif tab == "tab-3":
        return dbc.Row(
            [
                dbc.Col(
                    html.Div([tab3_panels]),
                    style={"padding-right": "5em"},
                    className="output-container",
                ),
            ]
        )
    elif tab == "tab-2":
        return dbc.Row(
            [
                dbc.Col(
                    html.Div([tab2_panels]),
                    style={"padding-right": "5em"},
                    className="output-container",
                ),
            ]
        )
    else:
        return dbc.Row(
            [
                dbc.Col(
                    html.Div([tab1_panels]),
                    style={"padding-right": "5em"},
                    className="output-container",
                ),
            ]
        )        
    
if __name__ == '__main__':
    app.run_server()
    #app.run_server(debug=True)
