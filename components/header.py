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

from index import app, server

title_div = html.Div(
    [
        html.H6("Hopefully's Dashboard", className="header_caption"),
        html.H1("Fun Flavor Games | Hero Park"),
    ]
)

dungeon_div = html.Div(
    [
        html.H6("Choose dungeon"),
        dcc.Dropdown(
            id="daily-dropdown",
            options=[
                {"label": "Old Dungeon", "value": "dungeon1"},
                {"label": "Ice Fortress", "value": "dungeon1.5"},
                {"label": "Graveyard", "value": "dungeon2"},
                {"label": "Demonic Castle", "value": "dungeon3"},
                {"label": "Dark Palace", "value": "dungeon4"}
            ],
            persistence=True,
            persistence_type="memory",
            placeholder = "Choose one from the list."
        )
    ],
    className="input_div"
)

dungeon_special1_div = html.Div(
    [
        html.H6("Select effect (2nd dungeon special)"),
        dbc.RadioItems(
            options=[],
            id="special1-radio",
            inline=True,
            persistence=True,
            persistence_type="memory"
        )
    ],
    className="input_div"
)

dungeon_special2_div = html.Div(
    [
        html.H6("Select effect (4th dungeon special)"),
        dbc.RadioItems(
            options=[],
            id="special2-radio",
            inline=True,
            persistence=True,
            persistence_type="memory"
        )
    ],
    className="input_div"
)

dungeon_special3_div = html.Div(
    [
        html.H6("Select effect (5th dungeon special)"),
        dbc.RadioItems(
            options=[
                {"label": "+10% armor break", "value": "dungeon.5a"},
                {"label": "+10% weapon break", "value": "dungeon.5b"},
                {"label": "+25% chance to attack a 2nd monster", "value": "dungeon.5c"}
            ],
            id="special3-radio",
            inline=True,
            persistence=True,
            persistence_type="memory"
        )
    ],
    className="input_div"
)

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(width={"size": 1}),
                dbc.Col([title_div], width={"size": 7}),
                dbc.Col(width={"size": 1}),
                html.Br(),
                dbc.Row(
                    [
                        html.Br(),
                        dbc.Col(dungeon_div, style={"width": "50%"}),
                        dbc.Col(dungeon_special1_div),
                        dbc.Col(dungeon_special2_div),
                        dbc.Col(dungeon_special3_div)
                    ],
                    style={"width": "80%", "padding-left": "10%", "padding-top": "1%"}
                )
            ],
            className="header_row",
        )
    ]
)

@app.callback(
    [
        Output("special1-radio", "options"),
        Output("special2-radio", "options")
    ],
    Input("daily-dropdown", "value")
)
def dungeon_options(dungeon):
    
    if dungeon == "dungeon1":
        options1 = [
            {"label": "+10% disease chance", "value": "dungeon1.2a"},
            {"label": "+20% monster damage", "value": "dungeon1.2b"},
            {"label": "+15% hero damage", "value": "dungeon1.2c"}
        ]
        options2 = [
            {"label": "+25% monster farm monster damage", "value": "dungeon1.4a"},
            {"label": "+25% undead monster damage", "value": "dungeon1.4b"},
            {"label": "-20% monster damage", "value": "dungeon1.4c"}
        ]
    elif dungeon == "dungeon1.5":
        options1 = [
            {"label": "+25% disease chance", "value": "dungeon1.5.2a"},
            {"label": "+20% monster damage", "value": "dungeon1.5.2b"},
            {"label": "+20% hero damage", "value": "dungeon1.5.2c"}
        ]
        options2 = [
            {"label": "+30% monster farm monster damage", "value": "dungeon1.5.4a"},
            {"label": "+30% undead monster damage", "value": "dungeon1.5.4b"},
            {"label": "-25% monster damage", "value": "dungeon1.5.4c"}
        ]
    elif dungeon == "dungeon2":
        options1 = [
            {"label": "+20% bone fracture chance", "value": "dungeon2.2a"},
            {"label": "+20% monster damage", "value": "dungeon2.2b"},
            {"label": "+15% hero damage", "value": "dungeon2.2c"}
        ]
        options2 = [
            {"label": "+30% disease chance", "value": "dungeon2.4a"},
            {"label": "+25% stone monster damage", "value": "dungeon2.4b"},
            {"label": "-20% monster damage", "value": "dungeon2.4c"}
        ]
    elif dungeon == "dungeon3":
        options1 = [
            {"label": "+25% burn chance", "value": "dungeon3.2a"},
            {"label": "+20% monster damage", "value": "dungeon3.2b"},
            {"label": "+15% hero damage", "value": "dungeon3.2c"}
        ]
        options2 = [
            {"label": "+35% bone fracture chance", "value": "dungeon3.4a"},
            {"label": "+25% fire monster damage", "value": "dungeon3.4b"},
            {"label": "-20% monster damage", "value": "dungeon3.4c"}
        ]
    elif dungeon == "dungeon4":
        options1 = [
            {"label": "+25% disease chance for monster farm monsters", "value": "dungeon4.2a"},
            {"label": "+25% bone fracture chance for monster farm monsters", "value": "dungeon4.2b"},
            {"label": "+20% monster damage", "value": "dungeon4.2c"},
            {"label": "+15% hero damage", "value": "dungeon4.2d"},
            
        ]
        options2 = [
            {"label": "+40% burn chance", "value": "dungeon4.4a"},
            {"label": "+30% monster farm monster damage", "value": "dungeon4.4b"},
            {"label": "-20% monster damage", "value": "dungeon4.4c"}
        ]
    else:
        options1 = []
        options2 = []
    
    return [options1, options2]



