---
title: Fourier transform 总结
date: 2018-09-07
category: physics
tags:
  - "Fourier transform"
  - "数学"
---

- [分类](#分类)
- [例子](#例子)
  - [实空间离散](#实空间离散)
  - [实空间有限尺寸](#实空间有限尺寸)
  - [实空间无穷大](#实空间无穷大)


## 分类

根据变量的连续与否，傅立叶变换有以下几种情况：

- 实空间离散，动量空间离散（又见[2026-06-18-群表示论备忘](./2026-06-18-physics-group_representation_theory.md)的 $Z_n$ 群）

$$
\begin{align*}
  \sum_{l = 1}^N e^{-i k'l} e^{i kl}=N\delta_{k,k'},
  \quad l = 1, 2, \cdots N,
  \quad k = 0, \frac{2\pi}{N}, 2 \frac{2\pi}{N}, \cdots (N-1)\frac{2\pi}{N}
\end{align*}
$$

- 实空间有限尺寸，动量空间离散

$$
\begin{align*}
  \int_{0}^{L} e^{-ik'x} e^{ikx} \mathrm{d}x = L \delta_{k, k'}, \quad
  k = 0, \pm\frac{2\pi}{L}, \pm 2\frac{2\pi}{L}, \cdots
\end{align*}
$$

- 实空间无穷大，动量空间无穷大

$$
\begin{align*}
  \int_{-\infty}^{\infty} e^{-ikx} e^{ik'x} \mathrm{d}x = 2\pi \delta (k-k')
\end{align*}
$$

上式的等号在[分布](https://en.wikipedia.org/wiki/Distribution_(mathematical_analysis)#Tempered_distributions_and_Fourier_transform)意义下成立。

## 例子

### 实空间离散

周期性边界条件下的紧束缚模型

$$
H = -t \sum_{j=1}^{N} \left( c_j^{\dagger} c_{j+1} + c_{j+1}^{\dagger} c_j \right)，
\quad c_{N + 1} = c_1
$$

具有平移对称性，本征态是平面波

$$
\begin{align}
  a_k^{\dagger} = \sum_j c_j^{\dagger} \langle j| k\rangle
  =\frac{1}{\sqrt{N}} \sum_j c_j^{\dagger} e^{i j k},\quad k = 0, \frac{2\pi}{N}, 2\frac{2\pi}{N}, \cdots (N - 1)\frac{2\pi}{N}
\end{align}
$$

所以

$$
\begin{align}
  H =& -t \sum_{j = 1}^N \sum_{k_1, k_2} \frac{1}{N}
   \left( a_{k_1}^\dagger a_{k_2} e^{-i j(k_1 - k_2)} e^{i k_2}
    +  a_{k_2}^\dagger a_{k_1} e^{-i j(k_2 - k_1)} e^{-ik_2} \right) \\
    =& -t \sum_k 2\cos k a_{k}^\dagger a_{k}
\end{align}
$$


### 实空间有限尺寸

尺寸为 $L$ 的周期性边界条件的一维系统（箱归一化）

动量本征态 $\psi_k(x) = \langle x | k\rangle$ 是周期函数

$$
\begin{align*}
\psi_k(x+L) = \psi_k(x) = \frac{1}{\sqrt{L}}e^{ikx}, \quad
k = 0, \pm \frac{2\pi}{L}, \pm 2\frac{2\pi}{L}, \pm 3\frac{2\pi}{L}, \cdots
\end{align*}
$$

动量本征态正交归一

$$
\begin{align*}
\langle k | k'\rangle = \int_{0}^{L} e^{-ikx} e^{ik'x} \mathrm{d}x = L \delta(k-k')
\end{align*}
$$

### 实空间无穷大

一维无穷空间中的动量本征函数

$$
\begin{align*}
-i \frac{\mathrm{d}}{\mathrm{d}x} \langle x|k\rangle
= k \langle x| k\rangle \quad
\Longrightarrow \quad \psi_k(x) = \langle x| k\rangle
= \frac{1}{\sqrt{2\pi}} e^{i kx}
\end{align*}
$$

正交归一

$$
\begin{align*}
\langle k | k' \rangle =
\frac{1}{2\pi}\int_{-\infty}^{\infty} e^{-ikx} e^{ik'x} \mathrm{d}x
=\frac{1}{2\pi} \int_{-\infty}^{\infty} e^{i(k'-k)x} \mathrm{d}x = \delta(k'-k)
\end{align*}
$$
