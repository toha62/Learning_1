inp_list = []
s = 0
while True:
    inp_list.append(int(input()))
    if sum(inp_list) == 0:
        break
for i in inp_list:
    s += i ** 2
print(s)



