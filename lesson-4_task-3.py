usr_list = range(20, 240)

new_list = [ el for el in usr_list if el % 20 ==0 or el % 21 == 0]
print(new_list)