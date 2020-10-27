base = [] # это база данных
result = {} # это аналитика
items_count = 0 # это количество товаров в базе
all_names = []
all_prices = []
all_counts = []
all_units = []
print('Товаров в базе:', items_count)
while True:
    intent = input('Желаете ввести данные о товаре? (да/нет) ')
    if intent == 'нет':
        print()
        print('Товары: ')
        for i in base:
            print(i)
        print()
        print('Аналитика:')
        for j in result.items():
            print(j)
        print()
        intent = input('Желаете ввести еще данные о товаре? (да/нет) ')
        if intent == 'нет':
            break
    if intent == 'да':
        name = input('Название: ')
        price = input('Цена: ')
        count = input('Количество: ')
        units = input('Единицы изм.: ')
        items_count += 1
        # создаем кортеж
        new_item = (items_count, {'название': name, 'цена': price, 'количество': count, 'ед.': units})
        base.append(new_item)  # добавляем кортеж в список
        all_names.append(name)
        all_prices.append(price)
        all_counts.append(count)
        all_units.append(units)
        result = {'название': all_names,'цена': all_prices, 'количество': all_counts, 'ед.': all_units}
        print('Товаров в базе:', items_count)
        continue
