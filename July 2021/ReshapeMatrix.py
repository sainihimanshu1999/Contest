'''Matrix reshaoe easy method'''


def reshapeMatrix(mat,r,c):

    if len(mat)*len(mat[0]) != r*c:
        return mat

    vals = [val for row in mat for val in row]

    ans = [[None]*c for _ in range(r)]

    i = 0

    for row  in range(r):
        for col in range(c):
            ans[row][col] = vals[i]
            i+=1

    return ans
