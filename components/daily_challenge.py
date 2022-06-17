import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import dash_bootstrap_components as dbc

import pandas as pd
import numpy as np
import math
import time
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from index import app
from components import functions

daily_div = html.Div(
    [
        html.H6("Choose daily challenge"),
        dcc.Dropdown(
            id="daily-dropdown",
            options=[
                {"label": "Treasures", "value": "Treasures"},
                {"label": "Catering", "value": "Catering"},
                {"label": "Weapons", "value": "Weapons"},
                {"label": "Armors", "value": "Armors"},
                {"label": "Monsters", "value": "Monsters"},
                {"label": "Training", "value": "Training"},
                {"label": "Temple", "value": "Temple"},
                {"label": "Alchemist", "value": "Alchemist"}
            ],
            persistence=True,
            persistence_type="memory",
            placeholder = "Choose one from the list."
        )
    ],
    className="input_div"
)

award_div = html.Div(
    [
        html.H6("Select award"),
        dbc.RadioItems(
            options=[
                {"label": "Bronze", "value": "Bronze"},
                {"label": "Silver", "value": "Silver"},
                {"label": "Gold", "value": "Gold"},
                {"label": "Platinum", "value": "Platinum"}
            ],
            value="Platinum",
            id="award-radio",
            inline=True,
            persistence=True,
            persistence_type="memory"
        )
    ],
    className="input_div",
)

total_pts_div = html.Div(
    [
        html.H6("Total award points"),
        dcc.Input(
            id="total-pts",
            type="number",
            min=0,
            value=0,
            style={
                "width": "60%",
                "height": "25px",
                "lineHeight": "25px",
                "textAlign": "center",
            }
        )
    ]
)

current_score_div = html.Div(
    [
        html.H6("Daily challenge score"),
        dcc.Input(
            id="current-score",
            type="number",
            min=0,
            value=0,
            style={
                "width": "60%",
                "height": "25px",
                "lineHeight": "25px",
                "textAlign": "center",
            }
        )
    ]
)

layout = dbc.Container(
    [
        dbc.Col(
            [
                dbc.Row(
                    [
                        dbc.Col(daily_div),
                    ], 
                    style = {"width": "50%"}
                ),
                html.H6(""),
                dbc.Row(
                    [
                        dbc.Col(award_div),
                    ]
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(total_pts_div),
                        dbc.Col(current_score_div)
                    ]
                ),
                html.Br(),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                [dbc.Button(
                                    "Calculate points", 
                                    id="pts-button",
                                    color="primary")],
                                style = {"textAlign": "center"}
                            )
                        )
                    ]
                ),
                html.Br(),
                html.Div(
                    [
                        dcc.Markdown("""TBD""", id = "pts-result")
                    ],
                    style = {"textAlign": "center"}
                ),
                html.Br(),
                html.Br(),
                html.Br()
            ],
            className="div-for-sidebar",
            width={"size": 8}
        )
    ]
)