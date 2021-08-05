dnk = input()
dnk_enc = ''
if len(dnk) > 1:
    j = 1
    i = 0
    while i < len(dnk) - 1:
        if dnk[i] == dnk[i + 1]:
            j += 1
        else:
            dnk_enc = dnk_enc + dnk[i] + str(j)
            j = 1
        i += 1
    dnk_enc = dnk_enc + dnk[i] + str(j)
else:
    dnk_enc = dnk + '1'
print(dnk_enc)
