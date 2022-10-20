import datetime as dt
import logging


import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape as cyto
import json


# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objs as go
# import plotly.io as pio
# from dash.dependencies import Input, Output, State

# """""""""""""""""""""""""""""""""" Initialization """""""""""""""""""""""""""""""""""
logger = logging.getLogger(__name__)
# plt.style.use("seaborn-whitegrid")
# pio.templates.default = "plotly_white"


# """""""""""""""""""""""""""""""""" App Boilerplate """""""""""""""""""""""""""""""""""
# external js scripts
external_scripts = [
    dict(
        src="https://code.jquery.com/jquery-3.6.1.slim.min.js",
        integrity="sha256-w8CvhFs7iHNVUtnSP0YKEg00p9Ih13rlL9zGqvLdePA=",
        crossorigin="anonymous",
    ),
    dict(
        src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js",
        integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3",
        crossorigin="anonymous",
    ),
]

# external CSS stylesheets
external_stylesheets = [
    dict(
        rel="stylesheet",
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css",
        integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi",
        crossorigin="anonymous",
    ),
]

app = dash.Dash(
    __name__,
    external_scripts=external_scripts,
    external_stylesheets=external_stylesheets,
)
# server = app.server  # expose for wsgi

# A hidden div where data can be stored and passed between callbacks
data_store = html.Div(id="data-store", style={"display": "none"})

# """""""""""""""""" Dash Components (to be arranged in the layout) """""""""""""""""""

data_map_tab = dcc.Tab(
    label="Data Map",
    children=html.Img(src="/assets/images/graph.png", width="100%"),
)

with open("apps/assets/graph-elements.json", "r") as f:
    graph_elements = json.load(f)

ontology_tab = dcc.Tab(
    label="Ontology",
    children=cyto.Cytoscape(
        id="ontology-graph",
        layout={"name": "circle", "directed": "true", "radius": 1000},
        style={"height": "80vh", "width": "100%"},
        minZoom=0.1,
        maxZoom=1,
        elements=graph_elements,
        stylesheet=[
            {
                "selector": "node",
                "style": {
                    "label": "data(label)",
                    "width": "350%",
                    "height": "350%",
                    "text-wrap": "wrap",
                    "text-valign": "center",
                    "text-halign": "center",
                    "text-max-width": "60px",
                    "color": "white",
                    "font-size": "55px",
                },
            },
            {
                "selector": "edge",
                "style": {
                    "width": "3px",
                    "target-arrow-shape": "triangle",
                    "source-arrow-shape": "triangle",
                    "curve-style": "bezier",
                    "label": "data(label)",
                    "edge-text-rotation": "autorotate",
                    "font-size": "40px",
                    "control-point-step-size": "100px",
                },
            },
        ],
    ),
)


app.layout = html.Div(
    dcc.Tabs(children=[data_map_tab, ontology_tab]),
    id="app-container",
    className="flex-container",
)

# """""""""""""""""""""""""""""""""" Input Components """"""""""""""""""""""""""""""""""
# # dropdown input
# dropdown_options_dict = {
#     "Option A": "option_a",
#     "Option B": "option_b",
#     "Option C": "option_c",
# }
# dropdown_options_val_to_name = {v: k for k, v in dropdown_options_dict.items()}
# dropdown_options = [
#     dict(label=name, value=val) for name, val in dropdown_options_dict.items()
# ]
# dropdown = dcc.Dropdown(
#     id="dropdown",
#     options=dropdown_options,
#     className="f-row",
#     value="option_a",
#     # multi=True, # allow multi-select
# )

# dropdown_card = html.Div(
#     [html.Div("Options:", className="f-row f-label"), dropdown],
#     id="dropdown-row",
#     className="f-column card",
# )

# date_range = dcc.DatePickerRange(
#     id="date-range",
#     min_date_allowed=dt.datetime(2022, 1, 1),
#     max_date_allowed=dt.datetime(2025, 1, 1),
#     start_date=dt.datetime(2022, 9, 1),
#     end_date=dt.datetime(2022, 9, 7),
# )

# date_range_card = html.Div(
#     [html.Div("Date Range:", className="f-row f-label"), date_range],
#     className="f-column card",
#     id="date-range-row",
# )

# run_button = html.Div(
#     html.Button("Run", id="run-button", className="btn btn-outline-primary"),
#     className="f-row",
# )
# run_button_card = html.Div(run_button, id="run-button-card", className="f-row card")

# # """""""""""""""""""""""""""""""""" Output Components """"""""""""""""""""""""""""""""

# mpl_figure = html.Img(id="mpl-figure")
# # Loading object creates loading animation while output is being computed
# mpl_figure_loading = dcc.Loading(mpl_figure, id="mpl-figure-loading", type="circle")
# mpl_figure_card = html.Div(
#     mpl_figure_loading, id="mpl-figure-card", className="f-row card"
# )

# plotly_figure = dcc.Graph(
#     id="plotly-figure"
# )  # generic container for plotly figure/chart
# plotly_figure_loading = dcc.Loading(
#     plotly_figure, id="plotly-figure-loading", type="circle"
# )
# plotly_figure_card = html.Div(
#     plotly_figure_loading, id="plotly-figure-card", className="f-row card"
# )


# """""""""""""""""""""""""""""""""" Component Layout """"""""""""""""""""""""""""""""""

# input_row = html.Div(
#     [date_range_card, run_button_card], id="input-row", className="f-row"
# )
# app.layout = html.Div(
#     [dropdown_card, input_row, plotly_figure_loading, mpl_figure_loading],
#     id="app-container",
#     className="flex-container",
# )


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
