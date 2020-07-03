# The transpose of a matrix is a new matrix whose row are the 
# columns of the old matrix and whose columns are the row of 
# old matrix

def transpose(matrix):
    n = len(matrix) # number of rows
    m = len(matrix[0]) # number of columns

    for i in range(n):
        for j in range(i, n): # old row becomes new column
           matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

if __name__ == "__main__":
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    """
    matrix
    [
        [1,2]
        [3,4]
        [5,6]
    ]
    """
    """
    Transposed matrix
    [
        [1,3,5]
        [2,4,6]
    ]
    """
    print(transpose(matrix))