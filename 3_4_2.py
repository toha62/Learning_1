def print_dict(dc):
    for i in dc:
        print(i, dc[i])


l_wrd = ''
with open('dataset_3363_3.txt') as inf:
#with open('input.txt') as inf:
    for line in inf:
        if line.strip() != '':
            l_wrd += ' ' + line.strip()


#print(l_wrd)

d = dict()
#lst = [i.lower() for i in l_wrd.split()]
lst = [i for i in l_wrd.split()]
#print(lst)

for i in lst:
    if i.lower() in d:
        d[i.lower()][0] += 1
        d[i.lower()].append(i)
    else:
        d[i.lower()] = [1, i]

mn = []
for key, val in d.items():
    if val[0] == max(d.values())[0]:
        #mn.append(val[1:])
        mn += val[1:]


print_dict(d)
print(mn)
print(sorted(mn))
print(max(d.values())[0])
print(min(mn))

