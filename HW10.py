a = float(input())
op = input()
b = float(input())
# a,op,b = input().split

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "/":
    if b == 0:
        print("Ошибка!На ноль делить нельзя!")
    else:
        print(a/b)
elif op == "*":
    print(a*b)
else:
    print ("Error")


#     try:
#
#         except ZeroDivisionError as err:
# print ("Ошибка!На ноль делить нельзя!")


