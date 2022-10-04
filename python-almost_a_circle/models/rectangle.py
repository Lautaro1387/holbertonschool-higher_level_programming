#!/usr/bin/python3
"""class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """class name: Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def area(self):
        """area"""
        return self.__width * self.__height

    @property
    def width(self):
        """getter"""
        self.__width = width

    @property
    def height(self):
        """getter"""
        self.__height = height

    @property
    def x(self):
        """getter"""
        self.__x = x

    @property
    def y(self):
        """getter"""
        self.__y = y

    @width.setter
    def width(self, width):
        """setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def display(self):
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            for w in range(self.__x):
                print(" ", end="")
            for k in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        if args:
            for i in range(len(args)):
                if i == 0:
                    setattr(self, "id", args[i])
                if i == 1:
                    setattr(self, "width", args[i])
                if i == 2:
                    setattr(self, "height", args[i])
                if i == 3:
                    setattr(self, "x", args[i])
                if i == 4:
                    setattr(self, "y", args[i])
        else:
            for key, value in kwargs.items():
                if key == "id":
                    setattr(self, "id", value)
                if key == "width":
                    setattr(self, "width", value)
                if key == "height":
                    setattr(self, "height", value)
                if key == "x":
                    setattr(self, "x", value)
                if key == "y":
                    setattr(self, "y", value)
