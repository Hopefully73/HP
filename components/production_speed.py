import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import dash_bootstrap_components as dbc

import pandas as pd
import numpy as np
import math
import time
from scipy import stats 
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
                {"label": "Alchemist", "value": "alchemist"},
                {"label": "Tavern", "value": "tavern"},
                {"label": "Armor Forge", "value": "armor"},
                {"label": "Weapon Forge", "value": "weapon"},
                {"label": "Magic Shop", "value": "magic"},
                {"label": "Trainer", "value": "trainer"},
                {"label": "Temple", "value": "temple"},
                {"label": "Junk Factory", "value": "loot"},
                {"label": "Monster Farm", "value": "monster1"},
                {"label": "Graveyard", "value": "monster2"},
                {"label": "Quarry", "value": "monster3"},
                {"label": "Fire Hole", "value": "monster4"},
                {"label": "Unicorn Food", "value": "food"},
            ],
            persistence=True,
            persistence_type="memory",
            placeholder = "Choose one from the list."
        )
    ],
    className="input_div"
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
                {"label": "Yes", "value": 50},
                {"label": "No", "value": 0}
            ],
            value=50,
            id="building-special-radio",
            inline=True,
            persistence=True,
            persistence_type="memory",
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
            persistence=True,
            persistence_type="memory",
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
            persistence=True,
            persistence_type="memory",
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
            persistence=True,
            persistence_type="memory",
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
                {"label": "None", "value": 0},
                {"label": "5%", "value": 5},
                {"label": "10%", "value": 10},
                {"label": "15%", "value": 15},
                {"label": "20%", "value": 20}
            ],
            value=20,
            id="statue-radio",
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
            id="relic-checklist",
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
                {"label": "Yes", "value": 2},
                {"label": "No", "value": 1}
            ],
            value=2,
            id="perk-radio",
            inline=True,
            persistence=True,
            persistence_type="memory",
        )
    ]
)

dsil_div = html.Div(
    [
        html.H6("Producing dragons and Dragon's sister-in-law assigned?"),
        dbc.RadioItems(
            options=[
                {"label": "Yes", "value": 2},
                {"label": "No", "value": 1}
            ],
            value=2,
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
            value=17,
            persistence=True,
            persistence_type="memory",
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
            persistence=True,
            persistence_type="memory",
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
            persistence=True,
            persistence_type="memory",
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
                dbc.Col(building_special_div, style={"padding-top": "1%"}, id = "building-special-div"),
                dbc.Col(max_level_div, style={"padding-top": "1%"})
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
                dbc.Col(relics_div, id = "relics-div"),
                dbc.Col(perk_div, id = "perk-div")
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(dsil_div, id = "dsil-div")
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
            dcc.Loading(
                None, id = "prod-final-result"
            ),
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
            dcc.Loading(
                [], id = "expected-time-result"
            ),
            style = {"textAlign": "center"}
        )
    ],
    className="div-for-sidebar"
)

# Callback for the building production speed special
@app.callback(
    Output("building-special-div", "style"),
    Input("building-dropdown", "value")
)
def show_building_special(building):
    if building in ("alchemist", "tavern", "armor", "weapon", "magic"):
        return {'display': 'block'}
    else:
        return {'display': 'none'}   
    
    
# Callback for the production speed relics
@app.callback(
    Output("relics-div", "style"),
    Input("building-dropdown", "value")
)
def show_relic_special(building):
    if building in ("trainer", "temple", "monster1", "monster2", "monster3", "monster4"):
        return {'display': 'block'}
    else:
        return {'display': 'none'}      
    
    
# Callback for the double production speed perk
@app.callback(
    Output("perk-div", "style"),
    Input("building-dropdown", "value")
)
def show_relic_special(building):
    if building != "food":
        return {'display': 'block'}
    else:
        return {'display': 'none'}    

    
# Callback for DSiL's double production speed legendary feature on dragons
@app.callback(
    Output("dsil-div", "style"),
    Input("building-dropdown", "value")
)
def show_relic_special(building):
    if building == "monster4":
        return {'display': 'block'}
    else:
        return {'display': 'none'}
    

# Callback for the max possible value for the maximum skill level
@app.callback(
    Output("max-level", "max"),
    Input("building-dropdown", "value")
)
def update_max(building):
    if building == "food":
        max = 38
        return max
    else:
        max = 30
        return max

    
# Callback for the calculate final production time button
@app.callback(
    Output("prod-final-result", "children"),
    Input("prod-calculate-button", "n_clicks"),
    [
        State("building-dropdown", "value"),
        State("building-level", "value"),
        State("building-special-radio", "value"),
        State("max-level", "value"),
        State("prod1-level", "value"),
        State("prod2-level", "value"),
        State("prod3-level", "value"),
        State("statue-radio", "value"),
        State("relic-checklist", "value"),
        State("perk-radio", "value"),
        State("dsil-radio", "value")
    ]
)
def update_time(n_clicks, building, b_level, b_special, maxi, prod1, prod2, prod3,
               statue, relic, perk, dsil):
    if n_clicks:
        time.sleep(1)
        inputs = {
            "Building or unicorn food": building,
            "Building level": b_level,
            "Maximum skill level": max,
            "Employee #1": prod1,
            "Employee #2": prod2,
            "Employee #3": prod3
        }
        if None in list(inputs.values()):
            missing_inputs = [x for x in list(inputs.keys()) if inputs[x] is None]
            error_message = f"Missing inputs: {', '.join(missing_inputs)}"
            return dcc.Markdown(error_message, style={"color": "red"}), None
        
        base = [2, 4, 6, 8, 10, 12.5, 15, 17.5, 20, 22.5, 25, 27, 29,
                31, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
        
        x = b_level - 10 + 1
        if x < 1:
            b_prod = 0
        else:
            b_prod = x * 5
            
        prod = prod1 + prod2 + prod3    
        relics = sum(relic)
        
        if building in ("armor", "weapon", "magic"):
            base_prod = base[maxi - 1] * 1.5
            final_prod = (base_prod / ((100 + b_prod + b_special + prod + statue) / 100)) / perk
            
        elif building == "monster3":
            base_prod = base[maxi - 1] * 1.5
            final_prod = (base_prod / ((100 + b_prod + prod + statue) / 100)) / perk
            
        elif building in ("temple", "trainer"):    
            base_prod = base[maxi - 1] * 2
            final_prod = (base_prod / ((100 + b_prod + prod + relics + statue) / 100)) / perk
            
        elif building == "monster4":
            base_prod = base[maxi - 1] * 2
            final_prod = (base_prod / ((100 + b_prod + prod + relics + statue) / 100)) / (perk * dsil)
            
        elif building == "food":
            base_prod = 3600 - ((maxi - 1) * 45)
            final_prod = (base_prod / ((100 + b_prod + prod + statue) / 100))
           
        elif building in ("alchemist", "tavern"):
            base_prod = base[maxi - 1]
            final_prod = (base_prod / ((100 + b_prod + b_special + prod + statue) / 100)) / perk
            
        else:
            base_prod = base[maxi - 1]
            final_prod = (base_prod / ((100 + b_prod + prod + statue) / 100)) / perk
            
        final_time = final_prod / 60
        minutes = int(final_time)
        seconds = final_prod % 60
        if minutes == 1:
            return dcc.Markdown("The result is **1 minute and {:.0f} seconds**.".format(seconds))
        elif minutes > 1:
            return dcc.Markdown("The result is **{} minutes and {:.0f} seconds**.".format(minutes, seconds))
        else:
            return dcc.Markdown("The result is **{:.2f} seconds**.".format(final_prod))
            
    else:
        raise PreventUpdate

        
# Callback for the expected production time button
@app.callback(
    Output("expected-time-result", "children"),
    Input("expected-time-button", "n_clicks"),
    [
        State("prod-final-result", "children"),
        State("building-dropdown", "value"),
        State("building-level", "value"),
        State("building-special-radio", "value"),
        State("max-level", "value"),
        State("prod1-level", "value"),
        State("prod2-level", "value"),
        State("prod3-level", "value"),
        State("statue-radio", "value"),
        State("relic-checklist", "value"),
        State("perk-radio", "value"),
        State("dsil-radio", "value"),
        State("min-level", "value"),
        State("desired-level", "value"),
        State("slots", "value")
    ]
)
def update_time(n_clicks, result, building, b_level, b_special, maxi, prod1, prod2, prod3,
               statue, relic, perk, dsil, mini, desired, slots):
    if n_clicks:
        time.sleep(1)
        inputs = {
            "Minimum skill level": mini,
            "Desired level": desired,
            "Slots": slots
        }
        if result is None:
            return dcc.Markdown("Please calculate the final production time first.", 
                                style={"color": "red"})
        
        if None in list(inputs.values()):
            missing_inputs = [x for x in list(inputs.keys()) if inputs[x] is None]
            error_message = f"Missing inputs: {', '.join(missing_inputs)}"
            return dcc.Markdown(error_message, style={"color": "red"})
        
        base = [2, 4, 6, 8, 10, 12.5, 15, 17.5, 20, 22.5, 25, 27, 29,
                31, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
        
        x = b_level - 10 + 1
        if x < 1:
            b_prod = 0
        else:
            b_prod = x * 5
            
        prod = prod1 + prod2 + prod3    
        relics = sum(relic)
        
        if building in ("armor", "weapon", "magic"):
            base_prod = base[maxi - 1] * 1.5
            final_prod = (base_prod / ((100 + b_prod + b_special + prod + statue) / 100)) / perk
            
        elif building == "monster3":
            base_prod = base[maxi - 1] * 1.5
            final_prod = (base_prod / ((100 + b_prod + prod + statue) / 100)) / perk
            
        elif building in ("temple", "trainer"):    
            base_prod = base[maxi - 1] * 2
            final_prod = (base_prod / ((100 + b_prod + prod + relics + statue) / 100)) / perk
            
        elif building == "monster4":
            base_prod = base[maxi - 1] * 2
            final_prod = (base_prod / ((100 + b_prod + prod + relics + statue) / 100)) / (perk * dsil)
            
        elif building == "food":
            base_prod = 3600 - ((maxi - 1) * 45)
            final_prod = (base_prod / ((100 + b_prod + prod + statue) / 100))
           
        elif building in ("alchemist", "tavern"):
            base_prod = base[maxi - 1]
            final_prod = (base_prod / ((100 + b_prod + b_special + prod + statue) / 100)) / perk
            
        else:
            base_prod = base[maxi - 1]
            final_prod = (base_prod / ((100 + b_prod + prod + statue) / 100)) / perk
            
        x = maxi - desired + 1
        n = maxi - mini + 1
        prob = x / n
        estimate = (1 / prob) * final_prod * slots
        
        estimate_time = estimate / 60
        estimate_minutes = int(estimate_time)
        estimate_seconds = final_prod % 60
        
        # F distribution
        a = stats.f.ppf(0.10, 2*x, 2*(n - x + 1)) 
        b = stats.f.ppf(0.90, 2*(x + 1), 2*(n - x))
        
        # https://www.danielsoper.com/statcalc/formulas.aspx?id=85
        c = (1 + ((n - x + 1) / (x * a)))**-1
        d = (1 + ((n - x) / ((x + 1) * b)))**-1
        
        lcl = (1 / c) * final_prod * slots  # lower limit
        lcl_time = lcl / 60
        lcl_minutes = int(lcl_time)
        lcl_seconds = final_prod % 60
        
        ucl = (1 / d) * final_prod * slots  # upper limit
        ucl_time = ucl / 60
        ucl_minutes = int(ucl_time)
        ucl_seconds = final_prod % 60
        
        return dcc.Markdown("""The expected total preparation time is around **{} minutes and {:.0f} seconds**.\n
        \nThe 90% confidence interval for this result is between **{} minutes and {:.0f} seconds** until
        **{} minutes and {:.0f} seconds**.""".format(estimate_minutes, estimate_seconds, ucl_minutes, ucl_seconds,
                                                 lcl_minutes, lcl_seconds))
            
    else:
        raise PreventUpdate