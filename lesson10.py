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


deep_list = [1, 2, 3, 4, [43, 53], [234, 53, [2, 343, 123, [3, 44]]]]


def unpack_list(_list, tmp=None):
    if not tmp:
        tmp = []
    for e in _list:
        if isinstance(e, list):
            unpack_list(e, tmp)
        else:
            tmp.append(e)
    return tmp



r = requests.post('https://httpbin.org/post', data = {'key':'value'})

import requests
import json
response = requests.get('https://api.privatbank.ua/p24api/pboffice?json&city=Днепропетровск&address=Титова')

data = response.content.decode()
json.loads(data)

"""
