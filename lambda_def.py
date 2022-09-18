# print((lambda a, b, c: a * b * c)(2, 5, 5))
# #
# ##################################################
# #
# nums = [3, 5, 7, 3, 9, 5, 7, 2]
# summa1 = list(map(lambda x: x**2, nums))
# summa2 = list(map(lambda x: x**3, nums))
#
# print(summa1)
# print(summa2)
#
# #################################################
#
# list_students = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98}
# ]
# res1 = min(list_students, key=lambda i: i['final'])
# res2 = max(list_students, key=lambda i: i['final'])
#
# print(res1)
# print(res2)
#
# #################################################
#
# list_students = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98}
# ]
#
# res1 = sorted(list_students, key=lambda i: i['name'])
# res2 = sorted(list_students, key=lambda i: i['final'], reverse=True)
#
# print(res1)
# print(res2)
