input_string = input('Введите что нибудь: ')
initial_string = "Это строка в которую {} новую строку".format(input_string)

print(initial_string)

initial_string = initial_string.replace(input_string, 'замена в строке')

print(initial_string)

print(len(initial_string))

if initial_string.find('строка') != -1:
    print('Да')
else:
    print('Нет')


a = int(input('D:'))
a = ((a % 10) * 100) + (((a // 10) % 10) * 10) + (a // 100)
print(a)
