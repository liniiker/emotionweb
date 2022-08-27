import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

# Initialize figure with 4 3D subplots
fig = make_subplots(
    rows=2, cols=2,
    specs=[[{'type': 'surface'}, {'type': 'surface'}],
           [{'type': 'surface'}, {'type': 'surface'}]])

# Generate data
x = 9.1*np.array([1,2,3])
y = 8*[1,2,3]
xGrid, yGrid = np.meshgrid(y, x)
z = xGrid * 3 + yGrid * 3

# adding surfaces to subplots.
fig.add_trace(
    go.Surface(x=x, y=y, z=z, colorscale='Viridis', showscale=False),
    row=1, col=1)

#fig.add_trace(
#    go.Surface(x=x, y=y, z=z, colorscale='RdBu', showscale=False),
#    row=1, col=2)

#fig.add_trace(
#    go.Surface(x=x, y=y, z=z, colorscale='YlOrRd', showscale=False),
#    row=2, col=1)

#fig.add_trace(
#    go.Surface(x=x, y=y, z=z, colorscale='YlGnBu', showscale=False),
#    row=2, col=2)

fig.update_layout(
    title_text='3D subplots with different colorscales',
    height=1300,
    width=1300
)

fig.show()