# метаклассы
class Dog:
    parts=100
    def __new__(cls, *args, **kwargs):


dog_parts = {
    "head": 1,
    "foot": 4,
    "body": 1,
    "tail": 1,
}
dog_1 = type('Dog', (), {'parts': 100})
dog_2 = type('Dogasaur', (), {'pieces': 200})
# ()-предки
dog_class = type("SimpleDog", (dog_1, dog_2), dog_parts)

print(type(dog_class))
print(dog_class)

a_dog = dog_class()
print(a_dog.head, a_dog.foot,a_dog.parts, a_dog.pieces)

#