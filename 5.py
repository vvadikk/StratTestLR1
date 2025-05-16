from random import randint

def printMatrix(matrix):
    for row in matrix:
        formatted_row = ' '.join('{:1}'.format(element) for element in row)
        print(formatted_row)
N = int(input('Количество строк: '))
M = int(input('Количество столбцов: '))
matrix = [[randint(20, 80) for i in range(M)] for j in range(N)]
printMatrix(matrix)
