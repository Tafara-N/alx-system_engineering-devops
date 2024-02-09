"""
A program that prompts the user to insert a coin, one at a time,
each time informing the user of the amount due.
"""


def coke():
    """ Coke machine """
    total = 0
    while total < 50:
        print(f"Amount Due: {50 - total}")
        coin = int(input("Insert Coin: "))
        if coin in [5, 10, 25]:
            total += coin
        # else:
        #     print("Invalid coin. Please insert a coin of denomination 5, 10, or 25 cents.")
    print(f"Change Owed: {total - 50}")


if __name__ == "__main__":
    coke()
