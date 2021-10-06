"""================================================================================================================
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
умножение созданных экземпляров. Проверьте корректность полученного результата.
====================================================================================================================="""
class Complex:
    def __init__(self, real, mnim):
        self.z = complex(real, mnim)

    def __str__(self):
        return str(f'{self.z.real} + {self.z.imag} j')


    def __mul__(self, other):
        r = self.z.real * other.z.real - self.z.imag * other.z.imag
        m = self.z.imag * other.z.real + self.z.real * other.z.imag
        return Complex(r,m)

    def __add__(self, other):
        return Complex((self.z.real + other.z.real),(self.z.imag + other.z.imag))

a = Complex(2,2)
b = Complex(3,4)
print(a + b)
print(a * b)