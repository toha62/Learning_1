lst = []
dict = {}


def print_dict(dc):
    for i in dc:
        print('{}:{} {} {} {} {}'.format(i, *dc[i]))


def adddict(d, key, l):
    for i in range(5):
        d[key][i] += l[i]


n = int(input())
for i in range(n):
    lst = input().split(';')
    if lst[0] not in dict:
        dict[lst[0]] = [0, 0, 0, 0, 0]
    if lst[2] not in dict:
        dict[lst[2]] = [0, 0, 0, 0, 0]
    if int(lst[1]) > int(lst[3]):
        adddict(dict, lst[0], [1, 1, 0, 0, 3])
        adddict(dict, lst[2], [1, 0, 0, 1, 0])
    elif int(lst[1]) < int(lst[3]):
        adddict(dict, lst[2], [1, 1, 0, 0, 3])
        adddict(dict, lst[0], [1, 0, 0, 1, 0])
    else:
        adddict(dict, lst[2], [1, 0, 1, 0, 1])
        adddict(dict, lst[0], [1, 0, 1, 0, 1])

print_dict(dict)
