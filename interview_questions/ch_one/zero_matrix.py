
sample_matrix = [[1, 2, 3, 4 ,5],
                [6, 7, 8, 9 ,10],
                [11, 0, 12, 13 ,14],
                [15, 16, 17, 18 ,19],
                [20, 21, 22, 23 ,24]]


def zero_matrix(matrix):
    matrix_copy = matrix.copy()
    x = 0
    y = 0
    # find the indices of zero in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                x = i 
                y = j
                break
    # replace the in
    for i in range(len(matrix_copy)):
        for j in range(len(matrix_copy)):
            if i == x or j == y:
                matrix_copy[i][j] = 0
    return matrix_copy


print(zero_matrix(sample_matrix))