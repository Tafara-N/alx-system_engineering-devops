"""
A program that prompts the user for the name of a variable in camel case
and outputs the corresponding name in snake case.
"""


def main():
    """
    Main function
    """
    camel_case = input("camelCase: ")
    snake_case = convert_to_snake_case(camel_case)
    print(f"{snake_case}")


def convert_to_snake_case(camel):
    """
    Converts camelCase to snake_case
    """
    snake_case = ""
    for char in camel:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case.lstrip("_")


main()
