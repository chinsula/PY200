import math


class TriangleCalculator:
    """ Класс-калькулятор площадей треугольников. """

    def area(self, *args):
        """
        Метод, который считает площадь по разным формулам,
         в зависимости от количества переданных аргументов.
        """
        if len(args) == 2:
            return self.area_by_height(*args)
        if len(args) == 3:
            return self.area_by_angle(*args)

    @staticmethod
    def area_by_angle(a, b, angle):
        """ Формула площади по двум сторонам и углу между ними. """
        return 0.5 * a * b * math.sin(angle)

    @staticmethod
    def area_by_height(a, h):  # TODO сделать статическим методом
        """ Формула площади по основанию и высоте. """
        return 0.5 * a * h


if __name__ == '__main__':
    TriangleCalculator().area()  # Работаем через экземпляр
    TriangleCalculator().area_by_height(5, 10)  # Работаем через экземпляр

    print(TriangleCalculator.area(TriangleCalculator(), 10, 20))  # Работаем через класс
    print(TriangleCalculator.area_by_height(5, 10))  # Работаем через класс
