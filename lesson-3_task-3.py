def my_func(a, b, c):
    # принимает три значения
    # возвращает сумму двух максимальных
    result = (a + b + c) - min(a, b, c)
    return result

print(my_func(20, 6, 9))
