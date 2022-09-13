
#Maximize the sum of the elements in the (N x N) submatrix located in the upper-left quadrant of the matrix
#Matrix size is (2N x 2N)s
#Given the initial configurations for matrix, reverse the rows and columns of the matrix to maximize the upper-left quadrant
def nMax(matrix):

    numIndex = int(len(matrix))-1
    n = int(len(matrix) / 2)

    reverseScore = 0

    for i in range(0, n):
        for k in range(0,n):
            reverseScore += max(
                matrix[i][k],
                #Horizontal Flip
                matrix[i][numIndex-k],
                #Vertical Flip
                matrix[numIndex-i][k],
                #Matrix Flip
                matrix[numIndex-i][numIndex-k]
                )

    return(reverseScore)

arr = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
print(nMax(arr))
