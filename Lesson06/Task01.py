"""====================================================================================================================
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы:
        красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
===================================================================================================================="""
import time

class TrafficLight():
    __color: str = ['Red', 'Yellow', 'Green']
    # Проверка нарушения порядка режима работы светофора
    # __color: str = ['Yellow', 'Red', 'Green']

    def running(self):
        # Длительность работы
        time_light: int = [7, 2, 8]
        if TrafficLight.__color[0] == 'Red' and TrafficLight.__color[1] == 'Yellow' and TrafficLight.__color[
            2] == 'Green':
            i = 0
            while i < 3:
                print(TrafficLight.__color[i])
                if i == 0:
                    print(f"Внимание! Через {time_light[i]} сек. будет выполнено переключение режима. Следующий режим: {TrafficLight.__color[i + 1]}.")
                    time.sleep(time_light[i])
                elif i == 1:
                    print(f"Внимание! Через {time_light[i]} сек. будет выполнено переключение режима. Следующий режим: {TrafficLight.__color[i + 1]}.")
                    time.sleep(time_light[i])
                elif i == 2:
                    print(f"Длительность режима {TrafficLight.__color[i]} составляет {time_light[i]} сек.")
                    time.sleep(time_light[i])
                    print(f"Полный цикл работы светофора завершен")
                i += 1
        else:
            print("Порядок переключения режимов светофора нарушен!")

if __name__ == '__main__':
    print(f'Светофор 1 включен')
    trafficlight = TrafficLight()
    trafficlight.running()
