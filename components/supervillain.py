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

disclaimer_div = html.Div(
    [
        html.H6("Disclaimer:"),
        dcc.Markdown("""To determine the **best** supervillain (SV), only the **finals levels** are 
        considered for comparison. Moreover, **alchemist special actions** are used for two reasons: 
        (a) force a SV to buy potion(s) to **gain an extra level** and (b) the cooldown can be 
        **refreshed easily** compared to other shops. Hover around the **item level** for an additional
        disclaimer.""")
    ]
)

sv_item_div = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H6(
                            [ 
                                html.Span(
                                    "Item level",
                                    id="sv-item-level-tooltip-target",
                                    style={"textDecoration": "underline", 
                                           "cursor": "pointer"}
                                )
                            ]
                        ),
                        dbc.Tooltip(
                            """Supervillains are strictly buying items only 
                            on this level for an easier comparison.""",
                            target="sv-item-level-tooltip-target",
                            placement="top"
                        ),
                        dcc.Input(
                            id="sv-item-level",
                            type="number",
                            min=1,
                            max=30,
                            placeholder="Enter any positive integer.",
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                            persistence=True,
                            persistence_type="memory",
                        )
                    ]
                ),
                dbc.Col(
                    [
                        #dcc.Markdown("""*Note: Potions A refers to **health potions**
                        #and Potions B refers to **mana/stamina potions**.*""")
                        html.H6(
                            [
                                "Bought an ",
                                html.Span(
                                    "amulet or ring",
                                    id="sv-thief-tooltip-target",
                                    style={"textDecoration": "underline", 
                                           "cursor": "pointer"}
                                ),
                                "?"
                            ]
                        ),
                        dbc.Tooltip(
                            """This occurs when the thief manages to successfully steal either
                            an amulet or ring from the supervillain.""",
                            target="sv-thief-tooltip-target",
                            placement="top"
                        ),
                        dbc.RadioItems(
                            options=[
                                {"label": "Yes", "value": 1},
                                {"label": "No", "value": 0}
                            ],
                            value=0,
                            id="sv-thief-radio",
                            inline=True,
                            persistence=True,
                            persistence_type="memory",
                        )
                    ]
                )
            ]
        )
    ]
)

sv1_div = html.Div(
    [
        html.H6("Supervillain #1"),
        dbc.Row(
            [
               dbc.Col(
                    [
                        html.H6("Level"),
                        dcc.Input(
                            id="sv1-level",
                            type="number",
                            min=20,
                            max=60,
                            value=60,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                            persistence=True,
                            persistence_type="memory",
                        )  
                    ]
                ), 
               dbc.Col(
                    [
                        html.H6("Weapons"),
                        dcc.Input(
                            id="sv1-weapons",
                            type="number",
                            min=3,
                            max=5,
                            value=4,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                            persistence=True,
                            persistence_type="memory",
                        )  
                    ]
                ), 
                dbc.Col(
                    [
                        html.H6("Armors"),
                        dcc.Input(
                            id="sv1-armors",
                            type="number",
                            min=3,
                            max=5,
                            value=4,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                            persistence=True,
                            persistence_type="memory",
                        )  
                    ]
                ), 
                dbc.Col(
                    [
                        html.H6("Potions A"),
                        dcc.Input(
                            id="sv1-hps",
                            type="number",
                            min=10,
                            max=20,
                            value=15,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                            persistence=True,
                            persistence_type="memory",
                        )  
                    ]
                ), 
                dbc.Col(
                    [
                        html.H6("Potions B"),
                        dcc.Input(
                            id="sv1-msps",
                            type="number",
                            min=10,
                            max=20,
                            value=15,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                            persistence=True,
                            persistence_type="memory",
                        )  
                    ]
                ), 
            ]
        )
    ]
)

sv2_div = html.Div(
    [
        html.H6("Supervillain #2"),
        dbc.Row(
            [
               dbc.Col(
                    [
                        html.H6("Level"),
                        dcc.Input(
                            id="sv2-level",
                            type="number",
                            min=20,
                            max=60,
                            value=60,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                            persistence=True,
                            persistence_type="memory",
                        )  
                    ]
                ), 
               dbc.Col(
                    [
                        html.H6("Weapons"),
                        dcc.Input(
                            id="sv2-weapons",
                            type="number",
                            min=3,
                            max=5,
                            value=4,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                            persistence=True,
                            persistence_type="memory",
                        )  
                    ]
                ), 
                dbc.Col(
                    [
                        html.H6("Armors"),
                        dcc.Input(
                            id="sv2-armors",
                            type="number",
                            min=3,
                            max=5,
                            value=4,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                            persistence=True,
                            persistence_type="memory",
                        )  
                    ]
                ), 
                dbc.Col(
                    [
                        html.H6("Potions A"),
                        dcc.Input(
                            id="sv2-hps",
                            type="number",
                            min=10,
                            max=20,
                            value=15,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                            persistence=True,
                            persistence_type="memory",
                        )  
                    ]
                ), 
                dbc.Col(
                    [
                        html.H6("Potions B"),
                        dcc.Input(
                            id="sv2-msps",
                            type="number",
                            min=10,
                            max=20,
                            value=15,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                            persistence=True,
                            persistence_type="memory",
                        )  
                    ]
                ), 
            ]
        )
    ]
)

sv3_div = html.Div(
    [
        html.H6("Supervillain #3"),
        dbc.Row(
            [
               dbc.Col(
                    [
                        html.H6("Level"),
                        dcc.Input(
                            id="sv3-level",
                            type="number",
                            min=20,
                            max=60,
                            value=60,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                            persistence=True,
                            persistence_type="memory",
                        )  
                    ]
                ), 
               dbc.Col(
                    [
                        html.H6("Weapons"),
                        dcc.Input(
                            id="sv3-weapons",
                            type="number",
                            min=3,
                            max=5,
                            value=4,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                            persistence=True,
                            persistence_type="memory",
                        )  
                    ]
                ), 
                dbc.Col(
                    [
                        html.H6("Armors"),
                        dcc.Input(
                            id="sv3-armors",
                            type="number",
                            min=3,
                            max=5,
                            value=4,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                            persistence=True,
                            persistence_type="memory",
                        )  
                    ]
                ), 
                dbc.Col(
                    [
                        html.H6("Potions A"),
                        dcc.Input(
                            id="sv3-hps",
                            type="number",
                            min=10,
                            max=20,
                            value=15,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                            persistence=True,
                            persistence_type="memory",
                        )  
                    ]
                ), 
                dbc.Col(
                    [
                        html.H6("Potions B"),
                        dcc.Input(
                            id="sv3-msps",
                            type="number",
                            min=10,
                            max=20,
                            value=15,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                            persistence=True,
                            persistence_type="memory",
                        )  
                    ]
                ), 
            ]
        )
    ]
)

sv4_div = html.Div(
    [
        html.H6("Supervillain #4"),
        dbc.Row(
            [
               dbc.Col(
                    [
                        html.H6("Level"),
                        dcc.Input(
                            id="sv4-level",
                            type="number",
                            min=20,
                            max=60,
                            value=60,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                            persistence=True,
                            persistence_type="memory",
                        )  
                    ]
                ), 
               dbc.Col(
                    [
                        html.H6("Weapons"),
                        dcc.Input(
                            id="sv4-weapons",
                            type="number",
                            min=3,
                            max=5,
                            value=4,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                            persistence=True,
                            persistence_type="memory",
                        )  
                    ]
                ), 
                dbc.Col(
                    [
                        html.H6("Armors"),
                        dcc.Input(
                            id="sv4-armors",
                            type="number",
                            min=3,
                            max=5,
                            value=4,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                            persistence=True,
                            persistence_type="memory",
                        )  
                    ]
                ), 
                dbc.Col(
                    [
                        html.H6("Potions A"),
                        dcc.Input(
                            id="sv4-hps",
                            type="number",
                            min=10,
                            max=20,
                            value=15,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                            persistence=True,
                            persistence_type="memory",
                        )  
                    ]
                ), 
                dbc.Col(
                    [
                        html.H6("Potions B"),
                        dcc.Input(
                            id="sv4-msps",
                            type="number",
                            min=10,
                            max=20,
                            value=15,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                            persistence=True,
                            persistence_type="memory",
                        )  
                    ]
                ), 
            ]
        )
    ]
)

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(disclaimer_div)
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(sv_item_div)
            ],
            style = {"width": "75%"}
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [sv1_div], width={"size": 6},
                ),
                 dbc.Col(
                    [sv2_div], width={"size": 6},
                )
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [sv3_div], width={"size": 6},
                ),
                 dbc.Col(
                    [sv4_div], width={"size": 6},
                )
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [dbc.Button(
                            "Calculate final levels", 
                            id="sv-button",
                            color="primary")],
                        style = {"textAlign": "center"}
                    )
                )
            ]
        ),
        html.Br(),
        html.Div(
            dcc.Loading(
                [], id = "sv-result"
            ),
            style = {"textAlign": "center"}
        )
    ],
    className="div-for-sidebar"
)


# Callback for the best supervillain button
@app.callback(
    Output("sv-result", "children"),
    Input("sv-button", "n_clicks"),
    [
        State("sv-item-level", "value"),
        State("sv-thief-radio", "value"),
        State("sv1-level", "value"),
        State("sv1-weapons", "value"),
        State("sv1-armors", "value"),
        State("sv1-hps", "value"),
        State("sv1-msps", "value"),
        State("sv2-level", "value"),
        State("sv2-weapons", "value"),
        State("sv2-armors", "value"),
        State("sv2-hps", "value"),
        State("sv2-msps", "value"),
        State("sv3-level", "value"),
        State("sv3-weapons", "value"),
        State("sv3-armors", "value"),
        State("sv3-hps", "value"),
        State("sv3-msps", "value"),
        State("sv4-level", "value"),
        State("sv4-weapons", "value"),
        State("sv4-armors", "value"),
        State("sv4-hps", "value"),
        State("sv4-msps", "value")
    ]
)
def det_best_sv(n_clicks, item, thief, level1, weapons1, armors1, hps1, msps1, level2, 
                weapons2, armors2, hps2, msps2, level3, weapons3, armors3, hps3, msps3, 
                level4, weapons4, armors4, hps4, msps4):
    if n_clicks:
        time.sleep(1)
        
        inputs = {
            "Item level": item, "Level - SV #1": level1, "Weapons - SV #1": weapons1, 
            "Armors - SV #1": armors1, "Health Potions - SV #1": hps1, 
            "Other Potions - SV #1": msps1, "Level - SV #2": level2, 
            "Weapons - SV #2": weapons2, "Armors - SV #2": armors2, 
            "Health Potions - SV #2": hps2, "Other Potions - SV #2": msps2,
            "Level - SV #3": level3,  "Weapons - SV #3": weapons3, 
            "Armors - SV #3": armors3, "Health Potions - SV #3": hps3, 
            "Other Potions - SV #3": msps3, "Level - SV #4": level4,
            "Weapons - SV #4": weapons4, "Armors - SV #4": armors4,
            "Health Potions - SV #4": hps4, "Other Potions - SV #4": msps4,
        }
        
        if None in list(inputs.values()):
            missing_inputs = [x for x in list(inputs.keys()) if inputs[x] is None]
            error_message = f"Missing inputs: {', '.join(missing_inputs)}"
            return dcc.Markdown(error_message, style={"color": "red"})
        
        equipment_mult = 0.08 * item
        potion_mult = 0.012 * item
        
        sv1_total = level1 + ((weapons1 + armors1 + thief) * equipment_mult) + \
                    ((hps1 + msps1) * potion_mult)
        sv2_total = level2 + ((weapons2 + armors2 + thief) * equipment_mult) + \
                    ((hps2 + msps2) * potion_mult)
        sv3_total = level3 + ((weapons3 + armors3 + thief) * equipment_mult) + \
                    ((hps3 + msps3) * potion_mult)
        sv4_total = level4 + ((weapons4 + armors4 + thief) * equipment_mult) + \
                    ((hps4 + msps4) * potion_mult)
        
        sv_list = ["SV #1", "SV #2", "SV #3", "SV #4"]
        total_list = [sv1_total, sv2_total, sv3_total, sv4_total]
        
        total_max = np.max(total_list)
        total_index = [i for i, j in enumerate(total_list) if j == total_max]
        
        sv_index = [sv_list[i] for i in total_index]
        sv_msg = f"{', '.join(sv_index)}"
        
        total_max_floor = math.floor(total_max)
        total_max_1pot = total_max + potion_mult
        floor1 = math.floor(total_max_1pot)
        total_max_2pots = total_max + (2 * potion_mult)
        floor2 = math.floor(total_max_2pots)
        
        if floor1 == total_max_floor + 1:
            hint = f"""For **{sv_msg}**: Use **one** alchemist special action (**+{potion_mult}**) 
            to gain one extra level."""
        elif floor2 == total_max_floor + 1:
            hint = f"""For **{sv_msg}**: Use **two** alchemist special actions (**+{2 * potion_mult}**) 
            to gain one extra level."""
        else:
            hint = f"""For **{sv_msg}**: There's **no need** to use any alchemist special actions 
            to gain one extra level."""
        
        return dcc.Markdown("""Final level per supervillain:\n
        \n**Supervillain #1**: {:.3f}\n
        \n**Supervillain #2**: {:.3f}\n
        \n**Supervillain #3**: {:.3f}\n
        \n**Supervillain #4**: {:.3f}\n
        \n{}""".format(sv1_total, sv2_total, sv3_total, sv4_total, hint))
        
    else:
        raise PreventUpdate
        
        