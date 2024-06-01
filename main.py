"""
Main entry script for the command line version of PyCalc
"""
from sys import exit
import pycalc


def display_menu() -> None:
    print("\n*************************\n"
          "*         Menu          *\n"
          "*************************")
    print("* 1.) Add (x+y)         *\n"
          "* 2.) Subtract (x-y)    *\n"
          "* 3.) Multiply (x*y)    *\n"
          "* 4.) Divide (x/y)      *\n"
          "* 5.) Pow (x^y)         *\n"
          "* 6.) Root(y root of x) *\n"
          "* 7.) Show History      *\n"
          "* 8.) Clear History     *\n"
          "* 9.) Esc               *\n"
          "*************************\n")


def main():
    input_: str
    history: list[str] = []

    print("************************\n"
          "*  Welcome to PyCalc!  *\n"
          "************************\n")

    running: bool = True
    x: float
    y: float
    result: float
    while running:
        display_menu()

        input_ = input("\nPlease make a selection (1-9): ")

        if not (input_ == '7' or input_ == '8' or input_ == '9'):
            x = float(input("Enter x: "))
            y = float(input('Enter y: '))

        match input_:
            case '1':
                result = pycalc.add(x, y)
                history.append(f"{x} + {y} = {result}")
                print(f"\n{x} + {y} = {result}")
            case '2':
                result = pycalc.subtract(x, y)
                history.append(f"{x} - {y} = {result}")
                print(f"\n{x} - {y} = {result}")
            case '3':
                result = pycalc.multiply(x, y)
                history.append(f"{x} * {y} = {result}")
                print(f"\n{x} * {y} = {result}")
            case '4':
                result = pycalc.divide(x, y)
                history.append(f"{x} / {y} = {result}")
                print(f"\n{x} / {y} = {result}")
            case '5':
                result = pycalc.xpowy(x, y)
                history.append(f"{x} ^ {y} = {result}")
                print(f"\n{x} ^ {y} = {result}")
            case '6':
                result = pycalc.xrooty(x, y)
                history.append(f"{y} root of {x} = {result}")
                print(f"\n{y} root of {x} = {result}")
            case '7':
                print(f"\n{history}")
            case '8':
                history = []
            case '9':
                print("\n************************\n"
                      "*       Goodbye!       *\n"
                      "************************\n")
                running = False
            case _:
                print(f"\nInvalid selection: {input_}")
    exit()


if __name__ == '__main__':
    main()
