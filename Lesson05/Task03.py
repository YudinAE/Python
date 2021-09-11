"""=====================================================================================================================
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
====================================================================================================================="""
import sys

MINIMAL_SALARY = 20000
# Создание наименование файла
FILENAME = "Task03.txt"

if __name__ == "__main__":
    print(f'========== Задание 3 ===========')
    try:
        with open(FILENAME, encoding='utf-8') as user_file:
            employees = user_file.readlines()
    except IOError as file_n_found:
        print(file_n_found)
        sys.exit(1)

    summ_salary = 0
    print(f'Фамилии сотрудников, у которых оклад менее 20 тыс.:')
    for employee in employees:
        name, salary = employee.split()
        try:
            salary = float(salary)
        except ValueError:
            continue

        summ_salary += salary
        if salary < MINIMAL_SALARY:
            print(name)
    print('Средняя величина дохода сотрудников составляет: ', round(summ_salary / len(employees), 2))
