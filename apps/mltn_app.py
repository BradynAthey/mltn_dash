import json
import logging

import dash
import dash_core_components as dcc
import dash_html_components as html
from .components import get_cyto_graph, get_static_image

logger = logging.getLogger(__name__)

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

data_map_tab = dcc.Tab(
    label="Data Map",
    children=get_static_image("/assets/images/graph.png"),
)

ontology_tab = dcc.Tab(
    label="Ontology",
    children=get_cyto_graph("apps/assets/graph-elements.json", id="ontology-graph"),
)

app.layout = html.Div(
    dcc.Tabs(children=[data_map_tab, ontology_tab]),
    id="app-container",
    className="flex-container",
)


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
