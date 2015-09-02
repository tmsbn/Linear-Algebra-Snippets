__author__ = 'tmsbn'

a = [[0, 1],
     [1, 2],
     [4, 5]]

b = [[11, 1, 2],
     [1, 12, 3]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# print(len(a[0]), len(b), a[0][1])  # len(a) give the row count, len(a[0] gives the column count of 1st column
# a[row][column])

for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a[0])):
            result[i][j] += a[i][k] * b[k][j]

            # Multiplication is done from horizontal to vertical ,
            # the result is always a square matrix
            # a[m][n] * b[n][m] = c[m][m]

print(result)

