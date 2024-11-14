# Reference:
# 博士学位论文： BEC-BCS 过渡体系的热力学性质与旋量 BEC 中的非阿贝尔约瑟夫森效应的研究 齐燃
# 计算过程，全部以温度 T 做单位，进行无量纲化处理
import numpy as np
from scipy import integrate
from scipy.special import zeta
from scipy import optimize
from scipy.misc import derivative
import matplotlib.pyplot as plt
from mpmath import polylog


def bose(beta, energy):
    """ Bose 分布函数
    有些计算中, energy 也可能是负的.
    """
    x = -beta * energy
    if energy > 0:
        return np.exp(x) / (1 - np.exp(x))
    else:
        return 1 / (np.exp(-x) - 1)


def fermi(beta, energy):
    '''
    Fermi distribution function
    '''
    x = -beta * energy
    return np.exp(x) / (1 + np.exp(x))


def free_fermion_density(mu):
    """
    Integrate[q^2/\[Pi]^2 1/(E^(q^2/2-\[Mu])+1),{q, 0, \[Infinity]}]
    >>  -(PolyLog[3/2,-E^\[Mu]]/(Sqrt[2] \[Pi]^(3/2)))
    """
    return - polylog(s=3/2, z=-np.exp(mu)).real / (np.sqrt(2) * np.pi**(3/2))


class PrincipalValueInt():
    """Calculate a 2nd order Cauchy integral:
    int  dx    f(x) / (a*x^2 + b^x + i0^+)
    latex:
    \int \mathrm{d}x \frac{f(x)}{a x^2 + b x + \mathrm{i}0^+}

    Attributes
    ----------
    get_image : float
                Calculate the imaginary part of the integral.
    get_real : float
        Calculate the real part of the integral.
    """

    def __init__(self, numerator, coeff: list,
                 lower_lim, upper_lim, debug=False):
        """
        numerator: function f(x)
        coeff: [a, b, c] is the coefficients in the denominator.
        lower_lim: lower limit of the integral
        upper_lim: upper limit of the integral
        """
        self.debug = debug
        self.numerator = numerator
        if isinstance(numerator, (int, float)):
            self.numerator = lambda x: numerator
        else:
            self.numerator = numerator
        self.lower_lim = lower_lim
        self.upper_lim = upper_lim
        self.a = coeff[0]
        if self.a == 0:
            raise ValueError("a should not be 0!")  # TODO: deal the a=0 case.
        self.b = coeff[1]
        self.c = coeff[2]
        self.delta = self.b**2 - 4*self.a*self.c
        self.root_exist = (self.delta > 0) and (self.a != 0)

        if self.root_exist:
            if self.a > 0:
                self.root1 = (-self.b - np.sqrt(self.delta)) / (2*self.a)
                self.root2 = (-self.b + np.sqrt(self.delta)) / (2*self.a)
            else:
                self.root1 = (-self.b + np.sqrt(self.delta)) / (2*self.a)
                self.root2 = (-self.b - np.sqrt(self.delta)) / (2*self.a)
            # cherck if the roots in the integral interval
            self.root1_in = lower_lim < self.root1 and self.root1 < upper_lim
            self.root2_in = lower_lim < self.root2 and self.root2 < upper_lim

    def get_imag(self):
        """Imaginary part of the integral."""
        if self.root_exist:
            imag = (self.root1_in) * self.numerator(self.root1)
            imag += (self.root2_in) * self.numerator(self.root2)
            imag *= -np.pi / np.abs(self.root2 - self.root1)
        else:
            imag = 0
        imag *= 1/self.a
        return imag

    def get_real(self):
        """
        Real part of the integral.

        Note(TODO):
        When upper_lim is very larg, e.g. self.upper_lim > 1e4,
        if the function do not decay to 0, the result is wrong.
        The same warning in Mathematica:
        NIntegrate[1/(x-10^8)^2, {x, 1, 10^8+1}]
        """
        if self.root_exist:
            if (not self.root1_in) and (not self.root2_in):
                if self.debug:
                    print('No root in!!!!!!!!!')
                res = integrate.quad((lambda x: self.numerator(x)
                                      / (self.a*x**2 + self.b*x + self.c)),
                                     self.lower_lim, self.upper_lim)[0]
                inte_metheod = 'no_root_in'
            elif self.root1_in and self.root2_in:
                if self.debug:
                    print('All root in~~~~~~~~~')
                mid = (self.root2 + self.root1)/2

                real1 = integrate.quad((lambda x: self.numerator(x)
                                        / (self.a * (x - self.root2))),
                                       self.lower_lim, mid,
                                       weight='cauchy', wvar=self.root1)[0]

                right_range = 2*self.root2 - self.root1
                if self.upper_lim > right_range:
                    # 如果积分上限特别大, 就分段积, 要不然算法找不到 pole 的贡献.
                    if self.debug:
                        print('Big upbound, range has been split!')
                    real2 = integrate.quad((lambda x: self.numerator(x)
                                            / (self.a * (x - self.root1))),
                                           mid, right_range,
                                           weight='cauchy', wvar=self.root2)[0]
                    real2 += integrate.quad((lambda x: self.numerator(x)
                                             / (self.a*x**2 + self.b*x +
                                                self.c)),
                                            right_range, self.upper_lim)[0]

                else:
                    real2 = integrate.quad((lambda x: self.numerator(x)
                                            / (self.a * (x - self.root1))),
                                           mid, self.upper_lim,
                                           weight='cauchy', wvar=self.root2)[0]
                res = real1 + real2
                inte_metheod = 'all_root_in'
            elif self.root1_in:
                if self.debug:
                    print('root1 in 111111111111111111111')
                res = integrate.quad((lambda x: self.numerator(x)
                                      / (self.a * (x - self.root2))),
                                     self.lower_lim, self.upper_lim,
                                     weight='cauchy', wvar=self.root1)[0]
                inte_metheod = 'root1_in'
            else:
                if self.debug:
                    print('root2 in 2222222222222222')

                right_range = 2*self.root2 - self.root1
                if self.upper_lim > right_range:
                    # 如果积分上限特别大, 就分段积, 要不然算法找不到 pole 的贡献.
                    if self.debug:
                        print('Big upbound, range has been split!')
                    res = integrate.quad((lambda x: self.numerator(x)
                                          / (self.a * (x - self.root1))),
                                         self.lower_lim, right_range,
                                         weight='cauchy', wvar=self.root2)[0]
                    res += integrate.quad((lambda x: self.numerator(x)
                                           / (self.a*x**2 + self.b*x +
                                              self.c)),
                                          right_range, self.upper_lim)[0]
                else:
                    res = integrate.quad((lambda x: self.numerator(x)
                                          / (self.a * (x - self.root1))),
                                         self.lower_lim, self.upper_lim,
                                         weight='cauchy', wvar=self.root2)[0]
                inte_metheod = 'root2_in'
        else:
            if self.a == 0:
                if self.debug:
                    print('a = 0 ! 000000000000')
                res = integrate.quad(lambda x: self.numerator(x)/self.b,
                                     self.lower_lim, self.upper_lim,
                                     weight='cauchy', wvar=-self.c/self.b)[0]
                inte_metheod = 'trivial'
            else:
                if self.debug:
                    print('Root Not Exist!...................')
                res = integrate.quad((lambda x: self.numerator(x)
                                      / (self.a*x**2 + self.b*x + self.c)),
                                     self.lower_lim, self.upper_lim)[0]
                inte_metheod = 'root_not_exist'
        return res, inte_metheod


def _g(x, y, muT, debug=False):
    """Qi PhD Eq.(3.48)

    Parameters
    ----------
    x : float
        x
    y : float
        y
    muT : float
          μ / T
    debug : bool
            debug
    Returns
    -------
    res : float
          g
    """
    a = x**2/2 + y**2/8 - muT
    b = x*y / 2
    if debug:
        print(f'a = {a:.2f}, b = {b:.2f}')
    if b == 0:
        # g = 4/(1 + np.exp(a))
        g = 4*np.exp(-a) / (np.exp(-a) + 1)
    else:
        g = np.exp(-b) + np.exp(-a)
        denominator = np.exp(-b) + np.exp(-a - 2*b)
        if denominator == 0:
            g = np.inf
        else:
            g /= denominator
        g = np.log(g)
        g *= 2/b
    return g


def _g_diff_a(x, y, muT):
    """d g / d a"""
    a = x**2/2 + y**2/8 - muT
    b = x*y / 2
    if b == 0:
        dg = np.exp(-a)
        dg /= (np.exp(-a) + 1)**2
    else:
        dg = 1 - np.exp(-2*b)
        dg /= 1 + np.exp(-2*b) + np.exp(-a-b) + np.exp(a-b)
        dg *= -2 / b
    return dg


def Gamma_0_re(q, omega, mu, a):
    """ 以 T 作单位制下的 particle-partilce propagator
    Eq.(3.47)
    Real part of inverse BCS pair propagator.

    a: a_s, s-wave scattering length, in unit of temperature
    q: q / sqrt(T)
    omega: omega / T
    mu : mu / T
    """

    Omega = omega + 2*mu - q**2/4

    re = -1 / (4*np.pi*a)
    pv = PrincipalValueInt(numerator=lambda x: x**2 * _g(x, q, muT=mu),
                           coeff=[1, 0, -Omega],
                           lower_lim=0, upper_lim=10).get_real()[0]
    re += pv / (4*np.pi**2)
    if Omega < 0:
        re += np.sqrt(-Omega) / (4*np.pi)
    return re


def Gamma_0_im(q, omega, mu):
    """ 以 T 作单位制下的 particle-partilce propagator
    (3.47)
    Imaginary part of inverse BCS pair propagator.
    虚部与散射长度无关!!!!!

    a: a_s, s-wave scattering length, in unit of temperature
    q: q / sqrt(T)
    omega: omega / T
    mu : mu / T
    """

    Omega = omega + 2*mu - q**2/4

    if Omega > 0:
        im = np.sqrt(Omega) / (8*np.pi)
        im *= _g(np.sqrt(Omega), q, muT=mu) - 2
    else:
        im = 0
    return im


def find_muT_at_Tc(a):
    """Find Tc

    use Re(0, 0, muT, aT) = 0, given a aT, return muT

    Parameters
    ----------
    a : scattering length (a_s * sqrt(T))
    Returns
    -------
    muT : float
          μ / T
    """
    res = optimize.root(lambda muT: Gamma_0_re(q=0, omega=0, mu=muT, a=a), -1)
    if not res.success:
        print('IMPORTANT ERROR !!!!!!!!!! ROOT NOT FIND!!!!!!find muT!')
    muT = res.x[0]
    return muT


def find_omegaT(qT, muT, a, debug=False):
    """Given aT, aT, find the dispersion curve ω_q
    a: s-wave scattering length in unit of temperature
    """
    def re_qT_omegaT(omegaT, qT=qT):
        return Gamma_0_re(q=qT, omega=omegaT, mu=muT, a=a)

    if qT > 1e-4:
        res = optimize.root(re_qT_omegaT, 0, options={'xtol': 1e-9})
        # 如果比较低的精度就能满足要求, 可以用比较低的精度, 来避免返回 res.success=False.
        if debug and (not res.success):
            print('Error infind omegaT, error message is:')
            print(res.message)
            print('error parameters is')
            print(f'qT={qT:.15f}, muT={muT:.15f}')
            print(f'res para={1/a:.15f}, root={res.x[0]}')
        omegaT = res.x[0]
    else:                       # 线性近似
        # TODO: 为了避免在 qT 很小时会剧烈抖动而找不到根, 采用了线性近似. 这个还是要改
        # 的. 现在去除了乘了两次 fluc 的 bug 后应该就没有这个问题了.
        omegaT = qT / (1e-4) * optimize.root((lambda omegaT:
                                                re_qT_omegaT(omegaT,
                                                            qT=1e-4)),
                                                0, options={'xtol':
                                                            1e-13}).x[0]
    return omegaT


class Density():
    """Density, in unit of Temperature
    """
    def __init__(self, mu, a, debug=True):
        """
        mu : chemical potential in unit of temperature, μ / T
        a: s-wave scattering length in unit of temperature,
        """
        self.mu = mu
        self.a = a
        self.debug = debug

    def _im_diff_mu_s(self, qT: float, omegaT: float):
        """d im / d μ, (delta part has no contribution)
           验证过, 没有问题! s-wave
        """
        OT = omegaT + 2*self.mu - qT**2/4
        if OT > 0:
            dim = (_g(np.sqrt(OT), qT, muT=self.mu) - 2) / np.sqrt(OT)
            dim += np.sqrt(OT) * _g_diff_a(np.sqrt(OT), qT, muT=self.mu)
            dim /= 8*np.pi
            dim += - np.sqrt(OT) / (8*np.pi) * _g_diff_a(np.sqrt(OT), qT,
                                                         muT=self.mu)
        else:
            dim = 0
        return dim

    def _fluc1_dense(self, qT, omegaT):
        """Eq. (3.49) and Eq. (3.49)"""
        real = Gamma_0_re(q=qT, omega=omegaT, mu=self.mu,
                          a=self.a)
        imag = Gamma_0_im(q=qT, omega=omegaT, mu=self.mu)

        volume_elem = (1 / np.pi) * (1 / (2*np.pi**2))

        diff_re = derivative((lambda mu: Gamma_0_re(q=qT, omega=omegaT, mu=mu,
                                                    a=self.a)),
                             self.mu, dx=.1)
        diff_im = self._im_diff_mu_s(qT, omegaT)
        fluctdens = qT**2 * bose(1, omegaT)
        fluctdens *= (imag*diff_re - real*diff_im) / (imag**2+real**2)
        res = fluctdens * volume_elem
        return res

    def _fluc1_s(self, qT, BCS):
        """ 计算 pair 涨落在连续激发区的贡献 """
        # 实部为 0 时对应的准粒子激发
        omega_p = find_omegaT(qT=qT, muT=self.mu,
                              a=self.a)
        print('omega p is', omega_p)

        if BCS:
            "如果在 BCS 极限下的的话, 连续激发边界的边界有比较重要的贡献"
            boundary = qT**2/4 - 2*self.mu  # 连续激发的边界
            # 从连续激发边界, 到准粒子激发处的贡献
            int1 = integrate.quad((lambda omega:
                                   self._fluc1_dense(qT=qT, omegaT=omega)),
                                  boundary, -2*omega_p, epsrel=1e-3, limit=40)
        else:
            int1 = [0]

        # 准粒子激发的贡献
        int3 = integrate.quad(lambda omega: self._fluc1_dense(qT=qT,
                                                              omegaT=omega),
                              -10*omega_p, 11*omega_p, epsrel=1e-3, limit=40)
        res = int1[0] + int3[0]
        return res

    def _fluc2_s(self, qT):
        """ use Qi PhD Eq.(3.52) at Tc
            pair 涨落的 single pole 部分.
        """
        volume_elem = qT**2 / (2*np.pi**2)

        def omega_q(muT):
            return find_omegaT(qT=qT, muT=muT, a=self.a)

        diff = derivative(omega_q, self.mu, dx=.1)
        energy = omega_q(self.mu)  # qT**2/4  # - 2*muT - aT**2
        if energy < qT**2/4 - 2*self.mu:
            fluc = bose(1, energy)
            fluc *= - diff
            fluc *= volume_elem
        else:
            fluc = 0
        return fluc

    def s_wave_density(self, para, debug=True):
        """ n / (T)^(3/2)
        Calculate the density.

        According the interaction strength, we use three different method to
        calculate the density.

        Parameters
        ----------
        muT : float
              μ / T
        aT : folat
             1 / (as * sqrt(T))
        Returns
        -------
        n : float
            density
        """
        if para.method == 'SinglePole_StrongBEC':
            """
            method [1]: SinglePole_StrongBEC.
            In Strong BEC limit, the density are mainly contributed by the
            dimers formed by two Fermion.

            Mathematica code:
            Integrate[q^2/(Exp[q^2/4]-1),{q,0,Infinity}]
            >> 2 Sqrt[\[Pi]] Zeta[3/2]
            """
            n = 4*np.sqrt(np.pi)*zeta(3/2)

        elif para.method == 'SinglePole':
            """
            method [2]: SinglePole.
            准粒子激发在 q=0 时, ω(q)=0. 因此, 在 μ<0 时, 准粒子激发完
            全位于连续激发外, 是孤立的奇点. 此时, 考虑自由费米子(几乎可以忽略) 和 Single
            Pole 的 pair 涨落的贡献.
            """
            n_fluc2 = integrate.quad(self._fluc2_s, 0, para.n_fluc2_up,
                                     epsrel=para.n_fluc2_epsrel)
            # 此处也用较低的精度即可. 接近 0 时平滑地走近于一个常数. TODO: 动量积分的下限
            # 做了近似, 0 处有bug
            n_fluc = n_fluc2[0]
            n_free = free_fermion_density(self.mu)
            n = n_free + n_fluc
            # print('*************', n_fxluc, n_free)
        elif para.method == 'NSR':
            """
            method [3]: NSR.
            在 μ>0 时, 准粒子激发几乎位于连续激发内, 在低动量低频率区有尖锐的
            准粒子峰贡献.
            BEC Unitary侧, 考虑自由费米子 和 pair 涨落(连续激发)."""
            n_fluc1 = integrate.quad((lambda qT:
                                      self._fluc1_s(qT, BCS=para.fluc1_BCS)),
                                     para.n_fluc1_a, para.n_fluc1_b,
                                     epsrel=para.n_fluc1_epsrel,
                                     limit=para.n_fluc1_limit)
            n_fluc = n_fluc1[0]
            n_free = free_fermion_density(self.mu)
            n = n_free + n_fluc
        return n


def plot_Tc(aT, para, debug=False):
    """
    aT : scattering length in unit of temperature
    """
    muT = []
    density_T = []
    for aTi in aT:
        print('Calculating the results for point a_s*sqrt(T)=',
              aTi, ' START!')
        muTi = find_muT_at_Tc(a=1/aTi)
        muT.append(muTi)
        density_T.append(Density(mu=muTi, a=1/aTi).s_wave_density(para))
        print('Calculating the results for point a_s*sqrt(T)=',
              aTi, ' FINISH!')

    n_T = np.array(density_T)  # density in unit of temperature
    kF = (3*np.pi**2*n_T) ** (1/3)  # Fermi momentum in unit of temperature
    EF = kF**2 / 2  # Fermi energy in unit of temperature
    kfas = aT / kF  # 1 / (k_F * a_s)
    Tc_EF = 1 / EF
    plt.plot(kfas, Tc_EF, 'o', label="This numerical program")


def plot_paper():
    """
    The data from the published papers.
    """
    paper_data = np.array([[-1.99903, 0.016667],
                           [-1.59262, 0.034058],
                           [-1.30582, 0.052899],
                           [-0.98741, 0.084058],
                           [-0.73053, 0.119565],
                           [-0.47717, 0.16087],
                           [-0.21622, 0.2],
                           [-0.0841, 0.214493],
                           [0.0013, 0.222464],
                           [0.10593, 0.228986],
                           [0.22578, 0.231884],
                           [0.35702, 0.231159],
                           [0.4381, 0.231159],
                           [0.56522, 0.226087],
                           [0.68084, 0.222464],
                           [0.83905, 0.221014],
                           [1.02812, 0.218841],
                           [1.19024, 0.218116],
                           [1.3524, 0.218116],
                           [1.41418, 0.218116]
                           ])
    t_star = np.array([[-1.99602, 0.029288],
                       [-1.76099, 0.038028],
                       [-1.53813, 0.052065],
                       [-1.33351, 0.070343],
                       [-1.09651, 0.102372],
                       [-0.86968, 0.147815],
                       [-0.62669, 0.217954],
                       [-0.48093, 0.271542],
                       [-0.26232, 0.365333]
                       ])
    plt.plot(paper_data[:, 0], paper_data[:, 1],
             label='results from published papers')
    plt.plot(t_star[:, 0], t_star[:, 1], '--')


class Para():
    """ 指定一些数值计算中需要调的参数.
    """
    def __init__(self, method: str, n_fluc2_up,
                 n_fluc2_limit, n_fluc2_epsrel,
                 n_fluc1_a, n_fluc1_b, n_fluc1_limit, n_fluc1_epsrel,
                 fluc1_BCS):
        """
        Parameters
        method : the method to be used when calculate the density.
                 There are three method can be use:
                 'SinglePole_StrongBEC', 'SinglePole', 'NSR'
        fluc1_BCS: bool
                 如果在 BCS 极限下的的话, 连续激发边界的边界有比较重要的贡献.
        """
        self.method = method

        self.n_fluc2_up = n_fluc2_up
        self.n_fluc2_limit = n_fluc2_limit
        self.n_fluc2_epsrel = n_fluc2_epsrel

        self.n_fluc1_a = n_fluc1_a
        self.n_fluc1_b = n_fluc1_b
        self.n_fluc1_limit = n_fluc1_limit
        self.n_fluc1_epsrel = n_fluc1_epsrel

        self.fluc1_BCS = fluc1_BCS


def runscp():
    # ============ Single pole 近似下, aT 取 1.5~4 (取 10 个点)是可以的. ==========
    paraSinglePole = Para(method="SinglePole",
                              n_fluc2_limit=10,
                              n_fluc2_up=10,
                              n_fluc2_epsrel=1e-2,
                              n_fluc1_a=2e-2, n_fluc1_b=10,
                              n_fluc1_limit=5, n_fluc1_epsrel=1e-3,
                              fluc1_BCS=False)
    plot_Tc(aT=[1.5, 2, 3, 4], para=paraSinglePole, debug=True)

    paraNSR = Para(method="NSR",
                   n_fluc2_limit=10,
                   n_fluc2_up=10,
                   n_fluc2_epsrel=1e-2,
                   n_fluc1_a=2e-2, n_fluc1_b=10,
                   n_fluc1_limit=5, n_fluc1_epsrel=1e-3,
                   fluc1_BCS=False)
    # plot_Tc(aT=[.1, .3, 0.5, 0.8, 1.0], para=paraNSR, debug=True)
    plot_Tc(aT=[0.1, 0.3], para=paraNSR, debug=True)

    paraNSR_BCS = Para(method="NSR",
                       n_fluc2_limit=10,
                       n_fluc2_up=10,
                       n_fluc2_epsrel=1e-2,
                       n_fluc1_a=2e-2, n_fluc1_b=10,
                       n_fluc1_limit=10, n_fluc1_epsrel=1e-3,
                       fluc1_BCS=True)
    # plot_Tc(aT=[-5, -3, -1], para=paraNSR_BCS, debug=True)
    plot_Tc(aT=[-.5, -.1], para=paraNSR_BCS, debug=True)
    # plot_Tc(aT=[-5], para=paraNSR_BCS, debug=True)

    plot_paper()
    plt.xlabel(r'$1/(k_F a_s)$')
    plt.ylabel(r'$T_C / \epsilon_F$')
    plt.legend()
    plt.show()


runscp()
