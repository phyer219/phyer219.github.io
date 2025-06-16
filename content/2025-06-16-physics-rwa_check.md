---
title: Rotating Wave Approximation Numerical Check
date: 2025/06/16
categories: 专业笔记
tags: [rotating wave approximation, ploly]
---

```python
import numpy as np
import qutip as qtp
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = 'browser'
pio.templates.default = 'plotly_dark'

w0 = 8
wL = 7
Omega = 1
tlist = np.linspace(0, 20, 1000)

psi0 = qtp.basis(2, 0)

H0 = w0/2 * qtp.sigmaz()

H_full = qtp.QobjEvo(lambda t: w0/2 * qtp.sigmaz()
                               + Omega*np.cos(wL*t)*qtp.sigmax())
H_rwa = qtp.QobjEvo(lambda t: w0/2 * qtp.sigmaz()
                              + Omega/2*np.exp(-1j*wL*t)*qtp.sigmap()
                              + Omega/2*np.exp(1j*wL*t)*qtp.sigmam())
H_neg = qtp.QobjEvo(lambda t: w0/2 * qtp.sigmaz()
                              + Omega/2*np.exp(1j*wL*t)*qtp.sigmap()
                              + Omega/2*np.exp(-1j*wL*t)*qtp.sigmam())

result_full = qtp.mesolve(H=H_full, rho0=psi0, tlist=tlist, c_ops=[],
                          e_ops=[(1 - qtp.sigmaz()) / 2])

result_rwa = qtp.mesolve(H=H_rwa, rho0=psi0, tlist=tlist, c_ops=[],
                         e_ops=[(1 - qtp.sigmaz()) / 2])
result_neg = qtp.mesolve(H=H_neg, rho0=psi0, tlist=tlist, c_ops=[],
                         e_ops=[(1 - qtp.sigmaz()) / 2])

fig = go.Figure()
fig.add_trace(go.Scatter(x=tlist, y=result_full.expect[0],
                         name="Full (no RWA)"))
fig.add_trace(go.Scatter(x=tlist, y=result_rwa.expect[0], name="RWA"))
fig.add_trace(go.Scatter(x=tlist, y=result_neg.expect[0], name="High-freq"))
# fig.add_trace(go.Scatter(x=tlist, y=result_neg.expect[0]+result_rwa.expect[0],
#                          name="High-freq + Low-freq", mode='markers'))
fig.update_layout(xaxis=dict(title=r'$\Omega t$'),
                  yaxis=dict(title=r'$|\psi_{\downarrow}|^2$'),
                  title='Rotating Wave Approximation')
fig.add_annotation(x=.8, y=1.2,
                   text=r'$\omega_0/\Omega='+f'{w0/Omega:n}'+ r', \omega_L/\Omega='+f'{wL/Omega:n}'+r'$',
                   showarrow=False,
                   xref='paper', yref='paper', font=dict(size=30))

fig.write_html('check1.html', include_mathjax="cdn")

w0 = 8
w1 = 7

g = 1

H0 = w0/2 * qtp.tensor(qtp.sigmaz(), qtp.qeye(2))
H1 = w1/2 * qtp.tensor(qtp.qeye(2), qtp.sigmaz())

V_full = g*qtp.tensor(qtp.sigmap() + qtp.sigmam(), qtp.sigmap() + qtp.sigmam())
V_rwa = g*(qtp.tensor(qtp.sigmap(), qtp.sigmam())
           +qtp.tensor(qtp.sigmam(), qtp.sigmap()))

psi0 = qtp.tensor(qtp.spin_coherent(j=1/2, theta=.7*np.pi, phi=1),
                  qtp.spin_coherent(j=1/2, theta=.8*np.pi, phi=2))

tlist = np.linspace(0, 20, 10000)
res_full = qtp.mesolve(H=H0+H1+V_full, rho0=psi0, tlist=tlist,
                       c_ops=[],
                       e_ops=[(1-qtp.tensor(qtp.sigmaz(), qtp.qeye(2))) / 2])
res_rwa = qtp.mesolve(H=H0+H1+V_rwa, rho0=psi0, tlist=tlist,
                      c_ops=[],
                      e_ops=[(1-qtp.tensor(qtp.sigmaz(), qtp.qeye(2))) / 2])
fig = go.Figure()
fig.add_trace(go.Scatter(x=tlist, y=res_full.expect[0], name='Full (no RWA)'))
fig.add_trace(go.Scatter(x=tlist, y=res_rwa.expect[0], name='RWA'))

fig.write_html('check2.html', include_mathjax="cdn")
```

[check.py](2025-06-16-physics-rwa_check/check.py)

<iframe src="2025-06-16-physics-rwa_check/check1.html" width="100%" height="600"></iframe>

<iframe src="2025-06-16-physics-rwa_check/check2.html" width="100%" height="600"></iframe>