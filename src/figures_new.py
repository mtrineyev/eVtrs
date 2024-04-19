class Figura:
    COLORS = ["жовтий", "блакитний"]

    def __init__(
            self,
            name="Фігура",
            square=0.0,
            color="жовтий"
    ) -> None:
        self.name = name
        self.square = square
        self.color = color

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        if "кропка" in name.lower():
            raise ValueError("Кропка не фігура")
        self.__name = name

    @property
    def square(self) -> float:
        return self.__square

    @square.setter
    def square(self, square) -> None:
        if not isinstance(square, float) and square <= 0:
            raise ValueError()
        self.__square = square

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color) -> None:
        if color not in self.COLORS:
            raise ValueError
        self.__color = color

    def __str__(self) -> str:
        return "\n".join(
            [
                f"Фигура: {self.name}",
                f"Площадь фигуры: {self.square}",
                f"Цвет фигуры: {self.color}"
            ]
        )

    @staticmethod
    def validate_figura(obj) -> None:
        if not isinstance(obj, Figura):
            raise TypeError(f"Об'єкт '{obj}' не фігура")

    def __lt__(self, other):
        self.validate_figura(other)
        return self.square < other.square

    def __eq__(self, other):
        self.validate_figura(other)
        return self.square == other.square


class Rectangle(Figura):
    def __init__(
            self,
            length=0.0,
            width=0.0,
            *arg,
            **kwargs
    ) -> None:
        super().__init__(*arg, **kwargs)
        self.length = length
        self.width = width
        self.square = length * width
        self.name = "Прямокутник"

    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, length) -> None:
        if not isinstance(length, float) and length < 0:
            raise ValueError("length патрэбна >= 0")
        self.__length = length

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width) -> None:
        if not isinstance(width, float) and width < 0:
            raise ValueError("width патрэбна >= 0")
        self.__width = width

    def __str__(self) -> str:
        return "\n".join(
            [
                super().__str__(),
                f"length: {self.length}",
                f"width: {self.width}",
               ]
        )


def main():
    figura1 = Rectangle(4, 4)
    figura2 = Rectangle(8, 2)
    if figura1 > figura2:
        print("Фігура1 більша")
    elif figura1 == figura2:
        print("Фігури рівні")
    else:
        print("Фігура2 більша")


if __name__ == "__main__":
    main()
