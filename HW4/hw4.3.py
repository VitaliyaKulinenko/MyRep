# # number= [1, 2, 3, 4, 5]
# # def count_numbers(number):
# #     count_dict = {}
# #     for i in number:
# #         if count.dict.get(i, 0):
# #             count_dict[i]+= 1
# #         else:
# #             count_dict[i] = 1
# #         return count_dict
# #     print(count_numbers(number))
# def result_count(num, data):
#     count = 0
#     for el in data:
#         if el == num:
#             count += 1
#     return count
# number=[1,1,4,5,6,7,5]
# result_dict = {}
# for num in number:
#      if num not in result_dict:
#          # result_dict[num]=result_count(data=number, num=num)
#          result_dict[num] = (lambda n, ln: sum([1 for i in ln if n==i ]))(num,number)
# print(result_dict)