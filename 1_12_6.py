a = int(input())
if 0 <= a <= 1000:
    if a % 100 != 11 and (a % 10) == 1:
        print(str(a) + ' программист')
    elif (2 <= (a % 10) <= 4) and not (12 <= (a % 100) <= 14):
        print(str(a) + ' программиста')
    else:
        print(str(a) + ' программистов')
