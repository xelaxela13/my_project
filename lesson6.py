"""
Множества — это неупорядоченная коллекция уникальных элементов,
сгруппированных под одним именем. Множество может быть неоднородным — включать элементы разных типов.
Множество всегда состоит только из уникальных элементов (дубли запрещены)
в отличие от списков и кортежей в Python.
Объект set — это также коллекция уникальных хэшируемых объектов.
Объект называется хэшируемым в том случае, если его значение хэша не меняется.
Это используется в ключах словарей и элементах множеств,
ведь значения хэшей применяются в их внутренних структурах.

Чаще всего множества в Python используются для проверки на принадлежность,
удаления повторов из последовательности и выполнения математических операций,
таких как пересечение, объединение, поиск разностей и симметрических разностей.
 Изображение ниже показывает два примера множеств (алфавит и цифры),
 каждый из которых включает уникальные неизменяемые объекты.

Запрещено добавлять элементы изменяемых типов, такие как список или словарь.
s = { 1, 2, 3, [5, 6, 7, 8] }

Все, что не является изменчивым может быть хешировано.
Помимо хеш-функции, которую нужно искать, например, в классе. dir(tuple) и ищем
__hash__ метод и объект можно сравнить с другими объектами
(ему нужен метод __eq__() или __cmp__())

hash(frozenset([1,2]))
hash({1,2})

tuple_a = (1,2,3)
tuple_a.__hash__()

Список неизменяемых типов:
int, float, decimal, complex, bool, string, tuple, range, frozenset, bytes

Список изменяемых типов:
list, dict, set, bytearray, user-defined classes


Добавление одного элемента в множество Python
add().

Добавление нескольких элементов в множество
update()

Удаление элементов из множеств
remove()
discard()
pop()

Метод discard() полезен, потому что он удаляет конкретный элемент и не возвращает ошибку,
если тот не был найден во множестве.

Объединение множеств
с помощью символа | или метода union().

Пересечение множеств
с помощью символа & или метода intersection()

Разность множеств
содержащий элементы, которые есть в первом, но не втором
с помощью символа - или метода difference()
A = {1, 2, 3, 4}
B = {3,4,5,6}
C = A - B # используя символьный метод
C = A.difference(B) # используя метод difference
print(C)
# {1,2}

Симметричная разность множеств
содержащий все элементы, кроме тех, что есть в обоих
с помощью символа ^ или метода symmetric_difference()
C = A ^ B  # используя символьный метод
C = A.symmetric_difference(B)  # используя метод symmetric_difference
print(C)
# {1, 2, 5, 6}

Подмножество и надмножество
Множество B (SetB) называется подмножество A (SetA),
если все элементы SetB есть в SetA.
Проверить на подмножество в Python можно двумя способами:
с помощью символа <= или метода issubset().
Он возвращает True или False в зависимости от результата.
A = {1, 2, 3, 4, 5}
B = {2,3,4}
B <= A  # используя символьный метод
B.issubset(A) # используя метод issubset
# True

Множество A (SetA) называется надмножество B (SetB),
если все элементы SetB есть в SetA.
Проверить на надмножество в Python можно двумя способами:
с помощью символа >= или метода issuperset().
Он возвращает True или False в зависимости от результата.
A = {1, 2, 3, 4, 5}
B = {2,3,4}
A >= B  # используя символьный метод
A.issuperset(B) # используя метод issubset
# True
"""
import random

"""
Словари

Структура. Словарь состоит из пар ключ-значение, которые разделяются запятыми. 
Внутри каждой пары значение отделяется от ключа двоеточием.
Составная структура. Словарь — полезная составная структура данных, 
которая может хранить разные типы данных. По аналогии со списком ее можно называть последовательностью данных.
Нет порядка. В отличие от списков и кортежей у словарей нет определенного порядка. 
Можно представить, что пары из ключа и значения перемешаны в мешке. 
И в нем не существует первого, второго или последнего элементов — они просто случайно существуют. 
Такая структура нацелена на увеличение производительности и предполагает доступ к значению по ключу.

Cловарь, где ключи являются целыми числами:

dict_sample = {1: 'mango', 2: 'pawpaw'}

Создание словаря с ключами разных типов:

dict_sample = {'fruit': 'mango', 1: [4, 6, 8]}

Можно также создать словарь, явно вызвав метод dict():

dict_sample = dict({1:'mango', 2:'pawpaw'})
Словарь можно создать с помощью последовательности, как в примере внизу:

dict_sample = dict([(1,'mango'), (2,'pawpaw')])
Словари могут быть вложенными. Это значит, что можно создавать словари внутри существующего словаря. Например:

dict_sample = {
1: {'student1': 'Nicholas', 'student2': 'John', 'student3': 'Mercy'}, 
2: {'course1': 'Computer Science', 'course2': 'Mathematics', 'course3': 'Accounting'}
}

dict_sample = {
  "Company": "Toyota", 
  "model": "Premio", 
  "year": 2012 
} 
x = dict_sample.get("model")

Добавление элементов

x.update({})
z[] = ''

x.setdefault()
x = {
  "Company": "Toyota", 
  "model": "Premio", 
  "year": 2012 
} 

x = x.setdefault("color", "Gray") 

x.fromkeys()

Удаление элементов
del x[key]

del x 
NameError: name 'x' is not defined

x.clear()

x.pop(key)
x.popitem()
"""

text = 'В единственной строке записан текст Для каждого слова из данного текста подсчитайте сколько раз оно встречалось в этом тексте'
keys = [w.strip().lower() for w in text.split(' ')]
d = {}.fromkeys(keys, 0)

for w in keys:
    if d.get(w, None) is not None:
        d[w] += 1

print(d)

"""
Опишите как могла бы работать функция superset() используя только if else и операции над множествами.
Например: даны два множества set_1 = {1,2,3,4} set_2 = {2,3,4,5} - является ли set_1 суперменом для set_2?
"""

set_1 = {1, 2, 3, 4}
set_2 = {1, 2, 3, 4, 5}

if set_1 >= set_2:
    print(True)

"""
Сформируйте два словаря из случайных букв в качестве ключа и случайных чисел в качестве значений.
dict_1 = {'a': 1, 'b': 2, 'c': 3, ....}
dict_2 = {'z': 1, 'x': 9, 'c': 6, ....}

Сформируйте новый словарь из двух существующих:

Если в исходных словарях есть повторяющиеся ключи, выбираем среди их значений 
максимальное и присваиваем этому ключу (например, в словаре_1 есть ключ “а” со значением 5, 
и в словаре_2 есть ключ “а”, но со значением 9. Выбираем максимальное значение, 
т. е. 9, и присваиваем ключу “а” в уже новом словаре).

Если ключ не повторяется, то он просто переносится со своим значением в новый 
словарь (например, ключ “с” встретился только у одного словаря, а у других его нет. 
Следовательно, переносим в новый словарь этот ключ вместе с его значением). 
Сформированный словарь возвращаем.
"""

import string

dict_1 = {k: v for k, v in
          zip([random.choice(string.ascii_lowercase) for _ in range(10)],
              [random.randint(1, 100) for _ in range(10)])}

dict_2 = {k: v for k, v in
          zip([random.choice(string.ascii_lowercase) for _ in range(10)],
              [random.randint(1, 100) for _ in range(10)])}

dict_3 = {}

if len(dict_1) > len(dict_2):
    first = dict_1
    second = dict_2
else:
    first = dict_2
    second = dict_1

print(first)
print(second)
for k, v in first.items():
    if k in second.keys():
        v = second[k] if v < first[k] else v
    dict_3[k] = v

print(dict_3)
