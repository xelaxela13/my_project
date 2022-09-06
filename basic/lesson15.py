"""

Переменные экземпляра класса предназначены для данных, уникальных для каждого
экземпляра класса, а переменные класса (атрибуты данных класса) -
для атрибутов и методов, общих для всех экземпляров класса.

Python вызывает специальный метод __init__(), который называют конструктором класса,
 каждый раз при создании нового экземпляра класса.
Вместо использования привычной точечной нотации для доступа к атрибутам можно
использовать встроенные функции:

getattr(obj, name [, default]) - для доступа к атрибуту name объекта класса obj.
hasattr(obj, name) - проверить, есть ли в классе obj атрибут name.
setattr(obj, name, value) - задать атрибут name со значением value.
Если атрибут не существует, он будет создан.
delattr(obj, name) - удалить атрибут name из объекта класса obj.
Где хранятся атрибуты класса и экземпляра класса?

Python не был бы Python без четко определенного и настраиваемого поведения атрибутов.
Атрибуты в Python хранятся в магическом методе с именем __dict__.
Получить доступ к нему можно следующим образом:

class A:
    public = 'public class A'
    _protected = 'protected class A'
    __private = 'private class A'

    def get_self_variables(self):
        return self.public, self._protected

    def get_self_private_variables(self):
        try:
            return self.__private
        except AttributeError as err:
            return err


class B(A):
    def get_parent_variables(self):
        return self.public, self._protected

    def get_parent_private_variables(self):
        try:
            return self.__private
        except AttributeError as err:
            return err


if __name__ == '__main__':
    a = A()
    b = B()
    print(a.get_self_variables(), a.get_self_private_variables())
    print(b.get_parent_variables(), b.get_parent_private_variables())


class T1:
    def __init__(self):
        self.n = 10

    def total(self, a):
        return self.n + int(a)


class T2(T1):
    def __init__(self):
        super().__init__()
        self.string = 'Hi'

    def total(self, a):
        return len(self.string + str(a))


super().method(*args, **kwargs)

raise NotImplementedError

Дескриптор это атрибут объекта со “связанным поведением”, то есть такой атрибут,
при доступе к которому его поведение переопределяется методом протокола дескриптора.
Эти методы  __get__, __set__ и __delete__.
Если хотя бы один из этих методов определен в объекте , то можно сказать что этот метод дескриптор.

import os

class DirectorySize:

    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))

class Directory:

    size = DirectorySize()              # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname          # Regular instance attribute

s = Directory('songs')
g = Directory('games')
s.size                              # The songs directory has twenty files
20
g.size                              # The games directory has three files
3
os.remove('games/chess')            # Delete a game
g.size                              # File count is automatically updated
2


Зачем использовать метаклассы?

"Метаклассы – это магия, о которой 99% пользователей не стоит даже задумываться.
Если вам интересно, нужны ли они вам – тогда точно нет.
Люди, которым они на самом деле нужны, знают, зачем, и что с ними делать."

~ Гуру Python Tim Peters


class SingletonMeta(type):
    '''
    В Python класс Одиночка можно реализовать по-разному. Возможные способы
    включают себя базовый класс, декоратор, метакласс. Мы воспользуемся
    метаклассом, поскольку он лучше всего подходит для этой цели.
    '''

    _instances = {}

    def __call__(cls, *args, **kwargs):
        '''
        Данная реализация не учитывает возможное изменение передаваемых
        аргументов в `__init__`.
        '''
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        '''
        Наконец, любой одиночка должен содержать некоторую бизнес-логику,
        которая может быть выполнена на его экземпляре.
        '''
        ...


    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = super().__new__(cls)
        return cls.__instance


class BaseHandlerMeta(type):

    def __new__(mcs, name, bases, dic):
        for method in METHODS.values():
            if method not in dic:
                dic[method] = lambda *args, **kwargs: ...
        return super().__new__(mcs, name, bases, dic)
"""

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'X = {self.x}, Y = {self.y}'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ge__(self, other):
        return self.x >= other.x, self.y >= other.y

    def __gt__(self, other):
        return self.x > other.x, self.y > other.y

    def distance(self, point):
        return ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) * .5


class Context:

    def __init__(self, filename, params='r'):
        self.filename = filename
        self.params = params
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.params)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file is not None:
            self.file.close()

open_file = Context

if __name__ == '__main__':
    a = Point(3, 5)
    b = Point(7, 2)
    print(a == b)
    print(a > b)
    print(a.distance(b))
    with open_file('lesson3.py') as f:
        print(f.read())
