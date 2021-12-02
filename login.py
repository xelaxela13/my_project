"""
Lesson8
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

Lesson9
В программу написанную в прошлом ДЗ добавить новый функционал (не изменяя старого)
username and password получать из командной строки как не обязательные аргументы.
Если оба аргумента переданы и имя и пароль прошли проверку то программа завершает работу не меняя прошлого поведения.
Если не правильное имя или пароль даем 3 попытки как и раньше.
Если передать только имя, то спрашивать только пароль, и наоборот, спрашивать пароль если передать только имя.
Основная идея в том что-бы расширить функционал прошлой программы, а не переписывать!

lesson10
Расширить функционал прошлого ДЗ:
После всех неудачных попыток войти в систему нужно блокировать пользователя на 5 минут.
Выводить сообщение "Вы заблокированы! Следующая попытка через N мин."
для решение понадобится хранить две даты-временя
последняя удачная попытка входа
последняя НЕ удачная попытка входа
действия с датой лучше вынести в отдельные функци
"""
import argparse
from datetime import datetime, timedelta
from functools import wraps

USERS = {
    'Alex': {'password': '12345',
             'last_login': {'success': None,
                            'fail': datetime.now() - timedelta(minutes=3)}
             },
}


class UserDoesNotExist(Exception):
    ...


def login_decorator(func):
    @wraps(func)
    def wrapper(username, password):
        if not get_user(username):
            return False
        if not can_login_from_last_fail(username):
            print(f'Вы заблокированы! '
                  f'Следующая попытка через {get_remaining_time(username)} мин')
            exit()
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
    try:
        assert all((username, password))
        get_user(username)
    except (UserDoesNotExist, AssertionError):
        return False
    return USERS[username]['password'] == password


def can_login_from_last_fail(username: str) -> bool:
    if not get_user(username):
        return False
    last_fail = USERS[username]['last_login']['fail']
    return last_fail < datetime.now() - timedelta(minutes=5)


def get_remaining_time(username) -> int:
    """
    @return: minutes as integer
    """
    last_fail = USERS[username]['last_login']['fail']
    now = datetime.now()
    if last_fail.minute < now.minute:
        remaining = now.minute - last_fail.minute
    else:
        remaining = now.minute - (60 - last_fail.minute)
    return remaining


def get_user(username: str) -> str or UserDoesNotExist:
    """
    @param username: str
    @return: username or None if does not exist
    """
    user = USERS.get(username, None)
    if not user:
        raise UserDoesNotExist('User does not exist')
    return user


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


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", action="store", help="Username")
    parser.add_argument("-p", "--password", action="store", help='Password')
    args = parser.parse_args()
    return args.username, args.password


if __name__ == "__main__":
    username, password = parse_args()
    if username and password:
        if login(username, password):
            exit()
        else:
            username, password = None, None
    i = 3
    while i > 0:
        if login(username or input('Введите ваш логин:'),
                 password or input('Введите ваш пароль:')):
            break
        i -= 1
        print(f'Оталось попыток: {i}' if i else 'Попытки истекли!')
