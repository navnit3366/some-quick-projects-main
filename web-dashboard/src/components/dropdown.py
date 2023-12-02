from typing import List
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from src.ids import ID_DROPDOWN, SELECT_ALL_BTN
#from components.ids import ID_DROPDOWN


def visualisation_layout(app: Dash, data) -> html.Div:
    list_nations = data.nation.unique()

    @app.callback(
        Output(ID_DROPDOWN, "value"),  #modify the value of the field
        Input(SELECT_ALL_BTN,
              "n_clicks"),  #if the user click the btn, nb_click change
    )
    def select_all_nations(_: int) -> List[str]:
        return list_nations

    return html.Div(children=[
        html.H6("Nations"),
        dcc.Dropdown(id=ID_DROPDOWN,
                     options=[{
                         "label": nation,
                         "value": nation
                     } for nation in list_nations],
                     value=list_nations,
                     multi=True),
        html.Button(
            id=SELECT_ALL_BTN, className="my-btn", children=["Select All"])
    ])
