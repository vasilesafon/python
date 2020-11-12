
read_file = open('lesson-5_task-3.txt', encoding='utf8')
staff = read_file.readlines()
staff_sum = []
print('Получают менее 2000:')
for line in staff:
    staff_sum.append(int(line.split()[1]))
    if int(line.split()[1]) < 20000:
        print(line.split()[0])
print('Средняя зарплата сотрудников: ')
print(sum(staff_sum) / len(staff_sum))
read_file.close()

# решение из разбора

with open('lesson-5_task-3.txt', encoding='utf8') as read_file:
    staff_sum = []
    staff = read_file.readlines()
    for str in staff:
        name, salary = str.split()
        staff_sum.append(int(salary))
        if int(salary) < 20000:
            print(name)
    print('Средняя зарплата сотрудников: ', sum(staff_sum) / len(staff_sum))
