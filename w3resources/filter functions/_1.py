nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def func(list):
    for i in list:
        if (i%2 == 0):
            continue
        else:
            list.pop(i)

new_nums = filter(func,nums)
print(list(new_nums))
#solution uses true and fase to filter. mine is wrong
#https://www.w3resource.com/python-exercises/filter/python-filter-exercise-1.php
#Write a Python function that filters out even numbers from a list of integers using the filter function.