---
title: Legendre Transform
date: 2020-08-05
category: physics
tags:
  - "物理"
  - "数学"
  - "Legendre transformation"
  - "classical mechanics"
  - "statistical mechanics"
---

## Intro

多次看到过 Legendre transform 这个名词.

Reference [Am. J. Phys. 77 (7), July 2009] 非常详细清晰友好地解答了我心中的各种
疑惑, 现将它做一个整理.

它在开头说道:

>The Legendre transform is a powerful tool in theoretical physics and plays an
>important role in classical mechanics, statistical mechanics, and
>thermodynamics.
>
>Legendre transform 在理论物理领域是一个强有用的工具, 在经典力学, 统计力学, 以及
>热力学中发挥了的作用.


进行 Legendre transform 之后, 相当于是相同的信息, 用了不同的方式进行展示
(display).

### Definition

给定一个函数 $F(x)$ 如果它满足

1. 是一个凸(convex)函数, 也就是像 $y=x^2$ 这种二阶导数恒正的函数. 并且是光滑的函
   数.

2. $F$ 的导数, 比 $x$ 本身, 更加容易去测量, 控制或者考虑.

那么对它 Legendre transform 更加方便.


对于函数 $F(x)$ 它的斜率

$$
\begin{align}
  s(x) \equiv \frac{\mathrm{d}F(x)}{\mathrm{d}x}
\end{align}
$$

$s(x)$ 是一个单调函数, 也就是说 $s$ 和 $x$ 是一一对应的. 那么, 就可以将 $s$ 做为
一个独立变量来代替 $x$, 即

$$
\begin{align}
  F(x(s))
\end{align}
$$

也就是说我们用了 $F$ 的导数, 而不是 $x$ 本身来描述这个函数关系.

这个用复合函数的方法, 将 $x$ 用 $F$ 的导数, 即 $s$ 做了替换. 这是最容易想到的.
而 Legendre transform 提供了另一种方法, 定义 $F(x)$ 的 Legendre transform $G(s)$
为

$$
\begin{align}
  G(s) \equiv s x(s) - F(x(s))
\end{align}
$$

需要注意的是上式只有一个独立变量 $s$ . Legendre transform 的好处是, $G(s)$ 和
$F(x)$ 一种对称的的关系(此外 Reference [Am. J. Phys. 77 (7), July 2009] 给出一一
种几何上的直观理解) 以及一些其它的性质. 这体现在

- 新函数对新变量的导数是旧变量，反之亦然

  $$
  \begin{align}
    x(s) = \frac{\mathrm{d}G}{\mathrm{d}s} \\
    s(x) = \frac{\mathrm{d}F}{\mathrm{d}x}
  \end{align}
  $$

- Legendre 变换的逆变换是它本身. 也就是说经过两次 Legendre 变换后, 回到函数本身.
   形式上将这种关系表示为

  $$
  \begin{align}
  \{F, x\} \Leftrightarrow \{G, s\} \\
    G(s) + f(x) = sx
  \end{align}
  $$

  要注意独立变量只有一个, $s, x$ 并不相互独立.

- 它们的极值

  $$
  \begin{align}
    F_{\mathrm{min}} = -G(0) \\
    G_{\mathrm{min}} = -F(0)
  \end{align}
  $$

## Examples

### Lagrangian to Hamiltonian

### In Statistical Thermodynamics (added in 2026-05-26)

一个封闭热力学系统，当给定体积 $V$，粒子数 $N$，和熵 $S$ 后，他的能量为这三个变量的函数

$$
\begin{align}
  E(N, S, V)
\end{align}
$$

如果我们对 $N, S, V$ 这三个变量做微小改变，那么系统的能量也会做微小改变，即

$$
\begin{align}
  \mathrm{d}E(N, S, V) =&
  \left.\left(\frac{\partial E}{\partial N}\right)\right|_{S, V} \mathrm{d}N
  + \left.\left(\frac{\partial E}{\partial S}\right)\right|_{N, V} \mathrm{d}S
  + \left.\left(\frac{\partial E}{\partial V}\right)\right|_{N, S} \mathrm{d}V\\
  =& \mu \mathrm{d}N + T \mathrm{d}S  - p \mathrm{d}V
\end{align}
$$

如果我们想用能量来描述这个系统， 也就是说固定系统的 $N, T, V$ (正则系综)。
那么我们就可以做 Legendre 变换（可以差一个符号约定）得到 Helmholtz free energy,

$$
\begin{align}
  F = E - \left.\left(\frac{\partial E}{\partial S}\right)\right|_{N, V} S
  = E - T S
\end{align}
$$

那么

$$
\begin{align}
  S = -\left.\left(\frac{\partial F}{\partial T}\right)\right|_{N, V}
\end{align}
$$

对应的微分

$$
\begin{align}
  \mathrm{d}F(N, T, V) =&
  \left.\left(\frac{\partial F}{\partial N}\right)\right|_{T, V} \mathrm{d}N
  + \left.\left(\frac{\partial F}{\partial T}\right)\right|_{N, V} \mathrm{d}T
  + \left.\left(\frac{\partial F}{\partial V}\right)\right|_{N, T} \mathrm{d}V\\
  =& \mu \mathrm{d}N - S \mathrm{d}T  - p \mathrm{d}V.
\end{align}
$$

同样的，我们也可以对 $N$ 做 Legendre 变换，得到 $\mu, T, V$ 巨正则系综的巨热力学势，

$$
\begin{align}
  \Omega = F - \left.\left(\frac{\partial F}{\partial N}\right)\right|_{T, V} N
  = F - \mu N = E - T S - \mu N
\end{align}
$$

$$
\begin{align}
  N = -\left.\left(\frac{\partial \Omega}{\partial \mu}\right)\right|_{T, V}
\end{align}
$$

$$
\begin{align}
  \mathrm{d}\Omega(\mu, T, V) =&
  \left.\left(\frac{\partial \Omega}{\partial \mu}\right)\right|_{T, V} \mathrm{d}\mu
  + \left.\left(\frac{\partial \Omega}{\partial T}\right)\right|_{\mu, V} \mathrm{d}T
  + \left.\left(\frac{\partial \Omega}{\partial V}\right)\right|_{\mu, T} \mathrm{d}V\\
  =& -N \mathrm{d}\mu - S \mathrm{d}T  - p \mathrm{d}V.
\end{align}
$$

类似的，还可以把 $F$ 对体积做 Legendre 变换得到等温等压系综的 Gibbs 自由能 $G(T, p, N) = E - TS + pV$，以及把内能 $E$ 对体积做 Legendre 变换得到等温等压系综的焓(Enthalpy) $H(S, p, N) = E + pV$.

## Reference

- Herbert Goldstein Charles P. Poole John Safko - Classical Mechanics

- Making sense of the Legendre transform, Am. J. Phys. 77 (7), July 2009
  (arXiv:0806.1147v2  [physics.ed-ph]  4 Mar 2009)
