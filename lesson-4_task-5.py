from functools import reduce

result = reduce(lambda x, y: x * y, range(100, 1001, 2))
print(result)