nums = [1, 2, [3,4], [5,6]]

def sum_multi_lists(multi_list):
    sum = 0
    for row in multi_list:
        if type(row) == type([]): # if row is a list
            sum = sum + sum_multi_lists(row) # add the return of the function call to the sum
        else:
            sum = sum + row # if the row is not a list then add element to the sum
    return sum

total = sum_multi_lists(nums)
print(total)