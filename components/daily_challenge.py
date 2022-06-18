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
                {"label": "Treasures", "value": "treasures"},
                {"label": "Catering", "value": "tavern"},
                {"label": "Weapons", "value": "weapons"},
                {"label": "Armors", "value": "armors"},
                {"label": "Monsters", "value": "monsters"},
                {"label": "Training", "value": "training"},
                {"label": "Temple", "value": "temple"},
                {"label": "Alchemist", "value": "alchemist"}
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
                {"label": "Bronze", "value": "bronze"},
                {"label": "Silver", "value": "silver"},
                {"label": "Gold", "value": "gold"},
                {"label": "Platinum", "value": "platinum"}
            ],
            value="platinum",
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
            placeholder="Enter any positive integer.",
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
            placeholder="Enter any positive integer.",
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
                    dcc.Loading(
                        [], id = "pts-result"
                    ),
                    style = {"textAlign": "center"}
                )
            ],
            className="div-for-sidebar",
            width={"size": 8}
        )
    ]
)

# Callback for the calculate points button
@app.callback(
    Output("pts-result", "children"),
    Input("pts-button", "n_clicks"),
    [
        State("daily-dropdown", "value"),
        State("award-radio", "value"),
        State("total-pts", "value"),
        State("current-score", "value")
    ]
)
def update_pts(n_clicks, daily, award, total, score):
    if n_clicks:
        time.sleep(1)
        inputs = {
            "Daily challenge": daily,
            "Award type": award,
            "Total award points": total,
            "Daily challenge score": score
        }
        if None in list(inputs.values()):
            missing_inputs = [x for x in list(inputs.keys()) if inputs[x] is None]
            error_message = f"Missing inputs: {', '.join(missing_inputs)}"
            return dcc.Markdown(error_message, style={"color": "red"})
        
        if daily == "training":
            base = 50
        elif daily == "temple":
            base = 75
        elif daily in ("alchemist", "tavern", "weapons"):
            base = 100
        elif daily in ("armors", "treasures"):
            base = 125
        else:
            base = 150
            
        
        if award == "bronze":
            mult = 10
        elif award == "silver":
            mult = 5.8
        elif award == "gold":
            mult = 4.2
        else:
            mult = 3.5    
        
        x = ((score * mult) / base) - (max(total, 5000) - 5000) / 20
        
        if x <= 0:
            y = (base / mult) * (1 + ((max(total, 5000) - 5000) / 20))
            result = math.floor(y - score)
            return dcc.Markdown("Improve your score by at least **{:,}** to earn more points.".format(result))
            
        else:
            result = math.floor(x)
            
            if result > 1:
                return dcc.Markdown("You will gain **{:,} points** for your score.".format(result))
            else:
                return dcc.Markdown("You will gain **{:,} point** for your score.".format(result))
        
    else:
        raise PreventUpdate

        