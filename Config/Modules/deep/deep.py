"""
Prompts the user for the answer to the Great Question of Life,
the Universe and Everything, outputting Yes or No
"""

question = input(
    "What is the answer to the Great Question of Life, the Universe, and Everything? "
).strip()

answer = question.lower()
if answer == "42" or answer == "forty two" or answer == "forty-two":
    print("Yes")
else:
    print("No")
