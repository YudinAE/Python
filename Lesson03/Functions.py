"""======================= Модуль с функциями =======================
Функции по всем заданиям урока 3 вынесены в отдельный модуль
Каждая функция подключается непосредственно в задании с помощью инструкций from и import
====================================================================="""
# ========== Добавление абстрактного типа данных number_types: int, float, complex numbers
import number_types as number_types
# number_types = (int, float, complex)

# ========== Функция нахождения частного ==========
def user_division(dividend: number_types, divider: number_types) -> number_types:
    """
    Делит число на число
    :param dividend: Делимое
    :param divider: Делитель
    :return: Частное от деления
    """
    return dividend / divider

# ========== Функция вывода информации по пользователю (вариант 1) ==========
def print_user_data(**user_data) -> None:
    """ Распечатывает в одну строку данные пользователя
    :param user_data: данные пользователя
    """
    print(f'ИМЯ: {user_data.get("name")}; ФАМИЛИЯ: {user_data.get("surname")}; '
          f'ГОД РОЖДЕНИЯ: {user_data.get("birth_year")}; ГОРОД ПРОЖИВАНИЯ: {user_data.get("city")}; '
          f'EMAIL: {user_data.get("email")}; ТЕЛЕФОН: {user_data.get("phone")}')

# ========== Функция вывода информации по пользователю (вариант 2) ==========
def print_user_data_input(**user_data):
    """ Выводим в одну строку данные пользователя
    :param user_data: данные пользователя
    """
    return list(user_data.values())

# ========== Функция удаления минимального элемента из списка ==========
def user_sum_double_element(a, b, c):
    user_list = [a, b, c]
    user_list.remove(min(a, b, c))
    return sum(user_list)
