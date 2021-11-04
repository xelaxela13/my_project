s = 10
for i in range(1, s, 2):
    i = ' ' * ((s - i) // 2) + '*' * i
    print(i)

for i in reversed(range(1, s-1, 2)):
    i = ' ' * ((s - i) // 2) + '*' * i
    print(i)
