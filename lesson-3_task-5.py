user_sum = 0

def row_sum(row):
    global user_sum
    new_nums = row
    for i in new_nums:
        if i == 'q' or i == 'Q':
            continue
        else:
            user_sum += int(i)
    print(user_sum)


while True:
    row = input('Введите числовой ряд через пробел. Для завершения - "Q". ').split()
    if 'q' in row or 'Q' in row:
        row_sum(row)
        print('Программа завершена.')
        break
    else:
        row_sum(row)
