read_file = open('lesson-5_task-2.txt')
lines = read_file.readlines()
lines_cnt = 0
for line in lines:
    lines_cnt +=1
    print(f'В строке {lines_cnt}: {len(line.split())} слов')
print()
print(f'В файле {lines_cnt} строк')
read_file.close()


# with open('lesson-5_task-2.txt') as read_file:
#     lines = read_file.readlines()
#     print(f'В файле {len(lines)} строк')
#     for numero, line in enumerate(lines, start=1):
#         print(f'В строке {numero}: {len(line.split())} слов')