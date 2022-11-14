import dash_bootstrap_components as dbc 
import dash_html_components as html
import dash_cytoscape as cyto

ontology = html.Div([
    cyto.Cytoscape(
        id='cytoscape-layout-2',
        layout={'name': 'circle','directed':'true','radius':1000},
        style={'height':'1200px','width':'100%'},
        elements=[
            {'data': {'id': 'player', 'label': 'Player'},
                'style':
                    {
                    'background-color': 'black',
                    }},
            {'data': {'id': 'map', 'label': 'Map'},
                'style':
                    {
                    'background-color': '#62897E',
                    }},
            {'data': {'id': 'game_mode', 'label': 'Game\nMode'},
                'style':
                    {
                    'background-color': '#23416A',
                    }},
            {'data': {'id': 'behavior_cohort', 'label': 'Behavior\nCohort'},
                'style':
                    {
                    'background-color': '#8597AD',
                    }},
            {'data': {'id': 'spend_class', 'label': 'Spend\nClass'}, 
                'style':
                    {
                    'background-color': '#2D615F',
                    }},
            {'data': {'id': 'marketing_method', 'label': 'Marketing\nMethod'}, 
                'style':
                    {
                    'background-color': '#5EBBC9',
                    }},
            {'data': {'id': 'engagement_class', 'label': 'Engagement\nClass'}, 
                'style':
                    {
                    'background-color': '#23416A',
                    }},
            {'data': {'id': 'player_2', 'label': 'Player'},
                'style':
                    {
                    'background-color': 'black',
                    }},
            {'data': {'id': 'future_game_dev', 'label': 'Future\nGame\nDev'}, 
                'style':
                    {
                    'background-color': '#23416A',
                    }},
            {'data': {'id': 'bundles', 'label': 'Bundles'}, 
                'style':
                    {
                    'background-color': '#5EBBC9',
                    }},
            {'data': {'id': 'weapon', 'label': 'Weapon'},
                'style':
                    {
                    'background-color': '#D5DEE8',
                    }},
            {'data': {'id': 'blueprint', 'label': 'BluePrint'},
                'style':
                    {
                    'background-color': '#8597AD',
                    }},
            #Define Edges 
            #Edges that all link to Player
            {'data': {'source': 'player', 'target': 'game_mode','label':'Enjoys'}},
            {'data': {'source': 'player', 'target': 'behavior_cohort','label':'Part of'}},
            {'data': {'source': 'player', 'target': 'spend_class','label':'Part of'}},
            {'data': {'source': 'player', 'target': 'marketing_method','label':'Effected by'}},
            {'data': {'source': 'player', 'target': 'engagement_class','label':'Part of'}},
            {'data': {'source': 'player', 'target': 'player_2','label':'Friends with'}},
            {'data': {'source': 'player', 'target': 'player_2','label':'Bullied by'}},
            {'data': {'source': 'player', 'target': 'player_2','label':'Cheating with'}},
            {'data': {'source': 'player', 'target': 'player_2','label':'Influenced by'}},
            {'data': {'source': 'player', 'target': 'future_game_dev'}},
            {'data': {'source': 'player', 'target': 'bundles','label':'Purchased'}},
            {'data': {'source': 'player', 'target': 'weapon','label':'Prefers'}},
            {'data': {'source': 'player', 'target': 'blueprint'}},
            {'data': {'source': 'player', 'target': 'map','label':'Prefers'}},
            
            #Other Edges 
            {'data': {'source': 'marketing_method', 'target': 'engagement_class','label':'Effected by'}},
            {'data': {'source': 'marketing_method', 'target': 'spend_class','label':'Designed for'}},
            {'data': {'source': 'spend_class', 'target': 'behavior_cohort','label':'Related to'}},
            {'data': {'source': 'behavior_cohort', 'target': 'game_mode','label':'Correlates to'}},
            {'data': {'source': 'game_mode', 'target': 'map','label':'Part of'}},
            {'data': {'source': 'map', 'target': 'blueprint','label':'Designed for'}},
            {'data': {'source': 'blueprint', 'target': 'weapon','label':'Includes'}},
            {'data': {'source': 'weapon', 'target': 'bundles'}},
            {'data': {'source': 'bundles', 'target': 'future_game_dev','label':'Impacts'}},
            {'data': {'source': 'game_mode', 'target': 'future_game_dev','label':'Impacts'}},
            {'data': {'source': 'future_game_dev', 'target': 'map'}},
            {'data': {'source': 'blueprint', 'target': 'game_mode'}},

            ],
            stylesheet= [
                {
                    'selector':'node',
                    'style':{
                        'label':'data(label)',
                        'width':'350%',
                        'height':'350%',
                        'text-wrap':'wrap',
                        'text-valign':'center',
                        'text-halign':'center',
                        'text-max-width':"60px",
                        'color':'white',
                        'font-size':'55px',
                    }
                },
                {
                    'selector':'edge',
                    'style':
                        {
                            'width':'3px',
                            'target-arrow-shape':'triangle',
                            'source-arrow-shape':'triangle',
                            'curve-style':'bezier',
                            'label':'data(label)',
                            'edge-text-rotation':'autorotate',
                            'font-size': '40px',
                            'control-point-step-size':'100px'

                        }

                },
        ]
    )
])

layout = html.Div([ontology])