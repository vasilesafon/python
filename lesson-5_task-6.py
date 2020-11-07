import re
my_dict = {}
with open('lesson-5_task-6.txt', encoding='utf-8') as f:
    list = f.readlines()
    for el in list:
        am = el.split()[1:]
        #my_dict[el.split()[0]] = sum(int(x[:x.find('(')]) for x in am if '(' in x) # подсмотренное решение
        my_dict[el.split()[0]] = sum(map(int, re.findall('[0-9]+', el))) # читерское :) решение
print(my_dict)