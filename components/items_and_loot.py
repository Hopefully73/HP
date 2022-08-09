import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import dash_bootstrap_components as dbc

import pandas as pd
import numpy as np
import math
import time
import json
from scipy import stats 
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from index import app

df = pd.read_csv("data/items.csv")

shop_div = html.Div(
    [
        html.H6("Choose building"),
        dcc.Dropdown(
            id="shop-dropdown",
            options=[
                {"label": "Alchemist", "value": "alchemist"},
                {"label": "Tavern", "value": "tavern"},
                {"label": "Armor Forge", "value": "armor"},
                {"label": "Weapon Forge", "value": "weapon"},
                {"label": "Magic Shop", "value": "magic"},
                {"label": "Trainer", "value": "trainer"},
                {"label": "Temple", "value": "temple"},
                {"label": "Junk Factory", "value": "loot"}
            ],
            persistence=True,
            persistence_type="memory",
            clearable=False,
            placeholder = "Choose one from the list."
        )
    ],
    className="input_div"
)

item_div = html.Div(
    [
        html.H6("Choose item or loot", id = "item-type-name"),
        dcc.Dropdown(
            id="item-dropdown",
            options=[],
            persistence=True,
            persistence_type="memory",
            placeholder = "Choose one from the list."
        )
    ],
    className="input_div"
)

item_level_div = html.Div(
    [
        html.H6("Maximum item or loot level", id = "item-level-name"),
        dcc.Input(
            id="item-max-level",
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

tips1_div = html.Div(
    [
        html.H6("Employee #1"),
        dcc.Input(
            id="tips1-level",
            type="number",
            min=0,
            max=44,
            value=0,
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

tips2_div = html.Div(
    [
        html.H6("Employee #2"),
        dcc.Input(
            id="tips2-level",
            type="number",
            min=0,
            max=44,
            value=0,
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

tips3_div = html.Div(
    [
        html.H6("Employee #3"),
        dcc.Input(
            id="tips3-level",
            type="number",
            min=0,
            max=44,
            value=0,
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

item_statue_div = html.Div(
    [
        html.H6("Select total gold income bonus (unicorn statue)"),
        dbc.RadioItems(
            options=[
                {"label": "None", "value": 0},
                {"label": "2%", "value": 2},
                {"label": "5%", "value": 5},
                {"label": "10%", "value": 10}
            ],
            value=10,
            id="item-statue-radio",
            inline=True,
            persistence=True,
            persistence_type="memory"
        ),
    ],
    style={'font-family': 'Noto Sans'}
)

item_relics_div = html.Div(
    [
        html.H6("Select activated gold income relic tier(s)"),
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
            id="item-relic-checklist",
            inline=True,
            persistence=True,
            persistence_type="memory"
        )
    ],
    style={'font-family': 'Noto Sans'}
)

loot_special_div = html.Div(
    [
        html.H6(
            [
                html.Span(
                    "Junk factory RP special",
                    id="loot-special-tooltip-target",
                    style={"textDecoration": "underline", "cursor": "pointer"}
                ),
                " bought?"
            ]
        ),
        dbc.Tooltip(
            """+25% RP when bought.""",
            target="loot-special-tooltip-target",
            placement="top"
        ),
        dbc.RadioItems(
            options=[
                {"label": "Yes", "value": 25},
                {"label": "No", "value": 0}
            ],
            value=25,
            id="loot-special-radio",
            inline=True,
            persistence=True,
            persistence_type="memory",
        )
    ]
)

dungeon_loot_div = html.Div(
    [
        html.H6("Select applied dungeon RP bonus"),
        dbc.Checklist(
            options=[],
            id="dungeon-loot-checklist",
            inline=True,
            persistence=True,
            persistence_type="memory",
        ),
    ],
    style={'font-family': 'Noto Sans'}
)

statue_loot_div = html.Div(
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
            id="statue-loot-radio",
            inline=True,
            persistence=True,
            persistence_type="memory"
        ),
    ],
    style={'font-family': 'Noto Sans'}
)

relics_loot_div = html.Div(
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
            id="loot-relic-checklist",
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
                dbc.Col(shop_div),
                dbc.Col(item_div),
                dbc.Col(item_level_div, style={"padding-top": "1%"})
            ]
        ),
        html.Br(),
        html.H6("Employee Tip Bonuses:", id = "item-group1"),
        dbc.Row(
            [
                dbc.Col(tips1_div, id = "tips1-div"),
                dbc.Col(tips2_div, id = "tips2-div"),
                dbc.Col(tips3_div, id = "tips3-div")
            ]
        ),
        html.Br(),
        html.H6("Special Building Bonuses:", id = "item-group2"),
        dbc.Row(
            [
                dbc.Col(item_statue_div, id = "item-statue-div"),
                dbc.Col(item_relics_div, id = "item-relics-div")
            ]
        ),
        dbc.Row(
            [
                dbc.Col(loot_special_div, id = "loot-special-div"),
                dbc.Col(dungeon_loot_div, id = "dungeon-loot-div"),
                dbc.Col(statue_loot_div, id = "statue-loot-div"),
                dbc.Col(relics_loot_div, id = "relics-loot-div")
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [dbc.Button(
                            "Calculate", 
                            id="item-loot-button",
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
                [], id = "item-loot-result"
            ),
            style = {"textAlign": "center"}
        )
    ],
    className="div-for-sidebar"
)

# Callback for the corresponding options for each shop 
@app.callback(
    [
        Output("item-dropdown", "options"),
        Output("item-type-name", "children"),
        Output("item-level-name", "children"),
        Output("item-loot-button", "children")
    ],
    Input("shop-dropdown", "value")
)
def update_item_dropdown(shop):
    
    if shop is None:
        raise PreventUpdate
    
    x = df.query("Shop == @shop")
    shop_type = x["Shop"].unique()
    items = x["Item"].unique()
    options = [{'label': i, 'value': i} for i in items]

    if shop_type == "alchemist":
        return [options, "Choose potion", "Maximum item level", 
                "Calculate item price"]
    elif shop_type == "tavern":
        return [options, "Choose tavern item", "Maximum item level", 
                "Calculate item price"]
    elif shop_type == "armor":
        return [options, "Choose armor", "Maximum item level", 
                "Calculate item price"]
    elif shop_type == "weapon":
        return [options, "Choose weapon", "Maximum item level", 
                "Calculate item price"]
    elif shop_type == "magic":
        return [options, "Choose wand or jewelry", "Maximum item level", 
                "Calculate item price"]
    elif shop_type == "trainer":
        return [options, "Choose training item", "Maximum item level", 
                "Calculate item price"]
    elif shop_type == "temple":
        return [options, "Choose temple item", "Maximum item level", 
                "Calculate item price"]
    else:
        return [options, "Choose loot", "Maximum loot level", "Calculate loot RP"]
        

# Callback for the dungeon loot RP bonus options
@app.callback(
    [
        Output("dungeon-loot-checklist", "options"),
        Output("dungeon-loot-checklist", "value")
    ],
    Input("dungeon-dropdown", "value")
)
def get_dungeon_rp(dungeon):
    if dungeon == "dungeon1":
        options = [
            {"label": "1st special: 20% more RP", "value": 20},
            {"label": "3rd special: 30% more RP", "value": 30}
        ]
        value = [20, 30]
    elif dungeon == "dungeon1.5":
        options = [
            {"label": "1st special: 40% more RP", "value": 40},
            {"label": "3rd special: 50% more RP", "value": 50}
        ]    
        value = [40, 50]
    elif dungeon == "dungeon2":
        options = [
            {"label": "1st special: 30% more RP", "value": 30},
            {"label": "3rd special: 40% more RP", "value": 40}
        ]
        value = [30, 40]
    elif dungeon == "dungeon3":
        options = [
            {"label": "1st special: 40% more RP", "value": 40},
            {"label": "3rd special: 50% more RP", "value": 50}
        ]
        value = [40, 50]
    elif dungeon == "dungeon4":
        options = [
            {"label": "1st special: 50% more RP", "value": 50},
            {"label": "3rd special: 60% more RP", "value": 60}
        ]     
        value = [50, 60]
    else:
        options=[]
        value=""
        
    return [options, value]        


# Callback for the corresponding options for either an item or loot
@app.callback(
    [
        Output("item-group1", "style"),
        Output("tips1-div", "style"),
        Output("tips2-div", "style"),
        Output("tips3-div", "style"),
        Output("item-group2", "style"),
        Output("item-statue-div", "style"),
        Output("item-relics-div", "style"),
        Output("loot-special-div", "style"),
        Output("dungeon-loot-div", "style"),
        Output("statue-loot-div", "style"),
        Output("relics-loot-div", "style")
    ],
    [
        Input("dungeon-dropdown", "value"),
        Input("shop-dropdown", "value"),
    ]
)
def show_options(dungeon, shop):
    if shop == "loot" and dungeon is None:
        return [{'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'},
                {'display': 'none'}, {'display': 'none'}, {'display': 'none'},
                {'display': 'block'}, {'display': 'none'}, {'display': 'block'}, {'display': 'block'}]
    elif shop == "loot" and dungeon is not None:
        return [{'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'},
                {'display': 'none'}, {'display': 'none'}, {'display': 'none'},
                {'display': 'block'}, {'display': 'block'}, {'display': 'block'}, {'display': 'block'}]
    elif shop in ("alchemist", "tavern", "armor", "weapon", "magic", "temple", "trainer"):
        return [{'display': 'block'}, {'display': 'block'}, {'display': 'block'}, {'display': 'block'},
                {'display': 'block'}, {'display': 'block'}, {'display': 'block'},
                {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}]
    else:
        return [{'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'},
                {'display': 'none'}, {'display': 'none'}, {'display': 'none'},
                {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}]
    

# Callback for the item price/gold income values or loot RP
@app.callback(
    Output("item-loot-result", "children"),
    Input("item-loot-button", "n_clicks"),
    [
        State("dungeon-dropdown", "value"),
        State("shop-dropdown", "value"),
        State("item-dropdown", "value"),
        State("item-max-level", "value"),
        State("tips1-level", "value"),
        State("tips2-level", "value"),
        State("tips3-level", "value"),
        State("item-statue-radio", "value"),
        State("item-relic-checklist", "value"),
        State("loot-special-radio", "value"),
        State("dungeon-loot-checklist", "value"),
        State("statue-loot-radio", "value"),
        State("loot-relic-checklist", "value")
    ]
)
def calculate_item_loot(n_clicks, dungeon, shop, item, level, tips1, tips2, tips3, item_statue, 
                        item_relic, special, dungeon_rp, loot_statue, loot_relic):
    if n_clicks:
        time.sleep(1)
        
        if shop == "loot":
            inputs = {
                "Dungeon": dungeon,
                "Loot": item,
                "Maximum loot level": level
            }
        elif shop in ("alchemist", "tavern", "armor", "weapon", "magic", "temple", "trainer"):
            inputs = {
                "Item": item,
                "Maximum item level": level,
                "Employee #1": tips1,
                "Employee #2": tips2,
                "Employee #3": tips3
            }
        else:
            inputs = {
                "Dungeon": dungeon,
                "Building": shop,
                "Item or loot": item
            }
        
        if None in list(inputs.values()):
            missing_inputs = [x for x in list(inputs.keys()) if inputs[x] is None]
            error_message = f"Missing inputs: {', '.join(missing_inputs)}"
            return dcc.Markdown(error_message, style={"color": "red"})
        
        lvl_prog = [1, 1.5, 2, 2.4, 2.8, 3.1, 3.35, 3.6, 3.85, 4.1, 4.3, 4.5, 4.7, 
                    4.9, 5.1, 5.25, 5.4, 5.55, 5.7, 5.85, 6, 6.1, 6.2, 6.3, 6.4, 
                    6.5, 6.6, 6.7, 6.8, 6.9]
        
        if shop == "loot":
            x = df.query("Item == @item")
            base_rp = x["Base"].unique()
            rp_lvl = base_rp * lvl_prog[level - 1]
            
            special_mult = (100 + special) / 100
            dungeon_mult = 1
            if dungeon_rp is None:
                dungeon_mult = 1
            else:    
                for i in dungeon_rp:
                    dungeon_mult = dungeon_mult * ((100 + i) / 100)
            statue_mult = 1 + (loot_statue / 100)
            relics_mult = 1 + (sum(loot_relic) / 100)
            
            rp = rp_lvl * special_mult * dungeon_mult * statue_mult * relics_mult
            rp = math.floor(rp)
            
            return dcc.Markdown("The result is **{:,} RP**.".format(rp))
        else:    
            x = df.query("Item == @item")
            base_price = x["Base"].unique()
            price_lvl = base_price * lvl_prog[level - 1]
            
            tips = (100 + tips1 + tips2 + tips3) / 100
            statue_mult = item_statue / 100
            relics_mult = sum(item_relic) / 100
            
            price = price_lvl * tips
            price = math.floor(price)
            income = price + (price * statue_mult) + (price * relics_mult)
            income = math.floor(income)
            
            return dcc.Markdown("""This item will be sold for **{:,} gold** to heroes.\n
            \nHowever, it will add **{:,} gold** to the total gold income stash.
            """.format(price, income))
    else:
        raise PreventUpdate    

