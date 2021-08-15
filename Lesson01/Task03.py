# Запрос от пользователя ввода числа
Number = input("Введите число >>> ")
# Конструкция try-except для выполнения инструкции с перехватом исключения
try:
    # Временная переменная для перевода введенного числа в int
    temp_number = int(Number)
    # Двойная склейка введенного пользователя числа c преобразованием в int
    Number_multiplication_x2 = int('{0}{1}'.format(temp_number, temp_number))
    # Тройная склейка введенного пользователя числа c преобразованием в int
    # Number_multiplication_x3 = int('{0}{1}{2}'.format(temp_number, temp_number, temp_number))
    Number_multiplication_x3 = int('{0}{1}'.format(temp_number, Number_multiplication_x2))
    # Сложение
    Number_total = temp_number + Number_multiplication_x2 + Number_multiplication_x3
    # Вывод
    print(Number_total)
    # Перехват исключения, если введено не целое число
except:
    # Вывести предупреждение
    print('Это не число!')
