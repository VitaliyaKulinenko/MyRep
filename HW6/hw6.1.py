a=b'r\xc3\xa9sum\xc3\xa9'
s=a.decode()
print(s)
k=s.encode(encoding="Latin1")
print(k)
l=k.decode()
print(l)

# ошибка в 6,7 поле?