#Write a Python program that creates a list of names and uses the filter 
#function to extract names that start with a vowel (A, E, I, O, U).
ls = [
        "emily",
        "tim",
        "homer",
        "maple"
     ]

ls_iter = iter(ls)
vowels = ['A', 'I', 'O', 'U', 'E']
new_iter = (i for i in ls_iter if i[0].upper() in vowels)

ls_list = list(new_iter)

print(ls_list)
