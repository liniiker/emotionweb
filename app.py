import base64
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_daq as daq
from datetime import datetime
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

import time
import cachetools

def load_data():
  start_time = time.time()
  data = []
  for i in range(100000):
    data.append(i)
  end_time = time.time()
  print("Tempo de carregamento:", end_time - start_time)

@cachetools.cached({})
def load_cached_data():
  start_time = time.time()
  data = []
  for i in range(100000):
    data.append(i)
  end_time = time.time()
  print("Tempo de carregamento:", end_time - start_time)

def main():
  load_cached_data()




#pip freeze > requirements.txt

#maxicon_jpg = 'logos/maxicon.jpg'
#maxicon_base64 = base64.b64encode(open(maxicon_jpg,'rb').read()).decode('ascii')

header_list = ['Time', 'Estado de Carga', 'Velocidade', 'Temperatura1', 'Temperatura2', 'Temperatura3', 'Temperatura4', 'RPM1', 'RPM2', 'RPM3', 'RPM4', 'TEMPERATURA MOTOR']
arq = pd.read_csv('data.csv', names=header_list)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

##################################################

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {

    'backgroundColor': '#000138',
    'color': 'white',
    'padding': '6px'
}

##################################################

app.layout = html.Div([
    html.Div([
        dcc.Interval(id='update_value',
                     interval=900,
                     n_intervals=0),
    ]),

    dcc.Tabs([
        dcc.Tab(label='Página 1', children=[

            dbc.Row([
                dbc.Col([
                    html.Div([
                        dcc.Graph(id='chart',
                                  animate=True,
                                  style={'height': '30vh'}
                                  )
                    ])
                ], width=8, ),
                dbc.Col([

                        html.Div(id='card_1')

                ], width=4),
            ], style={'height': '30vh', 'width': '100vw'}),

            dbc.Row([
                dbc.Col([
                    html.Div([
                        dcc.Graph(id='chart2',
                                  animate=True,
                                  style={'height': '30vh'}
                                  )
                    ])
                ], width=8),
                dbc.Col([

                        html.Div(id='card_2')

                ], width=4),
            ], style={'height': '33vh', 'width': '100vw'}),

            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Disco de freio dianteiro esquerdo", style={'color': 'white'}),
                        dbc.CardBody(html.Div(id='card_3'))
                    ], color='#112c38', style={'height': '25vh'})
                ], width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Disco de freio traseiro esquerdo", style={'color': 'white'}),
                        dbc.CardBody(html.Div(id='card_4'))
                    ], color='#112c38', style={'height': '25vh'})
                ], width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Disco de freio traseiro direito", style={'color': 'white'}),
                        dbc.CardBody(html.Div(id='card_5'))
                    ], color='#112c38', style={'height': '25vh'})
                ], width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Disco de freio dianteiro direito", style={'color': 'white'}),
                        dbc.CardBody(html.Div(id='card_6'))
                    ], color='#112c38', style={'height': '25vh'})
                ], width=3),
            ], style={'height': '30vh', 'width': '100vw', 'padding-top':'1vh'}),
        ], style=tab_style, selected_style=tab_selected_style),

        dcc.Tab(label='Página 2', children=[

        ], style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Página 3', children=[

        ], style=tab_style, selected_style=tab_selected_style),


    ], style=tabs_styles)
], style={'height': '100vh', 'width': '100vw', 'background-color': '#000138'})


# Gráfico 1
@app.callback(Output('chart', 'figure'),
              [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:

        header_list = ['Time', 'Estado de Carga', 'Velocidade', 'Temperatura1', 'Temperatura2', 'Temperatura3',
                       'Temperatura4', 'RPM1', 'RPM2', 'RPM3', 'RPM4', 'TEMPERATURA MOTOR']
        arq_graph = pd.read_csv('data.csv', names = header_list)
        temp_graph = arq_graph['Velocidade'].tail(100)
        time_interval = arq_graph['Time'].tail(100)


    return {
        'data': [go.Scatter(
            x = time_interval,
            y = temp_graph,
            #fill = 'tonexty',
            #fillcolor = 'rgba(255, 0, 255, 0.1)',
            mode = 'lines',
            line = dict(width = 2, color = '#33FFFC'),
            # marker = dict(size = 7, symbol = 'circle', color = '#D35400',
            #               line = dict(color = '#D35400', width = 2)
            #               ),

            hoverinfo = 'text',
            hovertext =
            '<b>Time</b>: ' + time_interval.astype(str) + '<br>' +
            '<b>Speed</b>: ' + [f'{x:,.2f}' for x in temp_graph] + '<br>'


        )],

        'layout': go.Layout(
            # paper_bgcolor = 'rgba(0,0,0,0)',
            # plot_bgcolor = 'rgba(0,0,0,0)',
            plot_bgcolor = 'rgba(50, 53, 70, 0)',
            paper_bgcolor = 'rgba(50, 53, 70, 0)',
            title = {
                'text': 'velocidade',

                'y': 0.97,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont = {
                'color': '#33FFFC',
                'size': 17},

            hovermode = 'closest',
            margin = dict(t = 25, r = 10, l = 70),

            xaxis = dict(range = [min(time_interval), max(time_interval)],
                         title = '<b>Time</b>',
                         color = '#33FFFC',
                         #showspikes=True,
                         showline = True,
                         showgrid = True,
                         linecolor = '#33FFFC',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = '#33FFFC')

                         ),

            yaxis = dict(range = [min(temp_graph) - 3, max(temp_graph) + 5],
                         title = '<b>Km/h</b>',
                         color = '#33FFFC',
                         #showspikes= False,
                         showline = True,
                         showgrid = True,
                         linecolor = '#33FFFC',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = '#33FFFC')

                         ),

            # legend = {
            #     'orientation': 'h',
            #     'bgcolor': '#F2F2F2',
            #     'x': 0.5,
            #     'y': 1.25,
            #     'xanchor': 'center',
            #     'yanchor': 'top'},
            font = dict(
                family = "sans-serif",
                size = 12,
                color = 'green')

        )#oi

            }


# Gráfico 2
@app.callback(Output('chart2', 'figure'),
              [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        header_list = ['Time', 'Estado de Carga', 'Velocidade', 'Temperatura1', 'Temperatura2', 'Temperatura3', 'Temperatura4', 'RPM1', 'RPM2', 'RPM3', 'RPM4', 'TEMPERATURA MOTOR']
        arq_graph2 = pd.read_csv('data.csv', names = header_list)
        temp_graph2 = arq_graph2['Temperatura1'].tail(10)
        time_interval = arq_graph2['Time'].tail(10)


    return {
        'data': [go.Scatter(
            x = time_interval,
            y = temp_graph2,
            #fill = 'tonexty',
            #fillcolor = 'rgba(255, 0, 255, 0.1)',
            mode = 'markers+lines',
            #k
            line = dict(width = 2, color = '#ff00ff'),
            # marker = dict(size = 7, symbol = 'circle', color = '#D35400',
            #               line = dict(color = '#D35400', width = 2)
            #               ),

            hoverinfo = 'text',
            hovertext =
            '<b>Time</b>: ' + time_interval.astype(str) + '<br>' +
            '<b>Bitcoin Price</b>: ' + [f'${x:,.2f}' for x in temp_graph2] + '<br>'


        )],

        'layout': go.Layout(
            # paper_bgcolor = 'rgba(0,0,0,0)',
            # plot_bgcolor = 'rgba(0,0,0,0)',
            plot_bgcolor = 'rgba(50, 53, 70, 0)',
            paper_bgcolor = 'rgba(50, 53, 70, 0)',
            title = {
                'text': 'Título',

                'y': 0.97,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont = {
                'color': 'white',
                'size': 17},

            hovermode = 'x unified',
            margin = dict(t = 25, r = 10, l = 70),

            xaxis = dict(range = [min(time_interval), max(time_interval)],
                         title = '<b>Time</b>',
                         color = 'white',
                         #showspikes=True,
                         showline = True,
                         showgrid = True,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')

                         ),

            yaxis = dict(range = [min(temp_graph2) - 3, max(temp_graph2) + 5],
                         title = '<b>Valor</b>',
                         color = 'white',
                         #showspikes= False,
                         showline = True,
                         showgrid = True,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')

                         ),

            # legend = {
            #     'orientation': 'h',
            #     'bgcolor': '#F2F2F2',
            #     'x': 0.5,
            #     'y': 1.25,
            #     'xanchor': 'center',
            #     'yanchor': 'top'},
            font = dict(
                family = "sans-serif",
                size = 12,
                color = 'white')

        )

            }

# Botão ligado / desligado
@app.callback(Output('card_1','children'),
                [Input('update_value','n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        arq2 = pd.read_csv('data.csv', names=header_list)
        etc = arq2['Estado de Carga'].tail(1).iloc[0]

    if etc > 1:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Br(),
                        dbc.Button(
                            "Carro desligado",
                            id="toggle",
                            color="success",
                            className="me-4",
                            n_clicks=0,
                        ),
                        html.Br(),
                        html.H4(["Estado de carga {0}%".format(etc)],style={'color': 'white'}),
                        daq.GraduatedBar(
                            step=1,
                            size = 400,
                            max=100,
                            color={"gradient": True, "ranges": {"red": [0, 40], "green": [40, 90], "purple": [90, 100]}},
                            showCurrentValue=True,
                            value=etc
                        ),

                    ])
            ]),
        ])
    ]
    else:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Br(),
                        dbc.Button(
                            "Carro ligado",
                            id="toggle",
                            color="danger",
                            className="me-4",
                            n_clicks=0,
                        ),
                        html.Br(),
                        html.H4(["Estado de carga {0}%".format(etc)], style={'color': 'white'}),
                        daq.GraduatedBar(
                            step=1,
                            size=400,
                            max=100,
                            color={"gradient": True,
                                   "ranges": {"red": [0, 40], "green": [40, 90], "purple": [90, 100]}},
                            showCurrentValue=True,
                            value=etc
                        ),

                    ])
                ]),
            ])
        ]

# Informativos das temperaturas e umidade dos containers
@app.callback(Output('card_2','children'),
                [Input('update_value','n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        arq2 = pd.read_csv('data.csv', names=header_list)
        t1_r1 = arq2['Temperatura1'].tail(1).iloc[0]
        rpm1 = arq2['Temperatura1'].tail(1).iloc[0]
    if t1_r1 < 80:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([

                        html.P('Container esquerdo',
                               style={'textAlign': 'center',
                                      'color': 'white',
                                      'fontSize': 15,
                                      'margin-top': '-3px'
                                      }
                               ),
                        html.P('Temperatura - Umidade',
                               style = {'textAlign':'center',
                                        'fontSize':15,
                                        'color':'white',
                                        'margin-top':'-15px'
                                        }),
                        html.P('M1:   {0:,.1f} ºC - {0:,.1f}%'.format(t1_r1,t1_r1),
                               style={'textAlign': 'center',
                                      'color': 'white',
                                      'fontSize': 15,
                                      'font-weight': 'bold',
                                      'margin-top': '-3px',
                                      'line-height': '1',
                                      }
                               ),
                        html.P('M2:   {0:,.1f} ºC - {0:,.1f}%'.format(t1_r1,t1_r1),
                               style={'textAlign': 'center',
                                      'color': 'white',
                                      'fontSize': 15,
                                      'font-weight': 'bold',
                                      'margin-top': '-3px',
                                      'line-height': '1',
                                      }
                               ),
                        html.P('M3:   {0:,.1f} ºC - {0:,.1f}%'.format(t1_r1,t1_r1),
                               style={'textAlign': 'center',
                                      'color': 'white',
                                      'fontSize': 15,
                                      'font-weight': 'bold',
                                      'margin-top': '-3px',
                                      'line-height': '1',
                                      }
                               ),
                        html.P('M4:   {0:,.1f} ºC - {0:,.1f}%'.format(t1_r1,t1_r1),
                               style={'textAlign': 'center',
                                      'color': 'white',
                                      'fontSize': 15,
                                      'font-weight': 'bold',
                                      'margin-top': '-3px',
                                      'line-height': '1',
                                      }
                               ),

                    ]),

                    dbc.Col([

                        html.P('Container direito',
                               style={'textAlign': 'center',
                                      'color': 'white',
                                      'fontSize': 15,
                                      'margin-top': '-3px'
                                      }
                               ),
                        html.P('Temperatura - Umidade',
                               style={'textAlign': 'center',
                                      'fontSize': 15,
                                      'color': 'white',
                                      'margin-top': '-15px'
                                      }),
                        html.P('M1:   {0:,.1f} ºC - {0:,.1f}%'.format(t1_r1,t1_r1),
                               style={'textAlign': 'center',
                                      'color': 'white',
                                      'fontSize': 15,
                                      'font-weight': 'bold',
                                      'margin-top': '-3px',
                                      'line-height': '1',
                                      }
                               ),
                        html.P('M2:   {0:,.1f} ºC - {0:,.1f}%'.format(t1_r1,t1_r1),
                               style={'textAlign': 'center',
                                      'color': 'white',
                                      'fontSize': 15,
                                      'font-weight': 'bold',
                                      'margin-top': '-3px',
                                      'line-height': '1',
                                      }
                               ),
                        html.P('M3:   {0:,.1f} ºC - {0:,.1f}%'.format(t1_r1,t1_r1),
                               style={'textAlign': 'center',
                                      'color': 'white',
                                      'fontSize': 15,
                                      'font-weight': 'bold',
                                      'margin-top': '-3px',
                                      'line-height': '1',
                                      }
                               ),
                        html.P('M4:   {0:,.1f} ºC - {0:,.1f}%'.format(t1_r1,t1_r1),
                               style={'textAlign': 'center',
                                      'color': 'white',
                                      'fontSize': 15,
                                      'font-weight': 'bold',
                                      'margin-top': '-3px',
                                      'line-height': '1',
                                      }
                               ),

                    ]),
                ])
            ])
        ]
    else:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([

                        html.P('Container esquerdo',
                               style={'textAlign': 'center',
                                      'color': 'red',
                                      'fontSize': 15,
                                      'margin-top': '-3px'
                                      }
                               ),
                        html.P('Temperatura - Umidade',
                               style={'textAlign': 'center',
                                      'fontSize': 15,
                                      'color': 'red',
                                      'margin-top': '-15px'
                                      }),
                        html.P('M1:   {0:,.1f} ºC - {0:,.1f}%'.format(t1_r1, t1_r1),
                               style={'textAlign': 'center',
                                      'color': 'red',
                                      'fontSize': 15,
                                      'font-weight': 'bold',
                                      'margin-top': '-3px',
                                      'line-height': '1',
                                      }
                               ),
                        html.P('M2:   {0:,.1f} ºC - {0:,.1f}%'.format(t1_r1, t1_r1),
                               style={'textAlign': 'center',
                                      'color': 'red',
                                      'fontSize': 15,
                                      'font-weight': 'bold',
                                      'margin-top': '-3px',
                                      'line-height': '1',
                                      }
                               ),
                        html.P('M3:   {0:,.1f} ºC - {0:,.1f}%'.format(t1_r1, t1_r1),
                               style={'textAlign': 'center',
                                      'color': 'red',
                                      'fontSize': 15,
                                      'font-weight': 'bold',
                                      'margin-top': '-3px',
                                      'line-height': '1',
                                      }
                               ),
                        html.P('M4:   {0:,.1f} ºC - {0:,.1f}%'.format(t1_r1, t1_r1),
                               style={'textAlign': 'center',
                                      'color': 'red',
                                      'fontSize': 15,
                                      'font-weight': 'bold',
                                      'margin-top': '-3px',
                                      'line-height': '1',
                                      }
                               ),

                    ]),

                    dbc.Col([

                        html.P('Container direito',
                               style={'textAlign': 'center',
                                      'color': 'red',
                                      'fontSize': 15,
                                      'margin-top': '-3px'
                                      }
                               ),
                        html.P('Temperatura - Umidade',
                               style={'textAlign': 'center',
                                      'fontSize': 15,
                                      'color': 'red',
                                      'margin-top': '-15px'
                                      }),
                        html.P('M1:   {0:,.1f} ºC - {0:,.1f}%'.format(t1_r1, t1_r1),
                               style={'textAlign': 'center',
                                      'color': 'red',
                                      'fontSize': 15,
                                      'font-weight': 'bold',
                                      'margin-top': '-3px',
                                      'line-height': '1',
                                      }
                               ),
                        html.P('M2:   {0:,.1f} ºC - {0:,.1f}%'.format(t1_r1, t1_r1),
                               style={'textAlign': 'center',
                                      'color': 'red',
                                      'fontSize': 15,
                                      'font-weight': 'bold',
                                      'margin-top': '-3px',
                                      'line-height': '1',
                                      }
                               ),
                        html.P('M3:   {0:,.1f} ºC - {0:,.1f}%'.format(t1_r1, t1_r1),
                               style={'textAlign': 'center',
                                      'color': 'red',
                                      'fontSize': 15,
                                      'font-weight': 'bold',
                                      'margin-top': '-3px',
                                      'line-height': '1',
                                      }
                               ),
                        html.P('M4:   {0:,.1f} ºC - {0:,.1f}%'.format(t1_r1, t1_r1),
                               style={'textAlign': 'center',
                                      'color': 'red',
                                      'fontSize': 15,
                                      'font-weight': 'bold',
                                      'margin-top': '-3px',
                                      'line-height': '1',
                                      }
                               ),

                    ]),
                ])
            ])
        ]

@app.callback(Output('card_3','children'),
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
                        daq.LEDDisplay(
                            label='TEMPERATURA ºC', style={'color': 'white'},
                            value=t1_r1,
                            color='white',
                            backgroundColor="red",
                            size=20
                        ),

                    ]),
                    dbc.Col([
                        daq.LEDDisplay(
                            label='RPM', style={'color': 'white'},
                            value=rpm1,
                            color='white',
                            backgroundColor="#112c38",
                            size=20
                        ),

                    ])
                ])
            ]),
        ]

    if 30 <= t1_r1 <= 80:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        daq.LEDDisplay(
                            label='TEMPERATURA ºC', style={'color': 'white'},
                            value=t1_r1,
                            color='white',
                            backgroundColor="080f68",
                            size=20
                        ),

                    ]),
                    dbc.Col([
                        daq.LEDDisplay(
                            label='RPM', style={'color': 'white'},
                            value=rpm1,
                            color='white',
                            backgroundColor="#112c38",
                            size=20
                        ),

                    ])
                ])
            ]),
        ]

    if t1_r1 < 30:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        daq.LEDDisplay(
                            label='TEMPERATURA ºC', style={'color': 'white'},
                            value=t1_r1,
                            color='white',
                            backgroundColor="purple",
                            size=20
                        ),

                    ]),
                    dbc.Col([
                        daq.LEDDisplay(
                            label='RPM', style={'color': 'white'},
                            value=rpm1,
                            color='white',
                            backgroundColor="#112c38",
                            size=20
                        ),

                    ])
                ])
            ]),
        ]

@app.callback(Output('card_4','children'),
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
                        daq.LEDDisplay(
                            label='TEMPERATURA ºC', style={'color': 'white'},
                            value=t1_r1,
                            color='white',
                            backgroundColor="red",
                            size=20
                        ),

                    ]),
                    dbc.Col([
                        daq.LEDDisplay(
                            label='RPM', style={'color': 'white'},
                            value=rpm1,
                            color='white',
                            backgroundColor="#112c38",
                            size=20
                        ),

                    ])
                ])
            ]),
        ]

    if 30 <= t1_r1 <= 80:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        daq.LEDDisplay(
                            label='TEMPERATURA ºC', style={'color': 'white'},
                            value=t1_r1,
                            color='white',
                            backgroundColor="080f68",
                            size=20
                        ),

                    ]),
                    dbc.Col([
                        daq.LEDDisplay(
                            label='RPM', style={'color': 'white'},
                            value=rpm1,
                            color='white',
                            backgroundColor="#112c38",
                            size=20
                        ),

                    ])
                ])
            ]),
        ]

    if t1_r1 < 30:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        daq.LEDDisplay(
                            label='TEMPERATURA ºC', style={'color': 'white'},
                            value=t1_r1,
                            color='white',
                            backgroundColor="purple",
                            size=20
                        ),

                    ]),
                    dbc.Col([
                        daq.LEDDisplay(
                            label='RPM', style={'color': 'white'},
                            value=rpm1,
                            color='white',
                            backgroundColor="#112c38",
                            size=20
                        ),

                    ])
                ])
            ]),
        ]

@app.callback(Output('card_5','children'),
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
                        daq.LEDDisplay(
                            label='TEMPERATURA ºC', style={'color': 'white'},
                            value=t1_r1,
                            color='white',
                            backgroundColor="red",
                            size=20
                        ),

                    ]),
                    dbc.Col([
                        daq.LEDDisplay(
                            label='RPM', style={'color': 'white'},
                            value=rpm1,
                            color='white',
                            backgroundColor="#112c38",
                            size=20
                        ),

                    ])
                ])
            ]),
        ]

    if 30 <= t1_r1 <= 80:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        daq.LEDDisplay(
                            label='TEMPERATURA ºC', style={'color': 'white'},
                            value=t1_r1,
                            color='white',
                            backgroundColor="blue",
                            size=20
                        ),

                    ]),
                    dbc.Col([
                        daq.LEDDisplay(
                            label='RPM', style={'color': 'white'},
                            value=rpm1,
                            color='white',
                            backgroundColor="#112c38",
                            size=20
                        ),

                    ])
                ])
            ]),
        ]

    if t1_r1 < 30:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        daq.LEDDisplay(
                            label='TEMPERATURA ºC', style={'color': 'white'},
                            value=t1_r1,
                            color='white',
                            backgroundColor="purple",
                            size=20
                        ),

                    ]),
                    dbc.Col([
                        daq.LEDDisplay(
                            label='RPM', style={'color': 'white'},
                            value=rpm1,
                            color='white',
                            backgroundColor="#112c38",
                            size=20
                        ),

                    ])
                ])
            ]),
        ]

@app.callback(Output('card_6','children'),
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
                        daq.LEDDisplay(
                            label='TEMPERATURA ºC', style={'color': 'white'},
                            value=t1_r1,
                            color='white',
                            backgroundColor="red",
                            size=20
                        ),

                    ]),
                    dbc.Col([
                        daq.LEDDisplay(
                            label='RPM', style={'color': 'white'},
                            value=rpm1,
                            color='white',
                            backgroundColor="#112c38",
                            size=20
                        ),

                    ])
                ])
            ]),
        ]

    if 30 <= t1_r1 <= 80:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        daq.LEDDisplay(
                            label='TEMPERATURA ºC', style={'color': 'white'},
                            value=t1_r1,
                            color='white',
                            backgroundColor="blue",
                            size=20
                        ),

                    ]),
                    dbc.Col([
                        daq.LEDDisplay(
                            label='RPM', style={'color': 'white'},
                            value=rpm1,
                            color='white',
                            backgroundColor="#112c38",
                            size=20
                        ),

                    ])
                ])
            ]),
        ]

    if t1_r1 < 30:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        daq.LEDDisplay(
                            label='TEMPERATURA ºC', style={'color': 'white'},
                            value=t1_r1,
                            color='white',
                            backgroundColor="purple",
                            size=20
                        ),

                    ]),
                    dbc.Col([
                        daq.LEDDisplay(
                            label='RPM', style={'color': 'white'},
                            value=rpm1,
                            color='white',
                            backgroundColor="#112c38",
                            size=20
                        ),

                    ])
                ])
            ]),
        ]

if __name__ == '__main__':
    main()
    app.run_server(debug=True, port=2020)