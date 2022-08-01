import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import dash_daq as daq
from datetime import datetime
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output
import pandas as pd


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

header_list = ['Time', 'Estado de Carga', 'Velocidade', 'Temperatura1', 'Temperatura2', 'Temperatura3', 'Temperatura4', 'RPM1', 'RPM2', 'RPM3', 'RPM4', 'TEMPERATURA MOTOR']
arq = pd.read_csv('data.csv', names=header_list)


card_style = {
    'padding':'10px'
}
app.layout = html.Div([

    dbc.Row([
        dbc.Col([
            dbc.CardImg(src=r"C:\\Users\\elima\\Desktop\\E-MOTION\\painelemotion\\img\\logo_branco.png",
                        style={'height': '67px',
                               'width': '135px',
                               }
                        )
                ], width=4),

        dbc.Col([
            html.Div("FÓRMULA E.MOTION UFPB",
                    style = {'color': 'white', 'fontSize': 30, 'textAlign': 'center'})
                ], width=4),

        dbc.Col([
            dbc.CardImg(src ="logos/logoufpb.png",
                        className = 'align-self-center',
                        style = {'height':'64px',
                                'width':'45px',
                                })
                ], width=4),
        ], style = {'background-color':'#181a25', 'textAlign':'center'},
    ), # mb-4 aparentemente serve como um padding bot

    dbc.Row(html.Hr(),style = {'color':'white', 'background-color':'#000138'}),
    html.Div([
        dcc.Interval(id = 'update_value',
                     interval = 500,
                     n_intervals = 0)
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.H2('Roda Dianteira Esquerda', style = {'color':'white', 'textAlign':'center'}),
                dbc.CardBody(html.Div(id='card_1'))
            ], color='#112c38', style={'height':'52vh'})
        ], width= 4),
        dbc.Col([
            dbc.Card([
                html.H2('VELOCIDADE', style = {'color':'white', 'textAlign':'center'}),
                dbc.CardBody(html.Div(id='card_2'))
            ], color='#112c38', style={'height':'52vh'})
        ], width= 4), # colocando um style aqui, posso aumentar o tamanho da coluna, ou fazer isso na row, para n encostar na row de baixo
        dbc.Col([
            dbc.Card([
                html.H2('Roda Dianteira Direita', style={'color': 'white', 'textAlign': 'center'}),
                dbc.CardBody(html.Div(id='card_3'))
            ], color='#112c38', style={'height':'52vh'})
        ], width=4, style = {'padding-bottom':'10vh'}),
    ], style = {'background-color':'#000138'}),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.H2('Roda Traseira Esquerda', style = {'color':'white', 'textAlign':'center'}),
                dbc.CardBody(html.Div(id='card_4'))
            ], color='#112c38', style = card_style)
        ], width= 4),
        dbc.Col([
            dbc.Card([
                html.H2('Estado de Carga', style = {'color':'white', 'textAlign':'center'}),
                dbc.CardBody(html.Div(id='card_5'))
            ], color='#112c38', style = card_style)
        ], width= 4),
        dbc.Col([
            dbc.Card([
                html.H2('Roda Traseira Direita', style={'color': 'white', 'textAlign': 'center'}),
                dbc.CardBody(html.Div(id='card_6'))
            ], color='#112c38', style=card_style)
        ], width=4),
    ], style = {'background-color':'#000138'}),
])

@app.callback(Output('card_1','children'),
                [Input('update_value','n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        arq2 = pd.read_csv('data.csv', names=header_list)
        t1_r1 = arq2['Temperatura1'].tail(1).iloc[0]
        rpm1 = arq2['RPM1'].tail(1).iloc[0]
    if t1_r1 > 80:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            daq.LEDDisplay(
                                label='TEMPERATURA ºc', style = {'color':'white'},
                                value=t1_r1,
                                color='white',
                                backgroundColor="red"
                                    ),
                            html.Br(),
                            daq.LEDDisplay(
                                label='RPM', style={'color': 'white'},
                                value=rpm1,
                                color='white',
                                backgroundColor="#112c38"
                                    )
                                ])
                            ]),
                    ])
            ]),
        ]

    if 30 <= t1_r1 <= 80:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            daq.LEDDisplay(
                                label='TEMPERATURA ºc', style = {'color':'white'},
                                value=t1_r1,
                                color='white',
                                backgroundColor="gray"
                                    ),
                            html.Br(),
                            daq.LEDDisplay(
                                label='RPM', style={'color': 'white'},
                                value=rpm1,
                                color='white',
                                backgroundColor="#112c38"
                                    )
                                ])
                            ]),
                    ])
            ]),
        ]

    if t1_r1 < 30:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            daq.LEDDisplay(
                                label='TEMPERATURA ºc', style = {'color':'white'},
                                value=t1_r1,
                                color='white',
                                backgroundColor="green"
                                    ),
                            html.Br(),
                            daq.LEDDisplay(
                                label='RPM', style={'color': 'white'},
                                value=rpm1,
                                color='white',
                                backgroundColor="#112c38"
                                    )
                                ])
                            ]),
                    ])
            ]),
        ]

@app.callback(Output('card_2', 'children'),
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        arq2 = pd.read_csv('data.csv', names=header_list)
        velo = arq2['Velocidade'].tail(1).iloc[0]
    if velo > 0:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            daq.Gauge(
                                color={"gradient": True, "ranges": {"purple": [0, 20], "green": [20, 60], "yellow": [60, 80], "red": [80, 140], "#800903":[140, 150]}},
                                showCurrentValue=True,
                                units="KMH",
                                value=velo,
                                #label='VELOCIMETRO',
                                style={'color': 'white', 'textAlign':'center'},
                                max=150,
                                min=0
                            ),
                            #daq.LEDDisplay(
                            #    value=velo,
                            #    color='white',
                            #    backgroundColor="#112c38",
                            #    style = {'textAlign':'center'}
                            #)
                        ])
                    ]),
                ])
            ]),
        ]
    if velo <= 0:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            daq.Gauge(
                                color={"gradient": True, "ranges": {"purple": [0, 20], "green": [20, 60], "yellow": [60, 80], "red": [80, 140], "#800903":[140, 150]}},
                                showCurrentValue=True,
                                units="KMH",
                                value=velo,
                                #label='VELOCIMETRO',
                                style={'color': 'white', 'textAlign':'center'},
                                max=150,
                                min=0
                            ),
                            #daq.LEDDisplay(
                            #    value=velo,
                            #    color='white',
                            #    backgroundColor="#112c38",
                            #    style = {'textAlign':'center'}
                            #)
                        ])
                    ]),
                ])
            ]),
        ]


@app.callback(Output('card_3', 'children'),
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        arq2 = pd.read_csv('data.csv', names=header_list)
        t2_r2 = arq2['Temperatura2'].tail(1).iloc[0]
        rpm2 = arq2['RPM2'].tail(1).iloc[0]
    if t2_r2 > 80:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            daq.LEDDisplay(
                                label='TEMPERATURA ºc', style={'color': 'white'},
                                value=t2_r2,
                                color='white',
                                backgroundColor="red"
                            ),
                            html.Br(),
                            daq.LEDDisplay(
                                label='RPM', style={'color': 'white'},
                                value=rpm2,
                                color='white',
                                backgroundColor="#112c38"
                            )
                        ])
                    ]),
                ])
            ]),
        ]

    if 30 <= t2_r2 <= 80:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            daq.LEDDisplay(
                                label='TEMPERATURA ºc', style={'color': 'white'},
                                value=t2_r2,
                                color='white',
                                backgroundColor="gray"
                            ),
                            html.Br(),
                            daq.LEDDisplay(
                                label='RPM', style={'color': 'white'},
                                value=rpm2,
                                color='white',
                                backgroundColor="#112c38"
                            )
                        ])
                    ]),
                ])
            ]),
        ]

    if t2_r2 < 30:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            daq.LEDDisplay(
                                label='TEMPERATURA ºc', style={'color': 'white'},
                                value=t2_r2,
                                color='white',
                                backgroundColor="green"
                            ),
                            html.Br(),
                            daq.LEDDisplay(
                                label='RPM', style={'color': 'white'},
                                value=rpm2,
                                color='white',
                                backgroundColor="#112c38"
                            )
                        ])
                    ]),
                ])
            ]),
        ]


@app.callback(Output('card_4', 'children'),
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        arq2 = pd.read_csv('data.csv', names=header_list)
        t3_r3 = arq2['Temperatura3'].tail(1).iloc[0]
        rpm3 = arq2['RPM3'].tail(1).iloc[0]
    if t3_r3 > 80:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            daq.LEDDisplay(
                                label='TEMPERATURA ºc', style={'color': 'white'},
                                value=t3_r3,
                                color='white',
                                backgroundColor="red"
                            ),
                            html.Br(),
                            daq.LEDDisplay(
                                label='RPM', style={'color': 'white'},
                                value=rpm3,
                                color='white',
                                backgroundColor="#112c38"
                            )
                        ])
                    ]),
                ])
            ]),
        ]

    if 30 <= t3_r3 <= 80:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            daq.LEDDisplay(
                                label='TEMPERATURA ºc', style={'color': 'white'},
                                value=t3_r3,
                                color='white',
                                backgroundColor="gray"
                            ),
                            html.Br(),
                            daq.LEDDisplay(
                                label='RPM', style={'color': 'white'},
                                value=rpm3,
                                color='white',
                                backgroundColor="#112c38"
                            )
                        ])
                    ]),
                ])
            ]),
        ]

    if t3_r3 < 30:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            daq.LEDDisplay(
                                label='TEMPERATURA ºc', style={'color': 'white'},
                                value=t3_r3,
                                color='white',
                                backgroundColor="green"
                            ),
                            html.Br(),
                            daq.LEDDisplay(
                                label='RPM', style={'color': 'white'},
                                value=rpm3,
                                color='white',
                                backgroundColor="#112c38"
                            )
                        ])
                    ]),
                ])
            ]),
        ]


@app.callback(Output('card_5', 'children'),
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        arq2 = pd.read_csv('data.csv', names=header_list)
        ec_b = arq2['Estado de Carga'].tail(1).iloc[0]
        tm = arq2['TEMPERATURA MOTOR'].tail(1).iloc[0]
    if ec_b >= 0:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            daq.GraduatedBar(
                                label = 'carga', style = {'color':'black', 'textAlign':'center'},
                                showCurrentValue=True,
                                color={"gradient": True, "ranges": {"red": [0, 10], "yellow": [10, 70], "purple": [70, 100]}},
                                min=0,
                                max=100,
                                step=5,
                                value=ec_b
                            ),
                            html.Br(),
                            daq.LEDDisplay(
                                label='TEMPERATURA MOTOR ºc',style={'color': 'white'},
                                value=tm,
                                color='white',
                                backgroundColor="#112c38"
                            )
                        ])
                    ]),
                ])
            ]),
        ]


@app.callback(Output('card_6', 'children'),
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        arq2 = pd.read_csv('data.csv', names=header_list)
        t4_r4 = arq2['Temperatura4'].tail(1).iloc[0]
        rpm4 = arq2['RPM4'].tail(1).iloc[0]
    if t4_r4 > 80:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            daq.LEDDisplay(
                                label='TEMPERATURA ºc', style={'color': 'white'},
                                value=t4_r4,
                                color='white',
                                backgroundColor="red"
                            ),
                            html.Br(),
                            daq.LEDDisplay(
                                label='RPM', style={'color': 'white'},
                                value=rpm4,
                                color='white',
                                backgroundColor="#112c38"
                            )
                        ])
                    ]),
                ])
            ]),
        ]

    if 30 <= t4_r4 <= 80:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            daq.LEDDisplay(
                                label='TEMPERATURA ºc', style={'color': 'white'},
                                value=t4_r4,
                                color='white',
                                backgroundColor="gray"
                            ),
                            html.Br(),
                            daq.LEDDisplay(
                                label='RPM', style={'color': 'white'},
                                value=rpm4,
                                color='white',
                                backgroundColor="#112c38"
                            )
                        ])
                    ]),
                ])
            ]),
        ]

    if t4_r4 < 30:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            daq.LEDDisplay(
                                label='TEMPERATURA ºc', style={'color': 'white'},
                                value=t4_r4,
                                color='white',
                                backgroundColor="green"
                            ),
                            html.Br(),
                            daq.LEDDisplay(
                                label='RPM', style={'color': 'white'},
                                value=rpm4,
                                color='white',
                                backgroundColor="#112c38"
                            )
                        ])
                    ]),
                ])
            ]),
        ]
if __name__ == '__main__':
    app.run_server(debug=True, port=8888)
    #app.run_server(host='0.0.0.0', debug=True)

