import math

class Figura:
    """
    ОСНОВНИЙ КЛАС (Батьківський)
    Тут ми демонструємо ІНКАПСУЛЯЦІЮ — приховування даних (використання __)
    та надання доступу до них через спеціальні методи (гетери та сетери).
    """
    COLORS = ["жовтий", "блакитний"]

    def __init__(self, name="Фігура", square=0.0, color="жовтий") -> None:
        self.name = name      # Викликає сетер @name.setter
        self.square = square  # Викликає сетер @square.setter
        self.color = color    # Викликає сетер @color.setter

    # --- ІНКАПСУЛЯЦІЯ (керування доступом до даних) ---
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
        # Перевірка: площа не може бути від'ємною
        if not isinstance(square, (int, float)) or square < 0:
            raise ValueError("Площа повинна бути числом >= 0")
        self.__square = float(square)

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color) -> None:
        if color not in self.COLORS:
            raise ValueError(f"Дозволені кольори: {self.COLORS}")
        self.__color = color

    # --- ПОЛІМОРФІЗМ (однакова назва методу __str__ працює по-різному для всіх фігур) ---
    def __str__(self) -> str:
        return f"Фігура: {self.name} | Площа: {self.square:.2f} | Колір: {self.color}"

    @staticmethod
    def validate_figura(obj) -> None:
        if not isinstance(obj, Figura):
            raise TypeError(f"Об'єкт '{obj}' не є фігурою")

    # Методи порівняння (поліморфізм: ми порівнюємо будь-які фігури між собою)
    def __lt__(self, other):
        self.validate_figura(other)
        return self.square < other.square

    def __eq__(self, other):
        self.validate_figura(other)
        return self.square == other.square


class Rectangle(Figura):
    """
    НАСЛІДУВАННЯ: Прямокутник отримує всі властивості Figura, 
    але додає свої (довжину та ширину).
    """
    def __init__(self, length=0.0, width=0.0, color="жовтий") -> None:
        # super() викликає конструктор батьківського класу Figura
        super().__init__(name="Прямокутник", color=color)
        self.length = length
        self.width = width
        # Автоматично обчислюємо площу при створенні
        self.square = float(length * width)

    def __str__(self) -> str:
        # Додаємо до опису базової фігури специфічні дані прямокутника
        return f"{super().__str__()} [L: {self.length}, W: {self.width}]"


class Circle(Figura):
    """
    НАСЛІДУВАННЯ: Коло — це теж фігура.
    Тут ми також бачимо ПОЛІМОРФІЗМ у дії: метод розрахунку площі свій, а назва класу спільна.
    """
    def __init__(self, radius=0.0, color="блакитний") -> None:
        super().__init__(name="Коло", color=color)
        self.radius = radius
        # Формула площі кола: S = pi * r^2
        self.square = math.pi * (radius ** 2)

    def __str__(self) -> str:
        return f"{super().__str__()} [Радіус: {self.radius}]"


def main():
    try:
        print("--- Налаштування Прямокутника ---")
        l = float(input("Введіть довжину прямокутника: "))
        w = float(input("Введіть ширину прямокутника: "))
        rect = Rectangle(length=l, width=w, color="жовтий")

        print("\n--- Налаштування Кола ---")
        r = float(input("Введіть радіус кола: "))
        circ = Circle(radius=r, color="блакитний")

        print("--- Список створених фігур ---")
        print(rect)
        print(circ)
        print("------------------------------\n")

        # ПОРІВНЯННЯ (працює завдяки магічним методам у базовому класі Figura)
        print(f"Порівнюємо {rect.name} та {circ.name}:")
        if rect > circ:
            print(f"Результат: {rect.name} має більшу площу.")
        elif rect < circ:
            print(f"Результат: {circ.name} має більшу площу.")
        else:
            print("Результат: Площі фігур рівні.")

    except ValueError as e:
        print(f"\nПомилка введення: Будь ласка, використовуйте лише числа з крапкою")
        print(f"Деталі помилки: {e}")

if __name__ == "__main__":
    main()
    