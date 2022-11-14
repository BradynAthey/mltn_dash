from dash import dcc, html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import yaml
import sys

#Internal Imports
from apps import welcome,data_map,ontology


#from apps import home 
from app import app
print(__name__)

with open('./config.yaml', "r") as f:
    CONFIG = yaml.safe_load(f)

HOST_ADDRESS = CONFIG['HOST_ADDRESS']
PORT_NUMBER = CONFIG['PORT_NUMBER']


#banner_image = html.Img(src="/assets/valkyrie_slogan.png",height='70px',width='95%')
title = html.H1(children='Machine Learning Transition Toolkit')
#description = html.P(children = 'Client Name')
navbar = dbc.Navbar(
            # dbc.Container([
                # dbc.Row([
                #         dbc.Col([
                #             banner_image
                #         ])
                #     ]),
                    # dbc.Row([ 
                        dbc.Nav([ 
                            dbc.NavItem(dbc.NavLink("Welcome", href="/welcome",disabled=False)),
                            dbc.NavItem(dbc.NavLink("Data Map", href="/data-map",disabled=False)),
                            dbc.NavItem(dbc.NavLink("Ontology Diagram", href="/ontology-diagram",disabled=False)),
                            dbc.NavItem(dbc.NavLink("MacroGraph", href="/macro-graph",disabled=False)),
                            dbc.NavItem(dbc.NavLink("Data & ML Readiness", href="/data-ml-readiness",disabled=False)),
                            dbc.NavItem(dbc.NavLink("ROI Assessment", href="/roi-assessment",disabled=False)),
                            dbc.NavItem(dbc.NavLink("Roadmap", href="/roadmap",disabled=False)),
                        # ])
                    #])
                ]
            ),className = 'navbar'#style = {"width":"100%", "height":"200px",'border':'2px solid black'}
)
       
app.layout =dbc.Container([
    dcc.Location(id='url', refresh=False),
    html.Div(title,className = 'header-title'),
    html.Div(navbar,className='navbar'),
    html.Div(id = 'page-content-container')
    ],
                className = 'grid-container')

#dbc.Container([
#             dcc.Location(id='url', refresh=False),
#         navbar,
#        html.Div(id = 'page-content-container')
# ],fluid=False,className='grid-container' )

@app.callback(Output('page-content-container', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):

    if pathname == '/welcome':
         return welcome.layout
    elif pathname == '/data-map':
         return data_map.layout
    elif pathname == '/ontology-diagram':
         return ontology.layout
    else:
        return welcome.layout


if __name__ == '__main__':
    print("Entering main loop")
    if sys.platform.startswith('darwin'):
        app.run_server(debug=True, host=HOST_ADDRESS, port=PORT_NUMBER)
    else:
        app.run_server(debug=False, host=HOST_ADDRESS, port=PORT_NUMBER)