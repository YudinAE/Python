"""=====================================================================================================================
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла:
firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
====================================================================================================================="""
from json import dumps

source_file = "Task07_firm.txt"
json_file = "Task07_firm.json"

if __name__ == "__main__":
    result = [{}, {}]
    try:
        # Поток чтения файла
        with open(source_file, encoding='utf-8') as open_source_file:
            lines = open_source_file.readlines()

        for line in lines:
            name, type_of_ownership, revenue, costs = line.split()
            # Расчет прибыли компании
            result[0][name] = int(revenue) - int(costs)

        # Расчет среднего
        result[1]['average_profit'] = round(
            sum(
                result for type_of_ownership, result in result[0].items() if result > 0) / len(result[0])
        )
        # Поток записи json-файла
        with open(json_file, "w", encoding='utf-8') as open_json_file:
            open_json_file.write(dumps(result))
    except IOError as file_n_found:
        print(f'Файл не найден:\n{file_n_found}')
    except ValueError:
        print("Некорректные данные")
