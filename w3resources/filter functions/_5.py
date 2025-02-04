text = ["", "huj", "", "huj" ]

def func(texts):
    for i in texts:
        if (i == ""):
            return False
        else:
            return True

text = filter(func,text)

for x in text:
    print(x)

#5. Write a Python function that filters out all empty strings from a list of strings using the filter function.
#correct but the solution used a diffrent method to make the filtering funcion
#https://www.w3resource.com/python-exercises/filter/python-filter-exercise-5.php