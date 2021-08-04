forma = input()
if forma == 'треугольник':
    a, b, c = int(input()), int(input()), int(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif forma == 'прямоугольник':
    a, b = int(input()), int(input())
    print(a * b)
elif forma == 'круг':
    print(int(input()) ** 2 * 3.14)
else:
    print('Не правильная форма')
