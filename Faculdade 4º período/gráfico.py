import matplotlib.pyplot as plt
import numpy as np
import math
from plotnine import ggplot


# Exercício 1

# x = np.arange(-math.pi, math.pi, 0.01)
# sin = np.sin(x)
# p1 = x
# p3 = (x - x**3)/6
# p5 = p3 + x**5/120
#
#
# plt.plot(x, p1)
# plt.plot(x, p3)
# plt.plot(x,p5)
# plt.plot(x, sin)
#
# plt.legend(['Seno', 'P1', 'P3', 'P5'])
# plt.xlabel("x")
# plt.ylabel("y")
# plt.axis([-math.pi, math.pi, -5, 5])
#
#
# plt.show()

# Exercício 2

# x = np.arange(1, 100, 0.01)
# y = x
# y2 = x**2
# y3 = x**3
#
# plt.plot(x, y)
# plt.plot(x, y2)
# plt.plot(x, y3)
# plt.loglog()
#
# plt.legend(['x', 'x²', 'x³'])
# plt.xlabel('x')
# plt.ylabel('y')
# plt.axis([10, 100, 10, 1000000])
#
# plt.show()

# Exercício 3

# e = 0
# theta = np.arange(0, 2* math.pi, 0.01)
# l = 2
# r = l/(e*np.cos(theta) + 1)

# plt.xlabel("r cos 0")
# plt.ylabel("r sin 0")

# plt.plot(theta, r)
# plt.show()

# Exercício 4
# e = 0
# theta = np.arange(0, 2* math.pi, 0.01)
# l = 2
# r = l/(e*np.cos(theta) + 1)
#
#
# plt.polar(theta, r)
# plt.show()
#


