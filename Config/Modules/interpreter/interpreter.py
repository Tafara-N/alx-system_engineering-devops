"""
A program that prompts the user for an arithmetic expression and then
calculates and outputs the result as a floating-point value formatted to one decimal place.
"""


def main():
    """
    Main function
    """
    expression = input("Expression: ")

    try:
        x, op, z = expression.split()
        x = float(x)
        z = float(z)

        if op in ["+", "-", "*", "/"]:
            result = interpreter(x, op, z)
            print(f"{result:.1f}")
        else:
            print("Invalid operator. Please use +, -, *, or /")

    except ValueError:
        print(
            "Invalid format. Please enter x y z, where x and z are numbers and y is an operator."
        )


def interpreter(x, operator, z):
    """
    Computes the arithmetic expression
    """
    if operator == "+":
        return x + z
    elif operator == "-":
        return x - z
    elif operator == "*":
        return x * z
    elif operator == "/":
        return x / z


main()
