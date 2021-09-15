"""====================================================================================================================
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
    name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
    оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
===================================================================================================================="""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        # Наследование
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        """
        Метод получения полного имени сотрудника
        :return: имя сотрудника
        """
        return self.name + ' ' + self.surname

    def get_total_income(self):

        """
        Методы получения дохода с учетом премии
        :return: доход сотрудника
        """
        return self._income.get('wage') + self._income.get('bonus')


employee = Position('Ivan', 'Ivanov', 'Developer', 100000, 62000)
print(f'Сотрудник: {employee.get_full_name()}')
print(f'Должность: {employee.position}')
print(f'Доход: {employee.get_total_income()}')
