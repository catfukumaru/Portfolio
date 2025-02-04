import itertools as it
print(list(it.accumulate([1,2,3,4,5,6,7], lambda x, y:(x*y))))

#Write a Python program that generates the running product of elements in an iterable.

#correct but the solution uses the mul operator
#https://www.w3resource.com/python-exercises/itertools/python-itertools-exercise-2.php