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

building_div = html.Div(
    [
        html.H6("Choose building or unicorn food"),
        dcc.Dropdown(
            id="building-dropdown",
            options=[
                {"label": "Alchemist", "value": "Alchemist"},
                {"label": "Tavern", "value": "Tavern"},
                {"label": "Armor Forge", "value": "Armor Forge"},
                {"label": "Weapon Forge", "value": "Weapon Forge"},
                {"label": "Magic Shop", "value": "Magic Shop"},
                {"label": "Trainer", "value": "Trainer"},
                {"label": "Temple", "value": "Temple"},
                {"label": "Junk Factory", "value": "Junk Factory"},
                {"label": "Monster Farm", "value": "Monster Farm"},
                {"label": "Graveyard", "value": "Graveyard"},
                {"label": "Quarry", "value": "Quarry"},
                {"label": "Fire Hole", "value": "Fire Hole"},
                {"label": "Unicorn Food", "value": "Unicorn Food"},
            ],
            persistence=True,
            persistence_type="memory",
            placeholder = "Choose one from the list."
        )
    ],
    className="input_div",
)

building_level_div = html.Div(
    [
        html.H6("Buiding level"),
        dcc.Input(
            id="building-level",
            type="number",
            min=1,
            max=25,
            value=20,
            style={
                "width": "60%",
                "height": "25px",
                "lineHeight": "25px",
                "textAlign": "center",
            }
        )
    ]
)

building_special_div = html.Div(
    [
        html.H6("Building production speed special bought?"),
        dbc.RadioItems(
            options=[
                {"label": "Yes", "value": "yes"},
                {"label": "No", "value": "no"}
            ],
            value="yes",
            id="building-special-radio",
            inline=True,
            persistence=True,
            persistence_type="memory",
        )
    ]
)

food_level_div = html.Div(
    [
        html.H6("Unicorn food level"),
        dcc.Input(
            id="food-level",
            type="number",
            min=1,
            max=38,
            value=38,
            style={
                "width": "60%",
                "height": "25px",
                "lineHeight": "25px",
                "textAlign": "center",
            }
        )
    ]
)

prod1_div = html.Div(
    [
        html.H6("Employee #1"),
        dcc.Input(
            id="prod1-level",
            type="number",
            min=0,
            max=88,
            value=0,
            step=2,
            style={
                "width": "60%",
                "height": "25px",
                "lineHeight": "25px",
                "textAlign": "center",
            }
        )
    ]
)

prod2_div = html.Div(
    [
        html.H6("Employee #2"),
        dcc.Input(
            id="prod2-level",
            type="number",
            min=0,
            max=88,
            value=0,
            step=2,
            style={
                "width": "60%",
                "height": "25px",
                "lineHeight": "25px",
                "textAlign": "center",
            }
        )
    ]
)

prod3_div = html.Div(
    [
        html.H6("Employee #3"),
        dcc.Input(
            id="prod3-level",
            type="number",
            min=0,
            max=88,
            value=0,
            step=2,
            style={
                "width": "60%",
                "height": "25px",
                "lineHeight": "25px",
                "textAlign": "center",
            }
        )
    ]
)

unicorn_statue_div = html.Div(
    [
        html.H6("Select bonus from unicorn statue"),
        dbc.RadioItems(
            options=[
                {"label": "5%", "value": 5},
                {"label": "10%", "value": 10},
                {"label": "15%", "value": 15},
                {"label": "20%", "value": 20}
            ],
            value=20,
            id="statue-prod-bonus-radio",
            inline=True,
            persistence=True,
            persistence_type="memory"
        ),
    ],
    style={'font-family': 'Noto Sans'}
)

relics_div = html.Div(
    [
        html.H6("Select activated production relic tier(s)"),
        dbc.Checklist(
            options=[
                {"label": "Bronze", "value": 5},
                {"label": "Silver", "value": 10},
                {"label": "Gold", "value": 15},
                {"label": "Platinum", "value": 20},
                {"label": "Devilish", "value": 25},
                {"label": "Unicorn", "value": 30}
            ],
            value=[5, 10, 15, 20, 25, 30],
            id="relic-prod-bonus-checklist",
            inline=True,
            persistence=True,
            persistence_type="memory"
        )
    ],
    style={'font-family': 'Noto Sans'}
)

perk_div = html.Div(
    [
        html.H6("Double production speed perk activated?"),
        dbc.RadioItems(
            options=[
                {"label": "Yes", "value": "yes"},
                {"label": "No", "value": "no"}
            ],
            value="yes",
            id="perk-radio",
            inline=True,
            persistence=True,
            persistence_type="memory",
        )
    ]
)

dragons_div = html.Div(
    [
        html.H6("Producing dragons?"),
        dbc.RadioItems(
            options=[
                {"label": "Yes", "value": "yes"},
                {"label": "No", "value": "no"}
            ],
            value="yes",
            id="dragons-radio",
            inline=True,
            persistence=True,
            persistence_type="memory",
        )
    ]
)

dsil_div = html.Div(
    [
        html.H6("Dragon's sister-in-law assigned in the fire hole?"),
        dbc.RadioItems(
            options=[
                {"label": "Yes", "value": "yes"},
                {"label": "No", "value": "no"}
            ],
            value="yes",
            id="dsil-radio",
            inline=True,
            persistence=True,
            persistence_type="memory",
        )
    ]
)

min_level_div = html.Div(
    [
        html.H6("Minimum skill level"),
        dcc.Input(
            id="min-level",
            type="number",
            min=1,
            max=30,
            value=1,
            style={
                "width": "60%",
                "height": "25px",
                "lineHeight": "25px",
                "textAlign": "center",
            }
        )
    ]
)

max_level_div = html.Div(
    [
        html.H6("Maximum skill level"),
        dcc.Input(
            id="max-level",
            type="number",
            min=1,
            max=30,
            value=25,
            style={
                "width": "60%",
                "height": "25px",
                "lineHeight": "25px",
                "textAlign": "center",
            }
        )
    ]
)

desired_level_div = html.Div(
    [
        html.H6("Minimum desired level to retain"),
        dcc.Input(
            id="desired-level",
            type="number",
            min=1,
            max=30,
            value=24,
            style={
                "width": "60%",
                "height": "25px",
                "lineHeight": "25px",
                "textAlign": "center",
            }
        )
    ]
)

slots_div = html.Div(
    [
        html.H6("Total number of slots to fill"),
        dcc.Input(
            id="slots",
            type="number",
            min=1,
            value=20,
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
        dbc.Row(
            [
                dbc.Col(building_div),
                dbc.Col(building_level_div, style={"padding-top": "1%", "padding-left": "5%"}),
                dbc.Col(building_special_div, style={"padding-top": "1%"}),
                dbc.Col(max_level_div, style={"padding-top": "1%"}),
                dbc.Col(food_level_div, style={"padding-top": "1%"})
            ]
        ),
        html.Br(),
        html.H6("Employee Production Speed Bonuses:"),
        dbc.Row(
            [
                dbc.Col(prod1_div),
                dbc.Col(prod2_div),
                dbc.Col(prod3_div)
            ]
        ),
        html.Br(),
        html.Br(),
        html.H6("Special Building Bonuses:"),
        dbc.Row(
            [
                dbc.Col(unicorn_statue_div),
                dbc.Col(relics_div),
                dbc.Col(perk_div)
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(dragons_div),
                dbc.Col(dsil_div)
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [dbc.Button(
                            "Calculate final production time", 
                            id="prod-calculate-button",
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
                dcc.Markdown("""TBD""", id = "prod-final-result")
            ],
            style = {"textAlign": "center"}
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(min_level_div),
                dbc.Col(desired_level_div),
                dbc.Col(slots_div),
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [dbc.Button(
                            "Determine expected preparation time", 
                            id="expected-time-button",
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
                dcc.Markdown("""TBD""", id = "expected-time-result")
            ],
            style = {"textAlign": "center"}
        ),
        html.Br(),
        html.Br(),
        html.Br()
    ],
    className="div-for-sidebar"
)


