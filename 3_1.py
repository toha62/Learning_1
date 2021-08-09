def modify_list(ls):
    i = 0
    while i < len(ls):
        a = ls.pop(i)
        if a % 2 == 0:
            ls.insert(i, int(a / 2))
            i += 1






lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]