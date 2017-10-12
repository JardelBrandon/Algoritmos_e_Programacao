def media(a=0, b=0, c=0):
    print(a, b, c)
    m = (a+b+c)/3
    return m

n1 = int(input("N1: "))
n2 = int(input("N2: "))
n3 = int(input("N3: "))

x = media(n1, n2, n3)

print(x, end="")