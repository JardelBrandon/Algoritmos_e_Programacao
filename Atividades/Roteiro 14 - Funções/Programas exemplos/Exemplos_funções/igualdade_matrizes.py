def recebe_matriz(tam=2):    m = []    for i in range(tam):        m.append([])        for j in range(tam):            elem = int(input())            m[i].append(elem)    return mdef print_tabular(m):    for linha in m:        for e in linha:            print(e, end=' ')        print()def matrizes_iguais(x, y):    if len(x) != len(y):        return False    for i in range(len(x)):        if len(x[i]) != len(y[i]):            return False        for j in range(len(x[i])):            if x[i][j] != y[i][j]:                return False    return Truen = int(input("Ordem da matriz 1: "))m1 = recebe_matriz(n)print_tabular(m1)n2 = int(input("Ordem da matriz 2: "))m2 = recebe_matriz(n2)print_tabular(m2)if(matrizes_iguais(m1, m2)):    print("Matrizes iguais!")else:    print("Matrizes diferentes!")