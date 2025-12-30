---
title: Plotly 绘制动图
date: 2025-06-18
categories: coding
tags:
  - plotly
  - python
---

## 基础版本

```python
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
```

[basic_ver.py](2025-06-18-coding-plotly_animation/basic_ver.py)

<iframe src="2025-06-18-coding-plotly_animation/basic_ver.html" width="100%" height=600></iframe>

## 高级版本

```python
import plotly.graph_objects as go
import numpy as np
import plotly.io as pio

pio.renderers.default = 'notebook_connected'

x = np.linspace(0, 2*np.pi, 50)
t = np.linspace(0, 2*np.pi, 500)
y1t = [np.sin(x + ti) for ti in t]
y2t = [np.cos(x + ti) for ti in t]
frames = [go.Frame(data=[go.Scatter(x=x, y=y1i, name=r'$\sin(x+t)$'),
                         go.Scatter(x=x, y=y2i, name=r'$\cos(x+t)$')],
                   name=f'{ti:.2f}')
          for y1i, y2i, ti in zip(y1t, y2t, t)]

fig = go.Figure(data=frames[0].data, frames=frames)

ani_opts = dict(frame={"duration": 20, "redraw": False})
bt_play = go.layout.updatemenu.Button(label="Play", method="animate",
                                      args=[None, ani_opts])

ani_opts_stop = dict(mode='immediate')
bt_stop = go.layout.updatemenu.Button(
    label="Stop", method="animate",
    args=[[fig.frames[0].name, fig.frames[1].name], ani_opts_stop])

ani_opts_slider = dict(frame={"duration": 20, "redraw": True})
slider_steps = [go.layout.slider.Step(args=[[f.name], ani_opts_slider],
                                      label=f.name, method='animate')
                for f in fig.frames]
slider = go.layout.Slider(active=0, steps=slider_steps)


fig.update_layout(updatemenus=[dict(type='buttons',
                                    buttons=[bt_play, bt_stop])],
                  sliders=[slider],
                  xaxis_title=r'$x$',
                  paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)')

fig.write_html(file="pro_ver.html", include_mathjax='cdn', auto_play=False)

```

[pro_ver.py](2025-06-18-coding-plotly_animation/pro_ver.py)

<iframe src="2025-06-18-coding-plotly_animation/pro_ver.html" width="100%" height=600></iframe>

## 参考

[Plotly Animations](https://plotly.com/python/animations/)
