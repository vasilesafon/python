# итератор, генерирующий целые числа, начиная с указанного
# выход из цикла ограничиваем временем указанным в секундах
import sys
from itertools import count
import time

name, num, gen_time = sys.argv
usr_list = []
start = time.time()
for el in count(int(num)):
    now = time.time()
    if now - start > int(gen_time):
        break
    usr_list.append(el)
    print(el)
print(f'За {gen_time} секунд, сгенерировано {len(usr_list)} чисел.')


