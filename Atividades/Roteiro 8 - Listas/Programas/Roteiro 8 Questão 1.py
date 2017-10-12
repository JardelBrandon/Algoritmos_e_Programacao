'''
1. Qual a saída de cada um dos seguintes programas abaixos: (Tente fazer no papel antes de usar
o interpretador python)

1°
l = []
print(l)

2°
x = [10,20,30]
print(x[1])

x = [10,20,30]
print(x[-1])

3°
l = [10,20,30]
print(l[3])

4°
l.append(50)
print(l)

5°
l.insert(40)
print(l)

6°
x.insert(40,3)
print(x)

7°
l.append(1)
print(l)

8°
x =[0, 1, [2]]
x[2][0] = 3
print(x)

9°
x[2].append(4)
print(x)

10°
x[2] = 2
print x
print(x+l)
'''

l = []
print(l)

x = [10,20,30]
print(x[1])

l = [10,20,30]
print(l[3])

l.append(50)
print(l)

l.insert(40)
print(l)

x.insert(40,3)
print(x)

l.append(1)
print(l)

x =[0, 1, [2]]
x[2][0] = 3
print(x)

x[2].append(4)
print(x)

x[2] = 2
print(x)
print(x+l)

'''
Foi apresentado as seguintes saídas no interpretador do python:
1°
>>> []

2°
>>> 20

3°
>>> Traceback (most recent call last):
  File "D:/Users/IFPB/Documents/Roteiro 8 - Listas (Jardel Brandon)/Programas/Roteiro 8 Questão 1.py", line 58, in <module>
    print(l[3])
IndexError: list index out of range

4°
>>> [10, 20, 30, 50]

5°
>>> Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    l.insert(40)
TypeError: insert() takes exactly 2 arguments (1 given)

6°
>>> [10, 20, 30, 3]

7°
>>> [10, 20, 30, 50, 1]

8°
>>> [0, 1, [3]]

9°
>>> [0, 1, [3, 4]]

10°
>>> [0, 1, 2]
    [0, 1, 2, 10, 20, 30, 50, 1]

'''