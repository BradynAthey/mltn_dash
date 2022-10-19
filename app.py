
print(__name__)

import dash
import os
import dash_bootstrap_components as dbc
BASE_PATH = os.getcwd()

external_stylesheets = [dbc.themes.LUX]#,'https://cdnjs.cloudflare.com/ajax/libs/vis/4.20.1/vis.min.css']
# external_stylesheets = [
#     {
#         "href": "https://fonts.googleapis.com/css2?"
#         "family=Lato:wght@400;700&display=swap",
#         "rel": "stylesheet",
#     },
# ]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Machine Learning Transition Toolkit"
server = app.server 
app.config.suppress_callback_exceptions = True