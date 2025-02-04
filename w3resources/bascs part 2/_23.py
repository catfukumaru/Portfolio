import itertools
stuff = [1,4, 5, 6, 7, 9]
subset = itertools.combinations(stuff, 2)
def func(num):
    for i in subset:
        print(i-num)


func(1)

#wrong
#//Write a Python program that accepts a positive number and subtracts from it the sum of its digits, and so on. Continue this operation until the number is positive.
#https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-23.php