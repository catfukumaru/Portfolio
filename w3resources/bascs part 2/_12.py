#Write a Python program that generates a list of all possible permutations from a given collection of distinct numbers.

nums = [1, 2, 3,4]
import itertools

perms = itertools.permutations(nums)

for perm in perms:
    print(perm)

#correct