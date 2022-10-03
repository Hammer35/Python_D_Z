from math import sqrt


class Rectangle:
    def __int__(self, l=0, w=0, res=0):
        self.__l = l
        self.__w = w
        self.__res = res

    def set_rectangle_area(self, l, w):
        res = l * w
        print("Площадь прямоугольника:", res)

    def square(self, l, w):
        res1 = (l + w) * 2
        print("Периметр прямоугольника:", res1)

    def hypotenuse(self, l, w):
        res2 = sqrt(l**2 + w**2)
        print("Периметр прямоугольника:", round(res2, 2))


p = Rectangle()
p.set_rectangle_area(3,9)
p.square(3,9)
p.hypotenuse(3, 9)



