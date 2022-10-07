#
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#
#
#     def set_num(self, num):
#         self.__num = num
#
#     def get_num(self):
#         return self.__num
#
#     def set_surname(self, surname):
#         self.__surname = surname
#
#     def get_surname(self):
#         return self.__surname
#
#
#     def set_percent(self, percent):
#         self.__percent = percent
#         self.__value += self.__value * self.__percent
#         print('Проценты изменены => ', end='')
#
#
#     def get_percent(self):
#         return self.__percent
#
#     def set_value(self, value):
#         self.__value = value
#         print('Сумма изменена => ', end='')
#
#     def get_value(self):
#         return self.__value
#
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.set_num('123')
# print(f'#{acc.get_num()} => Изменен номер счета')
# acc.set_surname('_Долгих_')
# print(f'Владелец: {acc.get_surname()} => изменен')
# acc.set_percent(0.04)
# print(acc.get_percent())
# acc.set_value(1101)
# print(acc.get_value())
#
#
#
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#
#
#     def set_num(self, num):
#         self.__num = num
#
#     def get_num(self):
#         return self.__num
#
#     def set_surname(self, surname):
#         self.__surname = surname
#
#     def get_surname(self):
#         return self.__surname
#
#
#     def set_percent(self, percent):
#         self.__percent = percent
#         self.__value += self.__value * self.__percent
#         print('Проценты изменены => ', end='')
#
#
#     def get_percent(self):
#         return self.__percent
#
#     def set_value(self, value):
#         self.__value = value
#         print('Сумма изменена => ', end='')
#
#     def get_value(self):
#         return self.__value
#
#     nm = property(get_num, set_num)
#     sm = property(get_surname, set_surname)
#     prc = property(get_percent, set_percent)
#     ve = property(get_value, set_value)
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.nm = "112233"
# print(f'#{acc.nm} => Изменен номер счета')
# acc.sm = '__Долгих__'
# print(f'Владелец: {acc.sm} => изменен')
# acc.prc = 0.04
# print(acc.prc)
# acc.ve = 1101
# print(acc.ve)
#
