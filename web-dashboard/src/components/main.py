from dash import Dash, html
from src.components import bar_chart, dropdown

#get a dataframe
from plotly import express as px

DATA_EXAMPLE = px.data.medals_long()


def create_main_layout(app: Dash) -> html.Div:

    return html.Div(className="div1",
                    children=[
                        html.H1(app.title),
                        html.Hr(),
                        html.Div(className="dropdown-container",
                                 children=[
                                     dropdown.visualisation_layout(
                                         app, data=DATA_EXAMPLE),
                                     bar_chart.render(app, data=DATA_EXAMPLE)
                                 ])
                    ])
