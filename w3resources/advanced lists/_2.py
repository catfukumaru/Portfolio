ls = [[1], [1,2]]
max = 0
for i in ls: 
    res = all(i < j for i, j in zip(ls, ls[1:]))
    if res:
        if (len(i)>max):
            max = len(i)
        else:
            pass

print(max)
# Write a Python function find the length of the longest increasing sub-sequence in a list.
# got the question wrong