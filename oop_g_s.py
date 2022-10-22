def get_edit_owner(surname):
    return surname


class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __init__(self, num, surname, percent, value=0):
        self.__num = num
        self.__surname = surname
        self.percent = percent
        self.value = value
        print(f'Счет #{self.__num} принадлежит {self.__surname} был открыт.')
        print('*' * 50)

    # def __del__(self):
    #     print('*' * 50)
    #     print(f'Счет #{self.__num} принадлежащий {self.__surname} был закрыт.')

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def edit_owner(self, surname):
        self.__surname = surname

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счета: {usd_val} {Account.suffix_usd}.')

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f'Состояние счета: {eur_val} {Account.suffix_eur}.')

    def print_balance(self):
        print(f'Текущий баланс {self.value} {Account.suffix}') # Баланс в рублях

    def print_info(self):  # Информация о счете
        print(f'Информация о счете:')
        print('-' * 20)
        print(f'#{self.__num}')
        print(f'Владелец: {self.__surname}')
        self.print_balance()
        print(f'Проценты: {self.percent:.0%}')
        print('-' * 20)

    def add_percents(self):
        self.value += self.value * self.percent
        print('Проценты были успешно начислены')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f'К сожалению у вас нет {val} {Account.suffix}')
        else:
            self.value -= val
            print(f'{val} {Account.suffix} было успешно снято!')
        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f'{val} {Account.suffix} было успешно добавлено!')
        self.print_balance()


    def set_edit_owner(self, surname):
        self.__surname = surname

    def get_edit_owner(self, surname):
        return surname


acc = Account('12345', 'Долгих', 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()

Account.set_usd_rate(2)
acc.convert_to_usd()

Account.set_eur_rate(3)
acc.convert_to_eur()
print()

acc.edit_owner('Дюма')
acc.print_info()
print()

acc.add_percents()
print()

acc.withdraw_money(3000)
print()

acc.withdraw_money(100)
print()

acc.add_money(5000)
print()

acc.withdraw_money(3000)
print()

acc1 = Account('12345', 'Савельева', 0.03, 1000)
acc.set_edit_owner('Савельева')
# print(get_edit_owner('Сахаров'))
acc.print_info()
print()

# property 7 40