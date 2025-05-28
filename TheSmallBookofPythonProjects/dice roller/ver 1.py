test = "100d6"
if '+' in test:
    d_split = test.split('d') # get the first value
    plus_split = d_split[1].split('+') # get the value after the d and before the plus
    #print(plus_split)
    import random
    dice_outcomes = []
    for i in range(int(d_split[0])):# loop for d_split[0] times
        outcome = random.randint(1, int(plus_split[0])) # choose a number inbetween 1 and the number after the d and before the plus
        dice_outcomes.append(outcome) # put the outcome in the list
    result = sum(dice_outcomes)  + int(plus_split[1]) # add the values inclusing the extra points
    add_points = '+' + plus_split[1] # format the addition of points string
    dice_outcomes.append(add_points) # add the string to the list
    print(f"{result} {tuple(dice_outcomes)}") # format the output
elif '-' in test:
    d_split = test.split('d')
    plus_split = d_split[1].split('-')
    #print(plus_split)
    import random
    dice_outcomes = []
    for i in range(int(d_split[0])):
        outcome = random.randint(1, int(plus_split[0]))
        dice_outcomes.append(outcome)
    result = sum(dice_outcomes)  - int(plus_split[1])
    add_points = '-' + plus_split[1]
    dice_outcomes.append(add_points)
    print(f"{result} {tuple(dice_outcomes)}")
else:
    d_split = test.split('d')
    import random

    dice_outcomes = []
    for i in range(int(d_split[0])):
        dice_outcomes.append(random.randint(1, int(d_split[1])))
    result = sum(dice_outcomes)
    print(f"{result} {tuple(dice_outcomes)}")