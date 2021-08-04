a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a <= b and c <= d and a < 11 and b < 11 and c < 11 and d < 11:

    for i in range(c, d + 1):
        print('\t{}'.format(i), end='')
    print('')

    for i in range(a, b + 1):
        print(i, end='')

        for j in range(c, d + 1):
            print('\t{}'.format(i * j), end='')

        print('')

else:
    print('Wrong range')
