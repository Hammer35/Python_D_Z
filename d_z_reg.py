import re
import os

# Регулярные выражения
# str = 'В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков.'
# reg = r'\d\d\W\d\d\W\d{4}'
# print(re.findall(reg, str))
#
#  # Тестовое значение: my-p@ssw0rd_
# str = input("Проверка соотверствия пароля: =>  ")
# reg = r'^[a-zA-Z0-9_\-@]{6,18}$'
# print(re.findall(reg, str))

# num = [3, 5, 7, 3, 9, 5, 7, 2]
# print(sorted(num))


# f = open("text.txt", "r", encoding='utf-8')
# print(("".join(f.readlines())))
# f.close()

#######################################################################
#######################################################################

begin_f = open('text.txt', 'r', encoding='utf-8')
read_f = begin_f.readlines()
pos = int(input('Укажите индекс строки: '))
rename = read_f.pop(pos)
res = (read_f.append(rename))

e = open("write_file.txt", "w", encoding='utf-8')
e.write(str(read_f))

begin_f.close()
e.close()






with open('three_file.txt', 'w') as three, open('one_file', 'r') as one, open('two_file', 'r') as two:









