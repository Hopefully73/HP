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
                {"label": "Armor Break", "value": "armor"},
                {"label": "Weapon Break", "value": "weapon"},
                {"label": "Status Effect", "value": "status"}
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
                {"label": "Armor forge special action", "value": "special"},
                {"label": "Cursed armors", "value": "cursed"},
                {"label": "Devilish statue", "value": "statue"}
            ],
            value=["special", "cursed", "statue"],
            id="armor-br-checklist",
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
                {"label": "Regular weaponry", "value": 0},
                {"label": "Cursed weapons", "value": 25},
                {"label": "Cursed wands", "value": 33}
            ],
            value=33,
            id="weaponry-radio",
            inline=True,
            persistence=True,
            persistence_type="memory"
        ),
    ],
    style={'font-family': 'Noto Sans'}
)

monster_div = html.Div(
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
            id="monster-radio",
            inline=True,
            persistence=True,
            persistence_type="memory",
        )
    ]
)

improved_div = html.Div(
    [
        html.H6("Use improved monsters?"),
        dbc.RadioItems(
            options=[
                {"label": "Yes", "value": 50},
                {"label": "No", "value": 0}
            ],
            value=50,
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
                {"label": "+10% (2nd special)", "value": 10},
                {"label": "+10% (3rd special)", "value": 10},
                {"label": "+10% (4th special)", "value": 10},
            ],
            value=[10, 10, 10],
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
                dbc.Col(armor_br_div, id = "armor-br-div"),
                dbc.Col(weaponry_div, id = "weaponry-div")
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(monster_div, id = "monster-div"),
                dbc.Col(prod_special_div, id = "prod-special-div"),
                dbc.Col(improved_div, id = "improved-div")
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
            dcc.Loading(
                [], id = "effect-final-result"
            ),
            style = {"textAlign": "center"}
        )
    ],
    className="div-for-sidebar"
)


# Callback for armor break sources
@app.callback(
    Output("armor-br-div", "style"),
    Input("effect-dropdown", "value")
)
def show_armor(effect):
    if effect == "armor":
        return {'display': 'block'}
    else:
        return {'display': 'none'}
    
    
# Callback for weapon break sources
@app.callback(
    Output("weaponry-div", "style"),
    Input("effect-dropdown", "value")
)
def show_armor(effect):
    if effect == "weapon":
        return {'display': 'block'}
    else:
        return {'display': 'none'}   
    
    
# Callback for the monster type, improved monsters, and monster production 
# building specials
@app.callback(
    [
        Output("monster-div", "style"),
        Output("prod-special-div", "style"),
        Output("improved-div", "style")
    ],
    Input("effect-dropdown", "value")
)
def show_others(effect):
    if effect == "status":
        return [{'display': 'block'}, {'display': 'block'}, {'display': 'block'}]
    else:
        return [{'display': 'none'}, {'display': 'none'}, {'display': 'none'}]
    
    
# Callback for the effect calculation button
@app.callback(
    Output("effect-final-result", "children"),
    Input("effect-calculate-button", "n_clicks"),
    [
        State("effect-dropdown", "value"),
        State("armor-br-checklist", "value"),
        State("weaponry-radio", "value"),
        State("monster-radio", "value"),
        State("improved-radio", "value"),
        State("prod-special-checklist", "value"),
        State("dungeon-dropdown", "value"),
        State("special1-dropdown", "value"),
        State("special2-dropdown", "value"),
        State("special3-dropdown", "value")
    ]
)
def update_chance(nclicks, effect, armor, weapon, monster, improved,
                  prod, dungeon, special1, special2, special3):
    if nclicks:
        time.sleep(1)
        if effect in ("armor", "weapon"):
            inputs = {
                "5th dungeon special": special3
            }
        else:    
            inputs = {
                "Dungeon": dungeon,
                "Effect category": effect,
                "2nd dungeon special": special1,
                "4th dungeon special": special2,
                "5th dungeon special": special3
            }
        
        if None in list(inputs.values()):
            missing_inputs = [x for x in list(inputs.keys()) if inputs[x] is None]
            error_message = f"Missing inputs: {', '.join(missing_inputs)}"
            return dcc.Markdown(error_message, style={"color": "red"})
            
        if effect == "armor":
            if special3 == "armor_br":
                x = 10
            else:
                x = 0
                
            if "statue" in armor:
                y = 25
            elif "special" in armor and "cursed" in armor:
                y = 99
            elif "special" in armor:
                y = 66
            elif "cursed" in armor:   
                y = 33
            else:
                y = 0
                
            max = x + y
            if max > 100:
                max = 1
            else:
                max = max / 100
                
            base = 1 - ((1 - max) ** (1/3))
            r1 = 1 - (1 - base)
            r2 = 1 - ((1 - base) ** 2)
            return dcc.Markdown("""Armor break chance per round:\n
            \nRound 1: {:.2f}%\n
            \nRound 2: {:.2f}%\n
            \nRound 3: {:.2f}%""".format(r1 * 100, r2 * 100, max * 100))
        
        elif effect == "weapon":
            if special3 == "weapon_br":
                x = 10
            else:
                x = 0    
                
            max = (x + weapon) / 100
            base = 1 - ((1 - max) ** (1/3)) 
            r1 = 1 - (1 - base)
            r2 = 1 - ((1 - base) ** 2)
            return dcc.Markdown("""Weapon break chance per round:\n
            \nRound 1: {:.2f}%\n
            \nRound 2: {:.2f}%\n
            \nRound 3: {:.2f}%""".format(r1 * 100, r2 * 100, max * 100))
            
        else:    
            return dcc.Markdown("""TBD""")
        
    else:
        raise PreventUpdate
        
        