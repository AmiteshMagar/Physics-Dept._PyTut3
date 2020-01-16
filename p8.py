m = int(input("Enter the number of rows"))
n = int(input("Enter the number of columns"))

mat1 = [[0 for i in range(n)] for j in range(m)]
for i in range(m):
    for j in range(n):
        mat1[i][j] = int(input())

matTrans = [[0 for i in range(m)] for j in range(n)]

for i in range(m):
    for j in range(n):
        matTrans[j][i] = mat1[i][j]

print(matTrans)
        
