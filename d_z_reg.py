import re

 # Регулярные выражения
str = 'В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков.'
reg = r'\d\d\W\d\d\W\d{4}'
print(re.findall(reg, str))

 # Тестовое значение: my-p@ssw0rd_
str = input("Проверка соотверствия пароля: =>  ")
reg = r'^[a-zA-Z0-9_\-@]{6,18}$'
print(re.findall(reg, str))

