import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash_table.Format import Format, Scheme, Group
import dash_bootstrap_components as dbc

import pandas as pd
import numpy as np
import math
import time
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from index import app, server
from components import functions

effect_div = html.Div(
    [
        html.H6("Select category"),
        dcc.Dropdown(
            id="effect-dropdown",
            options=[
                {"label": "Armor Break", "value": "Armor"},
                {"label": "Weapon Break", "value": "Weapon"},
                {"label": "Status Effect", "value": "Status"}
            ],
            persistence=True,
            persistence_type="memory",
            placeholder = "Choose one from the list."
        )
    ],
    className="input_div"
)

armor_br_div = html.Div(
    [
        html.H6("Select applied source(s)"),
        dbc.Checklist(
            options=[
                {"label": "Dungeon level 10 special", "value": "dungeon"},
                {"label": "Armor forge special action", "value": "special"},
                {"label": "Cursed armors", "value": "cursed"}
            ],
            value=["dungeon", "special", "cursed"],
            id="armor-br-checklist",
            inline=True,
            persistence=True,
            persistence_type="memory",
        ),
    ],
    style={'font-family': 'Noto Sans'}
)

weapon_br_div = html.Div(
    [
        html.H6("Select applied source(s)"),
        dbc.Checklist(
            options=[
                {"label": "Dungeon level 10 special", "value": "dungeon"},
                {"label": "Cursed weapons/wands", "value": "cursed"}
            ],
            value=["dungeon", "cursed"],
            id="weapon-br-checklist",
            inline=True,
            persistence=True,
            persistence_type="memory",
        ),
    ],
    style={'font-family': 'Noto Sans'}
)

weaponry_div = html.Div(
    [
        html.H6("Choose weaponry"),
        dbc.RadioItems(
            options=[
                {"label": "Cursed weapons", "value": "weapon"},
                {"label": "Cursed wands", "value": "wand"}
            ],
            value="weapon",
            id="weaponry-radio",
            inline=True,
            persistence=True,
            persistence_type="memory"
        ),
    ],
    style={'font-family': 'Noto Sans'}
)

improved_div = html.Div(
    [
        html.H6("Use improved monsters?"),
        dbc.RadioItems(
            options=[
                {"label": "Yes", "value": "yes"},
                {"label": "No", "value": "no"}
            ],
            value="yes",
            id="improved-radio",
            inline=True,
            persistence=True,
            persistence_type="memory",
        )
    ]
)

prod_special_div = html.Div(
    [
        html.H6("Select additional status effect chance(s)"),
        dbc.Checklist(
            options=[
                {"label": "+10% (2nd special)", "value": "chance1"},
                {"label": "+10% (3rd special)", "value": "chance2"},
                {"label": "+10% (4th special)", "value": "chance3"},
            ],
            value=["chance1", "chance2", "chance3"],
            id="prod-special-checklist",
            inline=True,
            persistence=True,
            persistence_type="memory"
        )
    ],
    style={'font-family': 'Noto Sans'}
)

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(effect_div)
            ], 
            style={"width": "50%"}
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(armor_br_div),
                dbc.Col(weapon_br_div)
                
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                #dbc.Col(weaponry_div),
                dbc.Col(improved_div),
                dbc.Col(prod_special_div),
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [dbc.Button(
                            "Calculate effect chance per round", 
                            id="effect-calculate-button",
                            color="primary"
                        )],
                        style = {"textAlign": "center"}
                    )
                )
            ]
        ),
        html.Br(),
        html.Div(
            [
                dcc.Markdown("""TBD""", id = "effect-final-result")
            ],
            style = {"textAlign": "center"}
        ),
        html.Br(),
        html.Br(),
        html.Br()
    ],
    className="div-for-sidebar"
)

