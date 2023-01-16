my_list= ("кек","топот","деревня")
print(list(filter(lambda x: x==''.join(reversed(x)),my_list)))

# в скобках первый параметр - условие,второй - где искать