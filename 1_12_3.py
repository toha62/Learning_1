a = float(input())
b = float(input())
d = input()
operators = ['mod', 'pow', 'div', '*', '/', '+', '-']

if d in operators:
    if not ((d == '/' or d == 'mod' or d == 'div') and b == 0):
        if d == 'mod':
            print(a % b)
        elif d == 'pow':
            print(a ** b)
        elif d == 'div':
            print(a // b)
        elif d == '*':
            print(a * b)
        elif d == '/':
            print(a / b)
        elif d == '+':
            print(a + b)
        else:
            print(a - b)
    else:
        print('Деление на 0!')
else:
    print('Нет такой операции')
