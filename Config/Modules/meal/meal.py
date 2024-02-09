#!/usr/bin/python3

"""
A program that prompts the user for a time and outputs whether it's
breakfast time, lunch time, or dinner time.
"""


def main():
    """
    Main function
    """
    time = input("What time is it? ")
    time_to_eat = convert(time)

    if 7.0 <= time_to_eat <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_to_eat <= 13.0:
        print("lunch time")
    elif 18.0 <= time_to_eat <= 19.0:
        print("dinner time")


def convert(time):
    """
    Converts time to float
    """
    hours, minutes = map(int, time.split(":"))
    return hours + (minutes / 60)


main()
