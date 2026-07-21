---
title: Arnoldi Iteration
date: 2026-07-20
category: physics
tags:
  - "numerical linear algebra"
  - "Krylov subspace"
---

## QR Factorization

```python
def gram_schmidt_unstable(A: np.ndarray):
    """
    Algorithm 7.1 in Book Trefethen&Bau Numerical Linear Algebra.

    A: m*n matrix, m >= n, very high matrix, full column rank.

    test:
    A = np.random.rand(5, 3) + 1j*np.random.rand(5, 3)
    Q, R = gram_schmidt_unstable(A)
    Q1, R1 = np.linalg.qr(A)
    print(Q)
    print(Q1)
    print(R)
    print(R1)
    """
    _, n = A.shape
    dtype = np.result_type(A, np.float64)
    R = np.zeros((n, n), dtype=dtype)
    Q = np.zeros(A.shape, dtype=dtype)
    for i in range(n):
        Q[:, i] = A[:, i]
        for j in range(i):
            R[j, i] = Q[:, j].conj()@A[:, i]
            Q[:, i] = Q[:, i] - R[j, i]*Q[:, j]
        R[i, i] = np.linalg.norm(Q[:, i])
        Q[:, i] = Q[:, i] / R[i, i]
    return Q, R


def gram_schmidt_modified(A: np.ndarray):
    """
    Algorithm 8.1 in Book Trefethen&Bau Numerical Linear Algebra.

    A: m*n matrix, m >= n, very high matrix, full column rank.

    A = np.random.rand(3, 3) + 1j*np.random.rand(3, 3)
    Q, R = gram_schmidt_modified(A)
    Q1, R1 = np.linalg.qr(A)
    print(Q)
    print(Q1)
    print(R)
    print(R1)
    """
    _, n = A.shape
    dtype = np.result_type(A, np.float64)
    R = np.zeros((n, n), dtype=dtype)
    Q = A.astype(dtype, copy=True)
    for i in range(n):
        R[i, i] = np.linalg.norm(Q[:, i])
        Q[:, i] = Q[:, i] / R[i, i]
        for j in range(i+1, n):
            R[i, j] = Q[:, i].conj()@Q[:, j]
            Q[:, j] = Q[:, j] - R[i, j]*Q[:, i]
    return Q, R
```

## Power Iteration

```python
def power_iteration(A: np.ndarray, n: int):
    """
    test:
    dim = 50
    # A = np.random.rand(dim, dim)
    A = np.random.uniform(-np.sqrt(3/dim), np.sqrt(3/dim), size=(dim, dim))
    A = A + A.conj().T
    w, v = np.linalg.eig(A)
    n = 150
    iter_num = list(range(1, n+1))
    eigmax = [res[0] for res in power_iteration(A, n)]
    fig = px.line(x=iter_num, y=eigmax)
    for wi in w:
        fig.add_scatter(x=iter_num, y=[np.real(wi)]*n,
                        mode='lines', line=dict(color='grey'))
    fig.show()
    """
    x = np.random.rand(A.shape[0])
    ev = x / np.linalg.norm(x)
    for _ in range(n):
        x = ev
        ev = A@x
        lam = x.conj()@ev
        ev = ev / np.linalg.norm(ev)
        yield lam, ev
```

## Arnoldi Iteration

### Definition

这里采用线性代数中常用的记号， $*$ 表示厄米共轭，即复共轭加转置。

与 power iteration 不同的是，Arnoldi Iteration 每一步都做正交化，类似于 power iteration 与 QR 分解的结合，

$$
\begin{align}
  A = Q R = Q H Q^*,
  \quad
  AQ = Q H.
\end{align}
$$

递推公式

$$
\begin{align}
  A Q_n = Q_{n + 1} \tilde{H}_n,
\end{align}
$$

即新一步的会新生一个新的向量，它是 $A$ 作用在前一步上之后，再做线性组合。
其中 $Q_n = [w_0, w_1, w_2, \cdots , w_{n - 1}]$ ，

$$
\begin{align}
  \tilde{H}_n = \begin{pmatrix}
    H_{00} & H_{01} & H_{02} & \cdots & H_{0, n-2} & H_{0, n-1} \\
    H_{10} & H_{11} & H_{12} & \cdots & H_{1, n-2} & H_{1, n-1} \\
    0      & H_{21} & H_{22} & \cdots & H_{2, n-2} & H_{2, n-1} \\
    \vdots & \vdots & \vdots & \ddots & \vdots     &\vdots      \\
    0      & 0      & 0      & \cdots & 0          & H_{n, n-1}
  \end{pmatrix},
\end{align}
$$

也就是

$$
\begin{align}
 A w_{n-1} = w_0 H_{0, n-1} + w_1 H_{1, n-1} + \cdots + w_{n}H_{n, n-1}.
\end{align}
$$

### 手算示例

$$
\begin{align}
  A = \begin{pmatrix}
    1 & 3 & 0 \\
    4 & 3 & 7 \\
    7 & 4 & 1
  \end{pmatrix}
\end{align}
$$

$$
\begin{align}
  b = \begin{pmatrix}
    0 \\ 2 \\ 0
  \end{pmatrix}
\end{align}
$$

#### Initialize

$$
\begin{align}
  w_0 = \frac{b}{||b||} = \begin{pmatrix}
    0 \\ 1 \\ 0
  \end{pmatrix}
\end{align}
$$

$$
\begin{align}
  Q = [w_0]
\end{align}
$$

#### Step 1

用 $A$ 作用在上一步的 $Q$ 的最后一个列向量上，

$$
\begin{align}
  w_1^{(1)} = A Q[-1] = A w_0 = \begin{pmatrix}
    3 \\ 3 \\ 4
  \end{pmatrix},
\end{align}
$$

其中 $w$ 的下标表示迭代的次数，上标表示在一次迭代中还未减去的其它基底的个数。

根据定义计算 $H_{00}$ ，也就是 $A$ 在新基底下的矩阵元，

$$
\begin{align}
  H_{00} = w_0^* A w_0 = w^*_0 w_1^{(1)}  = 3,
\end{align}
$$

同时它也是我们下一步需要的。减去在 $Q$ 的其它向量上的分量，构建正交基底，

$$
\begin{align}
  w_1^{(0)} = w_1^{(1)} - w^*_0 w_1^{(1)}\cdot  w_0 = \begin{pmatrix}
    3 \\ 0 \\ 4
  \end{pmatrix}.
\end{align}
$$

计算模长，然后归一化，

$$
\begin{align}
  ||w_1^{0}|| = 5,
\end{align}
$$

$$
\begin{align}
  w_1 = \frac{w_1^{(0)}}{||w_1^{(0)}||} = \begin{pmatrix}
    \frac{3}{5} \\ 0 \\ \frac{4}{5}
  \end{pmatrix}.
\end{align}
$$

同时根据 $H_{10}$ 的定义，发现它就是模长，

$$
\begin{align}
  H_{10} = w_1^* A w_0 = \frac{1}{||w_1^{(0)}||} w_1^{(0)*} A w_0
  = ||w_1^{(0)}|| = 5,
\end{align}
$$

其中投影 $w_1^{(0)*} A w_0$ 的物理意义也很明确，

$$
\begin{align}
  w_1^{(0)*} A w_0 = w_1^{(0)*} w_1^{(1)} = w_1^{(0)*}\left[
     w_1^{(0)} + w^*_0 w_1^{(1)}\cdot  w_0
     \right],
\end{align}
$$

第一项是在 $w_1^{(0)}$ 方向上的分量，即为模长 $||w_1^{(0)}||^2$ ，
第二项是在与之垂直的方向上的分量，为 $0$ 。

由此就得了本步的结果：

$$
\begin{align}
  Q = [w_0, w_1] = \begin{pmatrix}
    0 & \frac{3}{5} \\
    1 & 0 \\
    0 & \frac{4}{5}
  \end{pmatrix},
\end{align}
$$

$$
\begin{align}
  H = \begin{pmatrix}
    3 \\ 5
  \end{pmatrix},
\end{align}
$$

验证，

$$
\begin{align}
  Q[0]^* A Q[0] = 3 = H_{00}.
\end{align}
$$

#### Step 2

用 $A$ 作用在上一步的 $Q$ 的最后一个列向量上，

$$
\begin{align}
  w_2^{(2)} = A Q[-1] = A w_1 = \begin{pmatrix}
    \frac{3}{5} \\ 8 \\ 5
  \end{pmatrix}
\end{align}
$$

计算并减掉投影，

$$
\begin{align}
  H_{01} = w_0^* A w_1 = w^*_0 w_2^{(2)} = 8.
\end{align}
$$

$$
\begin{align}
  w_2^{(1)} = \begin{pmatrix}
    \frac{3}{5} \\ 0 \\ 5
  \end{pmatrix}.
\end{align}
$$

计算另一个方向上的投影并减掉，

$$
\begin{align}
  H_{11} =  w_1^* A w_1 = w^*_1 w_2^{(1)} = \frac{109}{25},
\end{align}
$$

$$
\begin{align}
  w_2^{(0)} = w_2^{(1)} - w_1^* w_2^{(1)} w_1 = \frac{63}{125}\begin{pmatrix}
    - 4 \\ 0 \\ 3
  \end{pmatrix}.
\end{align}
$$

计算模长，并归一化，

$$
\begin{align}
  H_{21} = || w_2^{(0)} || = \frac{63}{25}.
\end{align}
$$

得到本步的结果，

$$
\begin{align}
  w_2 = \frac{1}{5}\begin{pmatrix}
    -4 \\ 0 \\3
  \end{pmatrix}.
\end{align}
$$

$$
\begin{align}
    Q = [w_0, w_1, w_2]
\end{align}
$$

$$
\begin{align}
  H = \begin{pmatrix}
    3 & 8 \\
    5 & \frac{109}{25} \\
    0 & \frac{63}{25}
  \end{pmatrix}
\end{align}
$$

### code

```python
def arnoldi_iteration(A: np.ndarray, n: int, b=None, output_all=False):
    """
    Algorithm 33.1 in Book Trefethen&Bau Numerical Linear Algebra.

    A: square matrix, full rank, assuming no happy breakdown.

    Good example:
    A = np.array([[1, 3, 0],
              [4, 3, 7],
              [7, 4, 1]])
    b = np.array([0, 2, 0])
    arnoldi_iteration(A=A, b=b, n=2, output_all=True)
    """
    if b is None:
        b = np.random.rand(A.shape[0])
    dtype = np.result_type(A, b, np.float64)
    Q = [b/np.linalg.norm(b)]
    H = np.zeros((n+1, n), dtype=dtype)
    for i in range(n):
        v = A@Q[-1]
        for j in range(i+1):
            H[j, i] = Q[j].conj()@v
            v = v - H[j, i]*Q[j]
        H[i+1, i] = np.linalg.norm(v)
        Q.append(v/H[i+1, i])
    if output_all:
        return np.column_stack(Q), H
    else:
        return np.column_stack(Q)[:, :-1], H[:-1, :]
```

### Arnoldi and Polynomial Approximation

由递推式能看出 $w_n$ 是关于 $A$ 的 $n$ 次多项式，作用在初始向量 $b$ 上，
$$
\begin{align}
  w_n =& \frac{1}{H_{n, n-1}} \left[
    A w_{n-1} - \left( w_0 H_{0, n-1} + w_1 H_{1, n-1}, \cdots w_{n-1} H_{n-1, n-1} \right)
    \right] \\
    =& \# p^n(A)b
    = \# \left(c_0 b + c_1 Ab + c_2 A^2 b + \cdots +  A^{n} b \right) \\
    \equiv & \# \left( Q_n^* y + A^nb \right),
\end{align}
$$
其中 $\#$ 是一个系数， 最高阶系数 $c_n = 1$ 。
由于我们做了正交化，所以 $w_n$ 与
Krylov 子空间 $\mathcal{K}_{n - 1} = \{b, Ab, A^2, \cdots, A^{n - 1}b\}$ 垂直。
那么 $||w_n||/\#$ 可以看成是

$$
\begin{align}
\mathrm{Find} \quad   y \in \mathcal{K}, \quad
\mathrm{min} ||Q _n y + A^nb ||
\end{align}
$$

的 Residual 。

#### Roots of $p^n(z)$

$w_n = p^n(A)b \bot \mathcal{K}_{n - 1}$ 可以写成,

$$
\begin{align}
  Q_n^* \cdot p^n(A) b = 0
\end{align}
$$

变换到 $Q$ 基底下，

$$
\begin{align}
  Q_n^* Q \cdot Q^* p^n(A) Q \cdot Q^* b
  =Q_n^* Q \cdot p^n(H)  \cdot Q^* b = 0,
\end{align}
$$

其中 $Q^* b = (||b||, 0, 0, \cdots)^T$ ，
所以 $p^n(H)  \cdot Q^* b = ||b|| \cdot p^n(H)[0]$ ，是 $p^n(H)$ 第一列。
由正交性可得 $Q_n^* Q = (I_n, \mathbf{0})$ 。最终

$$
\begin{align}
  Q_n^* \cdot p^n(A) b = ||b||\cdot p^n(H)[:n, 0] = 0
\end{align}
$$

由于 $H$ 左下角为 $0$ ，所以 $p^n(H)[:n, 0] =0$ 就相当于要求 $p^n(H_n) =0$ 。
由 [Cayley-Hamilton theorem](https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem) 可知，
$p^n(H_n)$ 的特征多项式

$$
\begin{align}
   \prod_{i=1}^n (z - \lambda_i)
\end{align}
$$

即是我们要的 $p^n(z)$ 。

从物理上讲，我们选定了一个初态，然后用 Hamiltonian 作用在这个初态上。
每作用一次，相当于多一阶相互作用，把不同的态耦合起来。
而生成的 Krylov 子空间 $\mathcal{K}_n$ ，相当于从初态出发的 $n - 1$ 阶微扰能够耦合到的一个子空间。

#### Arnoldi Lemniscates

Arnoldi iteration 的 residual 为

$$
\begin{align}
C = \frac{||p^n(A)b||}{||b||}
\end{align}
$$

随着迭代次数的增加，$p^n$ 的根会变多，并且趋近 $A$ 的本征值，同时 residual $C$ 也逐渐变小。
如果我们在复平面上画出 $|p(z)|$ ，那么当迭代次数接近 $A$ 的维度时，$|p(z)|$ 在 $A$ 的本征值也接近于零。

下面我们画出 $\log |p(z)| = \log C$ 的等高线（红线）。

当 $n = 1$ 时，Heesenberg 矩阵 $H$ 是一维的，只有一个本征值，对应的 $|p(z)| = |z - \lambda|$ ，
因此在复平面上是一个完美的圆：

<iframe src="2026-07-20-physics-Arnoldi_iteration/arnoldi_lemniscates_n1.html" width="100%" height="600"></iframe>

当 $n = 2$ 时， Heesenberg 矩阵 $H$ 是二维的，有两个本征值（图中可以看出，在原点附近，位置比较接近）：
<iframe src="2026-07-20-physics-Arnoldi_iteration/arnoldi_lemniscates_n2.html" width="100%" height="600"></iframe>

当 $n = 3$ 时，有三个本征值：
<iframe src="2026-07-20-physics-Arnoldi_iteration/arnoldi_lemniscates_n3.html" width="100%" height="600"></iframe>

$n = 4$ ：
<iframe src="2026-07-20-physics-Arnoldi_iteration/arnoldi_lemniscates_n4.html" width="100%" height="600"></iframe>

$n = 5$ ：
<iframe src="2026-07-20-physics-Arnoldi_iteration/arnoldi_lemniscates_n5.html" width="100%" height="600"></iframe>

$n = 6$ ，可以数出，有六个零点：
<iframe src="2026-07-20-physics-Arnoldi_iteration/arnoldi_lemniscates_n6.html" width="100%" height="600"></iframe>

$n = 7$ ，它圈出了那个孤立的本征值：
<iframe src="2026-07-20-physics-Arnoldi_iteration/arnoldi_lemniscates_n7.html" width="100%" height="600"></iframe>

$n = 8$ ：
<iframe src="2026-07-20-physics-Arnoldi_iteration/arnoldi_lemniscates_n8.html" width="100%" height="600"></iframe>

$n = 9$ ：
<iframe src="2026-07-20-physics-Arnoldi_iteration/arnoldi_lemniscates_n9.html" width="100%" height="600"></iframe>

```python
# Ref: page 262, 263, Book Trefethen&Bau Numerical Linear Algebra.

# Generate random matrix A and initial vector b
rng = np.random.default_rng(12)
dim = 100
A = rng.normal(loc=0, scale=1/np.sqrt(dim), size=(dim, dim))
A[0, 0] = 1.5
b = rng.random(A.shape[0])

# Solve the exact eigenvalue of A
w, _ = np.linalg.eig(A)
# Arnoldi iteration
n = 9
Qn, Hn = arnoldi_iteration(A=A, n=n, b=b)
# Ritz values
thetas, _ = np.linalg.eig(Hn)
# Generate complex plane
n_data = 100
re = np.linspace(-2, 2, n_data)
im = np.linspace(-2, 2, n_data)
RE, IM = np.meshgrid(re, im)
Z = RE + 1j*IM
# log(abs(p(z)))
abs_p = np.sum([np.log(np.abs(Z-theta)) for theta in thetas], axis=0)
# Calculate the log of residual log(||p(A)b|| / ||b||)
coeff = np.poly(thetas)
C = coeff[0] * b
for c in coeff[1:]:
    C = A@C + c*b
C = np.linalg.norm(C) / np.linalg.norm(b)

fig = go.Figure()
fig.add_trace(go.Heatmap(x=re, y=im, z=abs_p,
                         colorbar=dict(title='log(||p(z)||)')))
fig.add_trace(go.Contour(x=re, y=im, z=abs_p,
                         contours=dict(start=np.log(C), end=np.log(C),
                                       size=1, coloring='lines'),
                         line=dict(width=3), showscale=False,
                         colorscale=[[0, "red"], [1, "red"]]
                         ))
fig.add_trace(go.Scatter(x=w.real, y=w.imag,
                         mode='markers', marker=dict(color='blue')))
fig.update_layout(width=500, height=500, title=f'n={n}, log(C)={C:.2f}',
                  xaxis=dict(title='Re'),
                  yaxis=dict(title='Im', scaleanchor='x', scaleratio=1))
# fig.show()
fig.write_html(f'arnoldi_lemniscates_n{n}.html', include_plotlyjs='cdn') #, include_mathjax="cdn")
```

## Reference

- 1997 - Lloyd N. Trefethen, David Bau - Numerical Linear Algebra