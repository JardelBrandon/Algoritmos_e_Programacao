m = [[1,2,3], [4,5,6], [7,8,9]]

for linha in range(len(m)):
    for col in range(len(m[linha])):
        if linha == len(m)-col-1:
            print(m[linha][col], end=' ')
        else:
            print(' ', end='')
    print()