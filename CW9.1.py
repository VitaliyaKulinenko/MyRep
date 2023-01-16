class Dog:
    def __init__(self, age, sex, months_pregnant=0):
        self.age = age
        self._sex = sex
        self.months_pregnant = months_pregnant
    @property
    def sex(self):
        return 'Male' if self._sex == 'm' else 'Female'

    @property
    def pregnancy(self):
        if self._sex == "m":
            return "Male cant be pregnant"
        elif self.age < 2:
            return "It is too young to be pregnant"
        elif self.months_pregnant < 4:
            return "Yes, its pregnancy"
        else:
            return "Puppies already born"





d1 = Dog(1, 'm')
d2 = Dog(3, 'male', 2)
d3 = Dog(5, 'male', 6)
for a_dog in (d1, d2, d3):
    print(a_dog.age, a_dog.sex, a_dog.pregnancy)