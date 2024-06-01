"""
Pycalc class file: Encapsulates PyCalc operations
"""


def add(x: float, y: float) -> float:
    """
    Returns the sum of 2 numbers.
    :param x: float
    :param y: float
    :return: float
    """
    return x + y


def subtract(x: float, y: float) -> float:
    """
    Returns the difference of two numbers.
    :param x: float
    :param y: float
    :return: float
    """
    return x - y


def multiply(x: float, y: float) -> float:
    """
    Returns the product of two numbers.
    :param x: float
    :param y: float
    :return: float
    """
    return x * y


def divide(x: float, y: float) -> float:
    """
    Returns the quotient of two numbers.
    :param x: float
    :param y: float
    :return: float
    """
    try:
        return x / y
    except ZeroDivisionError:
        print(f"\nDivide by Zero Error: Input - {x, y}")
        return -1.0


def xpowy(x: float, y: float) -> float:
    """
    Returns x raised to the power of y.
    :param x: float
    :param y: float
    :return: float
    """
    return x ** y


def xrooty(x: float, y: float) -> float:
    """
    Returns the yth root of x.
    :param x: float
    :param y: float
    :return: float
    """
    try:
        return x ** (1.0/y)
    except ZeroDivisionError:
        print(f"\nDivide by Zero Error: Input - {x, y}")
        return -1.0
