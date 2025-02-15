#
# Пусть горка имеет форму, которую можно описать формулами
# cos(x)
# cos(x) + 0.1*x2
# -tanh(x-π/2)
# -0.2*(x- π)3 + 0.5*(x- π)2 +1
# На отрезке от 0 до π.
# Найти длину этих горок.
# #
from matplotlib import pyplot as plt
import math

lst_x = []
lst_y = []
num = int(input('введите номер уравнения'))
L = 0
dx = 0.01
x = 0
while x < math.pi:
    if num == 1:
        L = L + math.sqrt((math.cos(x + dx) - math.cos(x))**2 + dx**2)
    elif num == 2:
        L = L + math.sqrt((math.cos(x + dx)+ 0.1*((x+dx)**2) - math.cos(x) - 0.1*(x**2))**2 + dx**2)
    elif num == 3:
        L = L + math.sqrt((math.tanh(x +dx - math.pi/2)-math.tanh(x-math.pi/2))**2 + dx**2 )
    elif num ==4:
        L = L + math.sqrt((-0.2*((x + dx- math.pi)**3) + 0.5*((x+dx- math.pi)**2) +1  - (-0.2*((x- math.pi)**3) + 0.5*((x- math.pi)**2) +1))**2 + dx**2)
    x = x + dx
print(L)


def eq(x,num):
    if num ==1:
        t = math.cos(x)
    elif num ==2:
        t = math.cos(x)+ 0.1*((x)**2)
    elif num == 3:
        t = math.tanh(x-math.pi/2)
    elif num == 4:
        t = -0.2*((x- math.pi)**3) + 0.5*((x- math.pi)**2) +1
    return t


x=0
while x < math.pi:
    x = x + 0.1
    lst_x.append(x)
    lst_y.append(eq(x,num))

plt.plot(lst_x,lst_y)
plt.grid()
plt.show()
