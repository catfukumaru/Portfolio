 #Write a Python program to create a sequence where the first four members of the sequence are equal to one. Each successive term of the sequence is equal to the sum of the four previous ones. Find the Nth member of the sequence.

def func(array):
    if array[i] <4:
        return 1
    else:
        return array[i] + array[i] - 2+array[i]-1+array[i] + array[2] -3 + func(array{4 + i})
    
#wrong but the consectp is right
#https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-22.php