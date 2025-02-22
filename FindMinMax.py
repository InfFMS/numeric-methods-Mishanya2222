
import matplotlib
import matplotlib.pyplot as plt
import numpy
import math
x = 0
lst_x = []
lst_y1 = []
lst_y2 = []


def eq1(x):
    t1 = math.sin(2*x) + 1
    return t1

def eq2(x):
    t2 = -0.2*(x**2) + 0.5
    return t2


while x <=math.pi:
    x = x + 0.01
    lst_x.append(x)
    lst_y1.append(eq1(x))
    lst_y2.append(eq2(x))

integ = 0
x = 0
while x <= math.pi:
    x = x + 0.01
    integ = integ + ((((eq1(x) - eq2(x)) + (eq1(x+0.01)-eq2(x + 0.01)))/2)*(0.01))

plt.plot(lst_x, lst_y1)
plt.plot(lst_x, lst_y2)
plt.show()

print(integ)
