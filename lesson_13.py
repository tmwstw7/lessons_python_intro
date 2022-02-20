"""
Инкапсуляция Х
Наследование X
Полиморфизм X
"""

"""
public
private
protected
"""

# ДОГОВОРЕННОСТЬ МЕЖДУ РАЗРАБОТЧИКАМИ
"""
_ - что это поле должно быть private
__ - это поле должно быть protected

"""
# Класс - абстракция сущности

class A:
    x = 1  # public
    _y = 2  # private
    __z = 3  # protected

    def __z_square(self):
        print('In z_square')
        self.__z = self.__z ** 2

    def _xyz(self):
        self.__z_square()
        print('In XYZ')
        print(self.x * self._y * self.__z)


# Объект класса
# a = A()
# a._xyz()
# print(a.x)
# print(a._y)
# print(a._A__z)
# print(a.__z)


class Rectangle:

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

        self.a = 0
        self.p = 0

    def area(self):
        self.a = self.side_a * self.side_b
        print(f"Area: {self.a}")

    def perimeter(self):
        self.p = 2 * (self.side_a + self.side_b)
        print(f"Perimeter: {self.p}")


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def __add__(self, other): # Dunder method / magic method
        return Rectangle(self.side_a + other.side_a,
                         self.side_b if self.side_b > other.side_b else other.side_b)

    def __repr__(self):
        return f"Square({self.side_a})"

    def __str__(self):
        data = {'Side': self.side_a,
                'Area': self.a,
                'Perimeter': self.p}
        return f"Square. {data}"

    def area(self):
        print(f"Square area: {self.side_a ** 2}")

    def print_square(self):
        print("[ ]")


s = Square(5)
print(s)
s.area()
s.perimeter()
print(s)
s_2 = Square(7)

new_r = s + s_2
print(new_r)
# s.area()
# s.perimeter()
# s.print_square()

# Если унаследовать квадрат еще и от класса А то у него будет функционал двух классов
# print(s.x)
# print(s._y)
# s._xyz()

