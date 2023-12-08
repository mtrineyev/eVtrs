class Flat:
    """Створюється квартира"""

    def __init__(
        self,
        area=80,
        number_of_rooms=3,
        number_of_residents=5,
        addresses="м. Миколаїв, пр. Свободи, 10"
    ):
        self.__area = area
        self.__number_of_rooms = number_of_rooms
        self.__number_of_residents = number_of_residents
        self.__addresses = addresses

    def __str__(self):
        return (
            f"Квартира площею {self.__area}, "
            f"кількість кімнат {self.__number_of_rooms}, "
            f"з {self.__number_of_residents} мешканцями, "
            f"за адресою {self.__addresses}"
        )

    def __lt__(self, other):
        self.validate_flat(other)
        return self.__area < other.__area

    def __eq__(self, other):
        self.validate_flat(other)
        return self.__area == other.__area

    @staticmethod
    def validate_flat(obj):
        if not isinstance(obj, Flat):
            raise TypeError("Неможливо порівняти квартиру з не квартирою")

    def set_area(self, area=80):
        self.__area = area

    def set_number_of_residents(self, number_of_residents):
        self.__number_of_residents = number_of_residents

    def rent_flat(self):
        """Орендуємо квартиру"""
        print(
            f"Ми орендуємо квартиру площею {self.__area}, "
            f"із кількістю кімнат {self.__number_of_rooms}, "
            f"для {self.__number_of_residents} мешканців, "
            f"за адресою {self.__addresses}"
        )


if __name__ == "__main__":
    my_flat = Flat()
    print(my_flat)
    yvgens_flat = Flat(area=200, addresses="м. Миколаїв, пр. Свободи, 12")

    if yvgens_flat > my_flat:
        print("Квартира Євгена більше")
    elif yvgens_flat < my_flat:
        print("Квартира Євгена менша")
    else:
        print("Квартири однакові")
