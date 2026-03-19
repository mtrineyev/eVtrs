class Flat:
    def __init__(
            self,
            square=10.0,
            rooms=1,
            residents=0,
            address=""
    ) -> None:
        self.square = square  # Площа квартири
        self.rooms = rooms  # Кількість кімнат
        self.residents = residents  # Кількість мешканців
        self.address = address  # Адреса

    @property
    def square(self) -> float:
        return self.__square

    @square.setter
    def square(self, square) -> None:
        if not isinstance(square, float) or square < 0:
            raise ValueError
        self.__square = square

    @property
    def rooms(self) -> int:
        return self.__rooms

    @rooms.setter
    def rooms(self, rooms) -> None:
        if not isinstance(rooms, int) or rooms < 0:
            raise ValueError
        self.__rooms = rooms

    @property
    def residents(self) -> int:
        return self.__residents

    @residents.setter
    def residents(self, residents) -> None:
        if not isinstance(residents, int) or residents < 0:
            raise ValueError
        self.__residents = residents

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address) -> None:
        if "росія" in address.lower():
            raise ValueError("Такої країни не існує")
        self.__address = address

    def __str__(self) -> str:
        return "\n".join(
            [
                f"Площа: {self.square}",
                f"Кількість кімнат: {self.rooms}",
                f"Кількість мешканців: {self.residents}",
                f"Адреса: {self.address}"
            ]
        )

    @staticmethod
    def validate_flat(obj) -> None:
        if not isinstance(obj, Flat):
            raise TypeError(f"Об'єкт '{obj}' не квартира")

    def __lt__(self, other):
        self.validate_flat(other)
        return self.square < other.square

    def __eq__(self, other):
        self.validate_flat(other)
        return self.square == other.square


class House(Flat):
    def __init__(
            self,
            floors=1,
            garden=0.0,
            basement=False,
            *args,
            **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.floors = floors
        self.garden = garden
        self.basement = basement

    @property
    def floors(self) -> int:
        return self.__floors

    @floors.setter
    def floors(self, floors: int) -> None:
        if not isinstance(floors, int) or floors < 0:
            raise ValueError
        self.__floors = floors

    @property
    def garden(self) -> float:
        return self.__garden

    @garden.setter
    def garden(self, garden: float) -> None:
        if not isinstance(garden, float) or garden < 0:
            raise ValueError
        self.__garden = garden

    @property
    def basement(self) -> int:
        return self.__basement

    @basement.setter
    def basement(self, basement: int) -> None:
        if not isinstance(basement, int) or basement < 0:
            raise ValueError
        self.__basement = basement

    def __str__(self) -> str:
        return "\n".join(
            [
                super().__str__(),
                f"Кількість поверхів: {self.floors}",
                f"Площа садиби: {self.garden}",
                f"Наявність підвалу: {self.basement}"
            ]
        )

    @staticmethod
    def validate_house(obj) -> None:
        if not isinstance(obj, House):
            raise TypeError(f"Об'єкт '{obj}' не будинок")

    def __lt__(self, other):
        self.validate_house(other)
        return super().__lt__(other) or self.garden < other.garden

    def __eq__(self, other):
        self.validate_house(other)
        return super().__eq__(other) and self.garden == other.garden


def main() -> None:
    print("Квартира з параметрами за замовчуванням:")
    flat1 = Flat()
    print(flat1)

    print("\nКвартира із зазначенням площі та кількості кімнат:")
    flat2 = Flat(square=40.0, rooms=2)
    print(flat2)

    print("\nПорівняння квартир:")
    if flat1 > flat2:
        print("Перша квартира більша")
    elif flat1 == flat2:
        print("Квартири однакові")
    else:
        print("Друга квартира більша")

    print("\nКвартира із зазначенням усіх атрибутів:")
    flat3 = Flat(
        square=68.0,
        rooms=3,
        residents=2,
        address="вул. Ярослав Вал, буд. 1"
    )
    print(flat3)

    print("\nБудинок за замовчуванням:")
    house1 = House(garden=100.0)
    print(house1)

    print("\nБудинок із зазначенням усіх атрибутів:")
    house2 = House(
        square=200.0,
        rooms=5,
        residents=4,
        address="вул. Шевченка, буд. 1",
        garden=70.0,
        basement=True
    )
    print(house2)

    print("\nПорівняння будинків:")
    if house1 > house2:
        print("Першій будинок більший")
    elif house1 == house2:
        print("Будинки однакові")
    else:
        print("Другій будинок більший")

    # print("\nПорівняння квартири та будинку за замовчуванням:")
    # if flat1 == house1:
    #     print("Жилі площі однакові")
    # else:
    #     print("Жилі площі різні")


if __name__ == "__main__":
    main()
