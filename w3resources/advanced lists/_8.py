import itertools
ls = [1,2, 3, 4, 1, 1, 2, , 1, 1, 2, , 3, 4, 5, 5, 5,]

for i in ls:
    if itertools.count(i) > 1:
        pos = ls.index(i)
        for j in ls[pos:]:
            if i == j:
                ls.pop(j)

print(ls)

#wromg. the idea is to make the numbers keys and thier count the data
#https://www.w3resource.com/python-exercises/list-advanced/python-list-advanced-exercise-8.php