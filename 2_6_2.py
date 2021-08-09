cnt = int(input())
b = []
for i in range(cnt):
    for j in range(i + 1):
        a = [j + 1 for k in range(j + 1)]

    b += a
print(*b[:cnt])
