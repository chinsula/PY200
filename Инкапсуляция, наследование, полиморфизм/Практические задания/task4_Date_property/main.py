class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.is_valid_date(day, month, year)
        self._day = day
        self._month = month
        self._year = year

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Проверяет, является ли год високосным"""
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
        return False

    def get_max_day(self) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if self.is_leap_year(self._year):
            days_count = self.DAY_OF_MONTH[1][self._month - 1]
        else:
            days_count = self.DAY_OF_MONTH[0][self._month - 1]
        return days_count

    def is_valid_date(self, day: int, month: int, year: int) -> None:
        """Проверяет, является ли дата корректной"""
        if not 1 <= month <= 12:
            raise ValueError

        if self.is_leap_year(year):
            days_count = self.DAY_OF_MONTH[1][month - 1]
        else:
            days_count = self.DAY_OF_MONTH[0][month - 1]

        if not 1 <= day <= days_count:
            raise ValueError

        return True

    def _get_day(self):
        return self._day

    def _set_day(self, value):
        if self.is_valid_date(value, self._month, self._year):
            self._day = value

    @property
    def days(self):
        return self._get_day()

    @days.setter
    def days(self, value):
        self._set._day(value)

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        if self.is_valid_date(self._day, value, self._year):
            self._month = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if self.is_valid_date(self._day, self._year, value):
            self._year = value


if __name__ == '__main__':
    date = Date(15, 12, 2021)
    print(date.month)
    date.month = 17
