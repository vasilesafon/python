import json

with open('lesson-5_task-7.txt', encoding='utf-8') as read_file:
    lines = read_file.readlines()

firms = {}
sum_profit = 0
cnt = 0
for line in lines:
    name = line.split()[0]
    profit = int(line.split()[2]) - int(line.split()[3])
    firms[name] = profit
    if profit > 0:
        sum_profit += profit
        cnt += 1
average_profit = {'average_profit': sum_profit / cnt}
result = [firms, average_profit]

with open('lesson-5_task-7.json', 'w') as write_file:
    json.dump(result, write_file)

