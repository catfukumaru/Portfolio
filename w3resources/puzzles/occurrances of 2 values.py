#Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.

state = True
counter = 0
state1, state2 = False 
counter2 = 0

user_list = [19,15,15,5,3,3,5,2]
while (state):
    for i in user_list:
        if (i == 19):
            ++counter

        if counter == 2:
            state1= True
        
        if (i == 3):
            ++counter2
        if counter2 >= 3:
            state2= True
        
        if state2 and state1:
            print("this list meets the criteria")
            break


## the solution uses built ins
#License: https://bit.ly/3oLErEI

# def test(nums):
#     return nums.count(19) == 2 and nums.count(5) >= 3
# nums = [19,19,15,5,3,5,5,2]
# print("Original list:")
# print(nums)
# print("Check two occurrences of nineteen and at least three occurrences of five in the said list:")
# print(test(nums))
# nums = [19,15,15,5,3,3,5,2]
# print("\nOriginal list:")
# print(nums)
# print("Check two occurrences of nineteen and at least three occurrences of five in the said list:")
# print(test(nums))
# nums = [19,19,5,5,5,5,5]
# print("\nOriginal list:")
# print(nums)
# print("Check two occurrences of nineteen and at least three occurrences of five in the said list:")
# print(test(nums))
