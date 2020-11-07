with open('lesson-5_task-4.txt', encoding='utf8') as eng_txt:
    lines = eng_txt.readlines()

with open('lesson-5_task-4_rus.txt', 'w', encoding='utf8') as rus_txt:
    for line in lines:
        if 'One' in line:
            line = line.replace('One', 'Один')
        elif 'Two' in line:
            line = line.replace('Two', 'Два')
        elif 'Three' in line:
            line = line.replace('Three', 'Три')
        elif 'Four' in line:
            line = line.replace('Four', 'Четыре')
        rus_txt.write(line)