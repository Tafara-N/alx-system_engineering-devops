"""
A program that prompts consumers users to input a fruit and
then outputs the number of calories in one portion of that fruit,
per the FDA's poster for fruits
"""


fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew Melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}


def fruit_calories(fruit):
    """
    Get the calories for a given fruit from the dictionary.
    If the fruit is not found, return None.
    """
    return fruits.get(fruit.lower())


def main():
    """
    Main function
    """

    item = input("Item: ").capitalize()

    # Check if the entered fruit is in the dictionary
    calories = fruit_calories(item)

    if calories is not None:
        print(f"Calories: {calories}")


if __name__ == "__main__":
    main()
