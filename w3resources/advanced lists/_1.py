#Write a Python function to reverse a list at a specific location.
def reverse_list(lst, a, b):
    return lst[0:a]+ list(reversed(lst[a:b]))+lst[b:]


a = reverse_list([1,2,4,5,6,7,8,9], 0,5)

print(a)