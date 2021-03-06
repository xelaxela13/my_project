"""
import requests


def get_image():
    response = requests.get('https://httpbin.org/image/jpeg')
    return response.content


def save_image_to_file(image_data):
    f = open('image.jpg', 'wb')
    f.write(image_data)
    f.close()


def main():
    image_data = get_image()
    save_image_to_file(image_data)


import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")


if __name__ == '__main__':
    main()


r - read
w - Write - will create a file if the specified file does not exist
x - Create - will create a file, returns an error if the file exist
a - Append - will create a file if the specified file does not exist
b - binary
+ - write

https://docs.python.org/3/library/contextlib.html#contextlib.asynccontextmanager
"""
import json


def main():
    filename = 'data.json'
    data = {
        "ФИО": "Иванов Сергей Михайлович",
        "ЕГЭ": {
            "Математика": 90,
            "Физика": 70,
            "Информатика": '80'
        },
        "Хобби": ["Рисование", "Плавание", ],
        "Возраст": 25.5,
        "ДомЖивотные": None
    }

    valid_data = json.dumps(data)
    with open(filename, 'w') as f:
        f.write(valid_data)

    with open(filename, 'r') as f:
        row = f.read()

    print(json.loads(row))


if __name__ == '__main__':
    main()
