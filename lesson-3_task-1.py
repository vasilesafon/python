def div(a,b):
    try:
        result = a / b
        print('Результат деления: ', result)
    except ZeroDivisionError:
        print("Деление на ноль!")


num_a = int(input('Введите первое число: '))
num_b = int(input('Введите второе число: '))

div(num_a, num_b)