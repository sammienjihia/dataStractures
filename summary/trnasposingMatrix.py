"""
Transposing an n*n matrix in place

"""
def transpose(matrix):

    num_rows = len(matrix)

    num_columns = len(matrix[0]) 

    # NB: Transposing a matrix means, the columns becomes the row, and the row becomes the columns

    for j in range(num_columns): # The columns become the rows
        for i in range(j,num_rows): # The rows becomes the columns
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


def transposeII(matrixI):
    return [[ matrixI[i][j] for i in range(len(matrixI))]for j in range(len(matrixI[0]))]


if __name__ == "__main__":
    print(transpose([[1,2,3], [4,5,6], [7,8,9]]))
    print(transposeII([[1,2,3], [4,5,6]]))