class Case:
    """
    Класс "Дело об административном правонарушении"
        :param date_ - дата возбуждения дела
        :param article - статья КоАП РФ
        :param result - исполнено - True или прекращено - False

        Примеры:
        case = Case("01.11.2023", "12.34ч1", True)  # инициализация экземпляра класса
    """

    def __init__(self, date_: str, article: str, result: bool):
        self.date_ = date_
        self.article = article
        self.result = result

        if not isinstance(date_, str):
            raise TypeError(f"Дата возбуждения не может быть типа {type(date_)}")

        if not isinstance(article, str):
            raise TypeError(f"Статья не может быть типа {type(article)}")

    def extend_the_case(self, prolongation):  # перенос сроков рассмотрения
        pass

    def resume_the_case(self, cancellation):  # переквалификация статьи КОАП
        pass


class Auto:
    """
     Класс "Автомобили ГИБДД"
         :param number - госномер
         :param year_of_release - дата выпуска
         :param serviceability - исправность

        Примеры:
        auto1 = Auto("T001CO86", 2023, True)  # инициализация экземпляра класса
     """

    def __init__(self, number: str, year_of_release: int, serviceability: bool):
        self.number = number
        self.year_of_release = year_of_release
        self.serviceability = serviceability

        if not isinstance(number, str):
            raise TypeError(f"Госномер не может быть типа {type(number)}")

        if not isinstance(year_of_release, int):
            raise TypeError(f"Год выпуска не может быть типа {type(year_of_release)}")

    def set_it_car_service(self, repair):  # нахождение в ремонте
        pass

    def changing_number(self, result):  # изменение госномера, перерегистрация
        pass


class Employee:
    """
         Класс "сотрудники Госавтоинспекции"
             :param number - ФИО
             :param year_of_release - стаж в должности
             :param serviceability - должность

         Примеры:
         employee1 = Employee("Иванов И.И.", 2, "инспектор")  # инициализация экземпляра класса
         """

    def __init__(self, name: str, experience: int, post: str):
        self.name = name
        self.experience = experience
        self.post = post

        if not isinstance(name, str):
            raise TypeError(f"Имя сотрудника не может быть типа {type(name)}")

        if not isinstance(experience, int):
            raise TypeError(f"Стаж работы не может быть типа {type(experience)}")

    def change_of_position(self, post):  # изменение должности
        pass

    def change_of_experience(self, experience):  # изменение стажа в должности
        pass


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
