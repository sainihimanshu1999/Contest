'''When we have to rotate the array by 90 degree, we have to transpose the matrix first and then interchange j and n-1-j column'''


def rotateArray90(matrix,target):
    m = len(matrix)

    #transposing
    for time in range(4):
        for i in range(m):
            for j in range(i+1,m):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        #90 degree rotating

        for i in range(m):
            for j in range(m//2):
                matrix[i][j],matrix[i][n-1-j] = matrix[i][n-1-j],matrix[i][j]


        if matrix == target:
            return True

    return False

