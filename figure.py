from abc import ABC, abstractmethod
from math import sqrt


class Figure(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calc_area(self):
        pass

    @abstractmethod
    def calc_perimetr(self):
        pass


class InvalidTriangleError(Exception):
    pass


class InvalidSquareError(Exception):
    pass


class Triangle(Figure):
    def __init__(self, a, b, c):
        if not self._is_valid_triangle(a, b, c):
            raise InvalidTriangleError("Invalid triangle sides")
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def _is_valid_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def calc_area(self):
        p = self.calc_perimetr() / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def calc_perimetr(self):
        return self.a + self.b + self.c


class Square(Figure):
    def __init__(self, a):
        if 0 < a:
            self.a = a
            return
        raise InvalidSquareError("Invalid square sides")

    def calc_area(self):
        return self.a ** 2

    def calc_perimetr(self):
        return 4 * self.a
