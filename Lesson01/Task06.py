# Запрос от пользователя результата первого дня
first_dist = input("Введите результат первого дня: >>> ")
# Запрос от пользователя расстояния
initial_dist = input("Введите расстояние, которое необходимо достигнуть >>> ")
try:
    first_dist = int(first_dist)
    initial_dist = int(initial_dist)
    count_day = 1
    while first_dist < initial_dist:
        count_day = count_day + 1
        increase_dist = first_dist * 0.1
        first_dist = first_dist + increase_dist
    print('На', count_day, 'день спортсмен достиг результата - не менее', initial_dist, 'км')
except:
    print('Необходимо ввести расстояние числами! Введены неправильные данные! Расчет невозможен.')

