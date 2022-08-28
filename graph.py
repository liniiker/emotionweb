from plotly.subplots import make_subplots
import numpy as np
import plotly.graph_objs as go
import dash
from dash import html, dcc

# Initialize figure with 4 3D subplots
fig = make_subplots(
    rows=2, cols=2,
    specs=[[{'type': 'surface'}, {'type': 'surface'}],
           [{'type': 'surface'}, {'type': 'surface'}]])

# Generate data
x = 0.2*np.array([1,2])
y = 0.1*np.array([1,2])
xGrid, yGrid = np.meshgrid(y, x)
z = xGrid ** 3 + yGrid ** 3


fig.add_trace(
    go.Surface(x=x, y=y, z=z, colorscale='Viridis', showscale=False),
    row=1, col=1)
fig.update_layout(
    title_text='3D subplots with different colorscales',
    height=1500,
    width=1500
)


app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter