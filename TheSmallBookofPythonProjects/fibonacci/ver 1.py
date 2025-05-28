

nth = 6

start_seq = [0,1]

for i in range(2,nth-1):
    next_element = start_seq[i-1]+start_seq[i-2]
    start_seq.append(next_element)

print(start_seq[-1])
print(start_seq)