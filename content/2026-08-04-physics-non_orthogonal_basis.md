---
title: 完备非正交基底
date: 2026-08-04
category: physics
tags:
  - "linear algebra"
---

- [当做普通的量子力学基底来考虑](#当做普通的量子力学基底来考虑)
  - [正交基底与非正交基底之间的变换关系](#正交基底与非正交基底之间的变换关系)
  - [矢量的分量在基底之间的变换关系](#矢量的分量在基底之间的变换关系)
- [Tensorial formalism](#tensorial-formalism)
  - [非正交完备基矢和一些相关概念的定义](#非正交完备基矢和一些相关概念的定义)
  - [一些有用的结论](#一些有用的结论)
  - [与正交基底的变换关系](#与正交基底的变换关系)
- [Reference](#reference)


## 当做普通的量子力学基底来考虑

下面的内容，先忽略上标和下标的区别，统一视为下标。后面会说明它们在张量记号下的含义。

### 正交基底与非正交基底之间的变换关系

在一个线性空间中，有一组正交基底

$$
\begin{align}
    |e_n\rangle
\end{align}
$$

和一组非正交基底

$$
\begin{align}
    |e_{\mu}\rangle.
\end{align}
$$

它们之间的变换关系为

$$
\begin{align}
    |e_{\mu} \rangle = \sum_n |e_n\rangle\langle e^n| e_{\mu}\rangle = \sum_n |e_n\rangle T^n{}_{\mu},
\end{align}
$$

$$
\begin{align}
    \langle e_{\mu} | = \sum_n \langle e_{\mu}| e^n\rangle \langle e_n|
     = \sum_n \langle e_n | \left(T^*\right)^n{}_{\mu}.
\end{align}
$$

反之

$$
\begin{align}
    |e_n\rangle = \sum_{\mu} |e_{\mu}\rangle \left(T^{-1}\right)^{\mu}{}_n,
\end{align}
$$

$$
\begin{align}
    \langle e_n | = \sum_{\mu} \left[ \left(T^{-1} \right)^* \right]^{\mu}{}_n
     \langle e_{\mu}|,
\end{align}
$$

其中

$$
T^n{}_{\mu} = \langle e^n | e_{\mu} \rangle.
$$

由此可得非正交基底的完备关系

$$
\begin{align}
    1 =& \sum_n | e_n \rangle \langle e^n|
    = \sum_n \sum_{\mu \nu} |e_{\mu}\rangle
       \left(T^{-1}\right)^{\mu}{}_{n}
      \left[ \left(T^{-1}\right)^*\right]^{\nu}{}_n
       \langle e_{\nu} | \\
      =& \sum_{\mu \nu} | e_{\mu} \rangle
      S^{\mu \nu} \langle e_{\nu}|,
\end{align}
$$

其中

$$
\begin{align}
    S^{\mu \nu} = \left[\left(T^{\dagger}T\right)^{-1}\right]^{\mu \nu} , \quad
    \left( T^{\dagger}T\right)_{\mu \nu} = \langle e_{\mu} | e_{\nu}\rangle.
\end{align}
$$

### 矢量的分量在基底之间的变换关系

空间中的任意态 $|\psi\rangle$ 用正交基底展开，

$$
\begin{align}
    |\psi\rangle = \sum_n |e_n\rangle \langle e^n | \psi\rangle
    = \sum_n \psi^n | e_n \rangle.
\end{align}
$$

转换到非正交基底

$$
\begin{align}
    |\psi\rangle =
    \sum_{\mu \nu} | e_{\mu} \rangle
    S^{\mu \nu} \langle e_{\nu}|
    \psi\rangle
    =\sum_{\mu} \psi^{\mu} |e_{\mu} \rangle,
\end{align}
$$

其中

$$
\psi^{\mu} = \sum_{\nu} S^{\mu \nu} \langle e_{\nu}|
    \psi\rangle
    = \sum_n \left(T^{-1}\right)^{\mu}{}_{n} \psi^n.
$$

反之

$$
\begin{align}
    \psi^n = \sum_{\mu}
    T^n{}_{\mu}
     \psi^{\mu}.
\end{align}
$$

## Tensorial formalism

接下来用张量的上下标的符号来描述非正交基底。

### 非正交完备基矢和一些相关概念的定义

在 Hilbert space $\mathcal{H}$ 中的一组非正交（当然正交是一种特殊的情况，也满足这些定义），完备的基矢为

$$
\begin{align}
    | e_{\mu} \rangle
\end{align}
$$

在 2020 - Sakurai and Napolitano - Modern Quantum Mechanics 中的 D.C. 的意义下，它有对应的左矢

$$
\begin{align}
    \langle e_\mu |
\end{align}
$$

每一基矢都存在一个与之正交归一的矢量，它们构成另外一组基矢，用上标标记

$$
\begin{align}
    \langle e^{\mu} |
\end{align}
$$

同样的，它也有对应的右矢

$$
\begin{align}
    | e^{\mu} \rangle
\end{align}
$$

在 REF:1991 中，也把它们分为 proper 或 improper ,总结如下

$$
\begin{align}
    \begin{matrix}
        \mathrm{proper} &  \mathrm{improper}
        \\ \hline
        |e_{\mu}\rangle &  \langle e_{\mu} | \\
        \langle e^{\mu}| & |e^{\mu}\rangle
    \end{matrix}
\end{align}
$$

它们的正交归一性可以写为

$$
\begin{align}
    \langle e^{\mu} | e_{\nu}\rangle =& \delta^{\mu}{}_{\nu} \\
    \langle e_{\mu} | e^{\nu}\rangle =& \delta_{\mu}{}^{\nu}
\end{align}
$$

它们之间的度规（[Metric](https://en.wikipedia.org/wiki/Metric_tensor)）定义为

$$
\begin{align}
    S_{\mu \nu} \equiv & \langle e_{\mu} | e_{\nu} \rangle \\
    S^{\mu \nu} \equiv & \langle e^{\mu} | e^{\nu} \rangle
\end{align}
$$

可以发现 metric $S$ 是一个厄米矩阵。

在 Hilbert space $\mathcal{H}$ 中的任意矢量 $|\psi\rangle$ ,定义它在这组基矢上的投影，或分量为（proper 的两个）

$$
\begin{align}
    \psi^{\mu} \equiv& \langle e^{\mu} | \psi\rangle \\
    \psi_{\mu} \equiv& \langle \psi | e_{\mu}\rangle
\end{align}
$$

以及 improper 的两个

$$
\begin{align}
    \psi^{\mu *} \equiv& \langle \psi | e^{\mu} \rangle \\
    \psi_{\mu}^{*} \equiv& \langle e_{\mu} | \psi \rangle
\end{align}
$$

由于 $\psi^{\mu}$ 只有一个指标，没法通过是行指标还是列指标来区分往左矢还投影还是往右矢投影，
所以固定上指标是往 proper 的左矢投影。
往上指标右矢的投影就直接写成其复共轭。也有文章用一个占位符，即 $\psi^{\cdot \mu}$ 来表示 $\psi^{\mu *}$ ，这里不采用。

同理固定下指标 $\psi_{\mu}$ 是往 proper 的右矢投影。

### 一些有用的结论

与正交基底类似的，在非正交基底中也存在单位算符

$$
\begin{align}
    1 = \sum_{\mu} | e_\mu \rangle \langle e^{\mu} |
      = \sum_{\mu} | e^\mu \rangle \langle e_{\mu} |
\end{align}
$$

证明：把它作用在任基矢上
$\sum_{\mu} | e_\mu \rangle \langle e^{\mu} | e_{\nu}\rangle = \sum_{\mu} | e_\mu \rangle \delta^{\mu}{}_{\nu} = |e_{\nu}\rangle$ ，相当于一个单位算符，易得作用在任意矢量上都相当于一个单位算符。

虽然 $S_{\mu \nu}$ 和 $S^{\mu \nu}$ 看起来像是同一个矩阵的矩阵元，但实际上它们是两个互逆的矩阵，

$$
\begin{align}
    \sum_{\lambda} S_{\mu \lambda} S^{\lambda \nu}
      =& \sum_{\lambda} \langle e_{\mu} | e_\lambda \rangle
        \langle e^{\lambda} | e^{\nu}\rangle
      = \langle e_{\mu} | e^{\nu}\rangle \\
      =& \delta_{\mu}{}^{\nu}
\end{align}
$$

度规可以把一个指标升上去或降下来，

$$
\begin{align}
    \psi^{\mu} =& \langle e^{\mu} | \psi \rangle
      = \sum_{\nu} \langle e^{\mu} | e^{\nu}\rangle\langle e_{\nu} | \psi \rangle \\
      =& \sum_{\nu} S^{\mu \nu} \psi_{\nu}^*
\end{align}
$$

同理

$$
\begin{align}
    \psi_{\mu}^* = \sum_{\nu} S_{\mu \nu} \psi^{\nu}
\end{align}
$$

对于任意算符也是一样，例如，

$$
\begin{align}
    B_{\mu \nu} =& \langle e_{\mu} | B | e_{\nu}\rangle \\
      =& \sum_{\lambda} S_{\mu \lambda} B^{\lambda}{}_{\nu} \\
      =& \sum_{\lambda} B_{\mu}{}^{\lambda} S_{\lambda \nu}
\end{align}
$$

对任意态 $|\psi\rangle$ , $\psi^{\mu}$ 和 $\psi^{\nu}$ 分别就是在两组互相对偶的非正交基底上的展开系数，

$$
\begin{align}
    |\psi\rangle = \sum_{\mu} | e_{\mu}\rangle \langle e^{\mu}| \psi\rangle
      = \sum_{\mu} \psi^{\mu} | e_{\mu} \rangle
\end{align}
$$

$$
\begin{align}
    \langle \psi | = \sum_{\mu} \langle\psi | e_{\mu}\rangle \langle e^{\mu}|
    = \sum_{\mu} \langle e^{\mu}| \psi_{\mu}
\end{align}
$$

### 与正交基底的变换关系

正交基底的对偶基底就是它本身，即

$$
\begin{align}
    |e_n \rangle = |e^n\rangle
\end{align}
$$

度规是单位阵

$$
\begin{align}
    S_{mn} = \langle e_m | e_n \rangle = \delta_{mn},
    \quad S^{mn} = \delta^{mn}
\end{align}
$$

展开系数

$$
\begin{align}
    \psi^n = \langle e^n | \psi \rangle = \langle e_n | \psi\rangle = \psi_n^*
\end{align}
$$

变换矩阵

$$
\begin{align}
    T^n{}_{\mu} = T_{n\mu} = \langle e_n|e_{\mu}\rangle
      = \langle e^n|e_\mu\rangle
\end{align}
$$

$$
\begin{align}
    T_n{}^{\mu} = T^{n\mu} = \langle e^n|e^{\mu}\rangle
      = \langle e_n|e^\mu\rangle
\end{align}
$$

$$
\begin{align}
    \sum_n T_{\mu n} T^{n \nu}
      = \sum_n \langle e_{\mu} | e_n\rangle \langle e^n|e^{\nu}\rangle
      = \delta_\mu{}^{\nu}
\end{align}
$$

注意，类似于度规，在这里 $T_{\mu n}$ 和 $T^{n \mu}$ 是两个互逆的矩阵的矩阵元。

变换关系为

$$
\begin{align}
    \psi^n = T^n{}_{\mu} \psi^{\mu}
\end{align}
$$

$$
\begin{align}
    \psi^{\mu} = T^{\mu}{}_n \psi^{n}
\end{align}
$$

证明如下

$$
\begin{align}
    |\psi\rangle =& \sum_n |e_n\rangle\langle e^n|\psi\rangle
        = \sum_n \psi^n |e_n\rangle \\
      =& \sum_n \sum_{\mu} |e_n \rangle \langle e^n | e_{\mu}\rangle
       \langle e^{\mu} | \psi\rangle
        = \sum_n \sum_{\mu} T^n{}_{\mu} \psi^{\mu} | e_n \rangle
\end{align}
$$

$$
\begin{align}
    |\psi\rangle =& \sum_{\mu} | e_{\mu}\rangle \langle e^{\mu} | \psi\rangle
        = \sum_{\mu} \psi^{\mu} | e_{\mu}\rangle \\
      =& \sum_{\mu}\sum_n | e_{\mu}\rangle \langle e^{\mu}
          |e_n\rangle\langle e^n| \psi\rangle
        = \sum_{\mu}\sum_n T^{\mu}{}_n \psi^n |e_\mu\rangle
\end{align}
$$

## Reference

- 2020, Sakurai and Napolitano, Modern Quantum Mechanics
- [1991, Phys. Rev. A 43, 5770, Nonorthogonal basis sets in quantum mechanics: Representations and second quantization](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.43.5770)
- [2017, Phys. Rev. B 95, 115155, Quantum mechanics in an evolving Hilbert space](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.95.115155)
- [Wikipedia: Covariance and contravariance of vectors](https://en.wikipedia.org/wiki/Covariance_and_contravariance_of_vectors)