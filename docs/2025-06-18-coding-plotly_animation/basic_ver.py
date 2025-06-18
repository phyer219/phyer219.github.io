import plotly.graph_objects as go
import numpy as np

x = np.linspace(0, 2*np.pi, 50)
t = np.linspace(0, 2*np.pi, 500)
yt = [np.sin(x + ti) for ti in t]
frames = [go.Frame(data=[go.Scatter(x=x, y=y1i)]) for y1i in yt]

fig = go.Figure(data=frames[0].data, frames=frames)

ani_opts = dict(frame={"duration": 20, "redraw": False})
bt = go.layout.updatemenu.Button(label="Play", method="animate",
                                 args=[None, ani_opts])

fig.update_layout(updatemenus=[dict(type='buttons', buttons=[bt])])

fig.write_html(file="basic_ver.html", include_mathjax='cdn', auto_play=False)
