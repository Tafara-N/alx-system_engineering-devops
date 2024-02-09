"""
A program that prompts the user for a greeting
"""

greeting = input("Greeting: ").strip()
greet = greeting.lower()


if greet.startswith("hello"):
    print("$0")
elif greet.startswith("h"):
    print("$20")
else:
    print("$100")
