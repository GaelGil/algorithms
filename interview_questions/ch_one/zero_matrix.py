
sample_matrix = [[1, 2, 3, 4 ,5],
                [6, 7, 8, 9 ,10],
                [11, 0, 12, 13 ,14],
                [15, 16, 17, 18 ,19],
                [20, 21, 22, 23 ,24]]


def zero_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                matrix[i] = [0] * (len(matrix[i]))
                nums = (i[j] == 0 for i in matrix)
                break


    
    return matrix


print(zero_matrix(sample_matrix))