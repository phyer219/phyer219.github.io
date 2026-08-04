---
title: Shot noise
date: 2026-07-24
category: physics
tags:
  - "quantum computing"
  - "probability theory"
  - "random variable"
  - "estimator"
---

## 对可观测量期望进行参数估计

一个系统处在态 $\rho$ 上，我们想得到某个可观测量 $\hat{O}$ ，的期望 $\langle \hat{O} \rangle = \mathrm{Tr}(\hat{O}\rho)$ 。

$\langle \hat{O} \rangle$ 可以看作是系统的一个参数。得到 $\langle \hat{O} \rangle$ 的过程可以看成是一个估计的过程（estimation process）。

## 测量过程

算符 $\hat{O}$ ，可以在它的本征基底 $\{|m\rangle\}$ 下做测量，其中 $|m\rangle$ 是本征值为  $\hat{O}|m\rangle = O_m |m\rangle$ 的本征态。
在测量后，系统一定处在它的某个本征态上。

测量过程可以由一系列 measurement operation

$$
\begin{align}
    \mathcal{E}_m(\rho) = M_m \rho M_m^\dagger,
\end{align}
$$

描述，其中 $M_m = |m\rangle\langle m|$ 是 measurement operator 。
测量过后，系统处在态

$$
\begin{align}
    \frac{\mathcal{E}_m(\rho)}{\mathrm{Tr}\left( \mathcal{E}_m(\rho) \right)}
\end{align}
$$

上的概率是

$$
\begin{align}
    \mathrm{Tr}\left( \mathcal{E}_m(\rho) \right)
\end{align}
$$

## 随机变量：从样本空间到可测空间的函数

假设系统在测量之前处在态 $\rho$ 。

可观测量的测量数值由随机变量（random variable）

$$
\begin{align}
    X_{\hat{O}}:\left\{
        \frac{\mathcal{E}_m(\rho)}{\mathrm{Tr}\left( \mathcal{E}_m(\rho)\right)}
        \right\}
        \to \left\{
            O_m
        \right\}
\end{align}
$$

描述。它是一个从样本空间（[sample space](https://en.wikipedia.org/wiki/Sample_space)）

$$
\begin{align}
    \left\{\frac{\mathcal{E}_m(\rho)}{\mathrm{Tr}\left( \mathcal{E}_m(\rho) \right)}\right\}
\end{align}
$$

到可测空间（[measurable space](https://en.wikipedia.org/wiki/Measurable_space)）$\{O_m\}$ 的函数。样本空间就是测量结果，也就是仪器上显示的结果构成的集合。在这里，我们假设仪器显示的结果就是系统在被观测后塌缩到的态。而这里的可测空间则由可观测量所有的本征值 $O_m$ 和上面的[ $\sigma$ 代数](https://en.wikipedia.org/wiki/%CE%A3-algebra)构成。

测量后的结果（outcome） $|m\rangle\langle m|$ 对应的概率是，

$$
\begin{align}
    P(X_{\hat{O}} = O_m) = \mathrm{Tr}\left[ \mathcal{E}_m(\rho) \right].
\end{align}
$$

随机变量 $X_{\hat{O}}$ 的期望值是

$$
\begin{align}
    E[X_{\hat{O}}] = \sum_m O_m P(X_{\hat{O}} = O_m) =
     \langle \hat{O}\rangle,
\end{align}
$$

其中 $\langle \hat{O}\rangle = \mathrm{Tr}[\hat{O}\rho]$ 是 $\hat{O}$ 的系综平均。

方差（variance）为

$$
\begin{align}
    \mathrm{var}\left[ X_{\hat{O}} \right]
    = E[X_{\hat{O}}^2] - E[X_{\hat{O}}]^2
    = \langle \hat{O}^2\rangle - \langle \hat{O}\rangle^2
\end{align}
$$

如果 $\rho$ 是纯态，它就是量子涨落（quantum fluctuation）。

## [Estimators](https://en.wikipedia.org/wiki/Estimator)

在实验中，为了得到精确的结果，我们通常重复运行同一个线路 $N_{\mathrm{shots}}$ 次。
我们可以用不同的估计量（[estimator](https://en.wikipedia.org/wiki/Estimator)）来对参数 $\langle \hat{O} \rangle$ 进行估计。

例如，我们可以选 sample mean estimator,

$$
\begin{align}
    \bar{X}_{\hat{O}} = \frac{1}{N_{\mathrm{shots}}}\sum_{l=1}^{N_{\mathrm{shots}}} X_{\hat{O}, l}.
\end{align}
$$

我们假设每次运行线路的都是相同的，每次的测量结果都是相互独立的。
$\{X_{\hat{O}, l}\}$ 对应的是独立同分布（independent and identically distributed，i.i.d.）。
sample mean estimator 的期望值（expectation value）为

$$
\begin{align}
    E[\bar{X}_{\hat{O}}]
    = \frac{1}{N_{\mathrm{shots}}}\sum_{l=1}^{N_{\mathrm{shots}}} E[X_{\hat{O}, l}]
    = \langle \hat{O}\rangle,
\end{align}
$$

方差为

$$
\begin{align}
    \mathrm{var}\left[ \bar{X}_{\hat{O}} \right]
    =& \frac{1}{N_{\mathrm{shots}}^2}\sum_{l=1}^{N_{\mathrm{shots}}}
    \mathrm{var} [ X_{\hat{O}, l} ]
    = \frac{1}{N_{\mathrm{shots}}^2} N_{\mathrm{shots}}
    \mathrm{var} [ X_{\hat{O}} ]\\
    =& \frac{1}{N_{\mathrm{shots}}}\mathrm{var} [ X_{\hat{O}} ].
\end{align}
$$

因此，在实验次数 $N_{\mathrm{shots}}\to \infty$ 的极限下，方差 $\mathrm{var}\left[ \bar{X}_{\hat{O}} \right] \to 0$ 。
也就是说，只要我们运行的次数足够多，就可以得到精确的结果。

## Bias

量子计算机上有噪声。

我们测量有噪声的 $\rho$ 与测量理想无噪声的 $\rho_{\mathrm{ideal}}$ ，结果会有所不同。

无噪声的 $\rho_{\mathrm{ideal}}$ 的期望是

$$
\begin{align}
    \langle \bar{X}_{\hat{O}} \rangle_{\mathrm{ideal}} = \mathrm{Tr}[\hat{O}\rho_{\mathrm{ideal}}]
\end{align}
$$

我们的 estimator 给出的估计，会与理想值，或真实值，存在 bias

$$
\begin{align}
    \mathrm{bias}[\bar{X}_{\hat{O}}] =
    E[\bar{X}_{\hat{O}}] - \langle \hat{O} \rangle_{\mathrm{ideal}}.
\end{align}
$$

Estimator 的 mean square error 为

$$
\begin{align}
    \mathrm{MSE}[\bar{X}_{\hat{O}}]
     =& E[(\bar{X}_{\hat{O}} - \langle \hat{O} \rangle_{\mathrm{ideal}})^2] \\
     =& \mathrm{bias} [\bar{X}_{\hat{O}}]^2 + \mathrm{var}[\bar{X}_{\hat{O}}].
\end{align}
$$

我们可以用 error mitigated estimator 来减少 bias 。

## 例子

我们测量
$\hat{\sigma}^z = |1\rangle\langle 1| - |0\rangle\langle 0|$,
时，它有两个本征值 $-1, 1$, 本征态 $|0\rangle, |1\rangle$ 。

我们在 computational basis $\{|0\rangle, |1\rangle\}$ 下进行测量。
对应的 quantum operations $M_m$ for this measurement 是

$$
\begin{align}
    M_{|0\rangle\langle 0|} = |0\rangle\langle 0 |,
    M_{|1\rangle\langle 1|} = |1\rangle\langle 1 |.
\end{align}
$$

我们将这个可观测量 $\hat{\sigma}^z$ 的随机变量记为 $X_{\hat{\sigma}^z}$ 。
它是一个函数，从 measurement outcomes
$\{|0\rangle\langle 0|, |1\rangle\langle 1|\}$ 到本征值的集合构成的可测空间 $\hat{\sigma}^z$ $\{-1, 1\}$ 的函数。
即

$$
\begin{align}
    X_{\hat{\sigma}^z} (|0\rangle\langle 0|) =& -1, \\
    X_{\hat{\sigma}^z} (|1\rangle\langle 1|) =& 1.
\end{align}
$$

对应的概率为

$$
\begin{align}
    P(X_{\hat{\sigma}^z} = -1) =& \mathrm{Tr}\left[
        M_{|0\rangle\langle 0|} \rho M^{\dagger}_{|0\rangle\langle 0|}
     \right], \\
     P(X_{\hat{\sigma}^z} = 1) =& \mathrm{Tr}\left[
        M_{|1\rangle\langle 1|} \rho M^{\dagger}_{|1\rangle\langle 1|}
     \right]
\end{align}
$$

可观测量的期望为

$$
\begin{align}
    E[X_{\hat{\sigma}^z}] =& P(X_{\hat{\sigma}^z} = 1)
    - P(X_{\hat{\sigma}^z} = -1) \\
    =& \mathrm{Tr}\left[
        \hat{\sigma}^z \rho
    \right] = \langle \hat{\sigma}^z \rangle    .
\end{align}
$$

由

$$
\begin{align}
    E[X^2_{\hat{\sigma}^z}] =& P(X_{\hat{\sigma}^z} = 1)
    +(-1)^2 P(X_{\hat{\sigma}^z} = -1)  \\
    =& \mathrm{Tr}\left[
        \left( \hat{\sigma}^z  \right)^2\rho
    \right] = \langle \left( \hat{\sigma}^z  \right)^2 \rangle
    =1   .
\end{align}
$$

可以得到这个可观测量的方差 ，

$$
\begin{align}
    \mathrm{var}[X_{\hat{\sigma}^z}] = E[X^2_{\hat{\sigma}^z}] - E[X_{\hat{\sigma}^z}]^2 = 1 - \langle \hat{\sigma}^z \rangle ^2.
\end{align}
$$

定义 sample mean estimator ，

$$
\begin{align}
    \bar{X}_{\hat{\sigma}^z} = \frac{1}{N_{\mathrm{shots}}}
    \sum_{l=1}^{N_{\mathrm{shots}}} X_{l, \hat{\sigma}^z}.
\end{align}
$$

其中 $X_{l, \hat{\sigma}^z}$ 是第 $l$ 次测量对应的随机变量。
我们假设密度矩阵是相同的，那么 $\{X_{l, \hat{\sigma}^z}\}$ 就是 independent and identically distributed (i.i.d.).
因此我们可以计算方差，

$$
\begin{align}
    \mathrm{var}\left[ \bar{X}_{\hat{\sigma}^z} \right]
    =& \frac{1}{N_{\mathrm{shots}}^2}\sum_{l=1}^{N_{\mathrm{shots}}}
    \mathrm{var}\left[  X_{l, \hat{\sigma}^z}  \right] \\
    =& \frac{1}{N_{\mathrm{shots}}^2} N_{\mathrm{shots}}
    \mathrm{var}\left[  X_{\hat{\sigma}^z}  \right] \\
    =& \frac{1}{N_{\mathrm{shots}}}
    \mathrm{var}\left[  X_{\hat{\sigma}^z}  \right] \\
    =& \frac{1}{N_{\mathrm{shots}}}
    \left[  1 -   \langle \hat{\sigma}^z \rangle ^2\right]
\end{align}
$$

这个 estimator 的标准差（standard errors） $\sqrt{\mathrm{var}[\bar{X}_{\hat{\sigma}^z}]}$ 常被用作 error bar 。

## Reference

- [arXiv: 2606.27856: Simulating the Dynamics of Markovian Quantum Processes by Quantum Collision Models on Quantum Computers](https://arxiv.org/abs/2606.27856)
