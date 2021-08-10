with open('input.txt') as inf:
    for dnk in inf:
        dnk = dnk.strip()
        print(dnk)

dnk_enc = ''
i = 0
while i < len(dnk) - 1:
    cn_s = ''
    sym = dnk[i]
    i += 1
    while dnk[i].isnumeric() and i < len(dnk) - 1:
        cn_s += dnk[i]
        i += 1
    if i == len(dnk) - 1:
        cn_s += dnk[i]
    cn = int(cn_s)
    dnk_enc += sym * cn

print(dnk_enc)

with open('text.txt', 'w') as ouf:
    ouf.write(dnk_enc)