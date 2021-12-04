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


if __name__ == '__main__':
    main()


r - read
w - write
a - append
b - binary
+ - write
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
