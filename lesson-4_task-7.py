
def fact(num): # функция создающая объект генератор
    for el in range(1, num + 1):
        yield el


def fact_calc(number): # функция считающая факториал
    result = 1
    for el in fact(number):
        result = el * result
        print(el)
    print()
    return (f'{number}! = {result}')

print(fact_calc(47))