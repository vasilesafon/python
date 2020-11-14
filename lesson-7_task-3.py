class Cell:

    def __init__(self, parts):
        self.parts = parts

    def make_order(self, len_row):
        self.one_row = self.parts // len_row
        print(('*' * len_row + '\n') * (self.parts // len_row) + '*' * (self.parts % len_row))

    def __add__(self, other):
        result =  self.parts + other.parts
        return result

    def __truediv__(self, other):
        result = self.parts // other.parts
        if result >= 1:
            return result
        else:
            return 'Check second cell!'

    def __sub__(self, other):
        result =  int(self.parts - other.parts)
        if result > 0:
            return result
        else:
            return 'Check second cell!'

    def __mul__(self, other):
        result =  self.parts + other.parts
        return result

first = Cell(16)
second = Cell(9)

print(first / second)
print(first - second)

first.make_order(10)

