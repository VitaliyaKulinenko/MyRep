a="mother"
b="father"
c="sister"
d="brother"
# открыли файл на запись
with open ("example6.2","w") as file:
    # как вывести слова на разных строчках?
    file.write(a)
    file.write(b)
file.close()
# открыли файл на дозапись
with open ("example6.2","a") as file:
    file.write(c)
    file.write(d)
file.close()