# Найти корни уравнений:
# x3 – x +1 = 0
# x3 – x2 – 9x + 9 = 0
# x2 – ex = 0
# 5x – 6ln(x) – 7 = 0
# cos(x) + 2x – 3 = 0
# C точностью до 0.01.
from matplotlib import pyplot as plt
import math

num = int(input("введите номер уравнения "))

lst_x = []
lst_y = []

def slove_equation(a ,b,eps):
    while b - a >= 2*eps:
        c = (a + b)/2
        if eq(a,num)*eq(c,num) <= 0:
            a = c
        else:
            b = c
    return c


def eq(x,num):
    if num ==1:
        t = x**3 - x +1
    elif num ==2:
        t = x**3 -x**2 - x*9 + 9
    elif num == 3:
        t = x**2 - math.exp(x)
    elif num == 4:
        t = 5*x - 6*math.log(x) - 7
    elif num == 5:
        t = math.cos(x) + 2*x - 3
    return t


#если искать корни  логаритфма, то x >0 должен быть
for i in range(-100,100):
    lst_x.append(i)
    lst_y.append(eq(i,num))











# def serch_a(a):
#     b =0
#     while True:
#         a = a + 1
#         b = b - 1
#         if eq(a)*eq(b) > 0:
#             break
#     return a
#
# def serch_b(b):
#     a=0
#     while True:
#         a = a + 1
#         b = b - 1
#         if eq(a)*eq(b) > 0:
#             break
#     return b


plt.plot(lst_x,lst_y)
plt.grid()
plt.show()

print(slove_equation(1, 100, 0.01))


