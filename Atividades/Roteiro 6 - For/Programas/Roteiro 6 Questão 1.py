#1. Observe qual valor gerado em cada um dos comandos abaixo e depois teste no interpreador
#Python.

#1. list(range(10))
#2. list(range(-5,5))
#3. list(range(-5,5,2))
#4. list(range(2,10))
#5. list(range(2,10,3))
#6. list(range(20,100))
#7. list(range(20,100,2))
#8. list(range(30,0,-1))
#9. list(range(30,15,-1))
#10.list(range(30,15,-2))


list(range(10))
#Saída do interpretador:
#>>>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list(range(-5,5))
#Saída do interpretador:
#>>>[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

list(range(-5,5,2))
#Saída do interpretador:
#>>>[-5, -3, -1, 1, 3]

list(range(2,10))
#Saída do interpretador:
#>>>[2, 3, 4, 5, 6, 7, 8, 9]

list(range(2,10,3))
#Saída do interpretador:
#>>>[2, 5, 8]

list(range(20,100))
#Saída do interpretador:
#>>>[20, 21, 22, 23, 24, 25, 26,
# 27, 28, 29, 30, 31, 32, 33, 34,
# 35, 36, 37, 38, 39, 40, 41, 42,
# 43, 44, 45, 46, 47, 48, 49, 50,
# 51, 52, 53, 54, 55, 56, 57, 58,
# 59, 60, 61, 62, 63, 64, 65, 66,
# 67, 68, 69, 70, 71, 72, 73, 74,
# 75, 76, 77, 78, 79, 80, 81, 82,
# 83, 84, 85, 86, 87, 88, 89, 90,
# 91, 92, 93, 94, 95, 96, 97, 98, 99]

list(range(20,100,2))
#Saída do interpretador:
#>>>[20, 22, 24, 26, 28, 30, 32,
# 34, 36, 38, 40, 42, 44, 46, 48,
# 50, 52, 54, 56, 58, 60, 62, 64,
# 66, 68, 70, 72, 74, 76, 78, 80,
# 82, 84, 86, 88, 90, 92, 94, 96, 98]

list(range(30,0,-1))
#Saída do interpretador:
#>>>[30, 29, 28, 27, 26, 25, 24,
# 23, 22, 21, 20, 19, 18, 17, 16,
# 15, 14, 13, 12, 11, 10, 9, 8,
# 7, 6, 5, 4, 3, 2, 1]

list(range(30,15,-1))
#Saída do interpretador:
#>>>[30, 29, 28, 27, 26, 25, 24,
#23, 22, 21, 20, 19, 18, 17, 16]

list(range(30,15,-2))
#Saída do interpretador:
#>>>[30, 28, 26, 24, 22, 20, 18, 16]