rating = []
while True:
    new_rate = int(input('Введите число: '))
    rating.append(new_rate)
    rating.sort()
    rating.reverse()
    # rating = rating[::-1]
    print(rating)