"""
A program that prompts the user for items, one per line.
Then output the user’s grocery list in all uppercase,
sorted alphabetically by item, prefixing each line with the number of times
the user inputted that item.
"""


def main():
    """
    Main function
    """

    grocery_list = {}

    try:
        while True:
            item = input().lower()
            grocery_list[item] = grocery_list.get(item, 0) + 1
    except EOFError:
        pass  # Handle Ctrl-D to end input

    print_grocery_list(grocery_list)


def print_grocery_list(grocery_list):
    """
    Printing grocery list one per line
    """

    sorted_items = sorted(grocery_list.items(), key=lambda x: x[0])
    print()
    for item, count in sorted_items:
        print(f"{count} {item.upper()}")


if __name__ == "__main__":
    main()
