class Case:
    def __init__(self, date_: str, article: str, result: bool):
        """
        Класс "Дело об административном правонарушении"
        :param date_: дата возбуждения дела
        :param article: статья КоАП РФ, по которой возбуждено
        :param result: результат рассмотрения дела: True - исполнено,
         прекращено - False
        Примеры:
        >>> case = Case("01.11.2023", "12.34ч1", True)  # инициализация экземпляра класса
        """

        if not isinstance(date_, str):
            raise TypeError(f"Дата возбуждения не может быть типа {type(date_)}")
        self.date_ = date_

        if not isinstance(article, str):
            raise TypeError(f"Статья не может быть типа {type(article)}")
        self.article = article

        if not isinstance(result, bool):
            raise TypeError(f"Результат рассмотрения не может быть типа {type(result)}")
        self.result = result

    def extend_the_case(self, prolongation):  # перенос сроков рассмотрения
        pass

    def resume_the_case(self, cancellation):  # переквалификация статьи КОАП
        pass


class CarPolice:
    def __init__(self, number: str, year_of_release: int, serviceability: bool):
        """
        Класс "Автомобили полиции"
        :param number: государственный регистрационный знак
        :param year_of_release: дата выпуска транспортного средства
        :param serviceability: исправность: True - исправен,
        False - неисправен
        Примеры:
        >>> auto1 = CarPolice("T001CO86", 2023, True)  # инициализация экземпляра класса
        """

        if not isinstance(number, str):
            raise TypeError(f"Госномер не может быть типа {type(number)}")
        self.number = number

        if not isinstance(year_of_release, int):
            raise TypeError(f"Год выпуска не может быть типа {type(year_of_release)}")
        self.year_of_release = year_of_release

        if not isinstance(serviceability, bool):
            raise TypeError(f"Исправность не может быть типа {type(serviceability)}")
        self.serviceability = serviceability


def change_serviceability(self, status):  # нахождение в ремонте
    self.serviceability = status


def changing_number(self, new_number):  # изменение госномера, перерегистрация
    pass


class Employee:
    def __init__(self, name: str, date_of_admission: int, post: str):
        """
        Класс "сотрудники полиции"
        :param name: Фамилия, инициалы сотрудника
        :param date_of_admission: дата трудоустройства
        :param post: занимаемая должность
        """

        if not isinstance(name, str):
            raise TypeError(f"Имя сотрудника не может быть типа {type(name)}")
        self.name = name

        if not isinstance(date_of_admission, int):
            raise TypeError(f"Дата трудоустройства не может быть типа {type(date_of_admission)}")
        self.experience = date_of_admission

        if not isinstance(post, int):
            raise TypeError(f"Должность не может быть типа {type(post)}")
        self.post = post

    def change_of_position(self, new_post):  # изменение должности
        pass

    def get_experience(self, experience):  # стаж службы
        pass


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
