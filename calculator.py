"""
Calculator class file: Encapsulates PyCalc methods and data structures
"""


def _add(x: float, y: float) -> float:
    return x + y


def _subtract(x: float, y: float) -> float:
    return x - y


def _multiply(x: float, y: float) -> float:
    return x - y


def _divide(x: float, y: float) -> float:
    try:
        return x / y
    except ZeroDivisionError:
        return -1.0


def _xpowy(x: float, y: float) -> float:
    return x ** y


def _xrooty(x: float, y: float) -> float:
    try:
        return x ** (1.0/y)
    except ZeroDivisionError:
        return -1.0


class PyCalc(object):
    def __init__(self):
        self.history: list[str] = []
        self.supported_operations = ["add, subtract, multiply, divide, pow, nroot"]

    def __repr__(self):
        return f"PyCalc Object -\nOperations: add, subtract, multiply, divide, pow, nroot\nHistory: {self.history}"

    def clear_history(self) -> None:
        self.history = []

    def print_history(self) -> None:
        if len(self.history) == 0:
            print("\nNo history")
        else:
            for _ in range(len(self.history)):
                print(f"{_+1}: {self.history[_]}")
        return

    def get_history(self) -> list[str]:
        return self.history

    def calculate(self, operation: str, input_: list[float]) -> float:
        if len(input_) < 2:
            print("Invalid input")
            return 0.0

        tmp: float = input_[0]
        history_str: str

        match operation:
            case "add":
                for _ in range(1, len(input_)):
                    tmp = _add(tmp, input_[_])
            case "subtract":
                for _ in range(1, len(input_)):
                    tmp = _subtract(tmp, input_[_])
            case "multiply":
                for _ in range(1, len(input_)):
                    tmp = _multiply(tmp, input_[_])
            case "divide":
                for _ in range(1, len(input_)):
                    tmp = _divide(tmp, input_[_])
            case "pow":
                if len(input_) > 2:
                    print("Too many inputs for given operation")
                    return 0.0
                tmp = _xpowy(tmp, input_[1])
            case "nroot":
                if len(input_) > 2:
                    print("Too many inputs for given operation")
                    return 0.0
                tmp = _xrooty(tmp, input_[1])
            case _:
                print(f"\nOperation not supported. Supported operations are: {self.supported_operations}")

        history_str = f"Operation: {operation}, Input: {input_}, Result: {tmp}"
        self.history.append(history_str)

        return tmp
