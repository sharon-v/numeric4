""" assignment 4
    team members: Hadar Amsalem, Sharon Vazana
    git link: https://github.com/sharon-v/numeric4.git"""
import math

import sympy as sp
from sympy import ln
from sympy.utilities.lambdify import lambdify


# bisection_method
# newton_raphson
# secant_method

def bisection_method(polynom, startPoint, endPoint, choice, epsilon):
    """
    :param polynom: original func
    :param startPoint: start of range
    :param endPoint: end of range
    :param epsilon: range of error allowed
    """
    print("*** Bisection_Method ***")
    partition(polynom, startPoint, endPoint, runBisection, choice, epsilon)


def partition(polynom, startPoint, endPoint, runMethod, choice, epsilon):
    """
    separates the original range into smaller ranges
    :param polynom: original func
    :param startPoint: start of range
    :param endPoint: end of range
    :param runMethod: function of the method to solve by
    :param choice: index of the method to solve by
    :param epsilon: range of error allowed
    :return: prints all roots if there are any
    """
    x = sp.symbols('x')
    f = lambdify(x, polynom)
    polynomTag = calcDerived(polynom)
    fTag = lambdify(x, polynomTag)
    i = startPoint
    while i < endPoint:
        j = i + 0.1
        # function ######################################################
        if choice is 0:  # bisection
            error = calcError(startPoint, endPoint, epsilon)
            c, iteration = runMethod(f, i, j, error, epsilon)
        elif choice is 1:  # newtonRaphson
            c, iteration = runMethod(polynom, i, j, epsilon)
        else:  # secant
            c, iteration = runMethod(f, i, j, epsilon)

        if c is not None:
            print("root: " + str(c) + " ,\titeration: " + str(iteration))

        # derived ########################################################
        if choice is 0:  # bisection
            error = calcError(startPoint, endPoint, epsilon)
            c, iteration = runMethod(fTag, i, j, error, epsilon)  # derived
        elif choice is 1:  # newtonRaphson
            c, iteration = runMethod(polynomTag, i, j, epsilon)
        else:  # secant
            c, iteration = runMethod(fTag, i, j, epsilon)

        if c is not None:
            if -epsilon < f(c) < epsilon:
                print("root: " + str(c) + " ,\titeration: " + str(iteration))
        i += 0.1
    print("------------------------")


def runBisection(f, startA, endB, error, epsilon):
    """
    :param f: original func
    :param startA: start of range
    :param endB: end of range
    :param error: max number of iterations
    :param epsilon: range of error allowed
    :return: root in this range if exists
    """
    fXl = f(startA)
    fXr = f(endB)
    if (fXl * fXr) > 0:
        return None, None
    i = 0
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
    """
    print the derivative in a symbol way
    :param my_f: original func
    :return: print func and derived
    """
    x = sp.symbols('x')
    print("my_func: ", my_f)
    my_f1 = sp.diff(my_f, x)
    print("f' : ", my_f1)
    d1 = sp.diff(my_f1)
    print("f'': ", d1)


def calcDerived(f):
    """
    :param f: original func
    :return: the derived without lambdify
    """
    # calc the derivative from func -> lambdify
    x = sp.symbols('x')
    f_prime = f.diff(x)
    return f_prime


def calcError(start, end, epsilon):
    """
    :param start: start of bigger range
    :param end: end of bigger range
    :param epsilon: range of error allowed
    :return: max number of iteration for Bisection method
    """
    return -(math.log(epsilon / (end - start)) / math.log(2))


# -------------- part 2 -------------


def Newton_Raphson(polynom, startPoint, endPoint, choice, epsilon):
    """
    :param polynom: original func
    :param startPoint: start of range
    :param endPoint: end of range
    :param epsilon: range of error allowed
    """
    print("*** Newton Raphson ***")
    partition(polynom, startPoint, endPoint, runNewton, choice, epsilon)


def runNewton(f, startA, endB, epsilon):
    """
    :param f: original func
    :param startA: start of range
    :param endB: end of range
    :param epsilon: range of error allowed
    :return: root in this range if exists
    """
    x = sp.symbols('x')
    fTag = lambdify(x, calcDerived(f))
    f = lambdify(x, f)
    fXl = f(startA)
    fXr = f(endB)
    if (fXl * fXr) > 0:
        return None, None
    i = 0
    c = (startA + endB) / 2
    while i < 100:
        i += 1
        newC = c - (f(c) / fTag(c))
        if abs(newC - c) < epsilon:
            return newC, i
        c = newC
    print("Could not find root, The function is not suitable for Newton Raphson")
    return None, None


# -------------- part 3 ----------------


def secant_method(polynom, startPoint, endPoint, choice, epsilon):
    """
    :param polynom: original func
    :param startPoint: start of range
    :param endPoint: end of range
    :param epsilon: range of error allowed
    """
    print("*** secant method ***")
    partition(polynom, startPoint, endPoint, runSecant, choice, epsilon)


def runSecant(f, startA, endB, epsilon):
    """
    :param f: original func
    :param startA: start of range
    :param endB: end of range
    :param epsilon: range of error allowed
    :return: root in this range if exists
    """
    fXl = f(startA)
    fXr = f(endB)
    if (fXl * fXr) > 0:
        return None, None
    c = startA
    newC = endB
    i = 0
    while i < 100:
        i += 1
        temp = newC
        newC = (c * f(newC) - newC * f(c)) / (f(newC) - f(c))
        c = temp
        if abs(newC - c) < epsilon:
            return newC, i
    print("Could not find root, The function is not suitable for secant method")
    return None, None


# --------------- part 4 ----------------
def driver():
    """
    the main function of the program
    """
    x = sp.symbols('x')
    # define polynom
    # f = x ** 4 + x ** 3 - 3 * x ** 2
    f = ln(x)

    # define range
    # startPoint = -3
    # endPoint = 2
    startPoint = 1
    endPoint = 2

    # define epsilon
    epsilon = 0.0001

    printDerived(f)
    print("-------------")
    choice = input("Enter 0 for Bisection method, 1 for Newton Raphson, 2 for Secant method, else for all\n")
    if choice is '0':
        bisection_method(f, startPoint, endPoint, 0, epsilon)
    elif choice is '1':
        Newton_Raphson(f, startPoint, endPoint, 1, epsilon)
    elif choice is '2':
        secant_method(f, startPoint, endPoint, 2, epsilon)
    else:
        bisection_method(f, startPoint, endPoint, 0, epsilon)
        Newton_Raphson(f, startPoint, endPoint, 1, epsilon)
        secant_method(f, startPoint, endPoint, 2, epsilon)


driver()
