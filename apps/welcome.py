import dash_html_components as html


welcome_text = 'Welcome to the ML Transition Package powered by Valkyrie. \n'
about_text = """\n You're here because you know your data has untapped potential,
                and we're here to help you unlock it. \n
                The tabs above represent the deliverables from this phase of work.
                Click through to explore a preview of the tools our team will build for you during our engagement. \n
                Should you have any questions, as always, please feel free to reach out to our team \n """ 

#title = html.H1(children='Machine Learning Transition Toolkit'),#className='header-title')
description = html.P(children = 'Client Name')

# title  = dbc.Row([
#                 html.Div(title),
#                  ])
# text = dbc.Row([
#             dbc.Col([
#                 html.Strong([welcome_text]),
#                 html.P([about_text])
#                 ],
#              className = 'textarea'
#             )
#         ])

# welcome_page = html.Div([
#         # dbc.Row([
#         #         dbc.Col([
#         #                 html.Div(title),
#         #                 #html.Div(text),
#         # ]),
#         dbc.Row([
#                 dbc.Col([
#                          html.Div(text),
#                 # ]),
#                 # dbc.Col([
#                 #         html.Img(src="/assets/valkyrie_intro_page.jpg")#,height='800px',width = '650px')
#                 ],)#style = {'margin-top':'10px'})
#         ])
# ])

layout = html.Div([html.Strong([welcome_text]),
                html.P([about_text])
                ],
             className = 'text-area')
        # style= {'background-image':"url('/assets/network1.jpg')",
        # 'background-size': 'cover',
        # 'background-position':'center',
        # 'background-size':'100%',
        # 'width':'100%', 
        # 'height':'100%',
        # 'top':'0px',
        # 'left':'0px'})


# from dash import dcc, html
# from app import app 

# app.layout = html.Div(
#     children=[
#         html.Div(
#             children =[
#                 html.Img(src=app.get_asset_url('valkyrie_logo.png'), className = 'header-image'),
#                 html.Img(src=app.get_asset_url('Activision_logo.png'), className = 'client-image'),
#                 html.H1(children='Machine Learning Transition Toolkit',className='header-title'),
#                 #html.P(children = 'Client Name',className = 'header-description'),
#             ],
#             className = 'header',
#             ),  
#         html.Div([
#             dcc.Tabs(id = 'tabs-component',value = 'tab-welcome',children=[
#                 dcc.Tab(label ='Welcome',value ='tab-welcome'),
#                 dcc.Tab(label='DataMap',value='tab-data-map'),
#                 dcc.Tab(label ='Ontology Diagram',value='tab-ontology-diagram'),
#                 dcc.Tab(label='MacroGraph',value='tab-micro_graph'),
#                 dcc.Tab(label ='Data & ML Readiness',value='tab-ml-readiness'),
#                 dcc.Tab(label='ROI Assesment',value='tab-roi-assesment'),
#                 dcc.Tab(label ='Roadmap',value='tab-roadmap'),
#                 ]),
#                 html.Div(id = 'tabs_test')
#             ],
#            # className = 'tabs'
#             ),
#             html.Div(
#                 children =[
#                     html.Strong('Welcome to the ML Transition Package powered by Valkyrie. \n',className = 'text-area-bold'),
#                     html.P([ """You're here because you know your data has untapped potential,
#                     and we're here to help you unlock it. \n
#                     The tabls above represent the deliverables from this phase of work.
#                     Click through to explore a preview of the tools our team will build for you during our engagement. \n
#                     Should you have any questions, as always, please feel free to reach out to our team \n """ ],className='text-area-weclcome')
#                 ],
#             className = 'textarea'
#             ),
            
            
#         ]
            
            
            
#     )