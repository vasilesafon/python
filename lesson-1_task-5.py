revenue = int(input('Выручка: '))
costs = int(input('Издержки: '))
margin = revenue - costs
if margin < 0:
    print('Ваша фирма работает в убыток!')
else:
    return_on_sales = margin / revenue
    print(f'Рентабельность выручки: {return_on_sales:.2f}')
    personal = int(input('Введите количество сотрудников: '))
    print(f'Прибыль вашей фирмы: {(margin / personal):.2f} на сотредника')