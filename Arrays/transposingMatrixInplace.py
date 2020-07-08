# The transpose of a matrix is a new matrix whose row are the 
# columns of the old matrix and whose columns are the row of 
# old matrix

def transpose(matrix):
    n = len(matrix) # number of rows
    m = len(matrix[0]) # number of columns

    for i in range(m):
        for j in range(i, n): # old row becomes new column
           matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

# def transposeB(matrix):
#     if not matrix:
#         return []
#     transposedMatrix = []
#     for i in range(len(matrix[0])): # this loop represents the rows which takes the columns of the original matrix
#         transposedMatrix.append([])
#         for j in range(len(matrix)): # this loop represents the columns which takes the rows of the original matrix
#             transposedMatrix[i].append(matrix[j][i])
#     return transposedMatrix

def transposeB(matrix):
    n = len(matrix) # number of rows
    m = len(matrix[0]) # number of columns
    transposedMatrix = []

    """
    Transposing a matrix is basically means the rows of the original matrix becomes the columns of the transposed matrix
    and the columns of the original matrix becomes the rows of the transposed matrix
    Example
    -------

    Orignal Matrix = [[1,2], [3,4], [5,6]] Two columns, 3 rows
    Transposed Matrix = [[1,3,5], [2,4,6]] Three columns 2 rows
    """
    # So for our transposed matrix the columns becomes the rows
    for i in range(m): # we shall have 2 rows
        # create a new row by appending an empty list, which shall be filled by the columns
        transposedMatrix.append([])
        for j in range(n): # we shall have 3 columns
            # on the i-th row of the transposed matrix append the columns, basically appending the i-th item of every j-th row in 
            # the original matrix
            transposedMatrix[i].append(matrix[j][i])

    return transposedMatrix



# transpose n by m matrix
def transposeX(matrix):
    n = len(matrix)
    m = len(matrix[0])

    # inner loop is the number of rows | becomes the new columns
    # outer loop is the number of columns | becomes the new rows

    return [[matrix[j][i] for j in range(n)] for i in range(m)]

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
    # print(transpose(matrix))
    print(matrix)
    print(transposeX(matrix))
    print(transposeB(matrix))