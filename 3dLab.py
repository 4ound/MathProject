import matplotlib.pyplot as plt
import numpy as np

EPS = 1e-3


def p(x):
    return "+" + ''.join(['(x - x{}) *'.format(i) for i in range(5) if i != x]) + \
           "y{}".format(x) + ''.join("/(x{} - x{})".format(x, i) for i in range(5) if i != x)


def make_polynom():
    l_n = "0" + ''.join(map(p, np.arange(5)))

    global points
    for i in range(5):
        l_n = l_n.replace("x{}".format(i), str(points[i][0])).replace("y{}".format(i), str(points[i][1]))

    return l_n


def draw_l():
    l = make_polynom()
    xg = np.arange(0, 3, EPS)
    yg = list(map(lambda x: eval(l.replace("x", str(x))), xg))
    plt.plot(xg, yg)
    global points
    for i in range(5):
        plt.scatter(points[i][0], points[i][1])
    plt.plot([x for x, y in points], [y for x, y in points])
    plt.show()


points = ((0.235, 1.082), (0.672, 1.805), (1.385, 4.280), (2.051, 5.011), (2.908, 7.082))
draw_l()
