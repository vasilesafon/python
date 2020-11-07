# итератор, повторяющий элементы некоторого списка, определенного заранее

from itertools import cycle
el_list = [400, None, "text", True, 4, 234, 45.8, "text", "word", "el", 867]
check = []
for el in cycle(el_list):
    if el in check:
        break
    check.append(el)
    print(el)
