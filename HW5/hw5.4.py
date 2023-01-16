from datetime import datetime

def time_of_funct(func):
    def wrapper(*args):
        start_time = datetime.now()
        result=func(*args)
        print(datetime.now()-start_time)
    return wrapper
@time_of_funct
def square(a):
    print("Квадрат числа", a, "равен",a**2)


@time_of_funct
def even(a):
    if a%2==0:
        print(a,"Четное")
    else:
        print(a,"Нечетное")





# главная программа,передаем значение функции
square(3)
even(10)