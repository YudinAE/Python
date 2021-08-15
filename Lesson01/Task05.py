# Запрос от пользователя выручки и издержек
revenue = input("Введите выручку фирмы >>> ")  # выручку вводит пользователь
costs = input("Введите издержки фирмы >>> ")  # издержки вводит пользователь
# Определение результата работы фирмы
try:
    revenue = int(revenue)
    costs = int(costs)
    if revenue > costs:
        # Расчет прибыли
        profit = revenue - costs
        print('Фирма добилась прибыли:', profit)
        # Расчет рентабельность как соотношение прибыли к выручке
        profitability = (revenue - costs) / revenue
        # Численность сотрудников вводит пользователь
        number_of_staff = input("Введите численность сотрудников фирмы>>> ")
        try:
            number_of_staff=int(number_of_staff)
            profit_per_employee = profit / number_of_staff
            print('Рентабельность фирмы составила:', profitability)
            print('Прибыль фирмы в расчете на одного сотрудника составляет:', profit_per_employee)
        except:
            print('Количество сотрудников должно быть числом! Введены неправильные данные! Расчет невозможен.')
    if costs > revenue:
        # Расчет убытка
        loss = costs - revenue
        print('Убыток прибыли составил:', loss)
except:
    print('Выручка и издержки должны быть числом! Введены неправильные данные')
