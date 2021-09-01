"""======================= Модуль с функциями =======================
Функции по всем заданиям урока 3 вынесены в отдельный модуль
Каждая функция подключается непосредственно в задании с помощью инструкций from и import
====================================================================="""
# Добавление абстрактного типа данных number_types: int, float, complex numbers
import number_types as number_types
# number_types = (int, float, complex)


def user_division(dividend: number_types, divider: number_types) -> number_types:
    """
    Делит число на число
    :param dividend: Делимое
    :param divider: Делитель
    :return: Частное от деления
    """
    return dividend / divider
