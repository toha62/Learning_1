def f(x):
    return x * 2


ls = []
n = int(input())
for i in range(n):
    ls.append(int(input()))
d = {}
for i in range(n):
    if ls[i] not in d:
        d[ls[i]] = f(ls[i])
        print(d[ls[i]])
    else:
        print(d[ls[i]])

#print(d)
