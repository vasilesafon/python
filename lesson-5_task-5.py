import random

with open('lesson-5_task-5.txt', 'w') as rnd_file:
    rnd_nums = []
    for i in range(0, 20):
        rnd_nums.append(str(random.randint(1, 100)) + ' ')
    rnd_file.writelines(rnd_nums)

with open('lesson-5_task-5.txt') as nums:
    numlist = nums.readline()
    sum = 0
    for num in numlist.split():
        sum += int(num)
    print(sum)

