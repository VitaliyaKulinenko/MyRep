name = input ("Введите свое имя :")
age = int(input( "Введите свой возраст:"))
count=0
if age < 0:
    print( name.title() , "так не бывает!")
    while age < 0:
        print ("Повторите ввод!")
        age = int(input("Ваш возраст: "))
        count += 1
elif age > 3 and age < 10:
    print (name.title() , "ты слишко молодо выглядишь!")
elif age >10 and age < 18:
    print( "Как жизнь", name.title(), "?")
elif age >18 and age < 100:
    print ( "Чего желаете", name.title(), "?")
elif age >= 100:
    print (name.title(), "столько не живут!")
    while age >= 100:
        print ("Повторите ввод!")
        age = int(input("Ваш возраст: "))
        count +=1
if count > 1:
    print(" Вот сразу бы так, чего томил?")
else:
    print("Ишь, какой правильный попался!")