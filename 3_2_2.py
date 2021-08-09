def print_dict(dc):
    for i in dc:
        print(i, dc[i])

d = dict()
lst = [i.lower() for i in input().split()]

for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print_dict(d)