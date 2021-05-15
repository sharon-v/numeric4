""" assignment 4
    team members: Hadar Amsalem, Sharon Vazana
    git link: https://github.com/sharon-v/numeric4.git"""
import math

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
    print("*** Bisection_Method ***")
    partition(polynom, startPoint, endPoint, runBisection, epsilon)


def partition(polynom, startPoint, endPoint, runMethod, epsilon=0.0001):
    x = sp.symbols('x')
    f = lambdify(x, polynom)
    fTag = calcDerived(polynom)
    i = startPoint
    while i < endPoint:
        j = i + 0.01
        c, iteration = runMethod(f, i, j, epsilon, startPoint, endPoint)
        if c is not None:
            print("root: " + str(c) + " ,\titeration: " + str(iteration))
        c, iteration = runMethod(fTag, i, j, epsilon, startPoint, endPoint)  # derived
        if c is not None:
            if -epsilon < f(c) < epsilon:
                print("root: " + str(c) + " ,\titeration: " + str(iteration))
        i += 0.01
    print("------------------------")


def runBisection(f, startA, endB, epsilon=0.0001, startPoint=0, endPoint=0):
    fXl = f(startA)
    fXr = f(endB)
    if (fXl * fXr) > 0:
        return None, None
    error = calcError(startPoint, endPoint, epsilon)
    i = -1
    c = startA
    while endB - startA > epsilon and i < error:
        i += 1
        # calc middleC
        c = (startA + endB) / 2
        if (f(startA) * f(c)) > 0:
            startA = c
        else:
            endB = c
    if i + 1 > error:
        print("Could not find root, The function is not suitable for bisection method")
        return None, None
    return c, i


def printDerived(my_f):
    # print the derivative in a symbol way
    x = sp.symbols('x')
    # my_f = x ** 3 + 2 * x + 5
    print("my_func: ", my_f)
    my_f1 = sp.diff(my_f, x)
    print("f' : ", my_f1)
    # d1 = sp.diff(my_f1)
    # print("f'': ", d1)


def calcDerived(f):
    # calc the derivative from func -> lambdify
    # f = x ** 3 + 2 * x + 5
    x = sp.symbols('x')
    f_prime = f.diff(x)
    # print("f : ", f)
    # print("f' : ", f_prime)
    # f = lambdify(x, f)
    f_prime = lambdify(x, f_prime)
    # print("f(1):", f(1))
    # print("f'(1):", f_prime(1))
    return f_prime


# def calcVal(f, val):
#     x = sp.symbols('x')
#     func = lambdify(x, f)
#     return func(val)


def calcError(start, end, epsilon=0.0001):
    return -(math.log(epsilon / (end - start)) / math.log(2))


# -------------- part 2 -------------


def Newton_Raphson(polynom, startPoint, endPoint, epsilon=0.0001):
    print("*** Newton Raphson ***")
    partition(polynom, startPoint, endPoint, runNewton, epsilon)


def runNewton(f, startA, endB, epsilon=0.0001):
    fXl = f(startA)
    fXr = f(endB)
    if (fXl * fXr) > 0:
        return None, None
    i = -1
    c = (startA + endB) / 2
    newC = abs(startA + endB)
    while abs(newC - c) > epsilon:
        i += 1
        newC = c - (f(c) / calcDerived(f)(c))
    if i >= 100:
        print("Could not find root, The function is not suitable for Newton Raphson")
        return None, None
    return c, i


# -------------- part 3 ----------------


def secant_method(polynom, startPoint, endPoint, epsilon=0.0001):
    print("*** secant_method ***")
    partition(polynom, startPoint, endPoint, runSecant, epsilon)


def runSecant(f, startA, endB, epsilon=0.0001):
    fXl = f(startA)
    fXr = f(endB)
    if (fXl * fXr) > 0:
        return None, None
    i = -1
    c = fXl
    newC = fXr
    while abs(newC - c) > epsilon:
        i += 1
        c = newC
        newC = (c * f(newC) - newC * f(c)) / (f(newC) - f(c))
    if i >= 100:
        print("Could not find root, The function is not suitable for secant method")
        return None, None
    return c, i


# --------------- part 4 ----------------
def driver():
    """
    the main function of the program
    """
    x = sp.symbols('x')
    # define polynom
    # f = x ** 3 - x - 1
    # f = x**2 - 1
    f = x ** 4 + x ** 3 - 3 * x ** 2
    # define range
    # startPoint = -2
    # endPoint = 2
    startPoint = -3
    endPoint = 2
    # epsilon = pow(10, -10)
    printDerived(f)
    print("-------------")
    choice = input("Enter 0 for bisection method, 1 for Newton Raphson, else for secant method\n")
    if choice is '0':
        bisection_method(f, startPoint, endPoint)
    elif choice is '1':
        Newton_Raphson(f, startPoint, endPoint)
    else:
        secant_method(f, startPoint, endPoint)


driver()
