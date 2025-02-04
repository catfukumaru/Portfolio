numbers = [6, 9, 3, 1]
sorted(numbers)

kth = int(input("kth smallest element"))
#I minused 1 cause the list is 0 based
if (kth -1 < len(numbers)):
    print(f"the kth element in the list is {numbers[kth]}")


#wrong cause it got sorted in ascending order
#https://www.w3resource.com/python-exercises/list-advanced/python-list-advanced-exercise-4.php