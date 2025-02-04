#Write a Python function that filters out all empty strings from a list of 
#strings using the filter function.
ls = [
        "",
        "",
        "hi everyone"
     ]

ls_iter = iter(ls)
new_ls = (i for i in ls_iter if len(i) != 0)

print(list(new_ls))