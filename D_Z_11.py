"""Дано три словаря.
Нужно объединить в один."""
# import a as a

# dict_1 = {1: 10, 2: 20}
# dict_2 = {3: 10, 4: 20}
# dict_3 = {5: 10, 6: 20}
# dict_4 = {}
#
# for i in dict_1:
#     dict_4.update(dict_1)
#     for n in dict_2:
#         dict_4.update(dict_2)
#         for f in dict_3:
#             dict_4.update(dict_3)
#
#
# print(dict_4)

"""Дан словарь:
{'empty1': {'name': 'Jon', 'salary': '7500'}, 'empty2': {'name': 'Emma', 'salary': '8000'},
         'empty3': {'name': 'Bard', 'salary': '6500'}} Изменить значение зарплаты Бреда с 6500 до 8500.
"""

# dic_t = {'empty1': {'name': 'Jon', 'salary': '7500'}, 'empty2': {'name': 'Emma', 'salary': '8000'},
#          'empty3': {'name': 'Bard', 'salary': '6500'}}
#
# print(dic_t['empty3'])
# print(dic_t['empty3']['salary'])
#
# dic_t['empty3']['salary'] = 850
#
# for i in dic_t:
#     print(i)
# for v in dic_t[i]:
#     print(v, ':', dic_t[i][v])


# studs = {}
# k = int(input("Количество студентов: "))
# s = 0
# for i in range(k):
#     name = input(str(i + 1) + "-й студент: ")
#     score = int(input("Балл: "))
#     studs[name] = score
#     s += score
#     a = s / k
# print("\nСредний балл: %.0f. Студенты с баллом выше среднего: " % a)
# for i in studs:
#     if studs[i] > a:
#         print(i)
