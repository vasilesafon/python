list = input('Введите список любых значений, разделяя пробелами: ')
list = list.split()
length = len(list)
first = 0
second = 1
while length > 1:
    temp = list[second]
    list[second] = list[first]
    list[first] = temp
    length -= 2
    first += 2
    second += 2
print(list)

