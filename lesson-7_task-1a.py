class Matrix():

    def __init__(self, mtrx):
        self.mtrx = mtrx

    def __str__(self):
        a = ''
        for i in self.mtrx:
            for k in i:
                a = a + "  " + str(k)
            a = a + '\n'
        return a

    def __add__(self, other):
        sum = ''
        if len(self.mtrx) == len(other.mtrx):
            for i in range(len(self.mtrx)):
                if len(self.mtrx[0]) == len(other.mtrx[0]):
                    for k in range(len(self.mtrx[0])):
                        sum = sum + str(self.mtrx[i][k] + other.mtrx[i][k]) + '   '
                    sum = sum + '\n'
                else:
                    print('error 002')
        else:
            print('error 001')
        return sum


matrix_one = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_two = [[3, 8, 4], [7, 9, 2], [0, 3, 5]]
matrix_three = [[3, 8, 4], [7, 9, 2], [0, 3, 5], [7, 9, 2], [0, 3, 5]]

my_matrix = Matrix(matrix_two)
your_matrix = Matrix(matrix_one)
matrix_three = Matrix(matrix_three)
print(my_matrix)
print(your_matrix)
print(my_matrix + your_matrix)

print(matrix_three + my_matrix)