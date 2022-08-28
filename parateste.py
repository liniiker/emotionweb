from plotly.subplots import make_subplots
import numpy as np
import plotly.graph_objs as go
import dash
from dash import html, dcc

fig = go.Figure(data=[
    go.Mesh3d(
        x=[0, 2, 2, 0],
        y=[0, 0, 2, 2],
        z=[3, 0, 3, 0],
        colorscale=[[0, 'gold'],
                    [0.5, 'black'],
                    [1, 'gold']],
        # Intensity of each vertex, which will be interpolated and color-coded
        intensity=[0, 0.1, 0.66, 1],
        # i, j and k give the vertices of triangles
        # here we represent the 4 triangles of the tetrahedron surface
        #i=[0, 0, 0, 1],
        #j=[1, 2, 3, 2],
        #k=[2, 3, 1, 3],
        name='y',
        showscale=True
    )
])


app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter

