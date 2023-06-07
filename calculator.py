import math
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    try:
        result =x / y
    except ZeroDivisionError:
        print("Error:divison by Zero")
        return None
    return result


def multiply(x, y):
    return x * y


def square(x):
    return x ** 2


def power(x, y):
    return x ** y


def sqrt(x):
    return math.sqrt(x)