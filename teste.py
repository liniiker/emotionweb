import dash
from dash import html,dcc
import plotly.graph_objs as go

# Dados de exemplo para o gráfico de linha
x_data = ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01']
y_data = [100, 110, 120, 122]

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Gráfico de Linhas'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                go.Scatter(
                    x=x_data,
                    y=y_data,
                    mode='lines',
                    name='Preço'
                )
            ],
            'layout': {
                'title': 'Histórico de Preços',
                'xaxis': {
                    'title': 'Data',
                    'rangeslider': {
                        'visible': False
                    }
                },
                'yaxis': {
                    'title': 'Preço'
                },
                'annotations': [
                    {
                        'x': 1.015,
                        'y': y_data[-1],
                        'xref': 'paper',
                        'yref': 'y',
                        'text': f'{y_data[-1]}',
                        'showarrow': False,
                        'font': {
                            'size': 16
                        },
                        'xanchor': 'left',
                        'yanchor': 'middle'
                    }
                ]
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
