#Write a Python program to find the single number in a list that doesn't occur twice.

#n find the occurance of each number
# print the number that only happens once  

ls = [5, 3, 4, 3, 4]
for item in ls:
    if(ls.count(item) == 1):
        print(f"the number {item} occurs once")


#correct