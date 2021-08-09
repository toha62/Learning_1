lst = [int(i) for i in input().split()]
x = int(input())
c = lst.count(x)
i = 0
if c != 0:
    while c != 0:
        i = lst.index(x, i) + 1
        print(i - 1, end=' ')
        c -= 1
else:
    print('Отсутствует')