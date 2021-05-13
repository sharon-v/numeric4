""" assignment 4
    team members: Hadar Amsalem, Sharon Vazana
    git link: https://github.com/sharon-v/numeric4.git"""

import sympy as sp
from sympy.utilities.lambdify import lambdify


# bisection_method
# Xm = (Xl + Xr) / 2
# (f(xl) * f(xm)) < 0
# newton_raphson
# secant_method


def bisection_method(polynom, startPoint, endPoint, epsilon=0.0001):
    """
    :param polynom:
    :param startPoint:
    :param endPoint:
    :param epsilon:
    :return:
    """
    pass


def printDerived(my_f):
    # print the derivative in a symbol way
    x = sp.symbols('x')
    # my_f = x ** 3 + 2 * x + 5
    print("my_func: ", my_f)
    my_f1 = sp.diff(my_f, x)
    print("f' : ", my_f1)
    d1 = sp.diff(my_f1)
    print("f'': ", d1)


def calcDerived(f, x):
    # calc the derivative from func -> lambdify
    # f = x ** 3 + 2 * x + 5
    f_prime = f.diff(x)
    print("f : ", f)
    print("f' : ", f_prime)
    f = lambdify(x, f)
    f_prime = lambdify(x, f_prime)
    # print("f(1):", f(1))
    # print("f'(1):", f_prime(1))


def calcY(f, x):
    return f(x)


def calcError():
    pass
