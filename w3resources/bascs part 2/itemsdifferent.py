#Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

nums = [1,2,3,4,5]

for i in nums:
    for j in nums[1:]:
        if i ==j:
            print("false the values in the list are not unique")
            break


#another way to solve it is vy using sets
def test_distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False;
print(test_distinct([1,5,7,9]))