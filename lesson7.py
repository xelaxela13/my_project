"""
Функции

Глобальные
Локальные
Лямбда
Методы

Синтаксис создания функции (глобальной или локальной) имеет сле􏰀 дующий вид:
def function_name(parameters):
    body

DOCSTRING

def name():
    pass
"""

"""
замыкание
локальная
глобальная
builtin
"""


def main(x, y, z=2):
    """
    Description text
    @param x: int
    @param y: int
    @param z: int
    @return: int
    >>> main(2, 2)
    8
    >>> main(2, 3)
    12
    >>> main('text', 4)
    'texttexttexttexttexttexttexttext'
    """
    return x * y * z


def checkio(number: int) -> int:
    """
    Дано положительное целое число. Вам необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
    Для примера: Дано число 123405. Результат будет: 1*2*3*4*5=120 (не забудьте исключить нули).
    @param number:
    @return:
    """
    r = 1
    for i in str(number):
        if int(i) != 0:
            r = r * int(i)
    return r


def square(a):
    """
    Написать функцию square, принимающую 1 аргумент — сторону квадрата,
    и возвращающую 3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
    @param a:
    @return:
    """
    return 4 * a, a ** 2, round(2 ** 0.5 * a, 2)


def arithmetic(first, second, operand):
    """
    Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа,
    третий - операция, которая должна быть произведена над ними.
    Функция должна вернуть результат вычислений зависящий от третьего аргумент +,
    сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе).
    В остальных случаях вернуть строку "Неизвестная операция".
    @return:
    """
    return {'+': first + second,
            '-': first - second,
            '/': first / second,
            '*': first * second}.get(operand, "Неизвестная операция")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1

    assert square(2) == (8, 4, 2.83)
    assert square(3) == (12, 9, 4.24)

    assert arithmetic(8, 4, '+') == 10
    assert arithmetic(8, 4, '-') == 4
    assert arithmetic(8, 4, '/') == 2.0
    assert arithmetic(8, 4, '*') == 32
