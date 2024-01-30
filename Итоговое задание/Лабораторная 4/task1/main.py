from datetime import datetime


class Car:
    """
    Базовый класс автомобиля
    """

    CAR_LIST = ["Acura", "Alfa romeo", "Aston martin", "Audi", "Bentley", "Bmw", "Brilliance", "Bugatti", "Buick",
                "Byd", "Cadillac", "Changan", "Chery", "Chevrolet", "Chrysler", "Citroen", "Dacia", "Daewoo",
                "Daihatsu", "Datsun", "Dodge", "Dongfeng", "Exeed", "Faw", "Ferrari", "Fiat", "Ford", "Gac", "Geely",
                "Genesis", "Gmc", "Great wall", "Haima", "Haval", "Honda", "Hongqi", "Hummer", "Hyundai", "Infiniti",
                "Isuzu", "Jac", "Jaguar", "Jetour", "Jeep", "Kia", "Lamborghini", "Lancia", "Land rover", "Lexus",
                "Lixiang", "Lifan", "Lincoln", "Lynk & co", "Lotus", "Marussia", "Maserati", "Maybach", "Mazda",
                "Mclaren", "Mercedes", "Mini", "Mitsubishi", "Nissan", "Omoda", "Opel", "Peugeot", "Polestar",
                "Pontiac", "Porsche", "Ravon", "Renault", "Rolls-royce", "Rover", "Saab", "Seat", "Skoda", "Smart",
                "Ssangyong", "Subaru", "Suzuki", "Tagaz", "Tank", "Tesla", "Toyota", "Volkswagen", "Voyah", "Volvo",
                "Zeekr", "Zotye", "Ваз", "Газ", "Заз", "Москвич", "Москвич 3", "Мотоцикл", "Уаз", "Leapmotor", "Jaecoo",
                "Vortex"]

    def __init__(self, manufacturer: str, year_release: int, engine_power: float):
        """
        Инициализируем атрибуты базового класса "Автомобиль"
        :param manufacturer: фирма-изготовитель
        :param year_release: год выпуска
        :param engine_power: мощность двигателя
        """
        # self.is_valid_data(manufacturer, year_release, engine_power)
        self.manufacturer = manufacturer
        self.year_release = year_release
        self.engine_power = engine_power

    # def is_valid_data(self):
    #     for self.manufacturer in self.CAR_LIST:
    #         if self.manufacturer:
    #             return True
    #         raise ValueError("Такой производитель отсутствует")
    #
    #     if 1950 <= self.year_release <= datetime.year:
    #         return True
    #     else:
    #         raise ValueError("Некорректный год выпуска")

    def __str__(self):
        return f"Автомобиль: {self.manufacturer}, год выпуска: {self.year_release} год, " \
               f"мощность двигателя: {self.engine_power} л.с."

    def __repr__(self):
        return f"{self.__class__.__name__}" \
               f"(manufacturer={self.manufacturer!r}, " \
               f"year_release={self.year_release!r}, " \
               f"engine_power={self.engine_power!r})"


class CarLittle(Car):
    """
    Класс легковой автомобиль (маленький)
    """

    def __init__(self, manufacturer: str, year_release: int, engine_power: float,  body_type: str):
        """
        Инициализируем атрибуты
        :param manufacturer: фирма-изготовитель
        :param year_release: год выпуска
        :param engine_power: мощность двигателя
        :param body_type: тип кузова
        """
        super().__init__(manufacturer, year_release, engine_power)
        self.body_type = body_type

    def __repr__(self):
        """
        Перезагружаем магический метод __repr__,
        ввиду добавления нового атрибута (body_type: тип кузова)
        в дочернем классе
        :return: официальное строковое представление объекта,
        который подается в конструктор
        """
        return f"{self.__class__.__name__}" \
               f"(manufacturer={self.manufacturer!r}, " \
               f"year_release={self.year_release!r}, " \
               f"engine_power={self.engine_power!r}, " \
               f"body_type={self.body_type})"


class CarBig(Car):
    """
    Класс грузовой автомобиль (большой)
    """

    def __init__(self, manufacturer: str, year_release: int, engine_power: float, lifting_capacity: float):
        """
        Инициализируем атрибуты
        :param manufacturer: фирма-изготовитель
        :param year_release: год выпуска
        :param engine_power: мощность двигателя
        :param lifting_capacity: грузоподъемность
        """
        super().__init__(manufacturer, year_release, engine_power)
        self.lifting_capacity = lifting_capacity

    def __repr__(self):
        """
        Перезагружаем магический метод __repr__,
        ввиду добавления нового атрибута
        (lifting_capacity: грузоподъемность) в дочернем классе
        :return: официальное строковое представление объекта,
        который подается в конструктор
        """
        return f"{self.__class__.__name__}" \
               f"(manufacturer={self.manufacturer!r}, " \
               f"year_release={self.year_release!r}, " \
               f"engine_power={self.engine_power!r}, " \
               f"lifting_capacity={self.lifting_capacity})"


if __name__ == "__main__":
    car_little = CarLittle("ВАЗ", 2023, 90, "седан")
    car_big = CarBig("КАМАЗ", 1984, 435.5, 10.4)
    print(car_little)
    print(car_little.__repr__())
    print(car_big)
    print(car_big.__repr__())