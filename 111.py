# q = 'Pyt'
# w = 'hon'
# e = q + w

# print(e)
# print(e * 3)

# print(e in 'I am learn Python') # Поиск элемента в строке дал True
# print(e in 'I am learn Java')  # Поиск элемента в строке дал False

# s = 'Hello'
# print(s[1]) # Поиск по индексу [1] найден второй елемент строки
# print(s[-5]) # Поиск по отрицательному индексу [-5]

# s = 'Hello'
# print(s[1:])  # Поиск по срезу => ello
# print(s[1:4])  # Поиск по срезу => ell
# print(s[:])  # Поиск по срезу  => Hello
# print(s[0:5:2])  # Поиск по срезу с заданным шагом. => Hlo
# print(s[::-1])  # Разворот строки  => olleH

# Строка не изменяемый тип данных
# s = "python"
# s = s[:3] + 'Еh' + s[4:]  #  Замена символа в строке. Создается новая строка.  => pytЕhon
# print(s)

# def changeStr(s, c_old, c_new):
#     i = 0
#     s2 = ''
#     while i < len(s):
#         if s[i] == c_old:
#             s2 = s2 + c_new
#         else:
#             s2 = s2 + s[i]
#         i = i + 1
#
#     return  s2
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = changeStr(str1, 'N', 'P')
# print(str1)
# print(str2)

# s = "iuojpkU uIOPJHPOU pouhpioyh "
# print(s.capitalize()) #  Переводит только первую букву предложения в верхний регистр
# print(s.islower()) #  Переводит все в нижний регистр
# print(s.upper()) #  все в верхний регистр
# print(s.swapcase()) #  меняет регистр
# print(s.title()) #  перед пробелом переводит в верхний регистр

# print(s.count("p", 3, -9)) # Количество искомых символов
# print(s.find("p")) # индекс первого совпадения
# print(s.find(".")) # Если совпадения нет возвращается -1

# my_str = "Test string for me"
# arr = [ord(x)  for x in my_str]
# print("ASCII коды: " , arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [x for x in [ord(x) for x in input("-> ")[:3]] if x not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:
#     print("Количество последних элементов: ", arr.count(arr[-1]) - 1)
#     arr.sort(reverse=True)
# print(arr)


# str = "I am learning Python. hello, WORLD!"
# print(str.count("h"))
# vsego_h = str.find("h")
# print(vsego_h)

# nums = [3, 5, 7, 3, 9, 5, 7, 2]
# nums = [3, 5, 7, 3, 9, 5, 7, 2]
# r = lambda i: i ** 2
# print(r(nums))
# for i in nums:
#     i = i ** 2
#     print(i, end=" ")

# print()
#
# for i in nums:
#     i = i ** 3
#     print(i, end=" ")

# import re
# # reg = '[0-9][0-9]:[0-9][0-9]'
# # ss = 'Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Е01:09.'
# # print(re.findall(reg, ss))
# import re
# email_text = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
# res = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+', email_text)
# print(res)


# email_text = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
# res = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+', email_text)
# print(res)


# h = '<p style="margin-bottom:20px;color:rgb(22,24,35);font-weight:bold">355438</p>'
# reg = r'\d{6,7}'
# print(re.findall(reg, h))


# print((lambda a, b, c: a * b * c)(2, 5, 5))

# num = [3, 5, 7, 3, 9, 5, 7, 2]
# print([(lambda x: x * 2)(3, 5, 7, 3, 9, 5, 7, 2)])
# print([(lambda x: x * 3)(3, 5, 7, 3, 9, 5, 7, 2)])


# list_students = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98}
# ]
#
# res1 = min(list_students, key=lambda i: i['final'])
# res2 = max(list_students, key=lambda i: i['final'])
# print(res1)
# print(res2)








