lst = []
dict = {}
av_mat, av_fis, av_rus, cnt = 0, 0, 0, 0

with open('input.txt', 'r', encoding='utf-8') as inf:
    for line in inf:
        if line.strip() != '':
            lst = line.strip().split(';')
            #print(lst)
            dict[lst[0]] = [int(i) for i in lst[1:]]
            dict[lst[0]].append((dict[lst[0]][0] + dict[lst[0]][1] + dict[lst[0]][2]) / 3)
            av_mat += dict[lst[0]][0]
            av_fis += dict[lst[0]][1]
            av_rus += dict[lst[0]][2]
            cnt += 1
av_mat /= cnt
av_fis /= cnt
av_rus /= cnt

for key in dict:
    print(dict[key][3])

print(av_mat, av_fis, av_rus)

with open('text.txt', 'w') as ouf:
    for key in dict:
        print(dict[key][3], file=ouf)
    print(av_mat, av_fis, av_rus, file=ouf)