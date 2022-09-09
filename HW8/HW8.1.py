class Auto:
    """описание авто"""
    def __init__(self, brand, age, colour, mark, weight):
        self.brand = brand
        self.age = age
        self.colour = colour
        self.mark = mark
        self.weight = weight

    def move(self):
        print("MOVE")

    def birthday(self):
        self.age += 1
        print(f'''My b-day {self.age}''')

    def stop(self):
        print("STOP")
# создаем объект и передаем аргументы
Auto1 = Auto("Audi", 2, "White", "A6",2600)
# обращаемся к свойствам
print(Auto1.age)
# обращаемся к методу

Auto1.birthday()

