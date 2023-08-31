from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

print('Enter a, b, and c coefficients of a quadratic equation ax^2 + bx + c = 0 below:')
a, b, c = float(input()), float(input()), float(input())
D = b ** 2 - 4 * a * c
if D < 0:
    real, img = -b/(a * 2), abs(sqrt(abs(D))/(a * 2))
    if img == 1:
        print('Roots are {0} + i and {0} - i'.format(real))
    else:
        print('Roots are {0} + {1}i and {0} - {1}i'.format(real, img))
elif D == 0:
    x0 = -b/(a * 2)
    print('The only root is {0}'.format(x0))
else:
    x1, x2 = (-b + sqrt(D))/(a * 2), (-b - sqrt(D))/(a * 2)
    print('Roots are {0} and {1}'.format(x1, x2))

# graph
x = np.arange(-10, 10)
y = a * x ** 2 + b * x + c
plt.plot(x, y, c='m')
plt.grid()
plt.show()
