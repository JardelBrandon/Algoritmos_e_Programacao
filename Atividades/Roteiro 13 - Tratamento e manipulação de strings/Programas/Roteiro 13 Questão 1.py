'''
1. Observe qual valor gerado em cada um dos comandos abaixo e depois teste no interpretador
Python.
s = “computador”
print(s[0])
for i in s:
print(i)
print(s[0] + s[3] + s[5])
print(s[0] + s[len(s)-1])
print(s[:5])
for k in range(0,len(s)):
print(s[k])
print(s[0:])
t = “celular”
for i in s:
print(i + t)
print(s[:])
for i in range(len(s)-1,-1,-1):
print(s[i])
'''

s = "computador"

print(s[0])

for i in s:
    print(i)

print(s[0] + s[3] + s[5])
print(s[0] + s[len(s)-1])
print(s[:5])

for k in range(0,len(s)):
    print(s[k])

print(s[0:])

t = "celular"

for i in s:
    print(i + t)

print(s[:])

for i in range(len(s)-1,-1,-1):
    print(s[i])

"""
Foi obtido na saída do interpretador python:
para : print(s[0])
>>> c

para : for i in s:
    print(i)
    
>>>c
o
m
p
u
t
a
d
o
r

para : print(s[0] + s[3] + s[5])
>>>cpt

para : print(s[0] + s[len(s)-1])
>>>cr

para : print(s[:5])
>>>compu

para : for k in range(0,len(s)):
    print(s[k])
>>>c
o
m
p
u
t
a
d
o
r

para : print(s[0:])
>>>computador

para : for i in s:
    print(i + t)
>>>ccelular
ocelular
mcelular
pcelular
ucelular
tcelular
acelular
dcelular
ocelular
rcelular

para : print(s[:])
>>>computador

para : for i in range(len(s)-1,-1,-1):
    print(s[i])
>>>r
o
d
a
t
u
p
m
o
c
"""