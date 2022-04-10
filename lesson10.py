"""
Рекурсия

def short_story():
    print("У попа была собака, он ее любил.")
    print("Она съела кусок мяса, он ее убил,")
    print("В землю закопал и надпись написал:")
    short_story()

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

Функция, которая вызывает себя рекурсивно, должна иметь план,
чтобы в конечном итоге остановиться.
Рекурсивные функции обычно следуют этому шаблону:

Есть один или несколько базовых случаев, которые решаются напрямую
без необходимости дальнейшей рекурсии.
Каждый рекурсивный вызов постепенно приближает решение к базовому случаю.

def countdown(n):
    print(n)
    if n == 0:
        return
    else:
        countdown(n - 1)

def countdown(n):
    print(n)
    if n > 0:
        countdown(n - 1)

deep_list = [1, 2, 3, 4, [43, 53], [234, 53, [2, 343, 123, [3, 44]]]]


def unpack_list(_list, tmp=None):
    tmp = tmp or []
    for e in _list:
        if isinstance(e, list):
            unpack_list(e, tmp)
        else:
            tmp.append(e)
    return tmp


flat_list=lambda d: isinstance(d, int) and [d] or sum(map(flat_list,d),[])


import sys
sys.getrecursionlimit()



from datetime import date, datetime, timedelta, time

d = date.today()
d > d.replace(month=5)
d.isoformat()
'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")
d.strftime("%d/%m/%y")
d.strftime("%A %d. %B %Y")


d = date(2005, 7, 14)
t = time(12, 30)
datetime.combine(d, t)

datetime.fromisoformat('2011-11-04 00:05:23.283')
YYYY-MM-DD[*HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]]

datetime.strptime('2011-11-04', '%Y-%m-%d')

https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes



r = requests.post('https://httpbin.org/post', data = {'key':'value'})

import requests
import json
response = requests.get('https://api.privatbank.ua/p24api/pboffice?json&city=Днепропетровск&address=Титова')

data = response.content.decode()
json.loads(data)

"""


setup_string = """
print("Recursive:")
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
"""
setup_string = """
print("Iterative:")
def factorial(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i
    return return_value
"""

setup_string = """
from functools import reduce
print("reduce():")
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])
"""
setup_string = """
from math import factorial
"""

from timeit import timeit

timeit("factorial(4)", setup=setup_string, number=10000000)
