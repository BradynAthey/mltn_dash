import base64
import datetime as dt
import logging
from io import BytesIO

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import plotly.io as pio
from dash.dependencies import Input, Output, State
from mltn import generate_random_timeseries

from utils import mpl_fig_to_uri

matplotlib.use("agg")

# """""""""""""""""""""""""""""""""" Initialization """""""""""""""""""""""""""""""""""
# logging.basicConfig(format="%(asctime)s %(name)s: %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)
plt.style.use("seaborn-whitegrid")
pio.templates.default = "plotly_white"


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

# """""""""""""""""""""""""""""""""" Input Components """"""""""""""""""""""""""""""""""
# dropdown input
dropdown_options_dict = {
    "Option A": "option_a",
    "Option B": "option_b",
    "Option C": "option_c",
}
dropdown_options_val_to_name = {v: k for k, v in dropdown_options_dict.items()}
dropdown_options = [
    dict(label=name, value=val) for name, val in dropdown_options_dict.items()
]
dropdown = dcc.Dropdown(
    id="dropdown",
    options=dropdown_options,
    className="f-row",
    value="option_a",
    # multi=True, # allow multi-select
)

dropdown_card = html.Div(
    [html.Div("Options:", className="f-row f-label"), dropdown],
    id="dropdown-row",
    className="f-column card",
)

date_range = dcc.DatePickerRange(
    id="date-range",
    min_date_allowed=dt.datetime(2022, 1, 1),
    max_date_allowed=dt.datetime(2025, 1, 1),
    start_date=dt.datetime(2022, 9, 1),
    end_date=dt.datetime(2022, 9, 7),
)

date_range_card = html.Div(
    [html.Div("Date Range:", className="f-row f-label"), date_range],
    className="f-column card",
    id="date-range-row",
)

run_button = html.Div(
    html.Button("Run", id="run-button", className="btn btn-outline-primary"),
    className="f-row",
)
run_button_card = html.Div(run_button, id="run-button-card", className="f-row card")

# """""""""""""""""""""""""""""""""" Output Components """"""""""""""""""""""""""""""""

mpl_figure = html.Img(id="mpl-figure")
# Loading object creates loading animation while output is being computed
mpl_figure_loading = dcc.Loading(mpl_figure, id="mpl-figure-loading", type="circle")
mpl_figure_card = html.Div(
    mpl_figure_loading, id="mpl-figure-card", className="f-row card"
)

plotly_figure = dcc.Graph(
    id="plotly-figure"
)  # generic container for plotly figure/chart
plotly_figure_loading = dcc.Loading(
    plotly_figure, id="plotly-figure-loading", type="circle"
)
plotly_figure_card = html.Div(
    plotly_figure_loading, id="plotly-figure-card", className="f-row card"
)


# """""""""""""""""""""""""""""""""" Component Layout """"""""""""""""""""""""""""""""""

input_row = html.Div(
    [date_range_card, run_button_card], id="input-row", className="f-row"
)
app.layout = html.Div(
    [dropdown_card, input_row, plotly_figure_loading, mpl_figure_loading],
    id="app-container",
    className="flex-container",
)

# """"""""""""""""""""""""""""""""""""" Callbacks """"""""""""""""""""""""""""""""""""""
@app.callback(
    Output("mpl-figure", "src"),
    [Input("run-button", "n_clicks")],
    [
        State("date-range", "start_date"),
        State("date-range", "end_date"),
        State("dropdown", "value"),
    ],
)
def fill_mpl_figure(n_clicks, start_date, end_date, option_value):

    if not n_clicks:
        logger.info("returning initial empty figure")
        f = plt.figure()
        plt.title("Empty Figure")
        return mpl_fig_to_uri(f)

    time_series = generate_random_timeseries(start_date, end_date, option_value)
    if time_series is None:
        f = plt.figure()
        plt.title("Results Empty")
        return mpl_fig_to_uri(f)

    logger.info("plotting figure")
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(time_series.date.values, time_series.quantity)
    plt.xticks(rotation=70)
    plt.title(f"Quantity Time Series for {dropdown_options_val_to_name[option_value]}")
    plt.tight_layout()

    return mpl_fig_to_uri(fig)


@app.callback(
    Output("plotly-figure", "figure"),
    [Input("run-button", "n_clicks")],
    [
        State("date-range", "start_date"),
        State("date-range", "end_date"),
        State("dropdown", "value"),
    ],
)
def fill_plotly_figure(n_clicks, start_date, end_date, option_value):

    if not n_clicks:
        return {}  # 'figure' object is dict-like, can return empty dict for no-op

    time_series = generate_random_timeseries(start_date, end_date, option_value)
    fig = px.line(
        time_series,
        x="date",
        y="quantity",
        title=f"Quantity Time Series for {dropdown_options_val_to_name[option_value]}",
    )
    # remove margins
    # fig.update_layout(margin=dict(l=0, r=0, t=0, b=0, pad=0))
    return fig


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
