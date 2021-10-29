
sample_matrix = [[1, 2, 3, 4 ,5],
                [6, 7, 8, 9 ,10],
                [11, 0, 12, 13 ,14],
                [15, 16, 17, 18 ,19],
                [20, 21, 22, 23 ,24]]


# \
# \ \ \ \ \ \ 
def rotate(matrix):
    prev = 0
    current = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            temp = matrix[j][i]
            current = prev
            
            matrix[j][i] = current
            prev = current 
            matrix[i][j] =  temp



    return matrix


print(rotate(sample_matrix))



