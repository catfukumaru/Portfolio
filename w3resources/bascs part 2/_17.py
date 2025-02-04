#rite a Python program to get all strobogrammatic numbers that are of length n.
a=[]
limit= 10
for d in range(1,limit):
    d=str(d)
    for i in str(d):
        if i == '0' or i  == '1' or i  == '8' or i  == '6' or i  == '9':
            if not '2' or not '4' or not'5' or not'7' in d:
                a.append([int(d)])
print(a)

#mine is wrong i dont get all the possible values of a length but the number in a range that match the condition
#https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-17.php