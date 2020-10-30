def int_func(row):
    cap_row = []
   # cap_list = row
    for element in row:
        element = element.capitalize()
        cap_row.append(element)
    return ' '.join(cap_row)

usr_row = input('Введите слово: ')
print(int_func(usr_row.split()))

usr_row = input('Введите строку: ').split()
print(int_func(usr_row))