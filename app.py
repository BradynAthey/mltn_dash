import dash 
import dash_core_components as dcc 
import dash_html_components as html
import pandas as pd
from dash.dependencies import Output, Input
import yaml
import sys

with open('./config.yaml', "r") as f:
    CONFIG = yaml.safe_load(f)

HOST_ADDRESS = CONFIG['HOST_ADDRESS']
PORT_NUMBER = CONFIG['PORT_NUMBER']

print(f'CONFIG READS: HOST - {HOST_ADDRESS}, PORT - {PORT_NUMBER}')

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Machine Learning Transition Toolkit"

app.layout = html.Div(
    children=[
        html.Div(
            children =[
                html.Img(src=app.get_asset_url('valkyrie_logo.png'), className = 'header-image'),
                html.Img(src=app.get_asset_url('Activision_logo.png'), className = 'client-image'),
                html.H1(children='Machine Learning Transition Toolkit',className='header-title'),
                #html.P(children = 'Client Name',className = 'header-description'),
            ],
            className = 'header',
            ),  
        html.Div([
            dcc.Tabs(id = 'tabs-component',value = 'tab-welcome',children=[
                dcc.Tab(label ='Welcome',value ='tab-welcome'),
                dcc.Tab(label='DataMap',value='tab-data-map'),
                dcc.Tab(label ='Ontology Diagram',value='tab-ontology-diagram'),
                dcc.Tab(label='MacroGraph',value='tab-micro_graph'),
                dcc.Tab(label ='Data & ML Readiness',value='tab-ml-readiness'),
                dcc.Tab(label='ROI Assesment',value='tab-roi-assesment'),
                dcc.Tab(label ='Roadmap',value='tab-roadmap'),
                ]),
                html.Div(id = 'tabs_test')
            ],
           # className = 'tabs'
            ),
            html.Div(
                children =[
                    html.Strong('Welcome to the ML Transition Package powered by Valkyrie. \n',className = 'text-area-bold'),
                    html.P([ """You're here because you know your data has untapped potential,
                    and we're here to help you unlock it. \n
                    The tabls above represent the deliverables from this phase of work.
                    Click through to explore a preview of the tools our team will build for you during our engagement. \n
                    Should you have any questions, as always, please feel free to reach out to our team \n """ ],className='text-area-weclcome')
                ],
            className = 'textarea'
            ),
            
            
        ]
            
            
            
    )

@app.callback(Output('tabs_test','children'),
    [Input('tabs-component','value')])

def render_content(tab):
    if tab == 'tab-data-map':
        return html.Div([
            html.H3('Tab content 1'),
            dcc.Graph(
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [3, 1, 2],
                        'type': 'bar'
                    }]
                }
            )
        ])
    elif tab == 'tab-ontology-diagram':
        return html.Div([
            html.H3('Tab content 2'),
            dcc.Graph(
                id='graph-2-tabs-dcc',
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [5, 10, 6],
                        'type': 'bar'
                    }]
                }
            )
        ])

  

if __name__ == '__main__':
    print("Entering main loop")
    if sys.platform.startswith('darwin'):
        app.run_server(debug=True, host=HOST_ADDRESS, port=PORT_NUMBER)
    else:
        app.run_server(debug=False, host=HOST_ADDRESS, port=PORT_NUMBER)