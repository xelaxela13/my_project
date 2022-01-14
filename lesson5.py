import random

"""
В Python есть несколько методов для удаления элементов из списка: remove(), pop() и clear().
Помимо них также существует ключевое слово del.
******************************************************************************
Метод remove() — это встроенный метод, который удаляет первый совпадающий элемент из списка.

Синтаксис: list.remove(element).

Передается элемент, который нужно удалить из списка.

Метод не возвращает значений.
Как использовать:

Если в списке есть повторяющиеся элементы, первый совпадающий будет удален.
Если элемента нет, будет брошена ошибка с сообщением о том, что элемент не найден.
Метод не возвращает значений.
В качестве аргумента нужно передать валидное значение.
******************************************************************************
Метод pop()

Этот метод удаляет элемент на основе переданного индекса.

Синтаксис: list.pop(index).

Принимает лишь один аргумент — индекс.

Для удаления элемента списка нужно передать его индекс. Индексы в списках стартуют с 0.
Для получения первого передайте 0. Для удаления последнего передайте -1.
Этот аргумент не является обязательным. Значение по умолчанию равно -1,
поэтому по умолчанию будет удален последний элемент.
Если этот индекс не найден или он вне диапазона, то метод выбросит исключение IndexError: pop index.
Возвращает элемент, удаленный из списка по индексу. Сам же список обновляется и больше не содержит этот элемент.
******************************************************************************
Метод clear()

Метод clear() удаляет все элементы из списка.

Синтаксис: list.clear().

Нет ни параметров, ни возвращаемого значения.
******************************************************************************
Ключевое слово del

Для удаления элемента из списка можно использовать ключевое слово del с названием списка после него.
Также потребуется передать индекс того элемента, который нужно удалить.

Синтаксис: del list[index].

Также можно выбрать элементы в определенном диапазоне и удалить их с помощью del.
Для этого нужно передать начальное и конечное значение диапазона.

Синтаксис: del list[start:stop].
******************************************************************************
any(iterable)  -> bool
all(iterable)  -> bool
******************************************************************************
Распаковка списка
a = []
[a, *a]

s=[['yellow', 1, 5, 6], ['blue', 2, 8, 3], ['green', 4, 9, 1], ['red', 1, 8, 2]]
for x, *y in s:
    print(x, type(x))
    print(y, type(y))
[y for x, *y in s]
******************************************************************************

''.join()
''.split()
''.strip()

******************************************************************************
По аналогии со списками кортежи в Python — это стандартный тип,
позволяющий хранить значения в виде последовательности.
Они полезны в тех случаях, когда необходимо передать данные, не позволяя изменять их.
Эти данные могут быть использованы, но в оригинальной структуре изменения не отобразятся.

numbers_tuple = 1,2,3,4,5
print(type(numbers_tuple))

numbers_tuple[3] = 99

import timeit
timeit.timeit('x=(1,2,3,4,5,6,7,8,9)', number=100000)
timeit.timeit('x=[1,2,3,4,5,6,7,8,9]', number=100000)

Не изменяемость кортежа
n = (1, 1, [3,4])
n.append(5)

Добавить элемент в кортеж нельзя, поэтому появляется последняя ошибка AttributeError.
Вот почему эта структура данных неизменна. Но всегда можно сделать вот так:

n[2].append(5)

Это позволяет изменять оригинальный кортеж? Куда в таком случае делась их неизменяемость?

Суть в том, что id списка в кортеже не меняется несмотря на добавленный в него элемент 5.
******************************************************************************
count() и len()

count() возвращает количество повторений элемента в кортеже.
len() — длину кортежа

Функция max()q возвращает самый большой элемент последовательности, а min() — самый маленький.

sum()

С помощью этой функции можно вернуть сумму элементов в кортеже. Работает только с числовыми значениями.

******************************************************************************
Функция sorted() возвращает новый отсортированный список итерируемого объекта (списка, словаря, кортежа).
По умолчанию она сортирует его по возрастанию.

Сортировка строк осуществляется по ASCII-значениям.

Возвращаемое значение — List (список).
Синтаксис: sorted(iterable,key=None,reverse=False).
iterable: строка, список, кортеж, множество, словарь
key (необязательный параметр): если указать ключ, то сортировка будет выполнена по функции этого ключа.
reverse (необязательный параметр): по умолчанию сортировка выполняется по возрастанию.
Если указать reverse=True, то можно отсортировать по убыванию.

Параметр key

Итерируемый объект можно также отсортировать по функции, указанной в параметре key. Это может быть:

Встроенная функция,
Определенная пользователем функция,
Лямбда-функция,
itemgetter,
attrgetter.
******************************************************************************
Распаковка картежа
n = (1,2,3)
a,b,c = n
print(a,b,c)
******************************************************************************
filter

filter(function, iterable)

a = [11, False, 18, 21, "", 12, 34, 0, [], {}]
filtered_a = filter(None, a)
list(filtered_a)

creature_names = ['Sammy', 'Ashley', 'Jo', 'Olly', 'Jackie', 'Charlie']
list(filter(lambda x: x[0].lower() in 'aeiou', creature_names))
******************************************************************************
"""

"""
Даны два списка чисел (можно сгенерировать при помощи генератора случайных чисел). 
Посчитайте, сколько уникальных чисел содержится одновременно как в первом списке, так и во втором.
- Примечание.
Эту задачу можно решить в одну строчку.
Множество использовать нельзя
"""
a = [random.randint(1, 100) for _ in range(10)]
b = [random.randint(1, 100) for _ in range(20)]
print(len([i for i in [*a, *b] if [*a, *b].count(i) == 1]))

"""
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей (слева и справа), 
и выведите количество таких элементов. Крайние элементы списка никогда не учитываются, поскольку у них недостаточно 
соседей.
"""
tmp = []
for i, e in enumerate(a):
    if i == 0 or i == len(a) - 1:
        continue
    if e > a[i - 1] and e > a[i + 1]:
        tmp.append((a[i - 1], e, a[i + 1]))

print(tmp, len(tmp))

"""
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это 
сделать.
  - Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в
  строю. После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.
  - Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как
  у Пети, то он должен встать после них.

  (
  1. Здесь понадобится сортировка. Вот пример:
    a = [5, 8, 2, 8, 4, 7, 0, 3, 1, 6, 9]
 print(a) # [5, 8, 2, 8, 4, 7, 0, 3, 1, 6, 9]
 a.sort(reverse=True)
 print(a) # [9, 8, 8, 7, 6, 5, 4, 3, 2, 1, 0]

 Параметр reverse=True отсортирует список в порядке убывания элементов.

 2. Так же, понадобится list comprehension который позволит создать список случайных значений
 )
"""

heights = [random.randint(150, 200) for _ in range(10)]
heights.sort()
petya = 175

for i, h in enumerate(heights):
    if petya < heights[0]:
        heights.insert(0, petya)
        break
    if petya > heights[-1]:
        heights.append(petya)
        break
    if petya > h:
        continue
    else:
        heights.insert(i, petya)
        heights.sort(reverse=True)
        break

print(heights)
