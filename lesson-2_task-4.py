# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

usr_str = input('Введите несколько слов разделенных пробелами: ')
usr_str = usr_str.split()
count = 0
for element in usr_str:
    count += 1
    print(count, '-', element[:10])