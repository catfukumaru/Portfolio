#Write a Python program to find the median among three given numbers.

nums = [1, 2, 3]
cum = 0
for i in nums:
    sum =+ i

median = sum/len(nums)
print(median)

#i found the average not the median
#https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-18.php
#i found that you can use a lib
import statistics
print(statistics.median(nums))