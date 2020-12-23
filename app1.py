# -*- coding: utf-8 -*-
"""
Module doc string
"""
import pathlib
import json
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output

import rdflib
g = rdflib.Graph()
g.parse("FinalOnto.owl")

def trouverInput(inp):
    qres1 = g.query(
        """
            SELECT ?input
            WHERE {
            :"""+inp+""" :has_input ?input.
                    }""")
    ls =[]
    for row in qres1:
        for col in row:
            ls.append(col.rsplit('#')[-1])
    return ls[0]

def trouverOutput(inp):
    qres1 = g.query(
        """
            SELECT ?output
            WHERE {
            :"""+inp+""" :has_output ?output.
                    }""")
    ls =[]
    for row in qres1:
        for col in row:
            ls.append(col.rsplit('#')[-1])
    return ls[0]

def trouverToolsAndTech(inp):
    qres1 = g.query(
        """
            SELECT ?tool
            WHERE {
            :"""+inp+""" :has_tool ?tool.	
                    }""")
    ls =[]
    for row in qres1:
        for col in row:
            ls.append(col.rsplit('#')[-1])
    return ls

def trouverDescription(objet):
    objet=objet.replace('_'," ")
    import pandas as pd
    dd=pd.read_table("sample.txt")
    resultat=""
    for s in dd[dd.columns[0]]:
        if objet in s:
            resultat+=s
    return resultat

NAVBAR = dbc.Navbar(
    children=[
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [

                    dbc.Col(
                        dbc.NavbarBrand("Decision Support System for Project Management based on Ontology Learning", className="ml-2")
                    ),
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://plot.ly",
        )
    ],
    color="dark",
    dark=True,
    sticky="top",
)

LEFT_COLUMN = dbc.Jumbotron(
    [
    ]
)


TOP_BIGRAM_COMPS = [
    dbc.CardHeader(html.H2("Please submit your request: ")),
    dbc.CardBody(
        [
            dcc.Loading(
                id="loading-bigrams-comps",
                children=[
#
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                   dbc.Input(id="inputNLP", placeholder="Type something...", type="text"),

                                ],

                            ),

                        ]
                    ),

                ],
                type="default",
            )
        ],
        style={"marginTop": 0, "marginBottom": 0},
    ),
]


TOP_BIGRAM_COMPS1 = [
    dbc.CardBody(
        [
            dcc.Loading(
                id="loading-bigrams-comps4",
                children=[
                    dbc.Row(
                        [
                            dbc.Col(html.H3("Input"), md=12),


                        ]
                    ),
    dbc.Alert(
    [
        html.H4("Well done!", className="alert-heading" , id="output1"),
        html.Hr(),
        html.P("Tools.", id="outputR1",
            className="mb-0",
        ),
    ]
)
                ],
                type="default",
            )
        ],
        style={"marginTop": 0, "marginBottom": 0},
    ),
]


TOP_BIGRAM_COMPS2 = [
    dbc.CardBody(
        [
            dcc.Loading(
                id="loading-bigrams-comps2",
                children=[
                    dbc.Row(
                        [
                            dbc.Col(html.H3("Ouput"), md=12),


                        ]
                    ),
dbc.Alert(
    [
        html.H4("Well done!", className="alert-heading" , id="output2"),
        #html.Ul(id='my-list', children=[html.Li(i) for i in ["aaa","bbb","ccc","ddd"]]),


        html.Hr(),
        html.P( "Tools.", id="outputR2"
        ),
    ],
    color="warning",
)
                ],
                type="default",
            )
        ],
        style={"marginTop": 0, "marginBottom": 0},
    ),
]

TOP_BIGRAM_COMPS3 = [
    dbc.CardBody(
        [
            dcc.Loading(
                id="loading-bigrams-comps1",
                children=[
                    dbc.Row(
                        [
                            dbc.Col(html.H3("Tools and Techniques"), md=12),


                        ]
                    ),
dbc.Alert(
    [
        html.H4("Well done!", className="alert-heading" , id="output3"),
        #html.Ul(id='my-list', children=[html.Li(i) for i in ["aaa","bbb","ccc","ddd"]]),


        html.Hr(),
        html.P( "Tools.", id="outputR3"
        ),
    ],
    color="warning",
)
                ],
                type="default",
            )
        ],
        style={"marginTop": 0, "marginBottom": 0},
    ),
]

BODY = dbc.Container(
    [
        dbc.Row([dbc.Col(dbc.Card(TOP_BIGRAM_COMPS)),], style={"marginTop": 30}),
        dbc.Row([dbc.Col(dbc.Card(TOP_BIGRAM_COMPS1)),], style={"marginTop": 30}),
        dbc.Row([dbc.Col(dbc.Card(TOP_BIGRAM_COMPS2)),], style={"marginTop": 30}),
        dbc.Row([dbc.Col(dbc.Card(TOP_BIGRAM_COMPS3)),], style={"marginTop": 30}),


    ],
    className="mt-12",
)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # for Heroku deployment

app.layout = html.Div(children=[NAVBAR, BODY])

"""
#  Callbacks
"""

#tools

@app.callback(
    Output("output3", "children"),
    [Input("inputNLP", "value")]
)
def update_output3(inputNLP):
    
    return '{}'.format(inputNLP)

@app.callback(
    Output("outputR3", "children"),
    [Input("inputNLP", "value")]
)
def update_NLP3(outputR3):
    value = "NLP3"
    trends = ['python', 'flask', 'java']

    return '{}'.format(value)

#Output

@app.callback(
    Output("output2", "children"),
    [Input("inputNLP", "value")]
)
def update_output2(inputNLP):
    if  trouverOutput(inputNLP) != None:
        return '{}'.format(trouverOutput(inputNLP)+": "+trouverDescription(trouverOutput(inputNLP)))
    else :
        return '{}'.format("- - -")

@app.callback(
    Output("outputR2", "children"),
    [Input("inputNLP", "value")]
)
def update_NLP2(outputR2):
    value = "Imported from PMBOK"
    return '{}'.format(value)


#Input
@app.callback(
    Output("output1", "children"),
    [Input("inputNLP", "value")]
)
def update_output1(inputNLP):
    if  trouverInput(inputNLP) != None:
        return '{}'.format(trouverInput(inputNLP)+": "+trouverDescription(trouverInput(inputNLP)))
    else :
        return '{}'.format("- - -")



@app.callback(
    Output("outputR1", "children"),
    [Input("inputNLP", "value")]
)
def update_NLP1(outputR1):
    value = "Imported from PMBOK"
    return '{}'.format(value)









if __name__ == "__main__":
    app.run_server(debug=True)
