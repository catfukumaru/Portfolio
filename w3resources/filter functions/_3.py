nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
value = 3
def func(ls):
    for i in range(ls):
        if (i <= 3):
            True
        else:
            False

new_nums = filter(func,nums)
print(list(new_nums))

#//solution doesnt use true or5 False
#https://www.w3resource.com/python-exercises/filter/python-filter-exercise-3.php
#Write a Python function that filters out all elements less than or equal than a specified value from a list of numbers using the filter function.