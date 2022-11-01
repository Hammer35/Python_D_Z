class Liquid:
    def __init__(self, name, density):
        self.name = name
        self.density = density

    def edit_density(self, val):
        self.density = val

    def calc_v(self, m):
        v = m / self.density
        print(f'Объем {m} кг {self.name} равен {v} m^3')

    def calc_m(self, v):
        m = v * self.density
        print(f'Вес {v} m^3 of {self.name} составляет {m} кг.')

    def print_info(self):
        print(f"Жидкость '{self.name}' (плотность = {self.density} kg/m^3).")

class Alcohol(Liquid):
    def __init__(self, name, density, strength):
        super().__init__(name, density)
        self.strength = strength

    def edit_strength(self, val):
        self.strength = val


a = Alcohol('Wine', 1064.2, 14)
a.print_info()

a.edit_density(1000)
a.print_info()

a.calc_v(300)
a.calc_m(0.5)

print(a.strength)
a.edit_strength(20)
print(a.strength)