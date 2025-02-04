num1 = 9
num2 = 8
print(num1 | num2)

##14. Write a Python program to add two positive integers without using the '+' operator.

# #the solution is 
# Steps

# Get two positive numbers a and b as input
# Then checks if the number b is not equal to 0
# Finds the carry value (a & b)
# Finds the sum value (a ^ b) and stores it in the variable a
# Then shifts the carry to the left by 1-bit stores it in b
# again goes back to step 2
# When b becomes 0 it finally returns the sum
# def Bitwise_add(a,b):
#     while b != 0:
#         carry = a&b # Carry value is calculated 
#         a = a^b # Sum value is calculated and stored in a
#         b = carry<<1 # The carry value is shifted towards left by a bit

#     return a # returns the final sum
# PythonCopy
# .
# The whole idea behind this code is that the carry gets added again 
# with the sum value. So what we do is we find the value of the carry 
# separately using the expression a & b and use it again to find the sum. 
# We keep on doing this till the carry value becomes 0.

# Another important point to note here is that we shift the carry 
# towards the left by 1 bit. That's because the carry value is added to
#  the next bit rather than the current bit. Take a look at this image 
# to get a better understanding.