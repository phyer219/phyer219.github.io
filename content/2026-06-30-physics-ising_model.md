---
title: Ising model
date: 2026-06-30
category: physics
tags:
  - "Ising model"
  - "statistical mechanics"
---

- [1D Ising model](#1d-ising-model)
- [2D Ising model](#2d-ising-model)
  - [Kramers-Wannier duality](#kramers-wannier-duality)
    - [方法一：高温展开（High temperature, HT）](#方法一高温展开high-temperature-ht)
    - [方法二：低温展开（Low temperature, LT）](#方法二低温展开low-temperature-lt)
    - [得相变点](#得相变点)
  - [Onsager's exact solution](#onsagers-exact-solution)
- [Reference](#reference)


## 1D Ising model

见 [2021-03-11-Susskind's Statistical Mechanics](./2021-03-11-physics-SusskindsStatisticalMechanics.md)

## 2D Ising model

### [Kramers-Wannier duality](https://en.wikipedia.org/wiki/Kramers%E2%80%93Wannier_duality)

对于二维正方晶格

$$
\begin{align}
  H = -J \sum_{\langle i j\rangle} s_i s_j, \quad s_i = \pm 1
\end{align}
$$

我们用两种方法计算配分函数

$$
\begin{align}
  Z =& \sum_{\{s_i\}} e^{\beta J \sum_{\langle i j\rangle} s_i s_j}.
\end{align}
$$

#### 方法一：高温展开（High temperature, HT）

$$
\begin{align}
  Z_{HT} =& \sum_{\{s_i\}} e^{\beta J \sum_{\langle i j\rangle} s_i s_j} \\
    =& \sum_{\{s_i\}} \prod_{\langle i j \rangle} e^{\beta J s_i s_j} \\
    =& \sum_{\{s_i\}} \prod_{\langle i j \rangle}
       \cosh(\beta J) \left[ 1 + s_i s_j \tanh (\beta J) \right] \\
    =& \cosh^{N_b}(\beta J)\sum_{\{s_i\}} \prod_{\langle i j \rangle}
        \left[ 1 + s_i s_j \tanh (\beta J) \right]
\end{align}
$$

其中 $N_b$ 是晶格中键的个数。

可以按照 $\tanh$ 的阶数把对连乘的求和展开

$$
\begin{align}
   & \prod_{\langle i j \rangle}
        \left[ 1 + s_i s_j \tanh (\beta J) \right] \\
    =& 1 + \sum_{\langle i j\rangle} s_i s_j \tanh(\beta J) \\
       & +  \sum_{\langle i j\rangle}
       \sum_{\langle k l\rangle < \langle i j\rangle}
             s_i s_j s_k s_l \tanh^2 (\beta J) \\
       & +  \sum_{\langle i j\rangle}
           \sum_{\langle k l\rangle < \langle i j\rangle}
            \sum_{\langle m n\rangle < \langle k l\rangle < \langle i j\rangle}
           s_i s_j s_k s_l s_m s_n \tanh^3 (\beta J) \\
       & + \cdots
\end{align}
$$

其中 $\sum_{\langle i j \rangle}$ 表示对相邻格点求和，
$\sum_{\langle k l\rangle < \langle i j\rangle}$ 表示每种组合只计算一次。
比如一个 $3\times 3$ 的晶格

```shell
a - b - c
|   |   |
d - e - f
|   |   |
h - i - j
```

对于一对格点，也就是一个键求和，

$$
\begin{align}
  &\sum_{\langle i j\rangle} s_i s_j  \\
  =&  s_a s_b + s_a s_d + s_b s_c \\
   & + s_b s_e + s_c s_f + s_d s_h \\
   & + s_d s_e + s_e s_i + s_e s_f \\
   & + s_f s_j + s_h s_i + s_i s_j
\end{align}
$$

上式中的每一项，对构型求和都为 $0$ ，

$$
\begin{align}
  \sum_{s_i, s_j = \pm 1} s_i s_j = \sum_{s_i = \pm 1} s_i \sum_{s_j=\pm 1} s_j
   = (1 - 1)\times (1 - 1) = 0
\end{align}
$$

对于两对格点的情况，当这两个键没有连在一起时，为 $0$ ，当连在一起时，
$\sum_{s_i, s_j, s_k} s_i (s_j)^2 s_k = \sum_{s_i, s_j, s_k} s_i s_k = 2\sum_{s_i, s_k} s_i s_k = 0$  。

我们发现，对于每一项，只要选出来的格点对中，存在只用了奇数次的格点时，它就为 $0$ 。
而所有非闭合的链，总是至少存在一个格点只用了一次，所以都为 $0$ 。
对于闭合的链，链中的每个键都会贡献一个 $\tanh(\beta J)$ ，所以

$$
\begin{align}
  Z_{HT} = & \cosh^{N_b}(\beta J)\sum_{\{s_i\}} \prod_{\langle i j \rangle}
        \left[ 1 + s_i s_j \tanh (\beta J) \right] \\
    = & \cosh^{N_b}(\beta J)2^{N} \sum_{C}  \tanh^{n_C}(\beta J)
\end{align}
$$

其中 $N$ 是所有的格点数， $C$ 表示闭合的链， $n_C$ 表示闭合链中的键的个数。
$C$ 包含没有键被选中的情况，也就是 $n_C = 0$。
$2^N$ 来自于求和 $\sum_{\{ s_i \}}$ 。

之所以叫高温展开，是因为当温度无穷高，$\beta \to 0$ 时，求和项只剩下 $n_C = 0$ 。
温度越低， $n_C$ 大的闭合回路就贡献越大。如果考虑了所有闭合回路，这个结果是严格的。

#### 方法二：低温展开（Low temperature, LT）

$$
\begin{align}
  Z_{LT} = & \sum_{\{s_i\}} \prod_{\langle i j \rangle} e^{\beta J s_i s_j} \\
    = & 2 e^{N_b \beta J}
      + 2 e^{N_b \beta J} \sum_{i} e^{-2\beta J \cdot 4} + \cdots \\
    = & 2 e^{N_b \beta J} \sum_{CD} e^{-2\beta J \cdot n_{CD}}
\end{align}
$$

其中 $CD$ 是表示对偶晶格的闭合回路，即格点变成键，键变成格点。
第二个等号后面，第一项是零温基态的构型对应的贡献，
第二项是翻转一个自旋对应的构型的贡献（翻转一个自旋，改变四个键，每个键能量增加 $2 J$）。
翻转一个自旋，相于这个自旋周围的键形成一个闭合回路，也就是 domain wall。

#### 得相变点

如果晶格的对偶晶格还是本身，那么高温展开和低温展开中的闭合回路求和对应同一个函数，记为

$$
\begin{align}
  f(x) = \sum_C x^{n_C} = \sum_{CD} x^{n_{CD}}
\end{align}
$$

那么配分函数

$$
\begin{align}
  Z_{HT} = \cosh^{N_b}(\beta J)2^{N} f(\tanh(\beta J))
\end{align}
$$

$$
\begin{align}
  Z_{LT} = 2 e^{N_b \beta J} f (e^{-2\beta J})
\end{align}
$$

它们对应的 Helmholtz 自由能密度

$$
\frac{F_{HT}}{N} = - \frac{1}{N\beta}\ln Z_{HT}
       = - \frac{1}{\beta} \left[
        \frac{N_b}{N} \ln \cosh(\beta J) + \ln 2 + \frac{1}{N}\ln f(\tanh(\beta J))
         \right]
$$

$$
\frac{F_{LT}}{N} = - \frac{1}{N\beta}\ln Z_{LT}
       = - \frac{1}{\beta} \left[
        \frac{\ln 2 }{N} + \frac{N_b}{N} \beta J + \frac{1}{N}\ln f(e^{-2 \beta J})
       \right]
$$

如果系统存在，且只存在一个相变点，也就是在某个温度下自由能不解析，
那么它只能是在热力学极限 $N\to \infty$ 时，
函数 $f(x)$ 在 $x$ 取特定值 $x = x_c$ 时不解析（有限闭合回路求和一定是解析的），
因为自由能中其它项显然都是解析的
（$N_b/N$ 是有限的，对于二维正方晶格，
$\lim_{L\to \infty} 2(L-1)L / L^2 = 2$ , $L^2$ 为格点的数目）。

而 $F_{HT}$ 和 $F_{LT}$ 对于任意的 $\beta$ 都应该是相同的。
所以这个唯一的相变点 $\beta = \beta_C$ ，应该对应 $x = x_C$ ，即

$$
\begin{align}
  x_C = \tanh(\beta_C J) = e^{- 2 \beta_C J}
\end{align}
$$

由此可解得

$$
\begin{align}
\beta_C J = \frac{1}{2} \ln (1 + \sqrt{2})
\end{align}
$$

相变温度

$$
\begin{align}
\frac{T_C}{J} = \frac{2}{\ln (1 + \sqrt{2})} \approx 2.269
\end{align}
$$

也容易验证，当 $\beta = \beta_C$ 时，高温展开和低温展开的自由能密度中剩下的解析的部分也相等
（需要用到 $\lim_{N\to\infty} N_b/N = 2$ ）。

正方晶格的对偶晶格是它本身，所以如果正方晶格存在唯一的一个相变点，这就是它的相变温度。

Kramers-Wannier duality 本身并不能说明系统是否存在相变以及相变点的个数，它只能给出相变点的候选位置。

### Onsager's exact solution

## Reference

- [Wikipedia: Ising model](https://en.wikipedia.org/wiki/Ising_model)
- [Wikipedia: Square lattice Ising model](https://en.wikipedia.org/wiki/Square_lattice_Ising_model)
