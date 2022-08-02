import numpy as np
import matplotlib.pyplot as plt

def sgn(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

def forward(wi, b, x, y):
    L = y - sgn(np.dot(wi, x) - b)
    wi = wi - np.dot(x,L)*0.01
    b = b - L*0.01
    # tmp = np.sqrt(wi[0]**2+wi[1]**2)
    # wi = wi / tmp
    # print(L)
    return wi, b
arrayx1 = np.array([1.200, 1.100, 1.000, 0.990, 1.100, 1.150, 1.450, 1.440, 1.600])
arrayy1 = np.array([1.55, 1.57, 2.65, 1.58, 1.64, 1.92, 1.86, 2.23, 2.18])
arrayx2 = np.array([1.970, 2.200, 1.990, 1.800, 1.840, 1.800, 2.000, 2.100, 2.160])
arrayy2 = np.array([2.78, 2.96, 2.87, 2.69, 2.48, 2.27, 2.69, 2.77, 2.84])


xi = np.array([[1.2, 1.55], [1.1, 1.57], [1.0, 2.65], [0.99, 1.58], [1.1, 1.64], [1.15, 1.92], [1.45, 1.86], [1.44, 2.23], [1.6, 2.18], [1.97, 2.78],
               [2.2, 2.96], [1.99, 2.87], [1.8, 2.69], [1.84, 2.48], [1.8, 2.27], [2.0, 2.69], [2.1, 2.77], [2.16, 2.84]])
y_expect = [-1, -1, -1, -1, -1, -1, -1, -1, -1,
             1, 1, 1, 1, 1, 1, 1, 1, 1]

wi = np.array([1, 1])
b = 0

for i in range(30):
    print("-----epoch{}-----".format(i))
    for j in range(len(xi)):
        wi, b = forward(wi, b, xi[j], y_expect[j])
    print(b)
print(wi, b)

x1 = np.linspace(0, 2.2, 1000)
x2 = -1*wi[0]/wi[1]*x1+b/wi[1]
plt.xlim((0, 2.5))
plt.plot(x1, x2, '-')

plt.plot(arrayx2, arrayy2, '.')
plt.plot(arrayx1, arrayy1, '.')
plt.savefig("pic4.svg", dpi=800)
plt.show()