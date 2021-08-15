# Запрос от пользователя ввода числа
positive_integer = input("Введите целое положительное число >>> ")
# Конструкция try-except для выполнения инструкции с перехватом исключения
try:
    # Временная переменная для перевода введенного числа в int
    temp_integer = int(positive_integer)
    big_number = temp_integer % 10
    remains = temp_integer // 10
   while remains > 0:
        if remains % 10 > big_number:
            big_number = remains % 10
        remains = remains // 10
    print(big_number)
except:
    print('Это не число!')

# Через преобразование введенного числа в список и нахождения максимального значения в списке
positive_integer = input("Введите целое положительное число еще раз>>> ")
try:
    # Временная переменная для перевода введенного числа в int
    temp_integer = int(positive_integer)
    # Преобразование введенного значения в список
    Int_to_list = list(positive_integer)
    # Вывод максимальногоо элемента списка
    print(max(Int_to_list))
except:
    print('Это не число!')
