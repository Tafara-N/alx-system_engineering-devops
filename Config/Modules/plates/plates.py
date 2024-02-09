"""
A program that prompts the user for a vanity plate and
then output Valid if meets all of the requirements or Invalid if it does not.
"""


def main():
    """
    Main function
    """

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """
    Check if the plate is valid
    """

    if has_minimum_length(s) and has_maximum_length(s) and\
            has_valid_characters(s) and has_valid_number_placement(s):
        return True
    else:
        return False


def has_minimum_length(s):
    """
    Check for required length
    """

    return len(s) >= 2


def has_maximum_length(s):
    """
    Check for required length
    """

    return 2 <= len(s) <= 6


def has_valid_characters(s):
    """
    Check for valid characters
    """

    return all(char.isalpha() or char.isdigit() for char in s)


def has_valid_number_placement(s):
    """
    Check for valid number placement
    """

    if s[-1].isdigit():
        return s[0].isalpha() and s[1:-1].isdigit() and s[1] != '0' and len(s) == 6
    else:
        return True


if __name__ == "__main__":
    main()
