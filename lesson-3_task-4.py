def ranc_func(x, y):
    result = x
    for i in range(1, abs(y)):
        result = result * x
    if y > 0:
        return result
    elif y < 0:
        return 1/result
    else:
        return 1

print(ranc_func(2, -5))


