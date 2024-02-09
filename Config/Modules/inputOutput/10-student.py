#!/usr/bin/python3

"""
A class Student that defines a student by: (based on 9-student.py)
"""


class Student:
    """
    Student to JSON with filter
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializing a new student

        Args:
            first_name (str): The student's first name
            last_name (str): The student's last name
            age (int): The student's age
       """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Gets a student's dictionary representation

        Args:
            attrs (list): (Optional) The attributes to be represented
        """

        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__
