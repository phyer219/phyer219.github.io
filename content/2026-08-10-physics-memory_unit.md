---
title: 存储单位
date: 2026-08-10
category: physics
tags:
  - "computer science"
  - "computer memory"
---

## 单位

| 名称 | 缩写 | 中文      | 备注                |
|----- |------|---------|--------------------|
|bit   |  b   | 比特，位 |一个 0 或 1 比位      |
|byte  |  B   | 字节     |1B=8b ，一个 ASCII 字符用 8b 来编码     |

## 二进制词头

- $1\mathrm{Ki} = 2^{10} = 1024 \approx 10^3$
- $1\mathrm{Mi} = 2^{20}$
- $1\mathrm{Gi} = 2^{30}$

## 十进制词头

- $1\mathrm{k} = 10^3$
- $1\mathrm{M} = 10^6$
- $1\mathrm{G} = 10^9$

## 数据类型

| 类型 | 大小 | 备注|
|------|-----|-----|
|`float32`| `32b = 4B`||
|`float64`| `64b = 8B`||
|`complex64` | `64b = 8B`|实部和虚部各 `32b`|
|`complex128`| `128b = 16B`|

`python` 默认用的 `int` ， `float` ， `complex` 都没有固定大小。
`numpy` 通常依赖于平台，比如有时会默认用的是 `float64` , `int64` , `complex128` 。

```python
>>> type(1)
<class 'int'>

>>> type(1.0)
<class 'float'>

>>> type(1j)
<class 'complex'>

>>> np.array([[1, 2], [3, 4]]).dtype
dtype('int64')

>>> np.array([[1.0, 2], [3, 4]]).dtype
dtype('float64')

>>> np.array([[1.0j, 2], [3, 4]]).dtype
dtype('complex128')
```

## 例子

例如，一个 $10000\times 10000$ 的矩阵，大约占的内存是
$8\times 10^8\mathrm{B}$ ，

```python
a = rng.random((10000, 10000))
>>> sys.getsizeof(a)
800000128
>>> a.dtype
dtype('float64')
```

多出的 128 字节是 `ndarray` 对象自身的管理信息。

再比如，我们创建一个大一点的矩阵，

```python
a = rng.random((2**15, 2**15, 10))
>>> sys.getsizeof(a)/2**30
80.00000013411045
>>> a.dtype
dtype('float64')
```

```shell
PID    COMMAND      %CPU TIME     #TH    #WQ  #PORTS MEM
53402  python3.13   0.0  00:44.53 1      0    22     80G
```

可以发现，用了大约 $8\times 10\times 2^{30} \mathrm{B} = 80\mathrm{GiB}$ 。

也就是说，一个 $15$ 个二能级系统的实数 Hamiltonian 在用 `float64` 稠密矩阵存储时，
用大概 $8\mathrm{GiB}$ 。
