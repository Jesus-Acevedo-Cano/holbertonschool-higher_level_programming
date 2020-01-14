#!/usr/bin/python3
class Rectangle():
    """class named Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization of instance attributes
           Args:
           width (int): width of rectangle
           height (int): rectangle height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter fun"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter function
           value: new value to set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter fun"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter function
           value: new value to set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """func to calculate the area
           Return: area of square
        """
        return self.__width * self.__height

    def perimeter(self):
        """func to calculate the area
           Return: perimeter of square
        """
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """ returning the string representation of the rectangle """

        sym = str(self.print_symbol)
        rectangle = ""

        if self.height == 0 or self.width == 0:
            return rectangle

        for i in range(self.__height):
            rectangle += sym * self.__width
            if i + 1 != self.__height:
                rectangle += "\n"

        return rectangle

    def __repr__(self):
        """ return a string representation of the rectangle """
        rep = "{}({}, {})".format(self.__class__.__name__,
                                  self.width, self.height)
        return rep

    def __del__(self):
        """prints msg when instance is deleted"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            Checks for the bigger rectangle
            Returns: The biggest rectangle or rect_1 if they are equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        elif rect_1.area() >= rect_2.area():
            return rect_1

    @classmethod
    def square(cls, size=0):
        """ Creates a Rectangle instance where
            width and height are same size
        """
        return cls(size, size)
