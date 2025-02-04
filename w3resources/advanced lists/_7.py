ls = [1,2,3]
ls2 = [1, 5, 6]
print("intersection of lists")
lst3 = [value for value in ls if value in ls2]
print(f"the intersection of the 2 lists are {lst3}\n")

print("union of lists")
print(f"{ls.extend(ls2)}") #gives an error

#solution u can use the & ans | but the work with sets
#https://www.w3resource.com/python-exercises/list-advanced/python-list-advanced-exercise-7.php