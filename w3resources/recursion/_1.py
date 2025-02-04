nums = [1,2,3,4,5]

def sum_list(ls):
   
    if len(ls) == 1:
        return ls[0]
    else:
        return ls[0] + sum_list(ls[1:])

total = sum_list(nums)         
print(total)