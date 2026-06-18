---
title: 群表示论备忘
date: 2026-06-18
category: physics
tags:
  - "group theory"
---

## Character is a function of class

Dimensions of the irreducible representations:

$$
\begin{align}
  \sum_r d_r^2 = N(G)
\end{align}
$$

Column orthogonality:

$$
\begin{align}
  \sum_c n_c (\chi^{(r)}(c))^* \, \chi^{(s)}(c) = N(G) \delta^{rs}
\end{align}
$$

Row orthogonality:

$$
\begin{align}
  \sum_r \chi^{(r)} (c)^* \, \chi^{(r)}(c') = \frac{N(G)}{n_c} \delta^{c c'}
\end{align}
$$

The character table is square:

$$
\begin{align}
N(C) = N(R)
\end{align}
$$

Great orthogonality theorem

$$
\begin{align}
\sum_g D^{(r) \dagger}(g)^i_{\, j} D^{(s)} (g)^k_{\, l}
= \frac{N(G)}{d_r} \delta^{rs} \delta^i_{\,l}\delta^k_{\,j}
\end{align}
$$

## Character table

### Cyclic groups $Z_n$

$Z_n$ 是 Abel 群。
Abel 群的等价类的个数与群元的个数相同。
Abel 群所有的不可约表示都是一维的。
不可约表示的个数又与类的个数相同。
所以 $Z_n$ 有 $n$ 个一维不可约表示。

如 $Z_3$ 的群元 $\{I, g, g^2\}$，特征值表为

$$
\begin{array}{c|ccc}
  \hline
  Z_3   &   I  &  g         &  g^2 \\
  \hline
  1     &   1  &  1         &  1   \\
  1'    &   1  &  \omega    &  \omega^2   \\
  1'    &   1  &  \omega^2  &  \omega   ,\\
\end{array}
$$
其中 $\omega=e^{2\pi i /3}$ 。

### Even permutation group $A_3$

$$
\begin{array}{ccc|ccc}
\hline
A_3 & n_c &            & 1 & 1'       & 1'' \\
\hline
    & 1   & I          & 1 & 1        & 1        \\
Z_3 & 1   & c=(123)    & 1 & \omega   & \omega^* \\
Z_3 & 1   & a=(132)    & 1 & \omega^* & \omega  \\
\hline
\end{array}
$$

### Even permutation group $A_4$

$$
\begin{array}{ccc|cccc}
\hline
A_4   &  n_c  &  c       &  1  &  1'       &   1''      &  3 \\
\hline
      &  1    &  I       &  1  &  1        &   1        &  3 \\
Z_2   &  3    & (12)(34) &  1  &  1        &   1        &  -1 \\
Z_3   &  4    & (123)    &  1  &  \omega   &   \omega^* &  0  \\
Z_3   &  4    & (132)    &  1  &  \omega^* &   \omega   &  0  \\
\hline
\end{array}
$$

### Permutation group $S_3$

$$
\begin{array}{ccc|ccc}
\hline
S_3 & n_c &               & 1 & \bar{1} & 2 \\
\hline
    & 1 & I               & 1 & 1  & 2  \\
Z_3 & 2 & (123),(132)     & 1 & 1  & -1_x \\
Z_2 & 3 & (12),(23),(31)  & 1 & -1 & 0_y  \\
\hline
\end{array}
$$

### Permutation group $S_4$

$$
\begin{array}{ccc|ccccc}
\hline
S_4 & n_c &        & 1 & \bar{1} & 2 & 3 & \bar{3} \\
\hline
    & 1 & I        & 1 & 1  & 2  & 3  & 3  \\
Z_2 & 3 & (12)(34) & 1 & 1  & 2  & -1 & -1 \\
Z_3 & 8 & (123)    & 1 & 1  & -1 & 0  & 0  \\
Z_2 & 6 & (12)     & 1 & -1 & 0  & 1  & -1 \\
Z_4 & 6 & (1234)   & 1 & -1 & 0  & -1 & 1  \\
\hline
\end{array}
$$

## Reference

- 2016 - A. Zee - Group Theory in a Nutshell for Physicists (2016, Princeton University Press)