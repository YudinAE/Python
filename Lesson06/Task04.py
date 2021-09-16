"""====================================================================================================================
4.Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты:
        speed, color, name, is_police (булево).
А также методы:
        go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов:
        TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
===================================================================================================================="""


class Car:
    # ============ Базовый класс автомобиля ============
    def __init__(
            self,
            name: str,
            color: str,
            is_police: bool = False
    ):
        """
        :param color: Цвет автомобиля
        :param name: Модель автомобиля
        :param is_police: Флаг, показывающий является ли машина полицейской
        ============ ============ ============ ============ """
        self._max_granted_speed = None
        self.color = color
        self.name = name
        self.is_police = True if is_police else False
        self.speed = 0
        self._direction = ''

    def go(self, speed: float):
        """ Метод начинает движение автомобиля с заданной скоростью
        :param speed: Скорость движения
        """
        try:
            self.speed = float(speed)
        except ValueError:
            print(f"Движение не начато.")
            pass

    def stop(self):
        """ Метод останавливает автомобиль """
        self.speed = 0

    def turn(self, direction: str):
        """ Задает поворот авто в движении
        :param direction: направление поворота ('left', 'right')
        """
        if direction not in ('left', 'right'):
            print(
                f"Некорректное направление поворота - {direction}. Поворачивать можно в двух направлениях: left, right")
            return

        if not self.speed:
            print(f"Повернуть без движения невозможно. Начните движения для маневра")
            return

        self._direction = direction

    def show_speed(self):
        """ Показать текущую скорость """
        if self.speed == 0:
            print(f'Автомобиль не двигается')
        else:
            print(f'Текущая скорость составляет {self.speed} km/h')

        # Проверяем, есть ли ограничения по скорости у автомобиля с помощью функции hasattr
        # Если ограничения есть - определяем, какое превышение при текущей скорости
        if (hasattr(self, '_max_granted_speed')
                and self._max_granted_speed
                and self.speed > self._max_granted_speed):
            print(f'Внимание! Сбавьте скорость! Скорость превышена на {self.speed - self._max_granted_speed} km/h. '
                  f'Ограничение составляет {self._max_granted_speed} km/h')

        # Использование декоратора <property> для превращение метода direction в свойства

    # Получения доступа к методу с помощью точечной нотации
    @property
    def direction(self):
        """  ======== Метод,показывающий направление поворота автомобиля  ========"""
        return self._direction


class TownCar(Car):
    """ ======== Класс городских автомобилей  ========"""
    # Ограничение скорости для данного класса
    _max_granted_speed = 60


class SportCar(Car):
    """  ======== Класс спортивного автомобиля  ========"""
    pass


class WorkCar(Car):
    """  ========Класс рабочего автомобиля  ======== """
    #  Ограничения скорости для данного класса
    _max_granted_speed = 40


class PoliceCar(Car):
    """  ======== Класс полицейского авто ======== """

    def __init__(self, *param):
        """
        :param param: Параметры автомобиля
        """
        # Наследование с базового класcа
        super().__init__(*param, is_police=True)


if __name__ == '__main__':
    cars = {
        ("Volkswagen Golf", "White"): TownCar,
        ("Bugati", "Red"): SportCar,
        ("Kamaz", "Orange"): WorkCar,
        ("Ford Focus", "White"): PoliceCar,
    }

    for car_name, car_colors in cars.items():
        car = car_colors(*car_name)
        print(' ========  Параметры автомобиля ========')
        print(f"Наименование автомобиля: '{car.name}'")
        print(f"Цвет автомобиля: '{car.color}'")
        print(f"Автомобиль полицейский '{car.is_police}'")
        print(f"Скорость автомобиля: '{car.speed}'")
        print(f"Направление автомобиля: '{car.direction}'")
        print(f"Текущая скорость автомобиля:  '{car.show_speed()}'")
        print(f'============ Начинаем движение на автомобиле {car.name} ========= ')
        car.turn('left')
        car.turn('ЛЕВО')
        car.go('ПОЕХАЛИ')
        print("Скорость движения автомобиля", car.speed)
        # Начинаем движения со скоростью 70 km/h c с дальнейшим изменение скорости объекта
        car.go(1)
        # Проверяем текущую скорость после начала движения
        car.show_speed()
        car.go(8)
        car.show_speed()
        car.go(12)
        car.show_speed()
        car.go(25)
        car.show_speed()
        car.go(60)
        car.show_speed()
        car.go(120)
        car.show_speed()
        car.go(30)
        car.show_speed()
        car.turn('left')
        print(f"Автомобиль повернул - '{car.direction}'")
        car.turn('right')
        car.go(70)
        car.show_speed()
        car.go(30)
        car.show_speed()
        print(f"Автомобиль повернул - '{car.direction}'")
        car.stop()
        car.show_speed()
        print(f'============ Движение на автомобиле {car.name} завершено. =========')
