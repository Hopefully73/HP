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
            id="dungeon-dropdown",
            options=[
                {"label": "Old Dungeon", "value": "dungeon1"},
                {"label": "Ice Fortress", "value": "dungeon1.5"},
                {"label": "Cursed Crypt", "value": "dungeon2"},
                {"label": "Demonic Castle", "value": "dungeon3"},
                {"label": "Dark Palace", "value": "dungeon4"}
            ],
            persistence=True,
            persistence_type="memory",
            clearable=False,
            placeholder = "Choose one from the list."
        )
    ],
    className="input_div"
)

dungeon_special1_div = html.Div(
    [
        html.H6("Select effect (2nd dungeon special)"),
        dcc.Dropdown(
            id="special1-dropdown",
            options=[],
            persistence=True,
            persistence_type="memory",
            clearable=False,
            placeholder = "Choose one from the list."
        )
    ],
    className="input_div"
)

dungeon_special2_div = html.Div(
    [
        html.H6("Select effect (4th dungeon special)"),
        dcc.Dropdown(
            id="special2-dropdown",
            options=[],
            persistence=True,
            persistence_type="memory",
            clearable=False,
            placeholder = "Choose one from the list."
        )
    ],
    className="input_div"
)

dungeon_special3_div = html.Div(
    [
        html.H6("Select effect (5th dungeon special)"),
        dcc.Dropdown(
            id="special3-dropdown",
            options=[],
            persistence=True,
            persistence_type="memory",
            clearable=False,
            placeholder = "Choose one from the list."
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
                        html.H5("Kindly fill up the dungeon settings below before proceeding.")
                    ],
                    style={"width": "80%", "padding-left": "9%"}
                ),
                dbc.Row(
                    [
                        html.Br(),
                        dbc.Col(dungeon_div, style={"width": "50%"}),
                        dbc.Col(dungeon_special1_div),
                        dbc.Col(dungeon_special2_div),
                        dbc.Col(dungeon_special3_div)
                    ],
                    style={"width": "90%", "padding-left": "9%"}
                )
            ],
            className="header_row",
        )
    ]
)

@app.callback(
    [
        Output("special1-dropdown", "options"),
        Output("special1-dropdown", "value"),
        Output("special2-dropdown", "options"),
        Output("special2-dropdown", "value"),
        Output("special3-dropdown", "options"),
        Output("special3-dropdown", "value")
    ],
    Input("dungeon-dropdown", "value")
)
def dungeon_options(dungeon):
    
    options3 = [
        {"label": "+10% armor break", "value": "armor_br"},
        {"label": "+10% weapon break", "value": "weapon_br"},
        {"label": "+25% chance to attack a 2nd monster", "value": 25}
    ]
    if dungeon == "dungeon1":
        options1 = [
            {"label": "+10% disease chance", "value": "disease"},
            {"label": "+20% monster damage", "value": "monster"},
            {"label": "+15% hero damage", "value": "hero"}
        ]
        options2 = [
            {"label": "+25% monster farm monster damage", "value": "regular"},
            {"label": "+25% undead monster damage", "value": "undead"},
            {"label": "-20% monster damage", "value": "monster"}
        ]
    elif dungeon == "dungeon1.5":
        options1 = [
            {"label": "+25% disease chance", "value": "disease"},
            {"label": "+20% monster damage", "value": "monster"},
            {"label": "+20% hero damage", "value": "hero"}
        ]
        options2 = [
            {"label": "+30% monster farm monster damage", "value": "regular"},
            {"label": "+30% undead monster damage", "value": "undead"},
            {"label": "-25% monster damage", "value": "monster"}
        ]
    elif dungeon == "dungeon2":
        options1 = [
            {"label": "+20% bone fracture chance", "value": "bone"},
            {"label": "+20% monster damage", "value": "monster"},
            {"label": "+15% hero damage", "value": "hero"}
        ]
        options2 = [
            {"label": "+30% disease chance", "value": "disease"},
            {"label": "+25% stone monster damage", "value": "stone"},
            {"label": "-20% monster damage", "value": "monster"}
        ]
    elif dungeon == "dungeon3":
        options1 = [
            {"label": "+25% burn chance", "value": "burn"},
            {"label": "+20% monster damage", "value": "monster"},
            {"label": "+15% hero damage", "value": "hero"}
        ]
        options2 = [
            {"label": "+35% bone fracture chance", "value": "bone"},
            {"label": "+25% fire monster damage", "value": "fire"},
            {"label": "-20% monster damage", "value": "monster"}
        ]
    elif dungeon == "dungeon4":
        options1 = [
            {"label": "+25% disease chance for monster farm monsters", "value": "disease"},
            {"label": "+25% bone fracture chance for monster farm monsters", "value": "bone"},
            {"label": "+20% monster damage", "value": "monster"},
            {"label": "+15% hero damage", "value": "hero"},
            
        ]
        options2 = [
            {"label": "+40% burn chance", "value": "burn"},
            {"label": "+30% monster farm monster damage", "value": "regular"},
            {"label": "-20% monster damage", "value": "monster"}
        ]
    else:
        options1 = []
        options2 = []
        options3 = []
    
    return [options1, None, options2, None, options3, None]

