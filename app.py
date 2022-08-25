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


#pip freeze > requirements.txt

#maxicon_jpg = 'logos/maxicon.jpg'
#maxicon_base64 = base64.b64encode(open(maxicon_jpg,'rb').read()).decode('ascii')

header_list = ['Time', 'Estado de Carga', 'Velocidade', 'Temperatura1', 'Temperatura2', 'Temperatura3', 'Temperatura4', 'RPM1', 'RPM2', 'RPM3', 'RPM4', 'TEMPERATURA MOTOR']
arq = pd.read_csv('data.csv', names=header_list)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.Div([
        dcc.Interval(id = 'update_value',
        interval = 900,
        n_intervals= 0),
    ]),

    dbc.Row([
        dbc.Col([
            html.Div([
                dcc.Graph(id = 'chart',
                          animate = True,
                          style = {'height':'30vh'}
                )
            ])
        ],width=8,),
        dbc.Col([
            dbc.Card([
                dbc.CardBody(html.Div(id='card_1'))
            ], color='#112c38', style = {'height':'30vh'})
        ],width=4),
    ], style={'height':'30vh','width':'100vw'}),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div([
                dcc.Graph(id = 'chart2',
                          animate = True,
                          style = {'height':'30vh'}
                )
            ])
        ],width=8),
        dbc.Col([
            dbc.Card([
                dbc.CardBody(html.Div(id='card_2'))
            ], color='#112c38', style = {'height':'30vh'})
        ],width=4),
    ], style={'height':'30vh','width':'100vw'}),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div([
                dcc.Graph(id = 'chart3',
                          animate = True,
                          style = {'height':'30vh'}
                )
            ])
        ],width=8),
        dbc.Col([
            dbc.Card([
                dbc.CardBody(html.Div(id='card_3'))
            ], color='#112c38', style = {'height':'30vh'})
        ],width=4),
    ], style={'height':'30vh','width':'100vw'}),
], style={'height':'100vh','width':'100vw','background-color':'#000138'})

@app.callback(Output('chart', 'figure'),
              [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:

        header_list = ['Time', 'Estado de Carga', 'Velocidade', 'Temperatura1', 'Temperatura2', 'Temperatura3',
                       'Temperatura4', 'RPM1', 'RPM2', 'RPM3', 'RPM4', 'TEMPERATURA MOTOR']
        bitcoin_df = pd.read_csv('data.csv', names = header_list)
        bitcoin_price = bitcoin_df['Temperatura1'].tail(100)
        time_interval = bitcoin_df['Time'].tail(100)


    return {
        'data': [go.Scatter(
            x = time_interval,
            y = bitcoin_price,
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
            '<b>Bitcoin Price</b>: ' + [f'${x:,.2f}' for x in bitcoin_price] + '<br>'


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

            yaxis = dict(range = [min(bitcoin_price) - 3, max(bitcoin_price) + 5],
                         title = '<b>Valor</b>',
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

        )

            }


@app.callback(Output('chart2', 'figure'),
              [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        header_list = ['Time', 'Estado de Carga', 'Velocidade', 'Temperatura1', 'Temperatura2', 'Temperatura3', 'Temperatura4', 'RPM1', 'RPM2', 'RPM3', 'RPM4', 'TEMPERATURA MOTOR']
        bitcoin_df = pd.read_csv('data.csv', names = header_list)
        bitcoin_price = bitcoin_df['Temperatura1'].tail(10)
        time_interval = bitcoin_df['Time'].tail(10)


    return {
        'data': [go.Scatter(
            x = time_interval,
            y = bitcoin_price,
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
            '<b>Bitcoin Price</b>: ' + [f'${x:,.2f}' for x in bitcoin_price] + '<br>'


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

            yaxis = dict(range = [min(bitcoin_price) - 3, max(bitcoin_price) + 5],
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


@app.callback(Output('chart3', 'figure'),
              [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        header_list = ['Time', 'Estado de Carga', 'Velocidade', 'Temperatura1', 'Temperatura2', 'Temperatura3',
                       'Temperatura4', 'RPM1', 'RPM2', 'RPM3', 'RPM4', 'TEMPERATURA MOTOR']
        bitcoin_df = pd.read_csv('data.csv', names = header_list)
        bitcoin_price = bitcoin_df['Temperatura1'].tail(10)
        time_interval = bitcoin_df['Time'].tail(10)


    return {
        'data': [go.Scatter(
            x = time_interval,
            y = bitcoin_price,
            #fill = 'tonexty',
            #fillcolor = 'rgba(255, 0, 255, 0.1)',
            mode = 'markers+lines',
            line = dict(width = 2, color = '#ff00ff'),
            # marker = dict(size = 7, symbol = 'circle', color = '#D35400',
            #               line = dict(color = '#D35400', width = 2)
            #               ),

            hoverinfo = 'text',
            hovertext =
            '<b>Time</b>: ' + time_interval.astype(str) + '<br>' +
            '<b>Bitcoin Price</b>: ' + [f'${x:,.2f}' for x in bitcoin_price] + '<br>'


        )],

        'layout': go.Layout(
            # paper_bgcolor = 'rgba(0,0,0,0)',
            # plot_bgcolor = 'rgba(0,0,0,0)',
            plot_bgcolor = 'rgba(50, 53, 70, 0)',
            paper_bgcolor = 'rgba(50, 53, 70, 0)',
            title = {
                'text': '',

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

            yaxis = dict(range = [min(bitcoin_price) - 3, max(bitcoin_price) + 5],
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
                        daq.LEDDisplay(
                            label='TEMPERATURA ºc', style = {'color':'white'},
                            value=t1_r1,
                            color='white',
                            backgroundColor="red",
                            size = 20
                            ),
                        daq.LEDDisplay(
                            label='TEMPERATURA ºc', style={'color': 'white'},
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
                            size = 20
                        ),
                        daq.LEDDisplay(
                            label='RPM', style={'color': 'white'},
                            value=rpm1,
                            color='white',
                            backgroundColor="#112c38",
                            size=20
                        )
                    ])
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
                                backgroundColor="gray",
                                size = 30
                                    ),
                            html.Br(),
                            daq.LEDDisplay(
                                label='RPM', style={'color': 'white'},
                                value=rpm1,
                                color='white',
                                backgroundColor="#112c38",
                                size = 30
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
                            daq.LEDDisplay(
                                label='TEMPERATURA ºc', style = {'color':'white'},
                                value=t1_r1,
                                color='white',
                                backgroundColor="green",
                                size = 30
                                    ),
                            ], width=6),
                    dbc.Col([
                        daq.LEDDisplay(
                            label='RPM', style={'color': 'white'},
                            value=rpm1,
                            color='white',
                            backgroundColor="#112c38",
                            size=30
                            )
                        ], width=6)
                    ])
            ]),
        ]

@app.callback(Output('card_2','children'),
                [Input('update_value','n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        arq2 = pd.read_csv('data.csv', names=header_list)
        t1_r1 = arq2['Temperatura1'].tail(1).iloc[0]
        rpm1 = arq2['Temperatura1'].tail(1).iloc[0]
    if t1_r1 > 80:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        daq.LEDDisplay(
                            label='TEMPERATURA ºc', style={'color': 'white'},
                            value=t1_r1,
                            color='white',
                            backgroundColor="red",
                            size=20
                        ),
                        daq.LEDDisplay(
                            label='TEMPERATURA ºc', style={'color': 'white'},
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
                        daq.LEDDisplay(
                            label='RPM', style={'color': 'white'},
                            value=rpm1,
                            color='white',
                            backgroundColor="#112c38",
                            size=20
                        )
                    ])
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
                                backgroundColor="gray",
                                size = 30
                                    ),
                            html.Br(),
                            daq.LEDDisplay(
                                label='RPM', style={'color': 'white'},
                                value=rpm1,
                                color='white',
                                backgroundColor="#112c38",
                                size = 30
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
                                backgroundColor="green",
                                size = 30
                                    ),
                            html.Br(),
                            daq.LEDDisplay(
                                label='RPM', style={'color': 'white'},
                                value=rpm1,
                                color='white',
                                backgroundColor="#112c38",
                                size = 30
                                    )
                                ])
                            ]),
                    ])
            ]),
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
                            label='TEMPERATURA ºc', style={'color': 'white'},
                            value=t1_r1,
                            color='white',
                            backgroundColor="red",
                            size=20
                        ),
                        daq.LEDDisplay(
                            label='TEMPERATURA ºc', style={'color': 'white'},
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
                        daq.LEDDisplay(
                            label='RPM', style={'color': 'white'},
                            value=rpm1,
                            color='white',
                            backgroundColor="#112c38",
                            size=20
                        )
                    ])
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
                                backgroundColor="gray",
                                size = 30
                                    ),
                            html.Br(),
                            daq.LEDDisplay(
                                label='RPM', style={'color': 'white'},
                                value=rpm1,
                                color='white',
                                backgroundColor="#112c38",
                                size = 30
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
                                backgroundColor="green",
                                size = 30
                                    ),
                            html.Br(),
                            daq.LEDDisplay(
                                label='RPM', style={'color': 'white'},
                                value=rpm1,
                                color='white',
                                backgroundColor="#112c38",
                                size = 30
                                    )
                                ])
                            ]),
                    ])
            ]),
        ]


if __name__ == '__main__':
    app.run_server(debug=True, port=1010)