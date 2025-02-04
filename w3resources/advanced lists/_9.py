#Write a Python a function to find the maximum sum sub-sequence in a list. Return the maximum value.
import itertools
ls = [[1], [1,2] ]
max = 0
for i in ls:
    i_sum = itertools.accumulate(i)
    if i_sum > max:
        max = i_sum


print(sum)

#understood it wrong
# https://www.w3resource.com/python-exercises/list-advanced/python-list-advanced-exercise-9.php