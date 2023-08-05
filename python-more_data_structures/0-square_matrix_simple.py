def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create a new matrix to store the square values
    square_matrix = [[0 for j in range(cols)] for i in range(rows)]
    
    # Compute the square value of each element in the matrix
    for i in range(rows):
        for j in range(cols):
            square_matrix[i][j] = matrix[i][j] ** 2
    
    return square_matrix