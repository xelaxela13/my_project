"""
Исключения

BaseException - базовое исключение, от которого берут начало все остальные.
SystemExit - исключение, порождаемое функцией sys.exit при выходе из программы.
KeyboardInterrupt - порождается при прерывании программы пользователем (обычно сочетанием клавиш Ctrl+C).
GeneratorExit - порождается при вызове метода close объекта generator.
Exception - а вот тут уже заканчиваются полностью системные исключения (которые лучше не трогать)
и начинаются обыкновенные, с которыми можно работать.
    StopIteration - порождается встроенной функцией next, если в итераторе больше нет элементов.
    ArithmeticError - арифметическая ошибка.
        FloatingPointError - порождается при неудачном выполнении операции с плавающей запятой. На практике встречается нечасто.
        OverflowError - возникает, когда результат арифметической операции слишком велик для представления.
        Не появляется при обычной работе с целыми числами (так как python поддерживает длинные числа),
        но может возникать в некоторых других случаях.
        ZeroDivisionError - деление на ноль.
    AssertionError - выражение в функции assert ложно.
    AttributeError - объект не имеет данного атрибута (значения или метода).
    BufferError - операция, связанная с буфером, не может быть выполнена.
    EOFError - функция наткнулась на конец файла и не смогла прочитать то, что хотела.
    ImportError - не удалось импортирование модуля или его атрибута.
    ModuleNotFoundError - todo
    LookupError - некорректный индекс или ключ.
        IndexError - индекс не входит в диапазон элементов.
        KeyError - несуществующий ключ (в словаре, множестве или другом объекте).
    MemoryError - недостаточно памяти.
    NameError - не найдено переменной с таким именем.
        UnboundLocalError - сделана ссылка на локальную переменную в функции, но переменная не определена ранее.
    OSError - ошибка, связанная с системой.
        BlockingIOError
        ChildProcessError - неудача при операции с дочерним процессом.
        ConnectionError - базовый класс для исключений, связанных с подключениями.
            BrokenPipeError
            ConnectionAbortedError
            ConnectionRefusedError
            ConnectionResetError
        FileExistsError - попытка создания файла или директории, которая уже существует.
        FileNotFoundError - файл или директория не существует.
        InterruptedError - системный вызов прерван входящим сигналом.
        IsADirectoryError - ожидался файл, но это директория.
        NotADirectoryError - ожидалась директория, но это файл.
        PermissionError - не хватает прав доступа.
        ProcessLookupError - указанного процесса не существует.
        TimeoutError - закончилось время ожидания.
    ReferenceError - попытка доступа к атрибуту со слабой ссылкой.
    RuntimeError - возникает, когда исключение не попадает ни под одну из других категорий.
    NotImplementedError - возникает, когда абстрактные методы класса требуют переопределения в дочерних классах.
    SyntaxError - синтаксическая ошибка.
        IndentationError - неправильные отступы.
            TabError - смешивание в отступах табуляции и пробелов.
    SystemError - внутренняя ошибка.
    TypeError - операция применена к объекту несоответствующего типа.
    ValueError - функция получает аргумент правильного типа, но некорректного значения.
    UnicodeError - ошибка, связанная с кодированием / раскодированием unicode в строках.
        UnicodeEncodeError - исключение, связанное с кодированием unicode.
        UnicodeDecodeError - исключение, связанное с декодированием unicode.
        UnicodeTranslateError - исключение, связанное с переводом unicode.
    Warning - предупреждение.

assert

assert x == "goodbye", "x should be 'hello'"

raise


dd = {'key': 'a'}
try:
    a = int(dd['key'])
except (KeyError, ValueError) as err:
    print('Error: ', err)
else:
    print('Looks good')
finally:
    print('Finally')
"""


class ValueTooSmallError(Exception):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Exception):
    ...


number = 10

while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
    except ValueTooLargeError:
        print("This value is too large, try again!")

print("Congratulations! You guessed it correctly.")

try:
    a = 2
finally:
    print('Ok')
