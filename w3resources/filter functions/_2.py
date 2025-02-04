strings = ["rfeW", "jfrujUJIKL"]

def func(para):
    for sentence in para:
        for j in sentence:
            j.isupper()
        
func(strings)
result = filter(func, strings)


#print(list(result))
#Write a Python program that uses the filter function to extract all uppercase letters from a list of mixed-case strings.
#https://www.w3resource.com/python-exercises/filter/python-filter-exercise-2.php