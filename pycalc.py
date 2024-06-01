"""
Pycalc class file: Encapsulates PyCalc operations
"""


def add(x: float, y: float) -> float:
    return x + y


def subtract(x: float, y: float) -> float:
    return x - y


def multiply(x: float, y: float) -> float:
    return x * y


def divide(x: float, y: float) -> float:
    try:
        return x / y
    except ZeroDivisionError:
        print(f"\nDivide by Zero Error: Input - {x, y}")
        return -1.0


def xpowy(x: float, y: float) -> float:
    return x ** y


def xrooty(x: float, y: float) -> float:
    try:
        return x ** (1.0/y)
    except ZeroDivisionError:
        print(f"\nDivide by Zero Error: Input - {x, y}")
        return -1.0
