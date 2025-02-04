#Write a Python function to find the longest common sub-sequence in two lists.
ls1 = [1, 2, 3, 4, 5, 6, 7, 8]
ls2 = [1, 2, 3, 6, 7, 34, 56]
ls3 = list(set(ls1) & set(ls2))
print(ls3)

#wrong
#https://www.w3resource.com/python-exercises/list-advanced/python-list-advanced-exercise-11.php