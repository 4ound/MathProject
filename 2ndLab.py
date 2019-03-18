import math
import pylab
import numpy as np
import random

x_0 = 0
ACC = 2
EPS = 0.1 ** ACC


def draw_graph(func):
    x_list = np.arange(0, 5, EPS)
    y_list = [func(x) for x in x_list]

    pylab.plot(x_list, y_list)
    pylab.plot([0, 5], [0, 0])
    pylab.plot([2, 2], [-3, 1.5])
    pylab.plot([3, 3], [-3, 1.5])
    pylab.scatter(x_0, 0, 100)
    pylab.text(2, -3, "  x = 2")
    pylab.text(3, -3, "  x = 3")
    pylab.text(x_0 - 5 * EPS, EPS * 15, "({}, 0)".format(round(x_0, ACC)))

    pylab.show()


def f(x):
    y = 1.5 - 0.4 * math.sqrt(x ** 3) - (math.e ** (- x ** 2)) * math.sin(x)
    if abs(y) < EPS:
        global x_0
        x_0 = x
    return y


def f_p(x):
    return -0.6 * math.sqrt(x) + 2 * x * (math.e ** (-x ** 2)) * math.sin(x) - math.cos(x) * (math.e ** (- x ** 2))


def f_pp(x):
    if not x:
        x += EPS
    return math.e ** (- x ** 2) * math.sin(x) * (3 - 4 * (x ** 2)) + 4 * (math.e ** (- x ** 2)) * x * \
           math.cos(x) - 0.4 * (3 / math.sqrt(x) - 9 * x / 4)


def guess_x(a, b):
    x = random.uniform(a, b)
    return x if f(x) * f_pp(x) < 0 else guess_x(a, b)


def newton():
    sch = 0
    x_now = guess_x(2, 3)
    x_next = x_now + 1

    while abs(x_now - x_next) > EPS:
        x_next = x_now - f(x_now) / f_p(x_now)
        x_now, x_next = x_next, x_now
        sch += 1

    print("X:{} Y:{}".format(x_now, f(x_now)))
    print(sch)


def chord():
    sch = 0

    x_prev = 2
    x_now = 3
    while abs(x_prev - x_now) > EPS:
        x_next = x_prev - f(x_prev) / (f(x_now) - f(x_prev)) * (x_now - x_prev)
        x_now, x_prev = x_next, x_now
        sch += 1
    print("X:{} Y:{}".format(x_now, f(x_now), ACC))
    print(sch)

if __name__ == '__main__':
    draw_graph(f)
    draw_graph(f_p)
    draw_graph(f_pp)
    newton()
    chord()
