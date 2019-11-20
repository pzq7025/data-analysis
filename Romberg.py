# 复化梯形求积公式
import math
import matplotlib.pyplot as plt


def integral(a_bottom, b_top, num, func_n):
    h = (b_top - a_bottom) / float(num)
    xk = [a_bottom + i * h for i in range(1, num)]
    return h / 2 * (func_n(a_bottom) + 2 * sum_fun_xk(xk, func_n) + func_n(b_top))


def sum_fun_xk(xk, func_n):
    return sum([func_n(each) for each in xk])


if __name__ == "__main__":

    func_1 = lambda x: x ** 2
    a, b = 2, 8
    n = 20
    print(integral(a, b, n, func_1))

    ''' 画图 '''

    plt.figure("play")
    ax1 = plt.subplot(111)
    plt.sca(ax1)

    tmpx = [2 + float(8 - 2) / 50 * each for each in range(50 + 1)]
    plt.plot(tmpx, [func_1(each) for each in tmpx], linestyle='-', color='black')

    for rang in range(n):
        tmpx = [a + float(8 - 2) / n * rang, a + float(8 - 2) / n * rang, a + float(8 - 2) / n * (rang + 1), a + float(8 - 2) / n * (rang + 1)]
        tmpy = [0, func_1(tmpx[1]), func_1(tmpx[2]), 0]
        c = ['r', 'y', 'b', 'g']
        plt.fill(tmpx, tmpy, color=c[rang % 4])
    plt.grid(True)
    plt.show()

#  龙贝格法求积分

a = 0  # 积分下限
b = 1  # 积分上限
eps = 10 ** -5  # 精度
T = []  # 复化梯形序列
S = []  # Simpson序列
C = []  # Cotes序列
R = []  # Romberg序列


def func(x):  # 被积函数
    y = math.exp(-x)
    return y


def romberg(a_bottom, b_top, eps_n, func_n):
    h = b_top - a_bottom
    T.append(h * (func_n(a_bottom) + func_n(b_top)) / 2)
    ep = eps_n + 1
    m = 0
    while ep >= eps_n:
        m = m + 1
        t = 0
        for i in range(2 ** (m - 1) - 1):
            t = t + func_n(a_bottom + (2 * (i + 1) - 1) * h / 2 ** m) * h / 2 ** m
        t = t + T[-1] / 2
        T.append(t)
        if m >= 1:
            S.append((4 ** m * T[-1] - T[-2]) / (4 ** m - 1))
        if m >= 2:
            C.append((4 ** m * S[-1] - S[-2]) / (4 ** m - 1))
        if m >= 3:
            R.append((4 ** m * C[-1] - C[-2]) / (4 ** m - 1))
        if m > 4:
            ep = abs(10 * (R[-1] - R[-2]))


romberg(a, b, eps, func)
print(T)
print(S)
print(C)
print(R)
# 计算机参考值0.6321205588 ：-e^x
# 0.333333：x^2
print("Romberg积分结果为：{:.5f}".format(R[-1]))
