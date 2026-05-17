n = 6
sequence = [n]
while n>0.0:
    if n %2 == 0: # correct
        n = int(n / 2)
        sequence.append(n)
        if n == 1:
            break
    if n %2 != 0: # correct
        n = n * 3 + 1
        sequence.append(n)

print(sequence)