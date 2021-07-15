'''In this matrix there are layers and we have to cyclically rotate the matrix, we would save the outer matrix in 
temp and then rotate it and then add them back in the array, and we do this from outer to inner of the matrix'''


def cyclically(matrix,k):
    m = len(matrix)
    n = len(matrix[0])

    i,j=0,0
    bottom,right = m-1,n-1

    while i<n//2 and j<n//2:
        temp = []

        for x in range(j,right):
            temp.append(matrix[i][x])

        for x in range(i,bottom):
            temp.append(matrix[x][right])

        for x in range(right,j,-1):
            temp.append(matrix[bottom][x])

        for x in range(bottom,i,-1):
            temp.append(matrix[x][j])


        index = 0

        for x in range(j,right):
            matrix[i][x] = temp[(k+index)%len(temp)]

            index +=1

        for x in range(i,bottom):
            matrix[x][right] = temp[(k+index)%len(temp)]

            index +=1

        for x in range(right,j,-1):
            matrix[bottom][x] = temp[(k+index)%len(temp)]

            index +=1

        for x in range(bottom,i,-1):
            matrix[x][j] = temp[(k+index)%len(temp)]

            index +=1

        i+=1
        j+=1
        bottom -=1
        right -=1

    return matrix

grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
k = 2

print(cyclically(grid,k))
