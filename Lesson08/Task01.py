"""====================================================================================================================
 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода:
    Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
    Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
===================================================================================================================="""
from datetime import datetime

class Data:

    def __init__(self, str):
        self.str = str
        pass

    def __str__(self):
        return str(self.str)

    @classmethod
    def to_int(cls, str):
        dline = datetime.strptime(str, "%d-%m-%Y")
        d = dline.day
        m = dline.month
        y = dline.year
        cls.d = d
        cls.m = m
        cls.y = y
        return d, m, y

    @staticmethod
    def to_valid(param1, param2, param3):
        if (param1 in range(1,31)) and (param2 in range(1,12)):
            return True
        else:
            return False

s = "06-10-2021"
dat = Data(s)

print('Дата >>>', dat)
print('Полуенные значения даты, месяца, года с преобразованием к типу int >>> ', dat.to_int(s))
print('Валидация даты >>>', dat.d)
print('Валидация месяца >>>', dat.m)
print('Валидация года >>>', dat.y)

x,y,z = dat.to_int(s)
print('Валидация значений даты >>> ',x,y,z)
print('Проверка валидации >>>', dat.to_valid(x,y,z))
