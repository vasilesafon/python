number = int(input('Введите целое положительное число: '))

tail = number % 10
body = number // 10
while body > 0:

    if tail < (body % 10):
        tail = body % 10
    else:
        body = body // 10

print(f'Самая большая цифра в вашем числе: {tail}')