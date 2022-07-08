# def password_length(func):
#     def wrapper(*args, **kwargs):
#         print('before')
#         password = kwargs.get('password')
#         if not password or len(password) < 8:
#             return False
#         result = func(*args, **kwargs)
#         if not result:
#             ...
#         print('after')
#         return result
#
#     return wrapper
#
#
# PASSWORD = {}
#
#
# @password_length
# def save_password(password: str = None, first_name: str = None) -> bool:
#     """
#     Password > 8 and contains > 1 digit and > 1 Upper case
#     @param password:
#     @param first_name:
#     @return:
#     """
#     if PASSWORD.get(first_name):
#         return False
#     PASSWORD.update({first_name: {'password': password}})
#     return True
#
#
# if __name__ == "__main__":
#     if save_password(password='1234567890', first_name="Alex"):
#         print(PASSWORD)

"""
Duck typing

Аннотации функций являются полностью необязательной информацией метаданных о типах, 
используемых пользовательскими функциями.

Аннотации хранятся в атрибуте функции __annotations__ как словарь и не влияют ни на какую другую часть функции. 
Аннотации аргументов определяются двоеточием после имени параметра, за которым 
следует выражение, оценивающее значение аннотации. 
Аннотации возвращаемых значений функции определяются литералом ->, 
за которым следует выражение, между списком параметров и двоеточием, обозначающим конец оператора def.

Для аннотаций сложных или пользовательских типов переменных необходимо использовать встроенный модуль typing.

Аннотации в функции, как для параметров, так и для возвращаемых значений, являются полностью необязательными.

Аннотации функций - не более чем способ связывания произвольных выражений Python с различными частями функции во время компиляции.

Синтаксис lambda-функций не поддерживает аннотации.

Новое в python 3.9

Например раньше, чтобы явно указать, что структура данных должна состоять только из целых чисел,
 то для этого нужно было импортировать из модуля typing:
 from typing import List, Dict
 List[int]
 Dict[str, int]

pip install mypy

Yield — это ключевое слово в Python, которое используется для возврата из функции
с сохранением состояния ее локальных переменных,
и при повторном вызове такой функции выполнение продолжается с оператора yield,
на котором ее работа была прервана. Любая функция, содержащая ключевое слово yield,
называется генератором. Можно сказать, yield — это то, что делает ее генератором.

# генерация нового списка, состоящего
# только из четных чисел
def get_even(list_of_nums) :
    for i in list_of_nums:
        if i % 2 == 0:
            yield i

# инициализация списка
list_of_nums = [1, 2, 3, 8, 15, 42]

# вывод начального списка
print ("До фильтрации в генераторе: " +  str(list_of_nums))

# вывод только четных значений из списка
print ("Только четные числа: ", end = " ")
for i in get_even(list_of_nums):
    print (i, end = " ")

# числа от 1 до 15, возведенные в куб,
# используя yield и, следовательно, генератор

# Функция ниже будет бесконечно генерировать
# последовательность чисел в третьей степени,
# начиная с 1
def next_cube():
    acc = 1

    # Бесконечный цикл
    while True:
        yield acc**3
        acc += 1 # После повторного обращения
                # исполнение продолжится отсюда

# Ниже мы запрашиваем у генератора
# и выводим ровно 15 чисел
count = 1
for num in next_cube():
    if count > 15:
        break
    print(num)
    count += 1

Преимущества yield:

Поскольку генераторы автоматически сохраняют и управляют состояниями своих локальных переменных,
программист не должен заботиться о накладных расходах, связанных с выделением и освобождением памяти.
Так как при очередном вызове генератор возобновляет свою работу,
а не начинает с самого начала, общее время выполнения сокращается.
"""

# def f(a: str, b: (list, tuple), c=None) -> None:
#     print(f.__annotations__, type(f.__annotations__))
#     return
#
#
# if __name__ == "__main__":
#     f('text', [])

from functools import wraps


def tag_decorator(tag):
    def decorator(func):
        @wraps(func)
        def wrapper(text):
            return f'<{tag}>{func(text)}</{tag}>'

        return wrapper

    return decorator


@tag_decorator(tag='div')
def f(text: str) -> str:
    return text.upper()


if __name__ == '__main__':
    print(f('text'))

"""
Написать мини программу, которая будет проверять пароль пользователя и если пароль подходит будет авторизировать пользователя:

Программа должна хранить Имена и Пароли в глобальном словаре
Должна содержать три функции:
check_password() возвращающая -> bool
authenticate() -> bool
login() принимающая минимум 2 аргумента username, password возвращающая -> bool
функция login() должна быть с декоратором в котором будет вся логика проверки check_password и authenticate
у пользователя должно быть 3 попытки после чего программа завершается и выводит сообщение "Попытки истекли!", 
при каждой не удачной попытки должно быть сообщение "У вас осталось Н попыток"
Сценарий: пользователь с консоли вводит Имя и Пароль, программа возвращает текст "Вы в системе!" или "Не правильное Имя или Пароль"
"""

USERS = {
    'Alex': '12345',
    'Bob': '54321',
    'John': 'Smith'
}


def login_decorator(func):
    @wraps(func)
    def wrapper(username, password):
        if not check_password(username, password):
            print('Не правильное Имя или Пароль')
            return False
        if not authenticate():
            return False
        return func(username, password)

    return wrapper


def check_password(username: str, password: str) -> bool:
    """
    Return True if Username exists in USERS dict and password is correct
    @param username: Username from USERS dict
    @param password: Password from USERS dict
    @return: bool
    """
    return USERS.get(username, None) == password


def authenticate() -> bool:
    """
    Function without any arguments, just for example
    @return: bool
    """
    print('Вы в системе!')
    return True


@login_decorator
def login(_username: str, _password: str) -> bool:
    """
    Just abstract function for example, always return True
    @param _username: Username from USERS dict
    @param _password: Password from USERS dict
    @return: bool
    """
    return True


if __name__ == "__main__":
    i = 3
    while i > 0:
        if login(input('Введите ваш логин:'), input('Введите ваш пароль:')):
            break
        i -= 1
        print(f'Оталось попыток: {i}' if i else 'Попытки истекли!')
