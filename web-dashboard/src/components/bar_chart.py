from typing import List
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from plotly import express as px
from src.ids import BAR_CHART, ID_DROPDOWN


def render(app: Dash, data) -> html.Div:

    @app.callback(Output(BAR_CHART, "children"), Input(ID_DROPDOWN, "value"))
    def update_bar_on_change(countries: List[str]) -> html.Div:
        data_filtered = data[data['nation'].isin(
            countries)]  #data.query("nation in @countries")
        if data_filtered.shape[0] == 0:
            return html.Div('no data selected')
        fig = px.bar(data_filtered,
                     x="medal",
                     y="count",
                     color="nation",
                     text="nation")
        return html.Div(dcc.Graph(figure=fig), id=BAR_CHART)

    return html.Div(id=BAR_CHART)
