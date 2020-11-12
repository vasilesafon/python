file_txt = open('lesson-5_task-1.txt', 'w')
txt_to_file = []
usr_txt = 'пустая строка для того чтобы сработала следующая строчка:)'
while usr_txt != '':
    usr_txt = input("Вводим строки файла: ")
    file_txt.write(usr_txt + '/n')
file_txt.close()

# затык здесь был в том, что запись получается не построчно,
# а в одну строку типа "первая строка/nвторая строка/nтретья строка/n/n"
# решение из разбора, так же делает однострочную запись

# with open('lesson-5_task-1.txt', 'w') as file_txt:
#     while True:
#         usr_txt = input("Вводим строки файла: ")
#         if usr_txt == '':
#             break
#         file_txt.write(usr_txt + '/n')
