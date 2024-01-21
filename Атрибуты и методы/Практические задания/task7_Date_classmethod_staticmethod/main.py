class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.__is_valid_date()

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"

    def is_leap_year(self):
        """Проверяет, является ли год високосным"""

        if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0:
            return True
        return False

    def get_max_day(self):
        """Возвращает максимальное количество дней в месяце для указанного года"""

        if self.is_leap_year():
            return self.DAY_OF_MONTH[1][self.month - 1]
        return self.DAY_OF_MONTH[0][self.month - 1]

    def __is_valid_date(self):
        """Проверяет, является ли дата корректной"""

        if not 1 <= self.month <= 12:
            raise ValueError

        if self.is_leap_year():
            days_count = self.DAY_OF_MONTH[1][self.month - 1]
        else:
            days_count = self.DAY_OF_MONTH[0][self.month - 1]

        if not 1 <= self.day <= days_count:
            raise ValueError

        return True


if __name__ == '__main__':
    date = Date(21, 2, 1999)
    print(date)
    print(date.get_max_day())
    print(date.is_leap_year())

# НЕМНОГО ЛОМАЕТСЯ ЛОГИКА РАБОТЫ С КЛАССОМ
# class Date:
#     """Класс для работы с датами"""
#     DAY_OF_MONTH = (
#         (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
#         (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
#     )
#
#     def __init__(self, day: int, month: int, year: int):
#         self.day = day
#         self.month = month
#         self.year = year
#
#         self.is_valid_date(self.day, self.month, self.year)
#
#     @staticmethod
#     def is_leap_year(year: int):
#         """Проверяет, является ли год високосным"""
#
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             return True
#         return False
#
#     def get_max_day(self, month: int, year: int):
#         """Возвращает максимальное количество дней в месяце для указанного года"""
#
#         if self.is_leap_year(year):
#             return self.DAY_OF_MONTH[1][month - 1]
#         return self.DAY_OF_MONTH[0][month - 1]
#
#     def is_valid_date(self, day: int, month: int, year: int):
#         """Проверяет, является ли дата корректной"""
#
#         if not 1 <= month <= 12:
#             return False
#
#         if self.is_leap_year(year):
#             days_count = self.DAY_OF_MONTH[1][month - 1]
#         else:
#             days_count = self.DAY_OF_MONTH[0][month - 1]
#
#         if not 1 <= day <= days_count:
#             return False
#
#         return True
#
#
#
# if __name__ == '__main__':
#     date = Date(29, 1, 1999)
#     date.get_max_day(1, 1999)

# ВСЕ СТАТИК МЕТОДЫ
#
# class Date:
#     """Класс для работы с датами"""
#
#     @staticmethod
#     def is_leap_year(year: int):
#         """Проверяет, является ли год високосным"""
#
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             return True
#         return False
#
#     @staticmethod
#     def get_max_day(month: int, year: int):
#         """Возвращает максимальное количество дней в месяце для указанного года"""
#
#         DAY_OF_MONTH = (
#             (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
#             (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
#         )
#
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             return DAY_OF_MONTH[1][month - 1]
#         return DAY_OF_MONTH[0][month - 1]
#
#     @staticmethod
#     def is_valid_date(day: int, month: int, year: int):
#         """Проверяет, является ли дата корректной"""
#
#         if not 1 <= month <= 12:
#             return False
#
#         DAY_OF_MONTH = (
#             (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
#             (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
#         )
#
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             days_count = DAY_OF_MONTH[1][month - 1]
#         else:
#             days_count = DAY_OF_MONTH[0][month - 1]
#
#         if not 1 <= day <= days_count:
#             return False
#
#         return True
#
#
# if __name__ == '__main__':
#     print(Date.is_leap_year(2024))
#     print(Date.is_leap_year(2023))
#
#     print(Date.get_max_day(2, 2024))
#     print(Date.get_max_day(2, 2023))
#
#     print(Date.is_valid_date(28, 2, 2024))
#     print(Date.is_valid_date(29, 2, 2024))
#     print(Date.is_valid_date(0, 2, 2024))
#     print(Date.is_valid_date(29, 1, 2024))
#     print(Date.is_valid_date(29, 0, 2024))
#     print(Date.is_valid_date(29, 12, 2024))
#     print(Date.is_valid_date(29, 13, 2024))
#
#     # date = Date(29, 1, 1999)
#     # date.get_max_day(1, 1999)


# ФУНКЦИОНАЛЬНЫЙ ПОДХОД
#
# DAY_OF_MONTH = (
#     (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
#     (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
# )
#
#
# def is_leap_year(year: int):
#     """Проверяет, является ли год високосным"""
#
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         return True
#     return False
#
#
# def get_max_day(month: int, year: int):
#     """Возвращает максимальное количество дней в месяце для указанного года"""
#
#     if is_leap_year(year):
#         return DAY_OF_MONTH[1][month - 1]
#     return DAY_OF_MONTH[0][month - 1]
#
#
# def is_valid_date(day: int, month: int, year: int):
#     """Проверяет, является ли дата корректной"""
#
#     if not 1 <= month <= 12:
#         return False
#
#     if is_leap_year(year):
#         days_count = DAY_OF_MONTH[1][month - 1]
#     else:
#         days_count = DAY_OF_MONTH[0][month - 1]
#
#     if not 1 <= day <= days_count:
#         return False
#
#     return True


# if __name__ == '__main__':
#     print(is_leap_year(2024))
#     print(is_leap_year(2023))
#
#     print(get_max_day(2, 2024))
#     print(get_max_day(2, 2023))
#
#     print(is_valid_date(28, 2, 2024))
#     print(is_valid_date(29, 2, 2024))
#     print(is_valid_date(0, 2, 2024))
#     print(is_valid_date(29, 1, 2024))
#     print(is_valid_date(29, 0, 2024))
#     print(is_valid_date(29, 12, 2024))
#     print(is_valid_date(29, 13, 2024))

# date = Date(29, 1, 1999)
