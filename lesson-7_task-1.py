class Matrix():

    def __init__(self, mtrx):
        self.mtrx = mtrx

    def __str__(self):
        for i in range(len(self.mtrx)):
            for j in range(len(self.mtrx[i])):
                print('{:4d}'.format(self.mtrx[i][j]), end = "")
            print()
        return ''

    def __add__(self, other):
        mtrx_sum = self.mtrx
        for i in range(len(self.mtrx)):
            for j in range(len(self.mtrx[0])):
                mtrx_sum[i][j] = self.mtrx[i][j] + other.mtrx[i][j]
        for i in range(len(mtrx_sum)):
            for j in range(len(mtrx_sum[i])):
                print('{:4d}'.format(mtrx_sum[i][j]), end = "")
            print()
        return ''


matrix_one = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_two = [[3, 8, 4], [7, 9, 2], [0, 3, 5]]

my_matrix = Matrix(matrix_two)
your_matrix = Matrix(matrix_one)
print(my_matrix)
print(your_matrix)
print(my_matrix + your_matrix)
