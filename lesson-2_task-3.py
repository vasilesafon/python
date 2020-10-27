month = int(input('Введите месяц цифрой от 1 до 12: '))

print('Решение через "list"')
seasons_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето',
                'Осень', 'Осень', 'Осень', 'Зима']
print(seasons_list[month - 1])

print('Решение через "dict"')
seasons_dic = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето',
               7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}
print(seasons_dic[month])

