import time


class Auto:
    """описание авто"""
    def __init__(self, brand, age, mark, colour= "White", weight = "2600"):
        self.brand = brand
        self.age = age
        self.colour = colour
        self.weight = weight
        self.mark = mark

    def move(self):
        print("MOVE")

    def birthday(self):
        self.age += 1
        print(f'''My b-day {self.age}''')

    def stop(self):
        print("STOP")
# создаем объект и передаем аргументы
Auto1 = Auto("Audi", 2, "A6")
# обращаемся к свойствам
print(Auto1.brand)
# обращаемся к методу

Auto1.birthday()
class Track (Auto):
    def  __init__(self, brand, age, mark):
        super().__init__(self, brand, age, mark)
        self.max_load = max_load

    def move(self):
        print ("ATTENTION!!!!!")
        super().move()
    def load(self):
        time.sleep(1)
        print(self.brand, self.mark)
        ////////////////////////

class Car (Auto):
    def __init__(self, brand, age, mark):
        super().__init__(self, brand, age, mark)
        self.max_speed = max_speed
    pass


class Summarizer:
    @staticmethod
    def sum_classes(*clacla):
        New_class = type("New_class", clacla, {})
        return New_class

CarTruck = Summarizer.sum_classes(Car,Track)
Auto2 = CarTruck("Audi", 15, "a6")
Auto2.load()





