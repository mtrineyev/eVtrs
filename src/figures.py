from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):
    def __init__(self, name="figure", color="red"):
        self.name = name
        self.color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError("Колір повинен бути рядком символів")
        self.__color = color

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Ім'я повинне бути рядком символів")
        self.__name = name

    @abstractmethod
    def __str__(self):
        return f"Figure({self.color=}, {self.name=})"

    @abstractmethod
    def get_area(self, *arg, **kwargs):
        pass


class Rectangle(Figure):
    def __init__(self, color, width, length):
        super().__init__("Прямокутник", color)
        self.width = width
        self.length = length

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not (isinstance(width, int) or isinstance(width, float)):
            raise TypeError("Ширина повинна бути числом")
        self.__width = width
        
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if not (isinstance(length, int) or isinstance(length, float)):
            raise TypeError("Довжина повинна бути числом")
        self.__length = length

    def get_area(self):
        area = self.width * self.length
        return area

    def __str__(self):
        return (
            "Rectangle("
            f"колір={self.color}, "
            f"ширина={self.width}, "
            f"довжина={self.length})"
        )


class Circle(Figure):
    def __init__(self, color, radius):
        super().__init__("Коло", color)
        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if not (isinstance(radius, int) or isinstance(radius, float)):
            raise TypeError("Радіус повинен бути числом")
        self.__radius = radius

    def get_area(self):
        area = pi * self.radius ** 2
        return area

    def __str__(self):
        return (
            f"Circle("
            f"колір={self.color}, "
            f"радіус={self.radius})"
        )


if __name__ == "__main__":
    r = Rectangle("yellow", 5, 2)
    print(r, f"площею {r.get_area()} кв.м.")

    circle = Circle("blue", 10)
    print(circle, f"площею {circle.get_area()} кв.м.")
