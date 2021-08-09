lst = []
tmp = input().split(' ')
while tmp[0] != 'end':
    lst.append(tmp)
    tmp = input().split(' ')
print(lst)
row = len(lst)
col = len(lst[0])

n_lst = [[0 for j in range(col)] for i in range(row)]

for i in range(row):
    for j in range(col):

        a = int(lst[i][j - 1]) + int(lst[i - 1][j])

        if j + 1 == col:
            b = int(lst[i][0])
        else:
            b = int(lst[i][j + 1])

        if i + 1 == row:
            d = int(lst[0][j])
        else:
            d = int(lst[i + 1][j])

        n_lst[i][j] = a + b + d

for i in range(row):
    for j in range(col):
        print(n_lst[i][j], end=' ')
    print()
