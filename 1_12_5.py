a, b, c = int(input()), int(input()), int(input())
if a >= b and a >= c:
    if b >= c:
        print('{} \n{} \n{}'.format(a, c, b))
    else:
        print('{} \n{} \n{}'.format(a, b, c))
elif b >= a and b >= c:
    if a >= c:
        print('{} \n{} \n{}'.format(b, c, a))
    else:
        print('{} \n{} \n{}'.format(b, a, c))
else:
    if a >= b:
        print('{} \n{} \n{}'.format(c, b, a))
    else:
        print('{} \n{} \n{}'.format(c, a, b))



