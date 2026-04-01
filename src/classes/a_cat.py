class Cat:
    # Конструктор: тут ми описуємо, які характеристики має кожен кіт
    def __init__(self, name, color):
        self.name = name   # Ім'я кота
        self.color = color # Колір кота

    # Метод: те, що кіт вміє робити
    def say_meow(self):
        print(f"{self.name} каже: Мяу!")

# Створюємо екземпляри (об'єкти) класу
my_cat = Cat("Мурчик", "сірий")
your_cat = Cat("Сніжок", "білий")

# Звертаємося до властивостей та методів
print(f"Мій кіт — {my_cat.name}, він {my_cat.color}.")
my_cat.say_meow()

print(f"Твій кіт — {your_cat.name}, він {your_cat.color}.")
your_cat.say_meow()
