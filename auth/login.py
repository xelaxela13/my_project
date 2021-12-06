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

lesson12
Написать собственный клас Исключения - UserDoesNotExist
Переписать функцию проверки пароля использую собственное исключения

lesson13
Перенести функционал программы login с глобальной переменной в файл.
Данные хранить в формате JSON
Добавить функцию registration() (по желанию)
"""
import argparse
import json
from datetime import datetime, timedelta
from functools import wraps
from json import JSONDecodeError

DATA_FORMAT = '%Y-%m-%d %H:%M'
USER = {}


class UserDoesNotExist(Exception):
    ...


def login_decorator(func):
    @wraps(func)
    def wrapper(username, password):
        if not get_user(username):
            print('Пользователь не найден, пожалуйста зарегистрируйтесь!')
            exit()
        if not can_login_from_last_fail(username):
            print(f'Вы заблокированы! '
                  f'Следующая попытка через {get_remaining_time(username)} мин')
            exit()
        if not check_password(username, password):
            print('Не правильное Имя или Пароль')
            return False
        if not authenticate(username):
            return False
        return func(username, password)

    return wrapper


def check_password(username: str, password: str) -> bool:
    """
    Return True if Username exists in USER dict and password is correct
    @param username: Username from USER dict
    @param password: Password from USER dict
    @return: bool
    """

    user_data = get_user(username)
    return all((username, password)) and user_data and user_data[
        'password'] == password


def can_login_from_last_fail(username: str) -> bool:
    user_data = get_user(username)
    if not user_data:
        return False
    last_fail = user_data['last_login']['fail']
    if not last_fail:
        return True
    last_fail = datetime.strptime(last_fail, DATA_FORMAT)
    return last_fail < datetime.now() - timedelta(minutes=5)


def get_remaining_time(username) -> int:
    """
    @return: minutes as integer
    """
    user_data = get_user(username)
    if not user_data:
        return False
    last_fail = datetime.strptime(user_data['last_login']['fail'], DATA_FORMAT)
    now = datetime.now()
    if last_fail.minute < now.minute:
        remaining = now.minute - last_fail.minute
    else:
        remaining = now.minute - (60 - last_fail.minute)
    return remaining


def get_user(username: str) -> str or None:
    """
    @param username: str
    @return: username or None if does not exist
    """
    global USER
    if not USER:
        try:
            user = load_data(username).get(username, None)
            if not user:
                raise UserDoesNotExist()
            USER = user
        except UserDoesNotExist:
            return
    return USER


def authenticate(username: str) -> bool:
    """
    Function without any arguments, just for example
    @return: bool
    """
    user_data = get_user(username)
    if user_data:
        user_data['last_login']['success'] = datetime.now().strftime(
            DATA_FORMAT)
        user_data['last_login']['fail'] = None
        data = {
            username: user_data
        }
        save_data(username, data)
    print('Вы в системе!')
    return True


@login_decorator
def login(_username: str, _password: str) -> bool:
    """
    Just abstract function for example, always return True
    @param _username: Username from USER dict
    @param _password: Password from USER dict
    @return: bool
    """
    return True


def registration(username: str, password: str) -> bool:
    user_data = get_user(username)
    if not user_data and username and password:
        print('Зарегистрироваться!')
        data = {
            username: {'password': password,
                       'last_login': {'success': None,
                                      'fail': None}
                       },
        }
        save_data(username, data)
        print('Вы успешно зарегистрировались!')
        return True
    print('Имя и пароль обязательны!')
    return False


def save_data(filename: str, data: dict):
    try:
        with open(f'users/{filename.lower()}.json', 'w') as f:
            f.write(json.dumps(data, ensure_ascii=False))
    except Exception as err:
        print('ERROR: ', err)
        exit()


def load_data(filename: str) -> dict:
    if filename:
        try:
            with open(f'users/{filename.lower()}.json', 'r') as f:
                return json.loads(f.read())
        except (FileNotFoundError, JSONDecodeError):
            pass
    return {}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", action="store", help="Username")
    parser.add_argument("-p", "--password", action="store", help='Password')
    parser.add_argument("-r", "--registration", action="store_true",
                        help='Add new user')
    args = parser.parse_args()
    return args.username, args.password, args.registration


def save_fail_attempt(username: str):
    user_data = get_user(username)
    if user_data:
        user_data['last_login']['fail'] = datetime.now().strftime(DATA_FORMAT)
        data = {
            username: user_data
        }
        save_data(username, data)


def main():
    username, password, is_registration = parse_args()
    if is_registration:
        registration(username or input('Введите ваш логин:'),
                     password or input('Введите ваш пароль:'))
        exit()
    if username or password:
        if login(username or input('Введите ваш логин:'),
                 password or input('Введите ваш пароль:')):
            exit()
    i = 3
    while i > 0:
        username = input('Введите ваш логин:')
        password = input('Введите ваш пароль:')
        if login(username, password):
            exit()
        i -= 1
        print(f'Оталось попыток: {i}' if i else 'Попытки истекли!')
    save_fail_attempt(username)


if __name__ == "__main__":
    main()
