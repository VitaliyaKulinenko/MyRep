# from abc import ABC


# АБС - шаблон, каркас для будущих классов
# если в имени класса вносим АБС,то происходит наследование
class Weapon():
    # вызываем встроенный декоратор
    # @property
    # def barrel(self):
    #     return 0
    # или
    def __init__(self, barrel_size=0):
        self.barrel=barrel_size
    # вызываем ф-цию сравнения
    # инкапсуляция
    def __gt__(self, other):
        # print(other)
        return self.barrel>other.barrel
    def load(self):
        # рэйс вызывается,если потомок должен переделать метод предка
        raise NotImplemented
    def shoot(self):
        pass

# производим наследование
class Gun(Weapon):
    @property
    def barrel(self):
        return 5

    def shoot(self):

        print("*Bang*")



class Rifle(Weapon):

    def barrel(self):
        return 10
    @classmethod
    def shoot(self):
        print("Baaaaaaaaang")

class Minigun(Gun):
    def shoot(self):
        for i in range(3):
            super().shoot()


mg = Minigun()
gun = Gun(5)
rifle = Rifle(10)

print(rifle>gun)

# for current_gun in [gun,rifle]:
#     current_gun.shoot()
# mg.shoot()
#
#
#
#
#
#
# print(gun.shoot(),rifle.shoot())
# print(type(a_gun))
print(Minigun.__mro__)