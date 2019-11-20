import matplotlib.pyplot as plt

# ===================================== 通用 ==============================================================
e_x_set = []
e_y_set = []
r_x_set = []
r_y_set = []


def fun(x, y):
    # y1 = y - 2 * x / y
    y1 = x * y
    # y1 = -y - x * y ** 2
    # y1 = x ** 2 + 100 * y ** 2
    return y1


# ===================================== 改进欧拉公式 ==============================================================
def euler(x0, y0, h, num):
    n = 1
    print("euler:")
    while n <= num:
        yp = y0 + h * fun(x0, y0)
        x1 = x0 + h
        yc = y0 + h * fun(x1, yp)
        y1 = (yp + yc) / 2
        n += 1
        e_x_set.append(x1)
        e_y_set.append(y1)
        print(f"x:{x1:.1f}  y:{y1:.5f}")
        x0 = x1
        y0 = y1


def draw_euler():
    x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    y = [1.0954, 1.1832, 1.2649, 1.3416, 1.4142, 1.4832, 1.5492, 1.6125, 1.6733, 1.7321]
    plt.title("Euler")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis([0, 1.2, 0, 2])
    plt.plot(x, y, color="red", linestyle="--")
    plt.plot(e_x_set, e_y_set, color="blue", linestyle="-.")
    plt.show()


# ==================================== 龙格-库塔方法 =============================================================
def runge_kuta(x0, y0, h, num):
    n = 1
    print("runge_kuta:")
    while n <= num:
        k1 = fun(x0, y0)
        x1 = h + x0
        k2 = fun((x0 + h / 2), (y0 + h / 2 * k1))
        k3 = fun((x0 + h / 2), (y0 + h / 2 * k2))
        k4 = fun(x1, (y0 + h * k3))
        y1 = y0 + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        n += 1
        r_x_set.append(x1)
        r_y_set.append(y1)
        print(f"x:{x1:.1f}  y:{y1:.5f}", k1, k2, k3, k4)
        x0 = x1
        y0 = y1


# def draw():
#     plt.title("x-2*x/y")
#     plt.xlabel("x")
#     plt.ylabel("y")
#     x = np.linspace(0, 1, 10000)
#     y = np.linspace(0.1, 1, 10000)
#     z = y - 2 * x / y
#     plt.plot(x, z, color='blue', linestyle="--")
#     plt.show()


def draw_runge_kuta():
    x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    y = [1.0954, 1.1832, 1.2649, 1.3416, 1.4142, 1.4832, 1.5492, 1.6125, 1.6733, 1.7321]
    plt.title("runge_kuta")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis([0, 1.2, 0, 2])
    plt.plot(x, y, color="red", linestyle="--")
    plt.plot(r_x_set, r_y_set, color="blue", linestyle="-.")
    plt.show()


if __name__ == '__main__':
    # draw()
    # 改进欧拉公式
    a = 0  # 初值点x
    b = 1  # 初值点y
    # h_e = 0.1
    # number_e = int(float(b - a) / h_e)
    # euler(a, b, h_e, number_e)
    # draw_euler()
    # 四阶龙格-库塔方法
    h_r = 0.1
    number_r = int(float(b - a) / h_r)
    runge_kuta(a, b, h_r, number_r)
    # draw_runge_kuta()
