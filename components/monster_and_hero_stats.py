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

df = pd.read_csv("data/monsters.csv")
x = df["Monster"]

### Hero Section

hero_level_div = html.Div(
    [
        html.H6("Hero level"),
        dcc.Input(
            id="hero-level",
            type="number",
            min=1,
            max=35,
            value=30,
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

get_monster_div = html.Div(
    [
        html.H6("Select monster"),
        dcc.Dropdown(
            id="monster-dropdown",
            options=[{'label': i, 'value': i} for i in x],
            persistence=True,
            persistence_type="memory",
            placeholder = "Choose one from the list."
        )
    ],
    className="input_div"
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
                "textAlign": "center"
            }
        )
    ]
)

boss_monster_div = html.Div(
    [
        html.H6(
            [
                "Select ", 
                html.Span(
                    "boss monster",
                    id="boss-monster-tooltip-target",
                    style={"textDecoration": "underline", "cursor": "pointer"}
                )
            ]
        ),
        dbc.Tooltip(
            """The golem king and mummy king have slightly higher life and RP.""",
            target="boss-monster-tooltip-target",
            placement="top"
        ),
        dbc.RadioItems(
            options=[
                {"label": "Dragon or others", "value": "others"},
                {"label": "Golem King or Mummy King", "value": "improved"}
            ],
            value="others",
            id="boss-monster-radio",
            inline=True,
            persistence=True,
            persistence_type="memory",
        )
    ]
)

boss_type_div = html.Div(
    [
        html.H6("Boss monster type"),
        dbc.RadioItems(
            options=[],
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
                "width": "30%",
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

prod_special1_div = html.Div(
    [
        html.H6([], id = "prod-special1-name"),
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
        html.H6([], id = "prod-special2-name"),
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
        html.H6([], id = "prod-special3-name"),
        dcc.Dropdown(
            id="prod-special3-dropdown",
            options=[],
            persistence=True,
            persistence_type="memory",
            placeholder = "Choose one from the list."
        )
    ]
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
                            "Calculate hero damage", 
                            id="hero-damage-button",
                            color="primary"
                       )]
                   ),
                   style = {"padding-top": "1%"}
               ),
               dbc.Col(
                   html.Div(
                       dcc.Loading(
                           None, id = "hero-damage-result"
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
                dbc.Col(get_monster_div, id = "get-monster-div"),
                dbc.Col(html.Div(monster_level_div, style = {"padding-top": "4%"}), 
                        id = "monster-level-div"),
                dbc.Col(boss_monster_div, id = "boss-monster-div"),
                dbc.Col(boss_type_div, id = "boss-type-div"),
                dbc.Col(boss_level_div, id = "boss-level-div"),
                dbc.Col(sv_level_div, id = "sv-level-div")
            ],
            style={"width": "75%"}
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(prod_special1_div, id = "prod-special1-div", style={"padding-top": "1%"}),
                dbc.Col(prod_special2_div, id = "prod-special2-div", style={"padding-top": "1%"}),
                dbc.Col(prod_special3_div, id = "prod-special3-div", style={"padding-top": "1%"})
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(dungeon_rp_div, id = "dungeon-rp-div"),
                dbc.Col(statue_rp_div),
                dbc.Col(relics_rp_div)
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [dbc.Button(
                            "Calculate monster stats", 
                            id="monster-stats-button",
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
                [], id = "monster-stats-result"
            ),
            style = {"textAlign": "center"}
        )
    ],
    className="div-for-sidebar"
)

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
def update_hero_dmg(n_clicks, level, bought, weapon, dungeon, special1):
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
        return dcc.Markdown("The result is **{} damage** per hit.".format(dmg))
        
    else:
        raise PreventUpdate  

### Monster Callback Sections

# Callback for the dungeon RP bonus
@app.callback(
    Output("dungeon-rp-div", "style"),
    Input("dungeon-dropdown", "value")
)
def show_dungeon_rp(dungeon):
    if dungeon is None:
        return {'display': 'none'}
    else:
        return {'display': 'block'}

    
# Callback for the dungeon RP bonus options
@app.callback(
    [
        Output("dungeon-rp-checklist", "options"),
        Output("dungeon-rp-checklist", "value")
    ],
    Input("dungeon-dropdown", "value")
)
def get_dungeon_rp(dungeon):
    if dungeon == "dungeon1":
        options = [
            {"label": "1st special: 10% more RP", "value": 10},
            {"label": "3rd special: 15% more RP", "value": 15}
        ]
        value = [10, 15]
    elif dungeon == "dungeon1.5":
        options = [
            {"label": "1st special: 20% more RP", "value": 20},
            {"label": "3rd special: 25% more RP", "value": 25}
        ]    
        value = [20, 25]
    elif dungeon == "dungeon2":
        options = [
            {"label": "1st special: 15% more RP", "value": 15},
            {"label": "3rd special: 20% more RP", "value": 20}
        ]
        value = [15, 20]
    elif dungeon == "dungeon3":
        options = [
            {"label": "1st special: 20% more RP", "value": 20},
            {"label": "3rd special: 25% more RP", "value": 25}
        ]
        value = [20, 25]
    elif dungeon == "dungeon4":
        options = [
            {"label": "1st special: 25% more RP", "value": 25},
            {"label": "3rd special: 30% more RP", "value": 30}
        ]     
        value = [25, 30]
    else:
        options=[]
        value=""
        
    return [options, value]    


# Callback for the monster production building options
@app.callback(
    [
        Output("prod-special1-name", "children"),
        Output("prod-special1-dropdown", "options"),
        Output("prod-special1-dropdown", "value"),
        Output("prod-special2-name", "children"),
        Output("prod-special2-dropdown", "options"),
        Output("prod-special2-dropdown", "value"),
        Output("prod-special3-name", "children"),
        Output("prod-special3-dropdown", "options"), 
        Output("prod-special3-dropdown", "value") 
    ],
    Input("monster-dropdown", "value")
)
def get_prod_building(monster):
    x = df.query("Monster == @monster")
    monster_type = x["Type"].unique()
    
    if monster_type == "regular":
        name = "monster farm"
        options1=[
            {"label": "+20% damage", "value": "damage"},
            {"label": "+20% life", "value": "life"},
            {"label": "+20% RP", "value": "rp"}
        ]
        options2=[
            {"label": "+25% damage", "value": "damage"},
            {"label": "+25% life", "value": "life"},
            {"label": "+25% RP", "value": "rp"}
        ]
        options3=[
            {"label": "+30% damage", "value": "damage"},
            {"label": "+30% life", "value": "life"},
            {"label": "+30% RP", "value": "rp"}
        ]
    elif monster_type == "undead":
        name = "graveyard"
        options1=[
            {"label": "+10% disease chance", "value": "disease"},
            {"label": "+20% life", "value": "life"},
            {"label": "+20% RP", "value": "rp"}
        ]
        options2=[
            {"label": "+10% disease chance", "value": "disease"},
            {"label": "+25% life", "value": "life"},
            {"label": "+25% RP", "value": "rp"}
        ]
        options3=[
            {"label": "+10% disease chance", "value": "disease"},
            {"label": "+30% life", "value": "life"},
            {"label": "+30% RP", "value": "rp"}
        ]
    elif monster_type == "stone":
        name = "quarry"
        options1=[
            {"label": "+10% bone fracture chance", "value": "bone"},
            {"label": "+20% life", "value": "life"},
            {"label": "+20% RP", "value": "rp"}
        ]
        options2=[
            {"label": "+10% bone fracture chance", "value": "bone"},
            {"label": "+25% life", "value": "life"},
            {"label": "+25% RP", "value": "rp"}
        ]
        options3=[
            {"label": "+10% bone fracture chance", "value": "bone"},
            {"label": "+30% life", "value": "life"},
            {"label": "+30% RP", "value": "rp"}
        ]
    elif monster_type == "fire":
        name = "fire hole"
        options1=[
            {"label": "+10% burn chance", "value": "burn"},
            {"label": "+20% life", "value": "life"},
            {"label": "+20% RP", "value": "rp"}
        ]
        options2=[
            {"label": "+10% burn chance", "value": "burn"},
            {"label": "+25% life", "value": "life"},
            {"label": "+25% RP", "value": "rp"}
        ]
        options3=[
            {"label": "+10% burn chance", "value": "burn"},
            {"label": "+30% life", "value": "life"},
            {"label": "+30% RP", "value": "rp"}
        ]
    else:
        name = "building"
        options1=[]
        options2=[]
        options3=[]
        
    return [f"Select effect (2nd {name} special)", options1, None, 
            f"Select effect (3rd {name} special)", options2, None, 
            f"Select effect (4th {name} special)", options3, None]


# Callback for the corresponding options under each monster category
@app.callback(
    [
        Output("get-monster-div", "style"),
        Output("monster-level-div", "style"),
        Output("boss-monster-div", "style"),
        Output("boss-type-div", "style"),
        Output("boss-level-div", "style"),
        Output("sv-level-div", "style"),
        Output("prod-special1-div", "style"),
        Output("prod-special2-div", "style"),
        Output("prod-special3-div", "style")
    ],
    Input("monster-cat-dropdown", "value")
)
def show_options(cat):
    if cat == "regular":
        return [{'display': 'block'}, {'display': 'block'}, {'display': 'none'},
                {'display': 'none'}, {'display': 'none'}, {'display': 'none'},
                {'display': 'block'}, {'display': 'block'}, {'display': 'block'}]
    elif cat == "boss":
        return [{'display': 'none'}, {'display': 'none'}, {'display': 'block'},
                {'display': 'block'}, {'display': 'block'}, {'display': 'none'}, 
                {'display': 'none'}, {'display': 'none'}, {'display': 'none'}]
    elif cat == "sv":
        return [{'display': 'none'}, {'display': 'none'}, {'display': 'none'},
                {'display': 'none'}, {'display': 'none'}, {'display': 'block'}, 
                {'display': 'none'}, {'display': 'none'}, {'display': 'none'}]
    else:
        return [{'display': 'none'}, {'display': 'none'}, {'display': 'none'},
                {'display': 'none'}, {'display': 'none'}, {'display': 'none'},
                {'display': 'none'}, {'display': 'none'}, {'display': 'none'}]

    
# Callback for the monster level max possible value
@app.callback(
    [
        Output("monster-level", "max"),
        Output("monster-level", "value")
    ],
    Input("monster-dropdown", "value")
)
def update_max(monster):
    if monster in ("Skeleton", "Zombie", "Mummy", "Golem"):
        return [25, 20]
    else:
        return [30, 25]

    
# Callback for the boss monster type
@app.callback(
    [
        Output("boss-type-radio", "options"),
        Output("boss-type-radio", "value")
    ],
    Input("boss-monster-radio", "value")
)
def update_boss_type(boss):
    if boss == "others":
        options=[
                {"label": "Regular", "value": "regular"},
                {"label": "Undead", "value": "undead"},
                {"label": "Stone", "value": "stone"},
                {"label": "Fire", "value": "fire"}
        ]
        value = "fire"
    else:
        options=[
                {"label": "Undead", "value": "undead"},
                {"label": "Stone", "value": "stone"}
        ]
        value = "undead"
        
    return [options, value]    


# Callback for the calculate monster stats button
@app.callback(
    Output("monster-stats-result", "children"),
    Input("monster-stats-button", "n_clicks"),
    [
        State("hero-damage-result", "children"),
        State("hero-level", "value"),
        State("hero-weapon-radio", "value"),
        State("hero-weapon-level", "value"),
        State("dungeon-dropdown", "value"),
        State("special1-dropdown", "value"),
        State("special2-dropdown", "value"),
        State("monster-cat-dropdown", "value"),
        State("monster-dropdown", "value"),
        State("monster-level", "value"),
        State("boss-monster-radio", "value"),
        State("boss-type-radio", "value"),
        State("boss-monster-level", "value"),
        State("sv-level", "value"),
        State("dungeon-rp-checklist", "value"),
        State("prod-special1-dropdown", "value"),
        State("prod-special2-dropdown", "value"),
        State("prod-special3-dropdown", "value"),
        State("statue-rp-radio", "value"),
        State("rp-relic-checklist", "value")
    ]
)
def update_monster_dmg(n_clicks, result, hero_lvl, bought, weapon, dungeon, special1, special2,
                       cat, monster, monster_lvl, boss, boss_type, boss_lvl, sv_lvl, dungeon_rp,
                       prod1, prod2, prod3, statue, relics):
    if n_clicks:
        time.sleep(1)
        
        text = json.dumps(result) # converts markdown dict result to string
        
        if result is None or "inputs" in text:
            return dcc.Markdown("Please calculate the hero damage first.", 
                                style={"color": "red"})
        
        if cat == "regular":
            inputs = {
                "2nd dungeon special": special1,
                "4th dungeon special": special2,
                "Monster": monster,
                "Monster level": monster_lvl,
                "2nd building special": prod1,
                "3rd building special": prod2,
                "4th building special": prod3
            }
        elif cat == "boss":
            inputs = {
                "2nd dungeon special": special1,
                "4th dungeon special": special2,
                "Boss monster level": boss_lvl
            }
        elif cat == "sv":
            inputs = {
                "2nd dungeon special": special1,
                "4th dungeon special": special2,
                "Supervillain level": sv_lvl
            }
        else:
            inputs = {
                "Dungeon": dungeon,
                "Monster category": cat,
                "2nd dungeon special": special1,
                "4th dungeon special": special2
            }
        
        if None in list(inputs.values()):
            missing_inputs = [x for x in list(inputs.keys()) if inputs[x] is None]
            error_message = f"Missing inputs: {', '.join(missing_inputs)}"
            return dcc.Markdown(error_message, style={"color": "red"})
        
        ## Hero damage
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
            
        if hero_lvl <= 10:
            x = ((hero_lvl - 1) * 11) + 25
            hero_dmg = (x + weapon_mult) * dungeon_mult
        else:
            x = ((hero_lvl - 1) * 13) + 25 + ((hero_lvl - 10) * 2)
            hero_dmg = (x + weapon_mult) * dungeon_mult
        
        ## Monster stats
        
        # General damage multipliers
        if special1 == "monster":
            more_mult = 1.2
        else:
            more_mult = 1
        
        # General damage diminishers
        if dungeon == "dungeon1.5" and special2 == "monster":
            less_mult = 1.25
        elif special2 == "monster":
            less_mult = 1.2
        else:
            less_mult = 1
        
        # General RP multipliers
        dungeon_mult = 1
        if dungeon_rp is None:
            dungeon_mult = 1
        else:    
            for i in dungeon_rp:
                dungeon_mult = dungeon_mult * ((100 + i) / 100)
        statue_mult = 1 + (statue / 100)
        relics_mult = 1 + (sum(relics) / 100)
        
        if cat == "regular":
            x = df.query("Monster == @monster")
            monster_type = x["Type"].unique()
            
            if monster_type == "regular" and dungeon in ("dungeon2", "dungeon3"):
                error_message = f"""The **{monster}** can only be placed in the **Old Dungeon/Ice Fortress** 
                and **Dark Palace**."""
                return dcc.Markdown(error_message, style={"color": "red"})
                
            if monster_type == "undead" and dungeon in ("dungeon3", "dungeon4"):
                error_message = f"""The **{monster}** can only be placed in the **Old Dungeon/Ice Fortress**  
                and **Cursed Crypt**."""
                return dcc.Markdown(error_message, style={"color": "red"})    
            
            if monster_type == "stone" and dungeon in ("dungeon1", "dungeon1.5", "dungeon4"):
                error_message = f"""The **{monster}** can only be placed in the **Cursed Crypt** 
                and **Demonic Castle**."""
                return dcc.Markdown(error_message, style={"color": "red"})
            
            if monster_type == "fire" and dungeon in ("dungeon1", "dungeon1.5", "dungeon2"):
                error_message = f"""The **{monster}** can only be placed in the **Demonic Castle**
                and **Dark Palace**."""
                return dcc.Markdown(error_message, style={"color": "red"})
            
            base_life = x["Life"].unique()
            base_dmg = x["Damage"].unique()
            base_rp = x["RP"].unique()
            life_lvl = base_life + ((0.75 * base_life) * (monster_lvl - 1))
            dmg_lvl = base_dmg + ((0.25 * base_dmg) * (monster_lvl - 1))
            rp_prog = [1, 1.5, 2, 2.4, 2.8, 3.1, 3.35, 3.6, 3.85, 4.1, 4.3, 4.5, 4.7,
                       4.9, 5.1, 5.25, 5.4, 5.55, 5.7, 5.85, 6, 6.1, 6.2, 6.3, 6.4, 
                       6.4, 6.4, 6.4, 6.4, 6.4]
            rp_lvl = base_rp * rp_prog[monster_lvl - 1]
            
            # Life multipliers
            if prod1 == "life":
                life_mult1 = 1.2
            else:
                life_mult1 = 1
                
            if prod2 == "life":
                life_mult2 = 1.25
            else:
                life_mult2 = 1
                
            if prod3 == "life":
                life_mult3 = 1.3
            else:
                life_mult3 = 1
                
            # Damage multipliers
            if monster_type == "regular" and prod1 == "damage":
                dmg_mult1 = 1.2
            else:
                dmg_mult1 = 1
                
            if monster_type == "regular" and prod2 == "damage":
                dmg_mult2 = 1.25
            else:
                dmg_mult2 = 1
                
            if monster_type == "regular" and prod3 == "damage":
                dmg_mult3 = 1.3
            else:
                dmg_mult3 = 1     
            
            if dungeon == "dungeon1" and special2 == "regular" and monster_type == "regular":
                extra_mult = 1.25
            elif dungeon == "dungeon1" and special2 == "undead" and monster_type == "undead":     
                extra_mult = 1.25
            elif dungeon == "dungeon1.5" and special2 == "regular" and monster_type == "regular":
                extra_mult = 1.3
            elif dungeon == "dungeon1.5" and special2 == "undead" and monster_type == "undead":     
                extra_mult = 1.3
            elif dungeon == "dungeon2" and special2 == "stone" and monster_type == "stone":     
                extra_mult = 1.25
            elif dungeon == "dungeon3" and special2 == "fire" and monster_type == "fire":     
                extra_mult = 1.25  
            elif dungeon == "dungeon4" and special2 == "regular" and monster_type == "regular":     
                extra_mult = 1.3
            else:
                extra_mult = 1
            
            # RP multipliers
            if prod1 == "rp":
                rp_mult1 = 1.2
            else:
                rp_mult1 = 1
                
            if prod2 == "rp":
                rp_mult2 = 1.25
            else:
                rp_mult2 = 1
                
            if prod3 == "rp":
                rp_mult3 = 1.3
            else:
                rp_mult3 = 1
                
            name = "monster"
            life = life_lvl * life_mult1 * life_mult2 * life_mult3
            dmg = dmg_lvl * dmg_mult1 * dmg_mult2 * dmg_mult3 * extra_mult * more_mult / less_mult
            rp = rp_lvl * rp_mult1 * rp_mult2 * rp_mult3 * dungeon_mult * statue_mult * relics_mult
        elif cat == "boss":
            if boss == "improved":
                improved_mult1 = 1 + (1 / 6) # more life
                improved_mult2 = 1 + (1 / 7) # more RP  
            else:   
                improved_mult1 = 1
                improved_mult2 = 1
                
            if dungeon == "dungeon1" and special2 == "regular" and boss_type == "regular":
                extra_mult = 1.25
            elif dungeon == "dungeon1" and special2 == "undead" and boss_type == "undead":     
                extra_mult = 1.25
            elif dungeon == "dungeon1.5" and special2 == "regular" and boss_type == "regular":
                extra_mult = 1.3
            elif dungeon == "dungeon1.5" and special2 == "undead" and boss_type == "undead":     
                extra_mult = 1.3
            elif dungeon == "dungeon2" and special2 == "stone" and boss_type == "stone":     
                extra_mult = 1.25
            elif dungeon == "dungeon3" and special2 == "fire" and boss_type == "fire":     
                extra_mult = 1.25  
            elif dungeon == "dungeon4" and special2 == "regular" and boss_type == "regular":     
                extra_mult = 1.3
            else:
                extra_mult = 1
            
            name = "boss monster"
            life = (300 + ((boss_lvl - 1) * 225)) * improved_mult1
            dmg = (40 + ((boss_lvl - 1) * 10)) * extra_mult * more_mult / less_mult
            rp = (2625 + ((boss_lvl - 1) * 35)) * dungeon_mult * statue_mult * relics_mult * improved_mult2
        else:
            name = "supervillain"
            life = 7625 + ((sv_lvl - 20) * 375)
            dmg = (287 + ((sv_lvl - 20) * 12.5)) * more_mult / less_mult
            rp = (9400 + ((sv_lvl - 20) * 100)) * dungeon_mult * statue_mult * relics_mult
            
        life = math.floor(life)
        dmg = math.floor(dmg)
        rp = math.floor(rp)
        hits = math.ceil(life / hero_dmg)    
            
        return dcc.Markdown("""**Life**: {:,}\n
        \n**Damage**: {:,}\n
        \n**RP**: {:,} \n
        \nIt will take **{} hits** to kill this **{}**.
        """.format(life, dmg, rp, hits, name))
        
    else:
        raise PreventUpdate  
    
            