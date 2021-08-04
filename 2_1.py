a, b = int(input()), int(input())
if b > a:
    a, b = b, a
i = a
while i % a != 0 or i % b != 0:
    i += a
print(i)