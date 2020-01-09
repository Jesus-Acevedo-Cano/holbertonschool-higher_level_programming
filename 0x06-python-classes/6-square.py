#!/usr/bin/python3
class Square():
    """class named square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialization of instance attributes
           Args:
           size (int): The size of the square
           position (tupple): square position
        """
        self.size = size
        self.position = position

    def area(self):
        """func to calculate the area
           Return: area of square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """getter fun"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter function
           value: new value to set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position
           Args:
           value (int): square position
        """
        if isinstance(value, tuple) and len(value) == 2:
                if isinstance(value[0], int) and isinstance(value[1], int):
                    if value[0] >= 0 and value[1] >= 0:
                        self.__position = value
                        return
        raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """print a # square """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("{}{}".format(" " * self.position[0], "#" * self.__size))
