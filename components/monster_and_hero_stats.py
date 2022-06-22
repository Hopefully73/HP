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

### Monster Section

monster_cat_div = html.Div(
    [
        html.H6("Select monster category"),
        dcc.Dropdown(
            id="monster-cat-dropdown",
            options=[
                {"label": "Regular monsters", "value": "regular"},
                {"label": "Boss monsters", "value": "boss"},
                {"label": "Supervillains", "value": "sv"}
            ],
            persistence=True,
            persistence_type="memory",
            placeholder = "Choose one from the list."
        )
    ],
    className="input_div"
)

monster_type_div = html.Div(
    [
        html.H6("Monster type"),
        dbc.RadioItems(
            options=[
                {"label": "Regular", "value": "regular"},
                {"label": "Undead", "value": "undead"},
                {"label": "Stone", "value": "stone"},
                {"label": "Fire", "value": "fire"},
            ],
            value="fire",
            id="monster-type-radio",
            inline=True,
            persistence=True,
            persistence_type="memory",
        )
    ]
)

monster_level_div = html.Div(
    [
        html.H6("Monster level"),
        dcc.Input(
            id="monster-level",
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

boss_type_div = html.Div(
    [
        html.H6("Boss monster type"),
        dbc.RadioItems(
            options=[
                {"label": "Dragon", "value": "dragon"},
                {"label": "Golem or Mummy", "value": "others"}
            ],
            value="dragon",
            id="boss-type-radio",
            inline=True,
            persistence=True,
            persistence_type="memory",
        )
    ]
)

boss_level_div = html.Div(
    [
        html.H6("Boss monster level"),
        dcc.Input(
            id="boss-monster-level",
            type="number",
            min=26,
            max=59,
            value=50,
            style={
                "width": "60%",
                "height": "25px",
                "lineHeight": "25px",
                "textAlign": "center",
            }
        )
    ]
)

sv_level_div = html.Div(
    [
        html.H6("Supervillain level"),
        dcc.Input(
            id="sv-level",
            type="number",
            min=20,
            max=99,
            value=60,
            style={
                "width": "60%",
                "height": "25px",
                "lineHeight": "25px",
                "textAlign": "center",
            }
        )
    ]
)

dungeon_rp_div = html.Div(
    [
        html.H6("Select applied dungeon RP bonus"),
        dbc.Checklist(
            options=[],
            id="dungeon-rp-checklist",
            inline=True,
            persistence=True,
            persistence_type="memory",
        ),
    ],
    style={'font-family': 'Noto Sans'}
)

statue_rp_div = html.Div(
    [
        html.H6("Select total RP bonus (unicorn statue)"),
        dbc.RadioItems(
            options=[
                {"label": "None", "value": 0},
                {"label": "2%", "value": 2},
                {"label": "5%", "value": 5},
                {"label": "9%", "value": 9}
            ],
            value=9,
            id="statue-rp-radio",
            inline=True,
            persistence=True,
            persistence_type="memory"
        ),
    ],
    style={'font-family': 'Noto Sans'}
)

relics_rp_div = html.Div(
    [
        html.H6("Select activated RP relic tier(s)"),
        dbc.Checklist(
            options=[
                {"label": "Bronze", "value": 1},
                {"label": "Silver", "value": 2},
                {"label": "Gold", "value": 3},
                {"label": "Platinum", "value": 4},
                {"label": "Devilish", "value": 5},
                {"label": "Unicorn", "value": 6}
            ],
            value=[1, 2, 3, 4, 5, 6],
            id="rp-relic-checklist",
            inline=True,
            persistence=True,
            persistence_type="memory"
        )
    ],
    style={'font-family': 'Noto Sans'}
)

prod_building_div = html.Div(
    [
        html.H6("Choose monster production building"),
        dcc.Dropdown(
            id="prod-building-dropdown",
            options=[
                {"label": "Monster Farm", "value": "prod1"},
                {"label": "Graveyard", "value": "prod2"},
                {"label": "Quarry", "value": "prod3"},
                {"label": "Fire Hole", "value": "prod4"},
            ],
            persistence=True,
            persistence_type="memory",
            placeholder = "Choose one from the list."
        )
    ],
    className="input_div"
)

prod_special1_div = html.Div(
    [
        html.H6("Select effect (2nd building special)"),
        dcc.Dropdown(
            id="prod-special1-dropdown",
            options=[],
            persistence=True,
            persistence_type="memory",
            placeholder = "Choose one from the list."
        )
    ]
)

prod_special2_div = html.Div(
    [
        html.H6("Select effect (3rd building special)"),
        dcc.Dropdown(
            id="prod-special2-dropdown",
            options=[],
            persistence=True,
            persistence_type="memory",
            placeholder = "Choose one from the list."
        )
    ]
)

prod_special3_div = html.Div(
    [
        html.H6("Select effect (4th building special)"),
        dcc.Dropdown(
            id="prod-special3-dropdown",
            options=[],
            persistence=True,
            persistence_type="memory",
            placeholder = "Choose one from the list."
        )
    ]
)

### Hero Section

hero_level_div = html.Div(
    [
        html.H6("Hero level"),
        dcc.Input(
            id="hero-level",
            type="number",
            min=1,
            max=35,
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

hero_weapon_div = html.Div(
    [
        html.H6("Bought a weapon/wand before combat?"),
        dbc.RadioItems(
            options=[
                {"label": "Yes", "value": "yes"},
                {"label": "No", "value": "no"}
            ],
            value="no",
            id="hero-weapon-radio",
            inline=True,
            persistence=True,
            persistence_type="memory"
        )
    ]
)

hero_weapon_level_div = html.Div(
    [
        html.H6("Weapon level"),
        dcc.Input(
            id="hero-weapon-level",
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

### Layout

layout = dbc.Container(
    [
        dbc.Row(
            [
               dbc.Col(hero_level_div),
               dbc.Col(hero_weapon_div),
               dbc.Col(hero_weapon_level_div, id = "hero_weapon_level_div"),
               dbc.Col(
                   html.Div(
                       [dbc.Button(
                            "Calculate damage", 
                            id="hero-damage-button",
                            color="primary"
                       )]
                   ),
                   style = {"padding-top": "1%"}
               ),
               dbc.Col(
                   html.Div(
                       dcc.Loading(
                           [], id = "hero-damage-result"
                       )
                   ),
                   style = {"padding-top": "2%"}
               )
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(monster_cat_div)
            ], 
            style={"width": "50%"}
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(monster_type_div, id = "monster_type_div"),
                dbc.Col(monster_level_div, id = "monster_level,div"),
                dbc.Col(boss_type_div, id = "boss_type_div"),
                dbc.Col(boss_level_div, id = "boss_level,div"),
                dbc.Col(sv_level_div, id = "sv_level,div")
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(prod_building_div, id = "prod_building_div"),
                dbc.Col(prod_special1_div, id = "prod_special1_div", style={"padding-top": "1%"}),
                dbc.Col(prod_special2_div, id = "prod_special2_div", style={"padding-top": "1%"}),
                dbc.Col(prod_special3_div, id = "prod_special3_div", style={"padding-top": "1%"})
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(dungeon_rp_div, id = "dungeon_rp_div"),
                dbc.Col(statue_rp_div, id = "statue_rp_div"),
                dbc.Col(relics_rp_div, id = "relics_rp_div")
            ]
        )
    ],
    className="div-for-sidebar"
)

### Monster Callback Sections


### Hero Callback Sections

# Callback for the bought weapon level
@app.callback(
    Output("hero_weapon_level_div", "style"),
    Input("hero-weapon-radio", "value")
)
def show_weapon_level(show):
    if show == "yes":
        return {'display': 'block'}
    else:
        return {'display': 'none'}
    
    
# Callback for the calculate hero damage button
@app.callback(
    Output("hero-damage-result", "children"),
    Input("hero-damage-button", "n_clicks"),
    [
        State("hero-level", "value"),
        State("hero-weapon-radio", "value"),
        State("hero-weapon-level", "value"),
        State("dungeon-dropdown", "value"),
        State("special1-dropdown", "value")
    ]
)
def update_time(n_clicks, level, bought, weapon, dungeon, special1):
    if n_clicks:
        time.sleep(1)
        if bought == "yes":
            inputs = {
                "Hero level": level,
                "Weapon level": weapon,
                "Dungeon": dungeon,
                "2nd dungeon special": special1
            }
        else:
            inputs = {
                "Hero level": level,
                "Dungeon": dungeon,
                "2nd dungeon special": special1
            }    
        
        if None in list(inputs.values()):
            missing_inputs = [x for x in list(inputs.keys()) if inputs[x] is None]
            error_message = f"Missing inputs: {', '.join(missing_inputs)}"
            return dcc.Markdown(error_message, style={"color": "red"})
        
        if dungeon == "dungeon1.5" and special1 == "hero":
            dungeon_mult = 1.2
        elif dungeon != "dungeon1.5" and special1 == "hero":
            dungeon_mult = 1.15
        else:
            dungeon_mult = 1
        
        if bought == "yes":
            weapon_mult = 4 * weapon
        else:
            weapon_mult = 1
            
        if level <= 10:
            x = ((level - 1) * 11) + 25
            dmg = (x + weapon_mult) * dungeon_mult
        else:
            x = ((level - 1) * 13) + 25 + ((level - 10) * 2)
            dmg = (x + weapon_mult) * dungeon_mult
            
        dmg = math.floor(dmg)   
        return dcc.Markdown("The result is **{} damage**.".format(dmg))
        
    else:
        raise PreventUpdate    
            
            