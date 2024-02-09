#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """
    A square is a rectangle

    Attributes:
        number_of_instances (int): The number of rectangle's instances
        print_symbol (any): The symbol used to represent a string
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializing a new rectangle

        Args:
            width (int): The new rectangle's width
            height (int): The new rectangle's height
        """

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Sets the width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Sets the height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the rectangle's area
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the rectangle's perimeter
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the rectangle with the biggest area.

        Args:
            rect_1 (Rectangle): First rectangle
            rect_2 (Rectangle): Second rectangle

        Raises:
            TypeError: If either of rectangle_1 or rectangle_2 != rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle with width and height equal to size

        Args:
            size (int): The width and height of the current rectangle
        """

        return cls(size, size)

    def __str__(self):
        """
        Returns the rectangle's printable representation

        Represents the rectangle with the # (pound) character.
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []
        for h in range(self.__height):
            [rectangle.append(str(self.print_symbol)) for w in range(self.__width)]
            if h != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)

    def __repr__(self):
        """
        Returns the rectangle's representation of a string
        """

        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle

    def __del__(self):
        """
        Prints a message for everytime delete the rectangle
        """

        type(self).number_of_instances -= 1
        print("Bye rectangle...")
