import dash_bootstrap_components as dbc 
import dash_html_components as html

#data_map_image = html.Img(src="/assets/datamap.png",height='55px')

datamap = html.Div([
            dbc.Row([
                dbc.Col([
                    html.Img(src="/assets/datamap.png",height='800px')
                ])
            ])
    ])

layout = html.Div([datamap])#,style={'height':'100%','background-image':'url("../assets/home_bg.jpeg")'})