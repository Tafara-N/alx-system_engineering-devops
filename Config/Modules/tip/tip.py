"""
A program that calculates the amount for a tip
"""


def main():
    """
    Prompts user for amount of the meal and a tip.
    """
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    """
    Strips the $
    """
    d = d.lstrip("$")
    return float(d)


def percent_to_float(p):
    """
    Strips the %
    """
    p = p.rstrip("%")
    return float(p) / 100


main()
