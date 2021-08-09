k, cnt, n = 0, 1, int(input())
if n != 1:
    mtr = [[0 for j in range(n)] for i in range(n)]
    while cnt <= n * n:
        for i in range(k, n - k):
            mtr[k][i] = cnt
            cnt += 1

        for i in range(k + 1, n - k):
            mtr[i][n - 1 - k] = cnt
            cnt += 1

        for i in range(n - k - 2, k - 1, -1):
            mtr[n - 1 - k][i] = cnt
            cnt += 1

        for i in range(n - k - 2, k, -1):
            mtr[i][k] = cnt
            cnt += 1
        k += 1

    for i in range(n):
        for j in range(n):
            print(mtr[i][j], end=' ')
        print()
else:
    print(1)