n = int(input())
m = int(input())

mat = []

for i in range(n):
    mat.append([])
    for j in range(m):
        elem = int(input())
        mat[i].append(elem)

print(mat)