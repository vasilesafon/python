start = int(input('Сколько км пробежал спортсмен в первый день? '))
finish = int(input('Сколько км спортсмен должен пробежать? '))


if start > finish:
    print('Ошибка. Спортсмен и так хорошо бегает')
else:
    day_x = 1
    while start < finish:
        day_x += 1
        start = start * 1.1
        print(f'На {day_x}-й день: {start:.2f}км')
print(f'Спортсмен пробежит не менее {finish} км на {day_x:.0f} день')