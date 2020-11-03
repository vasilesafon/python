usr_list = [26, 45, 68, 21, 78, 69, 14, 27, 84, 11, 37]
new_list = [b for b in usr_list if b > (usr_list[usr_list.index(b) - 1])]
print(new_list)
