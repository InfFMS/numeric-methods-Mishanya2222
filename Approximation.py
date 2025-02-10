# Найти корни уравнений:
# x3 – x +1 = 0
# x3 – x2 – 9x + 9 = 0
# x2 – ex = 0
# 5x – 6ln(x) – 7 = 0
# cos(x) + 2x – 3 = 0
# C точностью до 0.01.
from matplotlib import pyplot as plt

lst_x = []
lst_y = []

def slove_equation(a ,b,eps):
    while b - a >= 2*eps:
        c = (a + b)/2
        if eq(a)*eq(c) <= 0:
            a = c
        else:
            b = c
    return c


def eq(x):
    t = x**3 - x +1
    return t

for i in range(-100,100):
    lst_x.append(i)
    lst_y.append(eq(i))

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

print(slove_equation(-100, 100, 0.01))


