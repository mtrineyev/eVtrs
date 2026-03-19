from abc import ABC, abstractmethod
from math import pi
from typing import Union, Optional


# Використовуємо Union для позначення того, що число може бути як цілим, так і дробовим
Numeric = Union[int, float]

class Figure(ABC):
    def __init__(self, name: str = "figure", color: str = "red") -> None:
        self.name = name
        self.color = color

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str) -> None:
        if not isinstance(color, str):
            raise TypeError("Колір повинен бути рядком символів")
        self.__color = color

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Ім'я повинне бути рядком символів")
        self.__name = name

    @abstractmethod
    def __str__(self) -> str:
        """Повертає рядкове представлення об'єкта."""
        return f"Figure({self.color=}, {self.name=})"

    @abstractmethod
    def area(self) -> Numeric:
        """Абстрактний метод для обчислення площі."""
        pass


class Rectangle(Figure):
    def __init__(self, color: str, width: Numeric, length: Numeric) -> None:
        # Спочатку ініціалізуємо базовий клас, потім власні атрибути
        super().__init__("Прямокутник", color)
        self.width = width
        self.length = length

    @property
    def width(self) -> Numeric:
        return self.__width

    @width.setter
    def width(self, width: Numeric) -> None:
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина повинна бути числом")
        self.__width = width
        
    @property
    def length(self) -> Numeric:
        return self.__length

    @length.setter
    def length(self, length: Numeric) -> None:
        if not isinstance(length, (int, float)):
            raise TypeError("Довжина повинна бути числом")
        self.__length = length

    def area(self) -> Numeric:
        return self.width * self.length

    def __str__(self) -> str:
        return (
            "Rectangle("
            f"колір={self.color}, "
            f"ширина={self.width}, "
            f"довжина={self.length})"
        )


class Circle(Figure):
    def __init__(self, color: str, radius: Numeric) -> None:
        super().__init__("Коло", color)
        self.radius = radius

    @property
    def radius(self) -> Numeric:
        return self.__radius

    @radius.setter
    def radius(self, radius: Numeric) -> None:
        if not isinstance(radius, (int, float)):
            raise TypeError("Радіус повинен бути числом")
        self.__radius = radius

    def area(self) -> Numeric:
        return pi * self.radius ** 2

    def __str__(self) -> str:
        return (
            f"Circle("
            f"колір={self.color}, "
            f"радіус={self.radius})"
        )


if __name__ == "__main__":
    r: Rectangle = Rectangle("yellow", 5, 2)
    print(r, f"площею {r.area()} кв.м.")

    circle: Circle = Circle("blue", 10)
    print(circle, f"площею {circle.area():.2f} кв.м.")
