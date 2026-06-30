---
title: 群表示论备忘
date: 2026-06-18
category: physics
tags:
  - "group theory"
  - "Fourier transform"
---

- [Definition of group](#definition-of-group)
- [Definition of representation](#definition-of-representation)
- [Orthogonality theorems](#orthogonality-theorems)
- [正则表示（Regular Representation）约化出所有的不可约表示](#正则表示regular-representation约化出所有的不可约表示)
- [投影到某个不可约表示的投影算符](#投影到某个不可约表示的投影算符)
- [Schur's lemma and degeneracy](#schurs-lemma-and-degeneracy)
- [Character tables of some group](#character-tables-of-some-group)
  - [Even permutation group $A\_3$](#even-permutation-group-a_3)
  - [Even permutation group $A\_4$](#even-permutation-group-a_4)
  - [Permutation group $S\_3$](#permutation-group-s_3)
  - [Permutation group $S\_4$](#permutation-group-s_4)
- [Appendix](#appendix)
  - [Covariance and contravariance of vectors](#covariance-and-contravariance-of-vectors)
  - [直和](#直和)
- [Reference](#reference)

## Definition of group

群（group）是一个抽象的数学概念。定义如下（[Wikipedia: Group (mathematics)](https://en.wikipedia.org/wiki/Group_(mathematics))）:

A group is a set $G$ together with a binary operation on ⁠ $G$⁠, here denoted " $\cdot$ ", that combines any two elements $a, b\in G$ to form an element of ⁠$G$, denoted $ab$⁠ , such that the following three requirements, known as group axioms, are satisfied:

1. Associativity:
    $\forall a, b, c \in G$ ⁠, one has $(ab)c = a(bc)$ ⁠.
2. Identity element
    $\exists e \in G$ , $\forall a\in G$⁠, one has ⁠$e a = a e = a$ ⁠.
3. Inverse element
    $\forall a \in G$ ⁠, $\exists b \in G$ , such that $ab = ba = e$ .

Notes:

- 通过我们说一个 group $G$ 时，默认是包含乘法关系 $(G, \cdot)$ 乘法 " $\cdot$ "常省略不写。

## Definition of representation

一般一个数学上抽象的群会同态于一些具体的群。群的表示就是把一个群，映射到一个和它同态的矩阵构成的群。
群的乘法由矩阵乘法表示。
这样，我们就可以把具体实际物理意义的群，如对称操作构成的群，与矩阵乘法对应起来。

定义如下（[Wikipedia: Group representation](https://en.wikipedia.org/wiki/Group_representation)）：

A representation of a group $G$ on a vector space $V$ over a field $K$ is a group homomorphism from $G$ to $GL(V)$, the general linear group on $V$. That is, a representation is a map

$$
\begin{align}
  \rho \colon G\to \mathrm {GL} \left(V\right)
\end{align}
$$

such that

$$
\begin{align}
  \rho (g_{1}g_{2})=\rho (g_{1})\rho (g_{2}),\qquad \forall g_{1},g_{2}\in G.
\end{align}
$$

Notes:

- "vector space $V$ over a field $K$" : $K$ 决定了矢量空间中的数乘来自哪里。

- "Field"：有四则运算的集合，比如：实数域 $\mathbb{R}$ 。

- Homomorphism：同态。保持结构的映射，不要求一一对应，也不要求满射。

- Isomorphism: 同构。既是同态，又是双射。

- 群的表示是同态，不是同构，比如平凡表示就是多对一的关系。

- $GL(V)$ : General Linear。表示矢量空间 $V$ 上所有可逆线性变换组成的群。一般 $GL(V)$ 非常大，所以 $\rho \colon G\to \mathrm {GL} \left(V\right)$ 一般不是满射。

- 忠实表示 faithful representation：$\rho \colon G\to \mathrm {GL} \left(V\right)$ 是一个单射。

## Orthogonality theorems

$n_c$ 表示类 $c$ 中群元的个数。 $d_r$ 表示不可约表示 $r$ 的维度。

Dimensions of the irreducible representations:

$$
\begin{align}\label{eq:d-of-irr}
  \sum_r d_r^2 = N(G)
\end{align}
$$

Column orthogonality:

$$
\begin{align}\label{eq:col-orth}
  \sum_c n_c \cdot (\chi^{(r)}(c))^* \cdot \chi^{(s)}(c) = N(G) \delta^{rs}
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

## 正则表示（[Regular Representation](https://en.wikipedia.org/wiki/Regular_representation)）约化出所有的不可约表示

正则表示 $D^{(\mathrm{reg})}$ 是把所有的群元当基底，即 $|e\rangle, |g_1\rangle, |g_2\rangle, \cdots$，即

$$
\begin{align}
  D^{(\mathrm{reg})}(g) |h\rangle = |gh\rangle.
\end{align}
$$

将正则表示约化成不可约表示的直和 $D^{(\mathrm{reg})} \simeq \bigoplus_r n_r D^{(r)}$，
对应的特征标有 $\chi^{(\mathrm{reg})}(c) = \sum_r n_r \chi^{(r)}(c)$ ，其中 $n_r$ 表示不可约表示 $r$ 出现的次数 。
根据列正交公式 $\eqref{eq:col-orth}$ 可知，

$$
\begin{align}
\sum_c n_c \cdot(\chi^{(r)}(c))^* \cdot \chi^{(\mathrm{reg})}(c)
=& \sum_c \sum_s n_c\cdot (\chi^{(r)}(c))^* \cdot n_s\cdot \chi^{(s)}(c) \\
=& \sum_s N(G) \delta_{r,s} \cdot n_s \\
=& n_r N(G)
\end{align}
$$

即

$$
\begin{align}
  n_r = \frac{1}{N(G)} \sum_c n_c \cdot(\chi^{(r)}(c))^* \cdot \chi^{(\mathrm{reg})}(c)
\end{align}
$$

容易证明：

$$
\begin{align}
  \chi^{(\mathrm{reg})}(g) =
  \left\{
  \begin{matrix}
  N(G), \quad &g=e, \\
  0, \quad &g\neq e.
  \end{matrix}
  \right.
\end{align}
$$

所以

$$
\begin{align}
  n_r =& \frac{1}{N(G)} \sum_c n_c \cdot(\chi^{(r)}(c))^* \cdot N(G)\delta_{c,[e]} \\
  =& n_{[e]} \cdot (\chi^{(r)}(e))^* \\
  =& (\chi^{(r)}(e))^* \\
  =& d_r,
\end{align}
$$
其中 $[e]$ 表示单位元的类，它只有一个群元，即 $n_{[e]} = 1$ 。

即： **正则表示可以约化出所有的不可约表示，不可约表示出现的次数等于不可约表示的维度。也容易得公式 $\eqref{eq:d-of-irr}$ $\sum_r d_r^2 = N(G)$ 。**

对于 Abel 群，每个群元都自成一类。
又因为 the character table is square，不可约表示的个数又与类的个数相同，所以不可约表示的个数 $N(R) = N(G)$。根据 $\sum_r d_r^2 = N(G)$ 可得所有不可约表示都是一维的。
即，**对于有 $n$ 个群元的 Abel 群，它所有的不可约表示都是一维的，并且一共有 $n$ 个。**

例如：Cyclic groups $Z_n = \{g, g^2, g^3, \cdots g^{n-1}, g^n = e\}$ 是 Abel 群。
它的第 k 个一维不可约表示记为 $\lambda^{(k)}(g)$ , $k = 0, 1, 2, \cdots, n$ ，
那么 $\left[\lambda^{(k)}(g)\right]^n = 1$，
可解得 $\lambda^{(k)} (g) = e^{i k \frac{2\pi}{n}}$ 。
由正交定理可得
$$
\begin{align}
  \sum_{j = 1}^{n} e^{i \frac{2\pi}{n}j(l - k)} = \sum_{j=1}^n (\lambda^{(k)} (g^j))^*\cdot \lambda^{(l)} (g^j) =n\delta_{k,l}.
\end{align}
$$

如 $Z_3$ 的特征值表为

$$
\begin{array}{c|ccc}
  \hline
  Z_3   &   I  &  g         &  g^2 \\
  \hline
  1     &   1  &  1         &  1   \\
  1'    &   1  &  \omega    &  \omega^2   \\
  1''    &   1  &  \omega^2  &  \omega   ,\\
\end{array}
$$
其中 $\omega=e^{2\pi i /3}$ 。

## 投影到某个不可约表示的投影算符

假设表示 $D(g)$ 可以分解成不可约表示的直和
$D(g) = \bigoplus_p \left[ I_{n_p}\otimes D^{(p)} \right]$ ，
那么可以在表示 $D$ 的基底上构建到不可约表示 $r$ 的投影算符：

$$
\begin{align}
  P_{r} = \frac{d_r}{N(G)} \sum_{g\in G} \left(\chi^{(r)}(g)\right)^* D(g).
\end{align}
$$

可以写成分量式，并利用大正交定理证明它在 $r$ 表示上是单位阵，在其它表示上是 $0$ ，

$$
\begin{align}
  \left(P_{r}\right)_{pa_pi, qb_qj}
  =&  \frac{d_r}{N(G)} \sum_{g\in G}
   \left[
    \left( \sum_k D_{kk}^{(r)*}(g) \right)
    \left( \delta_{pq}\delta_{a_pb_p} D^{(p)}_{ij} \right)
   \right] \\
  =& \frac{d_r}{N(G)} \sum_{k} \delta_{pq}\delta_{a_pb_p}
   \cdot \frac{N(G)}{d_r}\delta_{rp} \delta_{ki}\delta_{kj} \\
  =& \delta_{rp} \cdot \delta_{rq} \delta_{a_pb_p} \delta_{ij}
\end{align}
$$
其中 $a_p$ 标记的是不可约表示 $p$ 的第几重。

在非块对角的基底下，即 $D'(g) \simeq \bigoplus_p \left[ I_{n_p}\otimes D^{(p)} \right]$ ，
时，也可以用同样的公式构造投影算符。因为投投影算符不会因为改变基底而改变。

## Schur's lemma and degeneracy

> If $D^{(r)}(g)$ is irreducible representation,
> If $\exists H, \forall g \in G$ , $HD^{(r)}(g) = D^{(r)}(g) H$,
> then $H = \lambda I$

也就是说，所有使得 Hamiltonian $H$ 保持不变的操作构成一个群 $G = \{g| g H = H g \}$ 。
如果选择合适基底，使得 Hilbert 空间所负载的群表示约化成了不可约表示的直和
$D(g) = \bigoplus_r I_{n_r} \otimes D^{(r)}$，并且所有出于的不可约表示都只有一重，
那么在这样的基底下， Hamiltonian 也是块对角的，并且每个块都是一个常数矩阵。
如果有不可约表示出现多重，那么 Hamiltonian 在同一个不可约表示之间可以有非对角项。

所以，如果我们可以找到一个系统的所有对称性，就相当于知道了它的所有的简并度。
当对称性破缺了一部分时，新对称群变成了原来的对称群的一个子群，原来的一些不可约表示变成了可约的，可进一步约化成维度更低的不可约表示，也就是说一些原来简并的能量本征态会解除简并。


## Character tables of some group

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
Z_3 & 2 & (123),(132)     & 1 & 1  & -1 \\
Z_2 & 3 & (12),(23),(31)  & 1 & -1 & 0  \\
\hline
\end{array}
$$

三个不可约表示：平凡一维表示 $1$ ，一维符号表示 $\bar{1}$ ，以及二维表示（三角形在平面中的对称操作）：

单位元：

$$
\begin{align}
  D^{(2)}(I) = \begin{pmatrix}
    1 & 0 \\
    0 & 1
  \end{pmatrix}
\end{align}
$$

旋转 $120$ 度:

$$
\begin{align}
  D^{(2)}((123)) =
  \begin{pmatrix}
    -\frac{1}{2}  & -\frac{\sqrt{3}}{2} \\
    \frac{\sqrt{3}}{2}  & -\frac{1}{2}
  \end{pmatrix}
\end{align}
$$

旋转 $-120$ 度:

$$
\begin{align}
  D^{(2)}((132)) =
  \begin{pmatrix}
    -\frac{1}{2}  & \frac{\sqrt{3}}{2} \\
    -\frac{\sqrt{3}}{2}  & -\frac{1}{2}
  \end{pmatrix}
\end{align}
$$

三个反射操作

$$
\begin{align}
  D^{(2)}((12)) =
  \begin{pmatrix}
    -1  & 0 \\
    0  & 1
  \end{pmatrix}
\end{align}
$$

$$
\begin{align}
  D^{(2)}((13)) =
  \begin{pmatrix}
    \frac{1}{2}  & -\frac{\sqrt{3}}{2} \\
    -\frac{\sqrt{3}}{2}  & -\frac{1}{2}
  \end{pmatrix}
\end{align}
$$

$$
\begin{align}
  D^{(2)}((23)) =
  \begin{pmatrix}
    \frac{1}{2}  & \frac{\sqrt{3}}{2} \\
    \frac{\sqrt{3}}{2}  & -\frac{1}{2}
  \end{pmatrix}
\end{align}
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

## Appendix

### [Covariance and contravariance of vectors](https://en.wikipedia.org/wiki/Covariance_and_contravariance_of_vectors)

在不正交的基底下：

- Covariance: 在不同表象间，基底的变换是 covariance，用下标， $\psi_j$ 。
- Contravariance: 在不同表象间，以与基底相反的方式变换，用上标， $\psi^j$ 。
- 它们之间由 metric 联系： $\psi_i = g_{ij} \psi^j， g^{ij}g_{jk}=\delta^i{}_k$ 。

例如：
例如，取二维非正交基底

$$
\begin{align}
  e_1 = \begin{pmatrix}
    1 \\
    0
  \end{pmatrix}
  ,\quad
  e_2 = \begin{pmatrix}
    1 \\
    1
  \end{pmatrix}
\end{align}
$$

任意向量 $\psi = \psi^1 e_1 + \psi^2 e_2$ 。如

$$
\begin{align}
  \psi = 3 e_1 + 5 e_2 = \begin{pmatrix}
    8 \\ 5
  \end{pmatrix}
\end{align}
$$

metric $g_{ij} = e_i \cdot e_j$ ,即

$$
\begin{align}
  g = \begin{pmatrix}
    1 & 1 \\
    1 & 2
  \end{pmatrix}
\end{align}
$$

比如可以用来计算长度 $\psi^i g_{ij} \psi^j = 89$ 。

但在这里考虑的**正交归一基底**下，只是为了少写复共轭符号：

$$
\begin{align}
  \psi_i \equiv (\psi^i)^*
\end{align}
$$

### 直和

如果一个矩阵是块对角的

$$
\begin{align}
  D = \begin{pmatrix}
    D^{(1)} & 0       & 0       & \cdots  \\
    0       & D^{(2)} & 0       & \cdots  \\
    0       & 0       & D^{(3)} & \cdots  \\
    \vdots  & \vdots  & \vdots  & \ddots
  \end{pmatrix}
\end{align}
$$

那么它可以写成直和的形式

$$
\begin{align}
  D =& \bigoplus_r D^{(r)} \\
    =& D^{(1)}\oplus D^{(2)} \oplus D^{(3)} \oplus \cdots
\end{align}
$$

写成分量

$$
\begin{align}
  D_{ri, sj} = \delta_{rs} D^{(r)}_{ij}
\end{align}
$$

如果同一个矩阵出现多次，则

$$
\begin{align}
  D =& \bigoplus_r \left( I_{n_r} \otimes D^{(r)} \right) \\
\end{align}
$$

其中 $n_r$ 是矩阵 $D^{(r)}$ 出现的次数，或重数， $I_{n_r}$ 是 $n_r$ 维的单位矩阵。
写成分量形式

$$
\begin{align}
  D_{ra_ri, sb_sj} = \delta_{rs}\delta_{a_r b_r} D^{(r)}_{ij}
\end{align}
$$

其中 $a_r , b_s$ 标记的是第 $r$ 个矩阵出现的第几重， $a_r = 1, 2, 3, \cdots, n_r$ 。

## Reference

- 2016 - A. Zee - Group Theory in a Nutshell for Physicists (2016, Princeton University Press)
